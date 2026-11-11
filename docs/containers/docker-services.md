# Docker Infrastructure and Services

[English](docker-services.md) | [Português (Brasil)](../pt-BR/containers/servicos-docker.md)

## 1. Overview

The Enterprise NOC — From Scratch laboratory uses Docker to host infrastructure, monitoring, and network services.

The container environment runs on the main IT workstation, a Dell OptiPlex 3020 with an Intel Core i5-4590 processor, approximately 8 GB of RAM, and Debian GNU/Linux 13 (Trixie).

The host was identified with the IPv4 address `192.168.10.12/24` during the evidence collection.

This document describes the Docker environment observed on November 6, 2026, using the `docker ps` output and Portainer screenshots.

## 2. Docker Environment

![Portainer environment summary](../assets/images/docker/portainer-environment-summary.png)

The Portainer dashboard reported the following resources:

| Resource | Observed quantity |
|---|---:|
| Docker environments | 1 |
| Stacks | 3 |
| Containers | 10 |
| Running containers | 10 |
| Stopped containers | 0 |
| Container images | 11 |
| Volumes | 4 |
| Docker networks | 6 |

Four containers were reported as healthy, with no unhealthy containers indicated by the dashboard at the time of collection.

These values represent a specific observation, not continuous availability statistics.

## 3. Container Inventory

![Running containers in Portainer](../assets/images/docker/portainer-running-containers.png)

The `docker ps` output identified ten running containers.

| Container | Image | Purpose |
|---|---|---|
| `reverse-proxy` | `nginx:alpine` | Reverse proxy |
| `zabbix-web` | `zabbix/zabbix-web-apache-mysql:ubuntu-7.0-latest` | Zabbix web interface |
| `zabbix-server` | `zabbix/zabbix-server-mysql:ubuntu-7.0-latest` | Zabbix monitoring server |
| `uptime-kuma` | `louislam/uptime-kuma:1` | Service availability monitoring |
| `zabbix-db` | `mariadb:11.4` | Zabbix database |
| `grafana` | `grafana/grafana-oss:latest` | Monitoring dashboards and visualization |
| `zabbix-agent` | `zabbix/zabbix-agent:ubuntu-7.0-latest` | Zabbix monitoring agent |
| `site-estatico` | `httpd:alpine` | Static website |
| `pihole` | `pihole/pihole:latest` | DNS filtering and management |
| `portainer` | `portainer/portainer-ce:latest` | Container management |

Image tags are reproduced from the collected output. Tags such as `latest` do not establish an exact installed software version.

## 4. Published Service Ports

The following host ports were identified in the collected `docker ps` output:

| Container | Published host port(s) |
|---|---|
| `reverse-proxy` | 80, 443 |
| `zabbix-web` | 8082 |
| `zabbix-server` | 10051 |
| `uptime-kuma` | 3001 |
| `zabbix-db` | No published host port |
| `grafana` | 3000 |
| `zabbix-agent` | 10050 |
| `site-estatico` | 8081 |
| `pihole` | 53 TCP/UDP, 8080 |
| `portainer` | 8000, 9000, 9443 |

These ports describe the container configuration at the time of collection. Published ports are recorded configuration values, not network-by-network reachability test results.

## 5. Docker Networking

![Docker networks in Portainer](../assets/images/docker/portainer-docker-networks.png)

Portainer reported six Docker networks.

The environment includes Docker's standard networking mechanisms and networks associated with the deployed application stacks.

The collected Linux system report also identifies Docker bridge interfaces and private container subnets.

The network inventory shows configured Docker networks, rather than an application-to-application connectivity test matrix.

## 6. Service Organization

The documented containers support several functions:

### Infrastructure and Application Access

- Nginx provides reverse-proxy functionality.
- Apache HTTP Server hosts a static website.
- Portainer provides container management.

### Monitoring and Observability

- Zabbix Server collects and processes monitoring data.
- Zabbix Web provides the monitoring interface.
- Zabbix Agent supplies monitoring data.
- Grafana provides dashboards and visualizations.
- Uptime Kuma monitors service availability.

### Supporting Services

- MariaDB provides database storage for Zabbix.
- Pi-hole provides DNS-related functionality.

The Asterisk and FreeRADIUS services are documented separately because they run on a different Linux computer.

## 7. Architecture, Service Relationships and Design Trade-offs

The infrastructure is organized around **one physical Debian host with ten observed containers** and a **separate Linux computer for Asterisk/FreeRADIUS**. This division is documented by the container inventory and the voice/authentication server records; it avoids treating the VoIP server as another Docker container.

### How an Application Request Moves Through the Lab

The published configuration gives concrete examples of a request path:

1. A client resolves an **internal service hostname** using its configured DNS. Pi-hole can answer or filter requests from clients configured to use it; the available evidence does not prove that every VLAN uses Pi-hole.
2. The client connects to the Debian infrastructure host on **HTTP 80 or HTTPS 443**, where the `reverse-proxy` container publishes its listeners.
3. Nginx selects a virtual host in [`lab.conf`](../../docker_configs/reverse-proxy/conf.d/lab.conf) and forwards the request over the Compose network to its application container. For instance, `grafana.noc.example.test` targets `grafana:3000`; `zabbix.noc.example.test` targets `zabbix-web:8080`.
4. Zabbix Web communicates with the Zabbix Server and MariaDB stack; the application is not equivalent to the front-end HTTP response alone. Grafana renders monitoring information using the Zabbix integration configured in the example.

The hostnames above are **sanitized examples**, not publicly resolvable production DNS records. The public Nginx configuration describes virtual hosts for the **portal, Zabbix, Grafana and Uptime Kuma**; it does not publish Pi-hole or Portainer virtual-host rules. The actual laboratory report also refers to those additional services, so the published sample must not be mistaken for a complete export.

### Why the Compose Dependencies Matter

| Relationship | Technical implication | What the evidence proves |
|---|---|---|
| `db` health check → `zabbix-server` | Zabbix processing requires database connectivity; the Compose example waits for an initialized MariaDB | The **declared dependency**, not successful processing of every item |
| `db` and `zabbix-server` → `zabbix-web` | Front-end startup is ordered after the database and Zabbix Server prerequisites | Startup ordering, **not** application-level readiness |
| `zabbix-server` → `zabbix-agent` | The agent is configured to exchange monitoring data with the named server | Configuration, **not** successful collection for every host |
| `reverse-proxy` → web applications | Proxy routes rely on upstream containers being reachable by name | Declared routes, **not** tested reachability from each VLAN |
| Grafana plugin → Zabbix | Dashboards can visualize the Zabbix monitoring data | Plugin configuration and dashboard evidence, not full metric correctness |

The use of a shared host simplifies access to logs, container inventories and dependent services, but also makes that host a **shared failure domain**. Neither high availability nor recovery time is established by the November 6 records. Persistent mounts protect data against ordinary container replacement when handled correctly; they do not by themselves establish a backup or restore procedure.

The examples use some mutable image tags, notably `latest`. For reproducible deployment, exact image tags or digests would need separate verification; the documented inventory alone cannot establish those digests.

## 8. Diagnostic and Validation Workflow

These are **reference commands for future checks**, not claims that the checks were performed during this review. Execute from an authorized host; first confirm the actual Compose project and paths.

```bash
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
docker network ls
docker volume ls
```

For an individual service, distinguish Docker's process status from its optional health check:

```bash
docker inspect --format '{{.State.Status}} {{if .State.Health}}{{.State.Health.Status}}{{else}}no-healthcheck{{end}}' zabbix-db
docker logs --tail 100 zabbix-server
```

A focused verification should check **the application and its dependency**: for a Zabbix Web failure, inspect the front end, Zabbix Server and MariaDB; for a portal failure, inspect DNS resolution, the Nginx route and `site-estatico`. A published port or a `running` container is an initial observation, not the final functional check.

**Known investigation boundaries:** The snapshots show ten running containers and four healthy checks, but do not give per-container CPU/RAM, per-VLAN connectivity tests, TLS validation, recovery drills or a confirmed root cause for any outage. Preserve any new log excerpts with timestamps and redact secrets before publishing.

**Operational procedures:** [Docker service failure runbook](../noc-operations/runbooks/docker-service-failure.md) · [DNS resolution runbook](../noc-operations/runbooks/dns-resolution-failure.md). Those documents describe troubleshooting methods; they do **not** assert that an incident occurred on November 6. 

## 9. Evidence Scope

The collected evidence confirms the presence of ten running Docker containers on November 6, 2026.

The Portainer screenshots also document container management, network configuration, and resource counts.

This dated container inventory does not record the following operational properties:

- Continuous service availability.
- Successful access from every VLAN.
- Complete application security.
- Correct operation of every monitoring item.
- High availability or redundancy.

The inventory describes containers, published ports and networks at the collection date, without treating those configuration entries as application test results.

## 10. Docker Compose Configuration

The following Docker Compose files are sanitized public examples based on the laboratory configuration. They exclude local certificates, secrets, persistent data, and other machine-specific prerequisites.

- [Monitoring and Infrastructure Stack](../../docker_configs/docker-compose.yml)
- [Pi-hole](../../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Portainer](../../docker_configs/lab-ti/portainer/docker-compose.yml)

### Reverse Proxy and Corporate Portal

The laboratory includes an Nginx reverse proxy and an
Apache HTTP Server container responsible for the corporate portal.

The collected configuration includes routes for Zabbix,
Grafana, Uptime Kuma, Portainer, Pi-hole, and the portal.

The public configuration currently documents the routes
for the portal, Zabbix, Grafana, and Uptime Kuma.

Configuration files:

- [Nginx Main Configuration](../../docker_configs/reverse-proxy/nginx.conf)
- [Reverse Proxy Rules](../../docker_configs/reverse-proxy/conf.d/lab.conf)

The public files use example domains and certificate paths.
The original environment used local DNS names and TLS certificates.

Private keys and institution-specific settings are not included.

The static website is hosted by the `site-estatico` container,
using the `httpd:alpine` image and port `8081` on the Docker host.

These files are sanitized versions of the collected configurations.
Credentials and institution-specific DNS settings have been removed.

**Evidence collection date:** November 6, 2026.
