"""Focused unit tests for repository validators (standard library only)."""

from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_documentation_links import check_reference, references  # noqa: E402
from check_infrastructure_config import check_env_coverage, proxy_consistency  # noqa: E402


class DocumentationChecks(unittest.TestCase):
    def test_valid_and_missing_file(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "docs" / "README.md"
            document.parent.mkdir()
            (root / "image.png").write_bytes(b"image")
            self.assertIsNone(check_reference(document, "../image.png", root))
            self.assertIn("missing", check_reference(document, "missing.png", root))

    def test_external_and_anchor_links(self):
        with TemporaryDirectory() as directory:
            document = Path(directory) / "README.md"
            self.assertIsNone(check_reference(document, "https://example.com/", Path(directory)))
            self.assertIsNone(check_reference(document, "#introduction", Path(directory)))

    def test_fenced_examples_are_ignored(self):
        sample = "[Working](README.md)\n~~~md\n[Example](not-real.md)\n~~~\n<img src='image.png'>"
        self.assertEqual([r for _, r in references(sample)], ["README.md", "image.png"])


class InfrastructureChecks(unittest.TestCase):
    def test_compose_example_environment_keys(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            manifest = base / "compose.yml"
            env = base / ".env.example"
            manifest.write_text("name: " + chr(36) + "{PROJECT:?required}\n", encoding="utf-8")
            env.write_text("PROJECT=example\n", encoding="utf-8")
            self.assertEqual(check_env_coverage(manifest, env), [])
            env.write_text("OTHER=example\n", encoding="utf-8")
            self.assertEqual(len(check_env_coverage(manifest, env)), 1)

    def test_proxy_target_consistency(self):
        with TemporaryDirectory() as directory:
            config = Path(directory) / "example.conf"
            config.write_text("proxy_pass http://app:8080;\n", encoding="utf-8")
            services = {
                "reverse-proxy": {"depends_on": {"app": {}}, "volumes": []},
                "app": {"ports": [{"target": 8080, "published": "8082"}]},
            }
            self.assertEqual(proxy_consistency({"services": services}, config), [])
            config.write_text("proxy_pass http://app:8081;\n", encoding="utf-8")
            self.assertEqual(len(proxy_consistency({"services": services}, config)), 1)


if __name__ == "__main__":
    unittest.main()
