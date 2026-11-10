# Runbook — DNS Resolution Failure

**English** | [Português (Brasil)](../../pt-BR/operacoes-noc/runbooks/falhas-resolucao-dns.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** DNS / NET / CNT · **Document type:** Operational troubleshooting runbook  
**Environment:** Pi-hole container on Debian NOC host; departmental networks; Docker reverse proxy and internal services

## 1. Purpose and recorded environment

This runbook separates DNS lookup failures from IP connectivity, application failure, deliberate DNS filtering and routing problems. The November 6 record identifies the Debian host `192.168.10.12/24` and a Pi-hole container with TCP/UDP port **53** published. The Pi-hole dashboard recorded **12,293 queries**, **1,827 blocked**, **14.9% blocked** and **13 active clients** within its displayed period. These counters are historical and do not prove that every VLAN or client used Pi-hole.

A hostname resolving is not proof that the destination application works. Conversely, a website being unreachable does not necessarily indicate DNS failure.

## 2. Safety and prerequisites

- Obtain permission to examine client DNS settings and the authorized resolver. Use current addresses, not historical host values.
- Begin with read-only checks. Never disable filtering, replace organization-wide DNS settings, remove blocklists or flush shared DNS caches without an approved change and rollback.
- DNS logs and client queries may contain sensitive information; sanitize before publication.
- Verify whether the target is an Internet name, an internal name, an intentionally blocked domain or a container-only DNS name.

## 3. Symptoms and investigation paths

| Symptom | Initial distinction |
|---|---|
| Name fails but destination IP responds | DNS path, record or filtering likely relevant |
| Both name and IP fail | Routing, link, firewall or application may be involved |
| `NXDOMAIN` | Name not found by queried DNS source; verify expected zone/record |
| `SERVFAIL` | Resolver/upstream/delegation problem possible |
| `REFUSED` or timeout | Query policy, access filtering, unreachable server or missing listener |
| One client affected, others healthy | Client resolver/DHCP/cache or network segment |
| Only a selected domain blocked | Intended Pi-hole filtering versus a mistaken rule |

## 4. Diagnostic sequence

### A. Client resolver and route

On Linux:

~~~bash
ip -br addr
ip route
cat /etc/resolv.conf
getent ahostsv4 example.org
~~~

If `resolvectl` is available:

~~~bash
resolvectl status
~~~

On Windows (PowerShell):

~~~powershell
ipconfig /all
Resolve-DnsName example.org
~~~

Compare the configured DNS server with the approved design. No DHCP-provided DNS option is established across all laboratory VLANs in the published evidence.

### B. Query a verified resolver directly

With `dig` installed, substitute the **approved, current** resolver IP and use an authorized test name:

~~~bash
dig @<VERIFIED_DNS_SERVER_IP> example.org A +time=2 +tries=1
dig @<VERIFIED_DNS_SERVER_IP> example.org AAAA +time=2 +tries=1
~~~

Examine `SERVER`, `status`, returned records and response time. Different results between the configured resolver and a separately approved diagnostic resolver can narrow the fault domain, but do not authorize bypassing corporate filtering.

Do not assume TCP/UDP 53 connectivity from the existence of published Docker ports. If UDP queries fail, check whether the authorized path supports TCP queries:

~~~bash
dig +tcp @<VERIFIED_DNS_SERVER_IP> example.org A +time=2 +tries=1
~~~

### C. Inspect Pi-hole and Docker without mutation

On the main Debian Docker host:

~~~bash
docker ps --filter name=pihole
docker logs --tail 80 pihole
docker port pihole
sudo ss -lntup | grep ':53'
~~~

The port listing and logs can identify the published port and recent messages; inspect whether binding conflicts, upstream failures or access controls explain symptoms. Remember that the Pi-hole container may belong to a **separate Compose stack** from the primary Zabbix/Grafana stack.

### D. Confirm expected outcome with a functional check

Test a known-allowed name and, only where approved, a known-blocked test case. An intentional Pi-hole block is not a service outage. For internal applications, confirm both name resolution and the **separate application endpoint** (for example an approved HTTPS request through the reverse proxy).

## 5. Decision and correction

| Confirmed diagnosis | Possible authorized response |
|---|---|
| Wrong DHCP-supplied resolver | Correct source configuration after validating scope and lease behavior |
| Pi-hole container not operating | Inspect service dependencies and logs; plan controlled recovery |
| DNS upstream unavailable | Restore/reconfigure approved upstream after independent verification |
| Missing internal record | Correct documented zone/record with change tracking |
| Intended blocklist match | Do not remove unless the domain is reviewed and exception approved |
| DNS works but HTTP fails | Transfer to application/reverse proxy troubleshooting |

Never edit Pi-hole records, client configurations or Docker mappings without documented approval and ability to revert.

## 6. Recovery validation

1. Confirm the correct resolver is selected by affected clients.
2. Verify a new successful response for a permitted test name, with timestamp and DNS server recorded.
3. Verify expected application access separately.
4. Check Pi-hole dashboard/logs for current processing, not solely historical query totals.
5. Check an affected and an unaffected client if the incident scope was departmental; document residual restrictions.

## 7. Incident report essentials

Capture client/VLAN, DHCP resolver supplied, test name classification (public/internal/blocked), timestamp, queried server, response code, timing, compared client results, actual corrective change, validation and remaining impact. Sanitize real query names where needed.

## 8. References

- [Incident management](../incident-management.md)
- [Pi-hole and Uptime Kuma evidence](../../services/dns-and-availability.md)
- [Docker architecture](../../containers/docker-services.md)
- [Router and DHCP evidence boundaries](../../networking/router-c8200l.md)
- [Docker service failure](docker-service-failure.md)

**Document scope:** Reference diagnostic procedure based on dated laboratory evidence, not an incident-execution record.