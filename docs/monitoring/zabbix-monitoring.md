# Zabbix Monitoring

[English](zabbix-monitoring.md) | [Português (Brasil)](../pt-BR/monitoramento/zabbix.md)

## 1. Overview

The Enterprise NOC — From Scratch laboratory uses Zabbix to monitor network equipment, Linux servers, Windows workstations, infrastructure services, and network traffic.

The monitoring environment integrates physical Cisco networking equipment with services hosted on Linux systems and Docker containers.

This documentation is based on screenshots collected on **November 6, 2026**.

The screenshots represent the environment at the time of collection. They are not live monitoring feeds.

## 2. Monitoring Architecture

The Zabbix environment is hosted on the main infrastructure computer, running Debian GNU/Linux 13.

The Docker deployment includes:

| Component | Purpose |
|---|---|
| Zabbix Server | Collection and processing of monitoring data |
| Zabbix Web | Web interface and dashboards |
| Zabbix Agent | Collection of system monitoring data |
| MariaDB | Storage of Zabbix monitoring information |

The monitored infrastructure includes:

- Cisco Catalyst C8200L router.
- Cisco Catalyst C9200L switch.
- Debian infrastructure server.
- Debian Asterisk and FreeRADIUS server.
- Eight Windows workstations.

The Cisco devices are monitored through SNMP interfaces, while the documented operating systems use Zabbix Agent interfaces.

Additional HTTP and service monitoring information is presented in the dashboards.

For details about the container deployment, see [Docker Infrastructure and Services](../containers/docker-services.md).

## 3. Zabbix System Information

![Zabbix system information](../assets/images/monitoring/zabbix/zabbix_info_system.png)

The system information page provides the following snapshot:

| Parameter | Observed value |
|---|---:|
| Zabbix Server version | 7.0.32 |
| Zabbix Frontend version | 7.0.32 |
| Registered hosts | 12 |
| Enabled hosts | 12 |
| Templates | 356 |
| Total items | 1,820 |
| Enabled items | 1,698 |
| Disabled items | 9 |
| Unsupported items | 113 |
| Total triggers | 1,082 |
| Enabled triggers | 1,073 |
| Disabled triggers | 9 |
| Triggers in problem state | 34 |
| High-availability cluster | Inactive |

The screenshot confirms that the Zabbix Server was running when the information was collected.

However, 113 unsupported items and 34 triggers in a problem state indicate that the monitoring environment still required investigation.

The number of unsupported items does not identify their individual causes.

## 4. Dashboard Evidence

Six screenshots document consecutive sections of the monitoring dashboards.

They are presented below in their original order.

### 4.1 Unified Infrastructure Dashboard

![Zabbix unified infrastructure dashboard](../assets/images/monitoring/zabbix/zabbix_dashboard1.png)

The unified dashboard provides an overview of:

- Host availability.
- Alarm severity.
- Application and service monitoring.
- Cisco infrastructure metrics.
- Linux server resource utilization.
- Asterisk service indicators.

At the time of collection, the availability widget reported:

| Status | Hosts |
|---|---:|
| Available | 7 |
| Unavailable | 5 |
| Total | 12 |

The interface breakdown showed five available and five unavailable passive Zabbix Agent interfaces, along with two available SNMP interfaces.

The service widgets also displayed positive checks for the corporate website, Pi-hole, Grafana, Zabbix Web, Portainer, and Asterisk.

These results represent individual monitoring observations rather than guaranteed long-term availability.

### 4.2 Cisco Router Interfaces and VLAN Traffic

![Cisco router interface and VLAN monitoring](../assets/images/monitoring/zabbix/zabbix_dashboard2.png)

This section presents monitoring information associated with the Cisco Catalyst C8200L router.

The dashboard includes:

- Interface and subinterface status.
- WAN and trunk traffic.
- VLAN-related traffic visualization.
- Network throughput over the displayed observation period.

The interface indicators are displayed as operational in the screenshot.

These observations demonstrate monitoring data collection but do not independently verify every routing or access-control policy.

### 4.3 Cisco Catalyst 9200L Monitoring

![Cisco Catalyst 9200L monitoring dashboard](../assets/images/monitoring/zabbix/zabbix_dashboard3.png)

The switch dashboard provides visibility into:

- CPU utilization.
- Memory utilization.
- Temperature sensors.
- Cooling and power indicators.
- Ethernet interface status.
- Traffic distribution across interfaces.

The screenshot shows a combination of interfaces marked as `up` and `down`.

An interface in the `down` state does not automatically indicate an incident. Unused, disconnected, or administratively disabled ports may legitimately remain down.

The screenshot also contains some truncated labels. Interface identities must be checked against the monitoring configuration before assigning specific physical-port functions.

### 4.4 Network Traffic, Service Performance, and Events

![Zabbix traffic, service performance, and incident monitoring](../assets/images/monitoring/zabbix/zabbix_dashboard4.png)

This section displays additional infrastructure monitoring information:

- Core and server network throughput.
- Departmental switch-port traffic.
- Corporate website response performance.
- CPU and memory utilization across monitored systems.
- Events and incident records.

The event panel contains incident and resolved-event entries.

These records demonstrate event tracking during the observed period, but they do not establish that every recorded issue was permanently resolved.

### 4.5 Infrastructure Resource Utilization

![Zabbix infrastructure resource utilization](../assets/images/monitoring/zabbix/zabbix_dashboard5.png)

This section presents resource-consumption indicators for monitored equipment.

The dashboard includes:

- CPU utilization indicators.
- RAM utilization indicators.
- Resource rankings across monitored computers and servers.

The collected screenshot also contains multiple indicators labeled with the same switch name.

The screenshots show repeated or truncated labels. Their values are preserved as displayed, without treating each label as a distinct monitoring item.

The screenshot is retained as evidence of the dashboard configuration observed on November 6, 2026.

### 4.6 Network Throughput and Windows Workstations

![Zabbix network throughput and Windows workstation monitoring](../assets/images/monitoring/zabbix/zabbix_dashboard6.png)

The final dashboard screenshot presents:

- Internet and core routing throughput.
- Traffic distribution across VLAN subinterfaces.
- Download traffic for Windows workstations.
- Upload traffic for Windows workstations.

The graphs demonstrate that the monitoring platform contained historical network-traffic series for selected interfaces and computers.

They do not establish complete monitoring coverage for every workstation.

## 5. Host Configuration and Availability

### 5.1 Configured Hosts

![Zabbix configured host list](../assets/images/monitoring/zabbix/zabbix_hosts.png)

The host configuration screen identifies twelve registered hosts:

- Eight Windows workstations.
- The main Zabbix infrastructure server.
- The Asterisk and FreeRADIUS Linux server.
- The Cisco Catalyst C8200L router.
- The Cisco Catalyst C9200L switch.

The Windows and Linux systems are associated with Zabbix Agent monitoring.

The Cisco router and switch use SNMP interfaces on UDP port 161.

### 5.2 Host Status and Incidents

![Zabbix host availability and incident list](../assets/images/monitoring/zabbix/zabbix_hosts2.png)

The second host-list screenshot complements the previous image.

It shows:

- Host availability indicators.
- Registered monitoring interfaces.
- Active host status.
- Links to collected data and graphs.
- Incident counters.

Although all twelve hosts were enabled, not all monitoring interfaces were available.

**A host being enabled in Zabbix does not mean its monitoring agent is reachable.**

## 6. Addressing Inconsistencies

A comparison between the Zabbix host interfaces and the workstation `ipconfig` photographs revealed six mismatches.

| Workstation | Photographed IPv4 | Zabbix registered IPv4 |
|---|---|---|
| IT 2 | `192.168.10.13` | `192.168.10.11` |
| Accounting 2 | `192.168.20.12` | `192.168.20.10` |
| Accounting 3 | `192.168.20.13` | `192.168.20.12` |
| Finance 1 | `192.168.30.10` | `192.168.30.13` |
| Sales 1 | `192.168.40.11` | `192.168.40.14` |
| Sales 2 | `192.168.40.10` | `192.168.40.13` |

Accounting 1 and Finance 2 had matching addresses in the compared records.

These inconsistencies may contribute to agent availability problems or missing monitoring data.

This collection does not establish a single root cause for every problem; agent settings, host addressing, firewall behavior, connectivity, and monitoring item configuration can all affect collection.

The photographed addresses are historical observations from November 6, 2026.

For the workstation inventory, see [Workstation and Server Inventory](../endpoints/workstation-inventory.md).

## 7. Interpretation of Historical Results

The November 6 capture records **five unavailable hosts, 113 unsupported items, 34 problem triggers, six address discrepancies** and some switch interfaces shown as down. The DHCP-based workstation addressing may contribute to mismatches but does not establish the cause of every alert. These measurements describe the captured state; individual item and interface status requires its own diagnosis.

## 8. Relationship with Grafana

Zabbix supplies monitoring data for Grafana dashboards covering Cisco equipment, Windows and Linux hosts, Asterisk and web services. See the [Grafana evidence](grafana-monitoring.md) for panel-specific observations.

## 9. Evidence Summary

| Evidence | Original filename |
|---|---|
| Unified monitoring | `zabbix_dashboard1.png` |
| Router interfaces and VLANs | `zabbix_dashboard2.png` |
| Cisco switch monitoring | `zabbix_dashboard3.png` |
| Traffic, performance, and events | `zabbix_dashboard4.png` |
| Infrastructure resource utilization | `zabbix_dashboard5.png` |
| Network throughput | `zabbix_dashboard6.png` |
| Registered hosts | `zabbix_hosts.png` |
| Host status and incidents | `zabbix_hosts2.png` |
| System information | `zabbix_info_system.png` |

All screenshots were collected on **November 6, 2026**.

This documentation describes the observed environment and its limitations. It does not claim uninterrupted availability, complete monitoring coverage, or a fully remediated infrastructure.
