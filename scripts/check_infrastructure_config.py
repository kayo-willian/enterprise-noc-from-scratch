#!/usr/bin/env python3
"""Validate public Docker Compose examples and reverse-proxy service references.

This checks configuration structure, not service runtime or lab connectivity.
No containers are started and no private environment files are loaded.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "docker_configs"
COMPOSE = (
    (CONFIG / "docker-compose.yml", CONFIG / ".env.example"),
    (CONFIG / "lab-ti/pihole/docker-compose.yml", CONFIG / "lab-ti/pihole/.env.example"),
    (CONFIG / "lab-ti/portainer/docker-compose.yml", None),
)
ENV_VAR = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)[^}]*\}")
PROXY_PASS = re.compile(r"\bproxy_pass\s+https?://([a-zA-Z0-9_-]+):(\d+)\s*;")


def env_example_keys(path: Path) -> set[str]:
    return {
        line.split("=", 1)[0].strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#") and "=" in line
    }


def check_env_coverage(compose_path: Path, env_path: Path | None) -> list[str]:
    required = set(ENV_VAR.findall(compose_path.read_text(encoding="utf-8")))
    if not required:
        return []
    if env_path is None or not env_path.is_file():
        return [f"{compose_path.name}: missing environment example"]
    missing = required - env_example_keys(env_path)
    return [f"{compose_path.name}: example missing variable {name}"
            for name in sorted(missing)]


def compose_config(path: Path, env_path: Path | None) -> dict:
    command = ["docker", "compose"]
    if env_path:
        command += ["--env-file", str(env_path)]
    command += ["-f", str(path), "config", "--format", "json"]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(f"docker compose config failed for {path.relative_to(ROOT)}: "
                           f"{result.stderr.strip()[:1200]}")
    return json.loads(result.stdout)


def proxy_consistency(main_compose: dict, config_file: Path) -> list[str]:
    """Compare HTTP upstream names and internal ports with Compose declarations."""
    problems: list[str] = []
    services = main_compose.get("services", {})
    if "reverse-proxy" not in services:
        return ["Main Compose does not define reverse-proxy"]
    proxy = services["reverse-proxy"]
    depends = proxy.get("depends_on", {})
    if isinstance(depends, list):
        depends = {name: {} for name in depends}
    references = PROXY_PASS.findall(config_file.read_text(encoding="utf-8"))
    if not references:
        return ["Reverse-proxy example contains no static HTTP upstreams"]
    for service_name, port in references:
        if service_name not in services:
            problems.append(f"Nginx upstream {service_name}:{port} has no Compose service")
            continue
        ports = services[service_name].get("ports", [])
        exposed = {str(p.get("target")) for p in ports if isinstance(p, dict)}
        exposed.update(str(p) for p in services[service_name].get("expose", []))
        if port not in exposed:
            problems.append(f"Nginx upstream {service_name}:{port} does not match a declared container port")
        if service_name not in depends:
            problems.append(f"Nginx upstream {service_name} missing reverse-proxy depends_on")
    return problems


def main() -> int:
    errors: list[str] = []
    configs = {}
    for path, env in COMPOSE:
        errors.extend(check_env_coverage(path, env))
        try:
            config = compose_config(path, env)
        except (RuntimeError, json.JSONDecodeError, OSError) as exc:
            errors.append(str(exc))
            continue
        configs[path] = config
        print(f"Compose valid: {path.relative_to(ROOT)} ({len(config.get('services', {}))} services)")
    main_compose = configs.get(CONFIG / "docker-compose.yml")
    if main_compose:
        errors.extend(proxy_consistency(main_compose, CONFIG / "reverse-proxy/conf.d/lab.conf"))
        nginx_conf = (CONFIG / "reverse-proxy/nginx.conf").read_text(encoding="utf-8")
        if "include /etc/nginx/conf.d/*.conf;" not in nginx_conf:
            errors.append("Nginx main configuration does not include the published site rules")
        mounts = main_compose["services"]["reverse-proxy"].get("volumes", [])
        targets = {item.get("target") for item in mounts if isinstance(item, dict)}
        for target in ("/etc/nginx/nginx.conf", "/etc/nginx/conf.d", "/etc/nginx/certs"):
            if target not in targets:
                errors.append(f"Missing reverse-proxy configuration mount: {target}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Infrastructure configuration checks: {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
