# Runbook — Docker Service Failure

**English** | [Português (Brasil)](../../../pt-BR/operacoes-noc/runbooks/falhas-servicos-docker.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** CNT / SYS / WEB · **Status:** Proposed runbook, not a resolved incident  
**Environment:** Debian 13 NOC computer; Docker, Compose, Portainer; dependent infrastructure services

## 1. Purpose and evidence

Investigate a container that is stopped, restarting, unhealthy, unreachable or responding incorrectly. The November 6, 2026 Portainer and Docker records showed **ten running containers**, not permanent availability. The published inventory names `reverse-proxy`, `zabbix-web`, `zabbix-server`, `uptime-kuma`, `zabbix-db`, `grafana`, `zabbix-agent`, `site-estatico`, `pihole` and `portainer`.

The publicly sanitized Compose configuration includes the monitoring/application stack, while **Pi-hole and Portainer have separate Compose examples**. Do not assume that all ten services belong to a single project or that the published configuration contains every prerequisite.

## 2. Safety and change boundaries

- Obtain authorization for the affected host and service. Start with read-only commands.
- Do **not** run `docker compose down -v`, `docker system prune`, image upgrades, database resets or volume deletion during troubleshooting.
- Restarting a container can interrupt users and obscure ephemeral state; only do it after approval, dependency review and rollback planning.
- `docker inspect` and environment dumps can contain credentials; collect selected fields and keep sensitive output out of public commits.
- Never assume a container is healthy merely because it is running or has a published host port.

## 3. Understand service dependencies

| Layer | Documented service / relevance |
|---|---|
| Zabbix database | `zabbix-db` (MariaDB 11.4 example); Zabbix depends on DB availability |
| Monitoring engine | `zabbix-server`; collects/processes metrics |
| Zabbix interface | `zabbix-web`; web UI and database/server dependencies |
| Visualization | `grafana`; includes Zabbix datasource/plugin integration |
| Proxy and web | `reverse-proxy` (Nginx) routes to selected internal services; `site-estatico` (Apache) hosts local corporate site |
| Availability | `uptime-kuma` checks configured targets |
| DNS filtering | `pihole` exposes DNS TCP/UDP 53 in the dated inventory |
| Management | `portainer` visualizes containers/networks |
| Monitoring agent | `zabbix-agent` belongs to the documented monitoring stack |

The **public GitHub Pages project showcase** is distinct from the Apache `site-estatico` container in the laboratory; their deployment and availability must not be conflated.

## 4. Initial triage

Record the timestamp, reported symptom, affected container, externally observed application behavior, recent changes and other dependent services.

~~~bash
docker version
docker info --format '{{.ServerVersion}}'
docker ps --all --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
docker ps --filter name=zabbix
~~~

If the Docker daemon is unavailable, inspect host status first:

~~~bash
systemctl status docker --no-pager
journalctl -u docker --since '-30 min' --no-pager
df -h
free -h
~~~

A Docker daemon problem affects multiple containers, whereas one application failure may be isolated.

## 5. Inspect an identified container

Replace `<CONTAINER>` with a **verified** name; do not insert credentials or untrusted names into shell commands.

~~~bash
docker logs --tail 100 --timestamps <CONTAINER>
docker inspect --format '{{.State.Status}} {{.State.ExitCode}} {{.State.OOMKilled}} {{if .State.Health}}{{.State.Health.Status}}{{else}}no-healthcheck{{end}}' <CONTAINER>
docker port <CONTAINER>
docker stats --no-stream
~~~

Interpretation:

| Finding | Investigation |
|---|---|
| `Exited`, nonzero exit code | Inspect error and previous dependencies |
| `Restarting` | Investigate crash loop, configuration or unavailable dependency |
| `OOMKilled=true` | Investigate host/container memory pressure before changing limits |
| `running`, health check failing | Inspect health evidence and application-specific checks |
| `running`, no health check | Status alone says nothing about application readiness |
| Proxy responds with an error | Separate proxy connectivity from upstream application status |

Some containers in the public configuration lack explicit health checks. Do not invent a health status for them.

## 6. Compose and network inspection

Work from the **actual deployment directory** after confirming its location. Avoid printing interpolated Compose configuration containing secrets into shared terminals or incident reports.

~~~bash
docker network ls
docker volume ls
docker compose ps
docker compose config --quiet
~~~

The final two commands apply only if the current directory contains the correct Compose project and its required private environment variables. Inspect container network membership with a narrowly scoped command:

~~~bash
docker inspect --format '{{json .NetworkSettings.Networks}}' <CONTAINER>
~~~

Network membership does not automatically prove connectivity to every other container or VLAN.

Use an approved functional check against a published endpoint as appropriate. A successful TCP connection alone does not prove Zabbix processing, MariaDB correctness or DNS filtering.

## 7. Corrective action decision

**Only after identifying the failure and approving change:**

- Resolve missing service dependencies or storage exhaustion using a controlled procedure.
- Restore an approved configuration from a known-good version when a mismatch is confirmed.
- Consider controlled restart of the affected service **only** when the service owner accepts the temporary interruption.
- Recreate containers or change images only with persistent data, backup, migration and rollback requirements understood.

Never delete `zabbix-db` or persistent volumes as a routine restart method. `latest` image tags in the inventory do not establish fixed application versions; avoid uncontrolled pulls.

## 8. Validation and closure

1. Confirm container status, actual application health and dependent service behavior.
2. Check fresh application logs after corrective action.
3. Test the expected internal URL, DNS or monitoring operation from an authorized client.
4. Verify Zabbix/Grafana/Uptime Kuma metrics where relevant; dashboards are complementary, not substitutes for application checks.
5. Record change, observed recovery, residual alerts, collection timestamps and rollback readiness.

## 9. Report template checklist

Capture container name, Compose project, host, stack dependencies, initial and final states, logs (sanitized), port/network context, application symptom, root cause versus hypothesis, approved action and functional validation. Do not describe a new repair as completed unless evidence exists.

## 10. References

- [Incident management](../incident-management.md)
- [Docker services and ten-container snapshot](../../containers/docker-services.md)
- [Sanitized main Compose file](../../../docker_configs/docker-compose.yml)
- [Pi-hole Compose](../../../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Portainer Compose](../../../docker_configs/lab-ti/portainer/docker-compose.yml)
- [DNS runbook](dns-resolution-failure.md)
- [Resource utilization runbook](host-resource-utilization.md)

**Evidence boundary:** This is an operational procedure. No new container outage, restart or recovery has been observed by preparing it.