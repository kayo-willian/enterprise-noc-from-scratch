# Linux and Docker — Infrastructure Services

**English** | [Português (Brasil)](../pt-BR/containers/servicos-docker.md)

**Evidence:** November 6, 2026 · **Host:** Dell OptiPlex 3020, Intel Core i5-4590, approximately 8 GB RAM, Debian GNU/Linux 13 (Trixie), observed IPv4 `192.168.10.12/24`.

This document separates the **running-container inventory** recorded through `docker ps` and Portainer from the **sanitized Compose configuration** published in the repository. Published configuration files describe deployment structure; they are not a verified, self-contained reproduction of the captured installation.

## Docker Inventory

![Portainer environment summary](../assets/images/docker/portainer-environment-summary.png)

| Portainer resource | Recorded on November 6 |
|---|---:|
| Docker environments | 1 |
| Stacks | 3 |
| Containers / running / stopped | 10 / 10 / 0 |
| Container images | 11 |
| Volumes | 4 |
| Networks | 6 |
| Containers reported healthy | 4 |
| Containers reported unhealthy | 0 |

The four *healthy* results refer to health checks reported by Portainer, not independent functional tests of every container.

![Running Docker containers](../assets/images/docker/portainer-running-containers.png)

| Container | Recorded image | Role | Published host ports |
|---|---|---|---|
| `reverse-proxy` | `nginx:alpine` | Nginx reverse proxy | 80, 443 |
| `zabbix-web` | `zabbix/zabbix-web-apache-mysql:ubuntu-7.0-latest` | Zabbix frontend | 8082 |
| `zabbix-server` | `zabbix/zabbix-server-mysql:ubuntu-7.0-latest` | Metrics and triggers | 10051 |
| `uptime-kuma` | `louislam/uptime-kuma:1` | Availability checks | 3001 |
| `zabbix-db` | `mariadb:11.4` | Zabbix database | None |
| `grafana` | `grafana/grafana-oss:latest` | Monitoring dashboards | 3000 |
| `zabbix-agent` | `zabbix/zabbix-agent:ubuntu-7.0-latest` | Zabbix Agent | 10050 |
| `site-estatico` | `httpd:alpine` | Static corporate portal | 8081 |
| `pihole` | `pihole/pihole:latest` | DNS filtering | 53 TCP/UDP, 8080 |
| `portainer` | `portainer/portainer-ce:latest` | Docker administration | 8000, 9000, 9443 |

The image references and ports come from the collected inventory. A `latest` tag does **not** identify an exact application version; a published port does **not** prove reachability from all VLANs.

## Deployment Structure and Dependencies

The public Compose files are organized by service group:

| Public configuration | Services declared | Relevant configuration |
|---|---|---|
| [Infrastructure stack](../../docker_configs/docker-compose.yml) | `db`, `zabbix-server`, `zabbix-web`, `zabbix-agent`, `grafana`, `uptime-kuma`, `reverse-proxy`, `site-estatico` | Shared `zabbix-net` bridge; application data mounts; startup dependencies |
| [Pi-hole](../../docker_configs/lab-ti/pihole/docker-compose.yml) | `pihole` | DNS TCP/UDP 53, web 8080, persistent configuration volumes |
| [Portainer](../../docker_configs/lab-ti/portainer/docker-compose.yml) | `portainer` | Docker socket mount, persistent `portainer_data` volume, administration ports |

The three public Compose groups together declare the **ten named containers** in the historical inventory. This correspondence does not establish that the exported files alone can recreate the laboratory, which also depended on local data, DNS, certificates and credentials.

### Main Stack

The public `docker-compose.yml` documents these relationships and settings:

- **MariaDB (`db`):** image `mariadb:11.4`, data directory bind mount `./zabbix-db-data:/var/lib/mysql`, a connection/initialization health check, `512M` InnoDB buffer pool and `300` maximum connections in the example.
- **Zabbix Server:** waits for `db` to report `service_healthy`; uses the same database environment variables, mounts external/alert scripts read-only and publishes TCP `10051`.
- **Zabbix Web:** depends on the database health check and the server startup; its internal port `8080` is published as host `8082`.
- **Zabbix Agent:** configured for passive monitoring with the server host set to `zabbix-server`; TCP `10050` is published.
- **Grafana:** the example specifies plugin `alexanderzobnin-zabbix-app` and persists `/var/lib/grafana` through `./grafana-data`.
- **Uptime Kuma:** persists `/app/data` through `./uptime-kuma-data`; its web interface is published on `3001`.
- **Nginx proxy:** depends on Zabbix Web, Grafana, Uptime Kuma and the static site; exposes `80`/`443` and mounts proxy rules and certificate paths.
- **Static site:** Apache `httpd:alpine` serves `./site-estatico-html` read-only at container port `80` / host `8081`.

These are **settings present in the sanitized repository configuration**, not evidence that the local system still uses those exact values.

### Pi-hole and Portainer

The Pi-hole example requires local values for `PIHOLE_ADMIN_PASSWORD` and `PIHOLE_DNS_UPSTREAMS`, sets the DNS listening mode to `ALL`, and mounts `./etc-pihole` and `./etc-dnsmasq.d`. Do not interpret the sample listening mode as proof of DNS filtering across every VLAN.

The Portainer example mounts `/var/run/docker.sock` and a named `portainer_data` volume. Docker-socket access is administratively sensitive; the example should not be published with real credentials.

## Networking and Reverse Proxy

![Docker networks in Portainer](../assets/images/docker/portainer-docker-networks.png)

Portainer showed **six Docker networks**. The published main Compose defines one named bridge, `zabbix-net`, while the other Compose groups are separate; the exact runtime network memberships and container-to-container reachability were not fully captured.

The public Nginx files are:

- [Main Nginx settings](../../docker_configs/reverse-proxy/nginx.conf)
- [Virtual hosts and upstreams](../../docker_configs/reverse-proxy/conf.d/lab.conf)

| Example hostname | Proxy target |
|---|---|
| `portal.noc.example.test` | `site-estatico:80` |
| `zabbix.noc.example.test` | `zabbix-web:8080` |
| `grafana.noc.example.test` | `grafana:3000` |
| `status.noc.example.test` | `uptime-kuma:3001` |

The files declare HTTP/HTTPS listeners and example certificate paths (`/etc/nginx/certs/lab.crt` and `lab.key`). The sanitized rules **do not include** Pi-hole or Portainer proxy virtual hosts, even though those services were recorded in the environment; the collected laboratory configuration and public example differ in scope. No automatic HTTP-to-HTTPS redirect is established by the published rules.

The real certificate files, database passwords, internal DNS settings and persisted application data are intentionally absent. Do not run the public stack without supplying local prerequisites and assessing the exposed interfaces.

## Evidence and Validation Boundaries

The November 6 `docker ps` / Portainer records establish ten running containers, published ports and resource counts. They do **not** establish uninterrupted uptime, complete application health, cross-VLAN reachability, high availability, backup recovery or production hardening.

- **Zabbix/Grafana monitoring evidence:** [Zabbix](../monitoring/zabbix-monitoring.md) · [Grafana](../monitoring/grafana-monitoring.md).
- **DNS and uptime observations:** [Pi-hole and Uptime Kuma](../services/dns-and-availability.md).
- **Services on another physical Linux computer:** [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md).
- **Linux and workstation inventory:** [Workstation and Server Inventory](../endpoints/workstation-inventory.md).
