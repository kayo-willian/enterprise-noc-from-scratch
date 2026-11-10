# Runbook — High CPU, Memory or Disk Utilization

**English** | [Português (Brasil)](../../pt-BR/operacoes-noc/runbooks/utilizacao-recursos-sistema.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** SYS / CNT / MON · **Status:** Proposed diagnostic procedure  
**Environment:** Debian 13 NOC host, separate Asterisk/FreeRADIUS Linux host, Windows endpoints, Docker services

## 1. Goal and historical context

Investigate sustained CPU load, memory pressure, disk-capacity exhaustion, inode exhaustion or resource-related application degradation. The November 6, 2026 inventory records two Linux Dell OptiPlex 3020 computers with Intel Core i5-4590 and approximately 8 GB RAM each. The main NOC hosts the Docker monitoring stack; the other Linux machine supports Asterisk/FreeRADIUS. Historical Grafana dashboards include resource metrics but **do not establish current saturation or a confirmed incident**.

A large percentage in one graph is not enough: correlate duration, user impact, expected workload and independent measurements. This runbook does not prescribe universal thresholds or a measured SLA.

## 2. Safety rules

- Obtain permission to inspect the system, its processes and logs.
- Use read-only commands first. Do not kill tasks, restart databases, delete logs, change resource limits, add swap, or clear caches merely to make a metric green.
- Before publishing process names, paths or logs, remove sensitive information.
- Never treat the root filesystem size in the inventory as a verified physical disk capacity.

## 3. Initial decision matrix

| Symptom | Questions to answer |
|---|---|
| CPU percentage high | For how long? Which process? Is the application slow? |
| High load average | Are tasks CPU-bound or waiting on I/O? Compare with CPU count |
| RAM usage high | Is memory reclaimable cache or actual process/swap pressure? |
| OOM events | Which process was terminated? Was a container limit involved? |
| Disk usage high | Which filesystem and mount point? Data, log or container storage? |
| Inodes exhausted | Are many small files preventing creation despite free bytes? |
| Container degraded | Is the host exhausted, or only one container constrained? |

## 4. Read-only Linux host examination

Run on the **identified** host. Exact command availability depends on installed packages.

~~~bash
date -Is
hostnamectl
uptime
nproc
free -h
cat /proc/meminfo | head -n 20
df -hT
df -i
lsblk -f
~~~

Interpret load average alongside `nproc` and elapsed time; a high load average does not by itself prove CPU usage is high. Interpret memory's `available` field and swap activity rather than treating cached memory as unusable.

Inspect major consumers:

~~~bash
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 15
ps -eo pid,comm,%cpu,%mem --sort=-%mem | head -n 15
~~~

For possible kernel memory exhaustion, read recent system messages with authorization:

~~~bash
journalctl -k --since '-2 hours' --no-pager
~~~

Search the result locally for OOM-related messages; avoid copying entire private logs into GitHub.

## 5. Docker-specific resource correlation

On the main Debian NOC computer:

~~~bash
docker stats --no-stream
docker ps --format 'table {{.Names}}\t{{.Status}}'
docker system df
~~~

`docker system df` is read-only; **do not** confuse it with `docker system prune`, which deletes data. The public monitoring Compose example binds MariaDB storage to `./zabbix-db-data` and Grafana storage to `./grafana-data`. These paths are relative to the actual deployment directory; they are not confirmed absolute locations.

If a filesystem is pressured, identify which mount backs the affected service and review authorized usage without modifying or exposing application data. A container reporting OOM does not automatically mean the physical host ran out of memory; check any per-container limits.

## 6. Windows endpoint checks

When a department workstation is affected and access is authorized:

~~~powershell
Get-ComputerInfo | Select-Object CsName,OsName
Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize
Get-Volume | Select-Object DriveLetter,FileSystem,Size,SizeRemaining
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name,CPU,WorkingSet64
~~~

`Get-Process` CPU is accumulated process time, not an instantaneous utilization percentage. A single snapshot must not be reported as a measured ongoing load.

## 7. Cause assessment and authorized response

| Verified condition | Potential action after approval |
|---|---|
| Specific process repeatedly consumes CPU | Examine application logs/workload and fix cause; plan restart only if justified |
| Sustained memory pressure with swap/OOM | Examine allocation and limits; consider carefully reviewed tuning or workload change |
| Log files consume disk | Review retention and logging policy; rotate through approved maintenance |
| Database/volume fills partition | Address storage capacity and retention with backup before changes |
| Filesystem out of inodes | Identify file creation pattern; remove nothing before ownership/impact assessment |
| Misleading dashboard panel | Review query, unit, aggregation and sampling, not server configuration |

No fixed recovery action should be selected from a screenshot alone. Escalate before interrupting monitoring, database, voice or shared network services.

## 8. Validation criteria

1. Verify resource measurements **after** the authorized action, using the same host and time window.
2. Check application health separately (e.g., Zabbix service behavior, Grafana response or VoIP functional test).
3. Verify that resource pressure and relevant errors no longer recur during an appropriate observation interval.
4. Compare monitoring panels against host measurements, respecting sampling delays and unit conversions.
5. Record original symptom, duration, confirmed cause, action, metrics and unresolved risks.

## 9. Evidence record

Capture time zone, host, filesystem/container, initial and new measurements, process/storage analysis, user impact, change authorization, validation window and supporting sanitized evidence. Do not claim improvement without paired measurements.

## 10. References

- [Incident management](../incident-management.md)
- [Linux and workstation inventory](../../endpoints/workstation-inventory.md)
- [Docker infrastructure](../../containers/docker-services.md)
- [Grafana metrics](../../monitoring/grafana-monitoring.md)
- [Docker failure runbook](docker-service-failure.md)

**Status:** This is a proposed diagnostic runbook; no performance incident or completed optimization is asserted.