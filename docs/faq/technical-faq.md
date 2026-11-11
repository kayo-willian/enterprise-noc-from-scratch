# Enterprise NOC — Technical FAQ

**English** | [Português (Brasil)](../pt-BR/faq/perguntas-frequentes.md)

**Project:** Enterprise NOC — From Scratch  
**Organization:** Tapajós Inovações  
**Environment:** Physical enterprise infrastructure laboratory  
**Documentation languages:** English and Brazilian Portuguese  

---

## Overview

This FAQ answers technical and architectural questions about the Enterprise NOC — From Scratch project.

It covers the laboratory infrastructure, Cisco networking equipment, Linux systems, Docker containers, monitoring platforms, enterprise services, troubleshooting activities, and implementation evidence.

The objective is to explain not only which technologies are present, but also their responsibilities, integration, technical decisions, and documented limitations.

The FAQ complements the technical documentation. It does not replace configuration records, infrastructure inventories, or operational procedures.

## Contents

1. Project Fundamentals
2. Physical Infrastructure and Hardware
3. Cisco Networking and VLANs
4. Wireless Networking and IoT
5. Linux, Docker, and Container Infrastructure
6. Monitoring and Observability
7. Enterprise Infrastructure Services
8. Security, Troubleshooting, and Project Evidence

---

# 1. Project Fundamentals

### 01. What is Enterprise NOC — From Scratch?

A physical enterprise infrastructure laboratory covering Cisco networking, Linux, Docker services, VoIP, DNS and centralized monitoring. The repository contains configurations, inventories, troubleshooting records and dated evidence.

### 02. Is Tapajós Inovações a real company?

No. Tapajós Inovações is the fictional business scenario; the equipment and laboratory records are real.

### 03. Why was the project designed around a Network Operations Center?

To connect network deployment, service availability, monitoring and troubleshooting in one documented environment. The NOC model organizes those operational activities.

### 04. Which business problems does the project address?

The fictional scenario identifies four issues: unreliable cabling, insecure Wi-Fi, unstable IP telephony and insufficient monitoring. These are scenario requirements, not verified current failures.

### 05. Is the infrastructure intended for production use?

No production certification is claimed. The project demonstrates deployment and monitoring on physical laboratory equipment; production use would require its own security, backup, resilience and operational validation.

### 06. Which period does the project documentation cover?

Records cover October–November 2026, including the November 4 switch configuration and November 6 infrastructure inventory and monitoring captures. Each record represents its collection date.

**Related documentation:**

- [Project README](../../README.md)
- [Infrastructure Overview](../architecture/infrastructure-overview.md)
- [Consolidated Logical Topology](../networking/consolidated-logical-topology.md)

---

# 2. Physical Infrastructure and Hardware

### 07. Which physical networking devices are used?

The principal networking devices are:

- Cisco Catalyst C8200L router.
- Cisco Catalyst C9200L switch.
- TP-Link Archer AX53 wireless equipment.
- Category 6 patch panel.
- Network rack and structured Ethernet cabling.

The laboratory also includes Linux computers, Windows workstations, Grandstream IP telephones, and an Amazon Alexa device.

Each component contributes to the project's physical or logical infrastructure.

### 08. What is the purpose of the network rack and patch panel?

The rack organizes networking equipment, cabling, and supporting infrastructure in a centralized physical installation.

The patch panel provides structured cable termination and allows connections to be organized through patch cords.

Separating fixed cabling from equipment connections improves physical organization and makes maintenance and cable identification easier.

The photographs document the installation, but do not constitute a complete certification report for every cable connection.

### 09. Which Ethernet wiring standard is used?

The laboratory uses the T568A pinout for manually assembled Ethernet cables.

The conductor order is:

| Pin | Wire color |
|---|---|
| 1 | White/Green |
| 2 | Green |
| 3 | White/Orange |
| 4 | Blue |
| 5 | White/Blue |
| 6 | Orange |
| 7 | White/Brown |
| 8 | Brown |

A straight-through cable using this standard has the same T568A termination at both ends.

The wiring pattern identifies the adopted standard; it does not independently certify the electrical performance of every assembled cable.

### 10. How many computers are included in the laboratory?

The infrastructure inventory contains ten computers:

| Department or Role | Computers |
|---|---:|
| IT / NOC | 2 |
| Accounting | 3 |
| Finance | 2 |
| Sales | 2 |
| Asterisk / FreeRADIUS server | 1 |
| **Total** | **10** |

Eight computers run Windows, while two are assigned to Linux infrastructure roles.

The inventory includes specifications where these were visible in the collected evidence.

### 11. Are the two Linux computers identical?

They have similar documented hardware specifications, including Dell OptiPlex 3020 systems with Intel Core i5-4590 processors and approximately 8 GB of RAM.

However, they perform different functions.

The main NOC computer runs Debian GNU/Linux 13 (Trixie) and hosts the Docker environment.

The second computer runs the documented Debian forky/sid environment and hosts Asterisk and FreeRADIUS.

Their operating-system releases should not be treated as identical.

### 12. What do the physical photographs prove?

The photographs document the presence and physical arrangement of the equipment at the time of collection.

They show the rack, Cisco devices, patch panel, structured cabling, and selected workstations.

However, photographs alone cannot establish successful inter-VLAN routing, correct access-control policies, complete interface functionality, or continuous service availability.

Those properties require corresponding configuration records and operational tests.

**Related documentation:**

- [Physical Infrastructure](../evidence/physical-infrastructure.md)
- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Evidence Collection Record](../evidence/evidence-collection-2026-11-06.md)

---

# 3. Cisco Networking and VLANs

### 13. What are the roles of the Cisco router and switch?

The C8200L is the router in the architecture; the C9200L records switching, VLAN assignments and the router-facing trunk. The complete C8200L configuration was not collected. See [router](../networking/router-c8200l.md) and [switch snapshot](../networking/switch-vlan-snapshot-2026-11-04.md).

### 14. Why does the infrastructure use seven VLANs?

VLANs **10/20/30/40/50/60/70** separate IT/NOC, Accounting, Finance, Sales, VoIP/Authentication, corporate Wi-Fi and IoT at Layer 2. See the [VLAN inventory](../networking/vlans.md).

### 15. What is the purpose of the trunk between the router and switch?

A trunk can carry multiple tagged VLANs. Switch interface `Gi1/0/1` is configured as the router-facing trunk; its allowed-VLAN list and the router-side interface were not captured. See the [switch snapshot](../networking/switch-vlan-snapshot-2026-11-04.md).

### 16. How are the switch interfaces distributed?

The November 4 snapshot assigns `Gi1/0/2–3` to VLAN 10, `4–6` to 20, `7–8` to 30, `9–10` to 40, `11–13` to 50, `14` to 70 and `15` to 60. See the [port map](../networking/switch-port-map.md).

### 17. Why is interface Gi1/0/11 treated differently?

`Gi1/0/11` contains `switchport access vlan 50` and `spanning-tree portfast trunk`, but no explicit `switchport mode access`. Its effective switching mode is not established by that snapshot. See the [port map](../networking/switch-port-map.md).

### 18. How are IP addresses assigned to workstations?

Workstations use DHCP. Captured endpoint gateways were `192.168.10.1`, `.20.1`, `.30.1` and `.40.1`; the DHCP server and pools were not established. See [VLANs](../networking/vlans.md).

### 19. Are departmental VLANs completely isolated?

The switch VLANs provide Layer 2 separation. Complete Layer 3 isolation and router ACL enforcement were not verified; those restrictions remain architectural requirements. See [VLANs](../networking/vlans.md).

### 20. Is inter-VLAN routing and NAT fully documented?

No. The records document the C8200L hardware, the switch-side trunk and observed gateways, but not complete router subinterfaces, NAT rules or end-to-end routing tests. See [C8200L](../networking/router-c8200l.md).

**Related documentation:**

- [VLAN Segmentation](../networking/vlans.md)
- [Consolidated Logical Topology](../networking/consolidated-logical-topology.md)
- [Cisco Catalyst C8200L](../networking/router-c8200l.md)
- [Switch Port Mapping](../networking/switch-port-map.md)
- [Switch Configuration Snapshot](../networking/switch-vlan-snapshot-2026-11-04.md)

---

# 4. Wireless Networking and IoT

### 21. Why are two TP-Link Archer AX53 devices used?

They provide separate corporate Wi-Fi (VLAN 60) and IoT (VLAN 70) roles. The devices are distinct physical Archer AX53 units.

### 22. Which switch interfaces connect the wireless networks?

The C9200L records corporate Wi-Fi on `Gi1/0/15` (VLAN 60) and IoT on `Gi1/0/14` (VLAN 70). See the [port map](../networking/switch-port-map.md).

### 23. How is Amazon Alexa integrated into the network?

Amazon Alexa is associated with the dedicated IoT Archer AX53, connected to the C9200L on VLAN 70. Alexa's IP address and application-level connectivity were not recorded. See [IoT](../networking/iot-vlan70.md).

### 24. Do the wireless routers operate in access point mode?

Their configurations were not captured. AP mode could bridge clients onto the upstream VLAN; router/NAT mode could place them on separate subnets. Neither mode is confirmed. See [Wi-Fi](../networking/corporate-wifi-vlan60.md) and [IoT](../networking/iot-vlan70.md).

### 25. Does corporate Wi-Fi authentication use FreeRADIUS?

A FreeRADIUS service is documented in VLAN 50, but there is no AX53 RADIUS client configuration or successful wireless-authentication log to confirm that integration. See [Asterisk/FreeRADIUS](../services/asterisk-freeradius.md).

**Related documentation:**

- [Corporate Wi-Fi — VLAN 60](../networking/corporate-wifi-vlan60.md)
- [IoT Network — VLAN 70](../networking/iot-vlan70.md)
- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)

---

# 5. Linux, Docker, and Container Infrastructure

### 26. What is the main NOC server configuration?

The NOC host is a Dell OptiPlex 3020 with Intel i5-4590, approximately 8 GB RAM, Debian 13, and `192.168.10.12/24`. It hosts the main Docker/monitoring services. See [inventory](../endpoints/workstation-inventory.md).

### 27. Why is Docker used in the project?

Docker runs the infrastructure applications as containers, with Compose defining services and dependencies. It does not imply high availability. See [Docker services](../containers/docker-services.md).

### 28. Which containers were running during evidence collection?

Ten containers were recorded as running on November 6: `reverse-proxy`, `zabbix-web`, `zabbix-server`, `uptime-kuma`, `zabbix-db`, `grafana`, `zabbix-agent`, `site-estatico`, `pihole` and `portainer`. See [Docker inventory](../containers/docker-services.md).

### 29. What are the differences between Docker Compose and Portainer?

Compose defines multi-container deployments in YAML; Portainer provides a graphical interface for Docker administration. Both are present in the laboratory.

### 30. Why are Nginx and Apache both present?

Nginx acts as the reverse proxy; Apache serves the static corporate site through `site-estatico`. See [Docker services](../containers/docker-services.md).

### 31. What is MariaDB used for?

MariaDB stores Zabbix monitoring data in the `zabbix-db` container. See [Docker services](../containers/docker-services.md).

### 32. Can the Docker infrastructure be reproduced directly from GitHub?

Not as a verified one-command deployment. Public Compose files are sanitized and omit local secrets, certificates, persistent data and machine-specific prerequisites. See [Docker services](../containers/docker-services.md).

**Related documentation:**

- [Docker Infrastructure and Services](../containers/docker-services.md)
- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Docker Compose Configuration](../../docker_configs/docker-compose.yml)

---

# 6. Monitoring and Observability

### 33. Why are Zabbix and Grafana used together?

Zabbix collects and processes monitoring items; Grafana visualizes them through the Zabbix integration. See [Zabbix](../monitoring/zabbix-monitoring.md) and [Grafana](../monitoring/grafana-monitoring.md).

### 34. How extensive was the Zabbix monitoring environment?

The November 6 snapshot recorded **12 hosts, 1,820 items, 1,698 enabled items, 113 unsupported items and 34 triggers in problem state**. See [Zabbix evidence](../monitoring/zabbix-monitoring.md).

### 35. How are Cisco devices and operating systems monitored?

Cisco equipment uses SNMP interfaces in Zabbix; Linux/Windows hosts use Zabbix Agent interfaces. Dashboards include CPU, memory, traffic and interface status. See [Zabbix](../monitoring/zabbix-monitoring.md).

### 36. Was the Cisco switch SNMP problem resolved?

Yes, for the **November 4 recorded SNMP case**: the community mismatch was corrected, `{$SNMP_COMMUNITY}` was configured and the monitoring cache refreshed, restoring discovery. This does not imply that unrelated later alerts were resolved. See [SNMP case study](../monitoring/snmp-troubleshooting.md).

### 37. Why did some Grafana workstation panels display `No data`?

On November 6, three workstation panels showed `ONLINE` and five `No data`. Missing samples may arise from agents, host addressing, item configuration or time-range selection; the screenshots do not determine one cause. See [Grafana](../monitoring/grafana-monitoring.md).

### 38. How can DHCP affect Zabbix monitoring?

Six workstation IPv4 addresses differed between captured endpoint data and Zabbix host registrations. DHCP changes are a possible contributor, not a proven common cause. See [workstation inventory](../endpoints/workstation-inventory.md).

### 39. What do the 113 unsupported Zabbix items indicate?

The **113 unsupported items** could not produce valid data under their recorded collection configurations. Their individual causes were not established by the screenshot; each requires item-level diagnosis. See [Zabbix](../monitoring/zabbix-monitoring.md).

### 40. Why is Uptime Kuma used if Zabbix already monitors availability?

Zabbix collects broader infrastructure metrics and alerts; Uptime Kuma performs targeted availability checks and records events. The captured Kuma dashboard included four monitors. See [DNS and availability](../services/dns-and-availability.md).

**Related documentation:**

- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)
- [Cisco SNMP Troubleshooting](../monitoring/snmp-troubleshooting.md)
- [DNS and Availability Services](../services/dns-and-availability.md)

---

# 7. Enterprise Infrastructure Services

### 41. What is Asterisk used for?

Asterisk provides the documented SIP/PJSIP IP telephony service on the Debian voice server in VLAN 50. See [Asterisk/FreeRADIUS](../services/asterisk-freeradius.md).

### 42. Which telephone extensions are configured?

Extensions **1001 (Sales)** and **1002 (IT)** are associated with Grandstream phones at `192.168.50.10` and `192.168.50.11`. See [Asterisk](../services/asterisk-freeradius.md).

### 43. Were successful telephone calls independently verified?

No independent call-detail records or recordings verify successful calls between both photographed phones. The configuration and extensions are documented. See [voice services](../services/asterisk-freeradius.md).

### 44. What is the purpose of FreeRADIUS?

FreeRADIUS supplies network authentication services on the VLAN 50 Debian host. Successful authentication of corporate Wi-Fi clients through the AX53 was not independently verified. See [FreeRADIUS](../services/asterisk-freeradius.md).

### 45. What does Pi-hole contribute to the infrastructure?

Pi-hole filters DNS queries and records client/domain activity. The November 6 dashboard showed **12,293 queries, 1,827 blocked (14.9%) and 13 active clients** in its displayed interval. See [DNS evidence](../services/dns-and-availability.md).

### 46. Does Uptime Kuma guarantee service availability?

No. Kuma recorded checks for **four monitored targets**; an observed successful check is not a guarantee of ongoing application health or an SLA. See [availability monitoring](../services/dns-and-availability.md).

**Related documentation:**

- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)
- [DNS Filtering and Service Availability](../services/dns-and-availability.md)

---

# 8. Security, Troubleshooting, and Project Evidence

### 47. Does a green monitoring indicator prove that a service is working correctly?

No. A green result confirms only the monitored condition. Functional checks and logs are still needed to establish application behavior.

### 48. Why are credentials and sensitive configurations excluded from GitHub?

The repository is public.

Publishing passwords, SNMP community strings, database credentials, private keys, authentication secrets, or sensitive device identifiers would expose unnecessary security risks.

Public configuration examples therefore use sanitized values and omit private operational data.

The objective is to preserve technical reproducibility without disclosing credentials or confidential infrastructure details.

### 49. Which troubleshooting activities are supported by recorded results?

The Cisco Catalyst C9200L SNMP troubleshooting record contains three documented cases:

1. SNMP monitoring unavailable because of mismatched community values.
2. Incorrect switch uptime reporting caused by an unsuitable monitoring item.
3. Empty dashboard widgets resulting from restrictive host filters.

The record describes the investigation, applied adjustments, and observed outcomes.

These cases provide evidence of actual troubleshooting activity.

### 50. Are all monitoring problems documented as resolved?

No.

The monitoring snapshots include unsupported items, unavailable hosts, inconsistent workstation addresses, and Grafana panels without data.

Some issues have documented investigations and results, while others remain historical observations without a verified individual resolution.

The project distinguishes these situations rather than treating every warning as a successfully resolved incident.

Additional NOC operational procedures and troubleshooting runbooks form a separate documentation workstream.

### 51. Does the financial analysis represent actual project expenditure?

No.

The financial documentation uses infrastructure cost scenarios and reference estimates.

The scenarios distinguish full deployment from scratch, implementation using existing equipment, and recurring operations or maintenance.

The analysis remains subject to final inventory reconciliation and verification of cost assumptions.

Partial subtotals must not be interpreted as confirmed real expenditure.

### 52. What are the next development priorities?

The project continues through technical documentation, infrastructure consistency reviews, monitoring analysis, and operational procedures.

The next major documentation workstream is **NOC Operations & Troubleshooting**.

It will address incident classification, monitoring triage, diagnostic procedures, corrective actions, validation, and incident reporting.

The financial analysis will be finalized after the technical inventory and remaining assumptions have been consolidated.

---

## Final Notes

This FAQ is based on the technical documentation and historical evidence available in the Enterprise NOC repository.

It distinguishes:

- Physical infrastructure and observed configurations.
- Technical designs and intended policies.
- Historical monitoring measurements.
- Documented troubleshooting results.
- Configuration details absent from the collected historical records.

Answers should be updated when new validated information is added to the project.

For detailed configurations, diagrams, inventories, and screenshots, consult the technical documents linked throughout this FAQ.

**Enterprise NOC — From Scratch**  
*From physical infrastructure to network operations.*
