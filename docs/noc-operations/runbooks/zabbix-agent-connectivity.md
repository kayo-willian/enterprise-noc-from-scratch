# Runbook — Zabbix Agent Connectivity

**English** | [Português (Brasil)](../../pt-BR/operacoes-noc/runbooks/conectividade-zabbix-agent.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** MON · **Document type:** Operational troubleshooting runbook  
**Environment:** Debian monitoring host in VLAN 10; Windows departmental hosts; Linux VoIP/authentication host in VLAN 50

## 1. Purpose and evidence boundary

Use this runbook when Zabbix reports an unavailable agent interface, missing passive-agent metrics, or intermittent host data. First distinguish **host failure**, **agent failure**, and **monitoring misconfiguration**. In the November 6, 2026 snapshot Zabbix recorded 12 registered hosts, seven available and five unavailable; six workstation addresses differed between collected records. These observations do not establish a common root cause or a subsequently successful repair.

The main monitoring computer was recorded at `192.168.10.12/24` (Debian 13); the Asterisk/FreeRADIUS Linux system at `192.168.50.2/24`. Workstation addresses may change through DHCP. All recorded IPs are historical examples, **not targets to assume are currently assigned**.

## 2. Safety and prerequisites

- Obtain permission to diagnose the host and use a management terminal with access to the relevant VLAN.
- Identify the affected **Zabbix host name**, monitored IP/DNS, interface type, latest item error, last valid sample, and expected check direction.
- Start with read-only inspection. Do not restart agents, change firewall rules, disable protection, or change addressing during initial triage.
- Do not publish credentials, unrestricted agent settings, private machine identifiers, or raw logs containing sensitive data.

## 3. Scope the symptom

| Observation | Interpretation to investigate |
|---|---|
| Ping fails and other services also fail | Network path or host may be unavailable; ICMP blocking alone is inconclusive |
| Host reachable, TCP 10050 unavailable | Passive agent not listening, filtering, or wrong target |
| TCP 10050 connects, Zabbix items fail | Agent permissions, allowed-server restrictions, key support or item settings |
| Active agent checks fail, passive checks work | Active server/proxy connection, hostname or port 10051 path |
| Grafana displays `No data` while Zabbix has values | Visualization, data source, query or time-range issue |

## 4. Read-only diagnostic sequence

### Step A — Confirm Zabbix configuration

In **Data collection → Hosts**, compare the host's agent interface address with the machine's presently observed address. Check whether the affected items are **Zabbix agent** (passive) or **Zabbix agent (active)**, and inspect the exact item error and data timestamp.

On a Windows machine (local PowerShell):

~~~powershell
ipconfig /all
Get-Service 'Zabbix Agent','Zabbix Agent 2' -ErrorAction SilentlyContinue
Get-NetTCPConnection -State Listen -LocalPort 10050 -ErrorAction SilentlyContinue
~~~

On a Linux host:

~~~bash
hostnamectl
ip -br addr
ip route
systemctl status zabbix-agent zabbix-agent2 --no-pager
sudo ss -lntp | grep ':10050'
~~~

Not every Linux host runs an agent as a systemd service: the documented main monitoring stack also includes a `zabbix-agent` **container**.

### Step B — Inspect the monitoring server

From the Debian Docker host, inspect the running containers and recent logs:

~~~bash
docker ps --filter name=zabbix
docker logs --tail 80 zabbix-server
docker logs --tail 80 zabbix-agent
~~~

The public Compose example publishes agent port **10050** and server port **10051**. Those ports describe configuration, not proof of end-to-end reachability.

### Step C — Test the actual path

From an authorized monitoring-side Linux shell, replace the placeholder with the **currently verified** endpoint:

~~~bash
ping -c 3 <CURRENT_HOST_IP>
nc -vz -w 3 <CURRENT_HOST_IP> 10050
~~~

If installed and the agent permits the request, an approved read-only item test can be performed:

~~~bash
zabbix_get -s <CURRENT_HOST_IP> -p 10050 -k agent.ping
~~~

A failed `ping` alone does not prove host failure. A successful TCP handshake alone does not prove supported monitoring items. For active checks, inspect whether the agent reaches its configured server/proxy on the appropriate listening port and whether its configured hostname matches the Zabbix host record.

### Step D — Interpret and correlate

| Finding | Next action |
|---|---|
| IP differs from Zabbix registration | Confirm DHCP lease/device identity before proposing any host-interface correction |
| Agent service/container stopped | Examine logs, configuration and service ownership before authorized recovery |
| Access denied by agent | Check authorized server list and agent configuration without weakening access restrictions |
| Unsupported monitoring key | Check item type, platform support, version and agent logs |
| Multiple hosts unavailable simultaneously | Review common routing, server/proxy and monitoring dependencies before individual edits |

## 5. Corrective-action decision

**No configuration changes are authorized by this runbook alone.** After confirming the cause, document the exact setting to change, expected impact, approval and rollback. A stale Zabbix host address can be corrected only after verifying the device's current identity and address. Avoid broadly opening agent ports or disabling firewalls as a troubleshooting shortcut. For repeat DHCP changes, consider an approved hostname or addressing strategy rather than assuming static leases already exist.

## 6. Recovery validation

1. Verify the host is reachable by its expected management path.
2. Confirm the appropriate agent item returns a **new timestamped value** in Zabbix.
3. Check whether the agent interface availability and original trigger have recovered.
4. Inspect one additional relevant item, rather than relying on a single green indicator.
5. Record both success and remaining unsupported or unavailable items; do not extrapolate a single repair to all historical alerts.

## 7. Incident record fields

Record detection time and timezone, device identity, VLAN, observed current address, registered Zabbix address, item type/error, read-only tests, approved change, before/after evidence, rollback availability, validation and final status.

## 8. References

- [Incident management](../incident-management.md)
- [Zabbix monitoring and historical limitations](../../monitoring/zabbix-monitoring.md)
- [Workstation inventory and DHCP differences](../../endpoints/workstation-inventory.md)
- [Docker infrastructure](../../containers/docker-services.md)
- [Grafana no-data runbook](grafana-no-data.md)

**Document scope:** Reference diagnostic procedure based on dated laboratory evidence, not an incident-execution record.