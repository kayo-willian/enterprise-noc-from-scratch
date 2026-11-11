# Grafana — NOC Dashboards

**English** | [Português (Brasil)](../pt-BR/monitoramento/grafana.md)

**Evidence date:** November 6, 2026 · **Deployment:** Grafana on Debian 13 / Docker · **Data source:** Zabbix integration

Grafana visualizes the collected infrastructure metrics. These are **dated dashboard screenshots**, not a live feed; complete data-source settings and dashboard JSON exports are not included in the collected evidence.

## Dashboard Organization

![Grafana dashboard organization](../assets/images/monitoring/grafana/grafana_order.png)

| Dashboard section | Recorded targets |
|---|---|
| Web Applications & Containers | Website, Docker services, HTTP checks |
| Cisco Router | Catalyst C8200L interfaces, VLAN traffic |
| Cisco Switch | Catalyst C9200L hardware and interfaces |
| Servers & VoIP | Debian NOC server and Asterisk/FreeRADIUS host |
| Windows Workstations & Endpoints | Departmental PCs, CPU/RAM, network traffic |

## Web Applications and Containers

![Web applications and containers](../assets/images/monitoring/grafana/grafana_dashboard_web_containers.png)

The panels display HTTP response status and time, web performance history, service availability and Docker heartbeat indicators.

- **HTTP result:** `200 OK` for the monitored web application during the recorded check.
- **Services represented:** corporate website, Pi-hole, Grafana, Zabbix Web and Portainer.
- **Scope:** selected services, **not** all ten containers in the [Docker inventory](../containers/docker-services.md). A successful HTTP request does not verify every application function.

## Cisco Catalyst C8200L — Router

![Router interface status and traffic](../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

The first view contains `UP` indicators for selected interfaces/subinterfaces and throughput related to WAN, trunk and VLAN connections.

![Router throughput history](../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

The second view contains historical interface and VLAN-subinterface traffic series. These readings document monitored paths in the selected time window, not the router's full configuration, ACL behavior or continuous bandwidth.

## Cisco Catalyst C9200L — Switch

![Switch hardware and interface status](../assets/images/monitoring/grafana/grafana_dashboard_switch1.png)

Includes CPU, RAM, temperature, fans, power supplies, interface status and network throughput. Both `UP` and `DOWN` are visible; a down port can be unused or administratively disabled.

**Mapping issue:** multiple status panels show the identical label `Gi1/0/1 TRUNK-ROUTER`. The screenshots alone cannot map each panel to a distinct physical interface.

![Switch interface throughput](../assets/images/monitoring/grafana/grafana_dashboard_switch2.png)

Historical traffic series for selected trunk, departmental and infrastructure interfaces. Panel labels and physical switch ports require cross-checking against monitoring items and the [switch port map](../networking/switch-port-map.md).

![Switch interface errors and temperature](../assets/images/monitoring/grafana/grafana_dashboard_switch3.png)

Interface errors, CRC-related readings and temperature history provide diagnostic context for the observed period.

## Linux Servers and VoIP

![Asterisk and Zabbix Linux servers](../assets/images/monitoring/grafana/grafana_dashboard_asterisk.png)

| System | Function | Displayed status |
|---|---|---|
| Asterisk / FreeRADIUS host | IP telephony and network authentication | `ONLINE` |
| Zabbix infrastructure server | Debian/Docker monitoring stack | `ONLINE` |

The panels include CPU, RAM, availability and Zabbix Agent history. Host availability does **not** verify a completed SIP call or RADIUS authentication; see [Asterisk/FreeRADIUS](../services/asterisk-freeradius.md).

## Windows Workstations

![Windows workstation availability and resources](../assets/images/monitoring/grafana/grafana_dashboard_pcs1.png)

Eight departmental Windows systems appear in the captured dashboard:

| Status panel | Workstations |
|---|---:|
| `ONLINE` | 3 |
| `No data` | 5 |
| **Total** | **8** |

Some CPU/RAM data appear despite missing status values. `No data` means the corresponding query returned no usable result for that panel and time range; it does **not** establish that the computer was powered off. Possible causes include item/query configuration, agents, networking and host references; none was confirmed as a common cause.

![Windows CPU, RAM and traffic history](../assets/images/monitoring/grafana/grafana_dashboard_pcs2.png)

Historical CPU, RAM, download and upload series exist for selected stations. Some legends repeat workstation identifiers; item-to-host mapping needs verification. Six workstation IPv4 addresses also differed from their Zabbix registrations in the [November 6 comparison](zabbix-monitoring.md#workstation-address-discrepancies).

## Reading the Dashboards as Evidence

Grafana **visualizes** the Zabbix monitoring data; its graphs are not separate proof that Zabbix collected every item correctly. The recorded dashboard organizes data into five areas: web applications/containers, C8200L, C9200L, Linux servers/VoIP and Windows workstations. This organization supports cross-checking a service symptom against network, host and application metrics.

| Dashboard indicator | Technical reading | What still needs verification |
|---|---|---|
| HTTP **200 OK** | The selected web check received a successful HTTP response | Other URLs, client networks and application functions |
| Router `UP` and interface traffic | Selected interfaces had reported states and throughput samples | Router-side VLAN subinterfaces, NAT, routing and ACL operation |
| Switch CPU, memory, temperature, fans, errors and traffic | Device telemetry was available for selected items | Physical interface mapping; duplicated `Gi1/0/1 TRUNK-ROUTER` labels |
| Linux server `ONLINE` | Host/agent availability for the displayed interval | Successful SIP calls or RADIUS authentication |
| Windows `No data` | The particular panel query had no usable result | Host power state, agent, item support, Grafana query and time range |

**Missing values require two different checks.** First determine whether Zabbix has valid recent data for the affected item. If not, investigate the host/IP, collection interface, agent/SNMP and item error. If it does, check Grafana's data source, query, time range, variables and panel filters. Repeated interface labels should not be “corrected” without confirming the actual source item. Refer to the [Grafana No Data runbook](../noc-operations/runbooks/grafana-no-data.md).

The collected screenshots do **not** include complete data-source settings or dashboard JSON exports; a visually correct panel is evidence of the observed interface, not proof that the dashboards are reproducible solely from GitHub. All values above refer to the **November 6, 2026** captures; no new live test is claimed.

## Monitoring Findings Requiring Verification

| Recorded symptom | Required check |
|---|---|
| Five Windows status panels with `No data` | Zabbix item status, Grafana query, host identity and selected time range |
| Repeated Cisco interface labels | Zabbix item/interface identity and physical switch port mapping |
| Mixed `UP`/`DOWN` ports | Expected operational state against the current topology |
| Historical availability and HTTP readings | Independent service-specific functional tests when required |
| Incomplete exported dashboard configuration | Obtain data-source settings / dashboard JSON before claiming a reproducible dashboard |

**Related records:** [Zabbix monitoring](zabbix-monitoring.md) · [Cisco SNMP troubleshooting](snmp-troubleshooting.md) · [Docker services](../containers/docker-services.md)

The ten original screenshots above are preserved from **November 6, 2026**. They do not demonstrate subsequent incident resolution.
