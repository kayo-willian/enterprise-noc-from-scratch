# Pi-hole and Uptime Kuma — DNS and Availability

**English** | [Português (Brasil)](../pt-BR/servicos/dns-e-disponibilidade.md)

**Evidence date:** November 6, 2026 · **Host:** main Debian 13 Docker server, observed IPv4 `192.168.10.12/24`.

Pi-hole filters and reports DNS queries; Uptime Kuma checks the availability of selected targets. They complement Zabbix metrics and Grafana visualizations rather than replacing them.

| Service | Recorded container image | Published host ports |
|---|---|---|
| Pi-hole (`pihole`) | `pihole/pihole:latest` | DNS TCP/UDP 53; web 8080 |
| Uptime Kuma (`uptime-kuma`) | `louislam/uptime-kuma:1` | Web 3001 |

The published ports document the container configuration. Reachability from every network segment is not independently confirmed.

## Pi-hole — DNS Filtering

![Pi-hole DNS dashboard](../assets/images/services/pihole_dashboard.png)

| Dashboard indicator | Recorded value |
|---|---:|
| DNS queries | **12,293** |
| Blocked queries | **1,827** |
| Blocked percentage | **14.9%** |
| Domains in blocklists | **75,952** |
| Active clients | **13** |
| Service state | **Active** |

The screenshot also includes query activity over time, query types, upstream DNS information and client activity. Values refer to the interval displayed by the dashboard, not permanent totals.

**Interpretation:** A blocked query matched the configured DNS filtering rules; it is not proof of malware, an attack or prevention of all unwanted connections. The blocklist domain count is not the number of queries blocked.

![Pi-hole domains and client statistics](../assets/images/services/pihole_dashboard_tops.png)

Four tables show **top allowed domains**, **top blocked domains**, **clients by query volume** and **clients by blocked-query volume**. Private IPv4 client addresses from more than one laboratory segment appear; these records demonstrate DNS activity, **not** verified device identities or confirmed DNS policy coverage across all VLANs.

**Privacy:** Client addresses and DNS query history are sensitive operational data; consider user privacy before reusing these screenshots publicly.

## Uptime Kuma — Service Checks

![Uptime Kuma monitors and historical events](../assets/images/services/UpTimeKuma.png)

| Monitor status | Recorded count |
|---|---:|
| Up | **4** |
| Down | 0 |
| Maintenance | 0 |
| Unknown | 0 |
| Paused | 0 |

| Named monitor | Target |
|---|---|
| Grafana NOC | Grafana |
| Portal Web Zabbix | Zabbix frontend |
| Cisco C8200L Router | Cisco router |
| Institutional Website | Corporate web portal |

The interface displays **100%** for all four monitors within its configured reporting context. That value is **not** a verified SLA or proof of uninterrupted service.

The historical event table also records HTTP `200 OK` checks, unsuccessful Cisco router connectivity checks, a Grafana connection-reset event and later successful checks. A monitor marked `Up` at capture time can therefore have earlier recorded failures.

Uptime Kuma's four selected monitors do **not** represent all ten Docker containers or all network devices.

## Configuration References

- [Pi-hole Compose](../../docker_configs/lab-ti/pihole/docker-compose.yml): host DNS `53/tcp` and `53/udp`, web `8080`, persistent `etc-pihole` and `etc-dnsmasq.d` mounts, locally supplied admin password and upstream DNS.
- [Main infrastructure Compose](../../docker_configs/docker-compose.yml): Uptime Kuma `3001` and persistent application data at `./uptime-kuma-data:/app/data`.
- [Docker inventory and reverse proxy](../containers/docker-services.md): distinguishes actual dated container inventory from sanitized Compose and Nginx examples.
- [Zabbix](../monitoring/zabbix-monitoring.md) / [Grafana](../monitoring/grafana-monitoring.md): broader infrastructure metrics and visualizations.

The public Compose files omit actual secrets and machine-local data. The captured dashboards demonstrate the **recorded DNS activity and monitor states**, not continuous availability, deployment hardening, service-level compliance or complete DNS coverage.

**Original images:** `pihole_dashboard.png`, `pihole_dashboard_tops.png`, `UpTimeKuma.png` — collected November 6, 2026.
