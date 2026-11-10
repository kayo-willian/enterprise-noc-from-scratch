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

Enterprise NOC — From Scratch is a practical enterprise infrastructure project developed in a physical training laboratory.

It integrates Cisco networking equipment, departmental workstations, Linux servers, containerized applications, IP telephony, DNS services, and centralized monitoring.

The project documents infrastructure implementation, network segmentation, service integration, operational observations, and technical troubleshooting.

### 02. Is Tapajós Inovações a real company?

No. Tapajós Inovações is the fictional organization used to establish the business requirements and corporate context of the project.

The infrastructure laboratory itself is real.

The equipment, physical installation, system inventories, and published monitoring screenshots represent technical activities performed in the training environment.

The fictional business scenario must not be confused with an actual production deployment.

### 03. Why was the project designed around a Network Operations Center?

A Network Operations Center (NOC) provides centralized visibility into infrastructure availability, operational events, and network performance.

The project uses this concept to integrate network administration with monitoring and troubleshooting.

Rather than documenting isolated configurations, the infrastructure demonstrates how network devices, operating systems, applications, and monitoring platforms relate to one another.

### 04. Which business problems does the project address?

The simulated business scenario identifies four main challenges:

- Unreliable structured cabling and physical connectivity.
- Inadequate wireless network security.
- Instability affecting internal IP telephony.
- Limited infrastructure monitoring and operational visibility.

The project responds to these requirements through structured cabling, network segmentation, dedicated services, and centralized monitoring.

These initial problems describe the fictional organization's requirements, not verified failures occurring continuously in the physical laboratory.

### 05. Is the infrastructure intended for production use?

The environment was developed for technical education and practical infrastructure implementation.

It demonstrates enterprise networking concepts using real equipment and services, but it is not presented as a production-certified environment.

Production adoption would require additional security validation, backup procedures, availability requirements, configuration reviews, and operational testing.

### 06. Which period does the project documentation cover?

The repository contains technical records from October and November 2026.

Important evidence includes the Cisco switch configuration collected on November 4 and the infrastructure, workstation, service, and monitoring records collected on November 6.

The documented laboratory development period extends through November 17, 2026.

Individual screenshots and configuration records represent their respective collection dates, not a continuously updated infrastructure state.

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

The Cisco Catalyst C8200L is the routing platform associated with communication between the enterprise network segments.

The Cisco Catalyst C9200L provides Ethernet switching and VLAN segmentation for departmental workstations, servers, telephones, and wireless devices.

The switch configuration includes a trunk interface associated with the router connection.

The complete router-side configuration was not included in the collected evidence.

### 14. Why does the infrastructure use seven VLANs?

VLANs logically separate different departments and infrastructure functions at Layer 2.

The documented organization is:

| VLAN | Purpose |
|---|---|
| 10 | IT / NOC |
| 20 | Accounting |
| 30 | Finance |
| 40 | Sales |
| 50 | VoIP and authentication services |
| 60 | Corporate Wi-Fi |
| 70 | IoT |

This structure helps organize traffic and provides a foundation for applying network access policies.

VLAN separation alone does not guarantee security between routed networks.

### 15. What is the purpose of the trunk between the router and switch?

A trunk interface can carry traffic associated with multiple VLANs using VLAN tagging.

The collected Catalyst C9200L configuration identifies `Gi1/0/1` as the router-facing trunk.

This supports the intended multi-VLAN architecture.

However, the switch-side configuration does not independently establish the router's corresponding interface configuration or successful communication between all VLANs.

### 16. How are the switch interfaces distributed?

The November 4 configuration records departmental and infrastructure port assignments.

Interfaces `Gi1/0/2–3` are associated with VLAN 10, `Gi1/0/4–6` with VLAN 20, `Gi1/0/7–8` with VLAN 30, and `Gi1/0/9–10` with VLAN 40.

The remaining documented assignments include VLAN 50 for voice services, `Gi1/0/14` for IoT, and `Gi1/0/15` for corporate Wi-Fi.

The detailed interface inventory is maintained separately.

### 17. Why is interface Gi1/0/11 treated differently?

The historical configuration for `Gi1/0/11` includes:

```cisco
switchport access vlan 50
spanning-tree portfast trunk
```

Unlike the other documented access interfaces, it does not contain an explicit `switchport mode access` statement.

The configuration also includes a PortFast trunk command.

Therefore, the records preserve the VLAN 50 association without claiming an operating mode that was not independently established.

### 18. How are IP addresses assigned to workstations?

The laboratory uses DHCP for workstation addressing.

The collected workstation configurations identify default gateways including:

| VLAN | Observed gateway |
|---|---|
| 10 | `192.168.10.1` |
| 20 | `192.168.20.1` |
| 30 | `192.168.30.1` |
| 40 | `192.168.40.1` |

These are observed endpoint settings.

The collected records do not establish the complete DHCP server configuration, address pools, or relay mechanisms.

### 19. Are departmental VLANs completely isolated?

The intended architecture restricts unauthorized communication between departments and limits access to administrative resources.

However, a VLAN configuration is not equivalent to an independently verified access-control policy.

The available router evidence does not include a complete ACL configuration or comprehensive inter-VLAN access tests.

Consequently, the project documents departmental isolation as an architectural requirement rather than a fully demonstrated security result.

### 20. Is inter-VLAN routing and NAT fully documented?

No.

The available evidence identifies the Cisco router, switch-side trunk, VLAN design, observed workstation gateways, and router monitoring dashboards.

It does not include the complete C8200L running configuration.

The router's exact subinterfaces, NAT translation rules, external connectivity configuration, and successful forwarding between every VLAN are not independently established by the collected records.

**Related documentation:**

- [VLAN Segmentation](../networking/vlans.md)
- [Consolidated Logical Topology](../networking/consolidated-logical-topology.md)
- [Cisco Catalyst C8200L](../networking/router-c8200l.md)
- [Switch Port Mapping](../networking/switch-port-map.md)
- [Switch Configuration Snapshot](../networking/switch-vlan-snapshot-2026-11-04.md)

---

# 4. Wireless Networking and IoT

### 21. Why are two TP-Link Archer AX53 devices used?

The infrastructure separates corporate wireless connectivity from IoT connectivity.

One TP-Link Archer AX53 is associated with VLAN 60, while another dedicated device is associated with VLAN 70.

The devices belong to different physical wireless segments in the laboratory design.

Using separate equipment allows the two network functions to be documented and administered independently.

### 22. Which switch interfaces connect the wireless networks?

The November 4 Catalyst C9200L configuration identifies:

| Interface | VLAN | Function |
|---|---|---|
| `Gi1/0/15` | 60 | Corporate Wi-Fi |
| `Gi1/0/14` | 70 | IoT connectivity |

These assignments are visible in the recorded switch configuration.

The switch evidence alone does not demonstrate the complete wireless configuration or successful enforcement of isolation policies.

### 23. How is Amazon Alexa integrated into the network?

The laboratory includes an Amazon Alexa associated with the dedicated IoT wireless network.

The documented connectivity is:

```text
Amazon Alexa
     |
   Wi-Fi
     |
TP-Link Archer AX53
     |
  Ethernet
     |
Cisco Catalyst C9200L
     |
   VLAN 70
```

The topology describes the physical wireless-to-switch relationship.

It does not independently establish the Alexa device's IP address or complete application connectivity.

### 24. Do the wireless routers operate in access point mode?

The collected evidence does not establish their operating modes.

A wireless device configured as an access point may bridge clients into the associated network segment.

A device operating as a router may instead use NAT and provide a separate client subnet.

Without the corresponding configuration export, the project's documentation does not attribute either behavior to the installed equipment.

### 25. Does corporate Wi-Fi authentication use FreeRADIUS?

The infrastructure includes a FreeRADIUS server and a documented network authentication architecture.

However, the collected evidence does not independently demonstrate successful authentication between the photographed Archer AX53 and FreeRADIUS.

The presence of both components does not establish a completed wireless RADIUS integration.

Authentication behavior must be supported by configuration and transaction evidence before it can be represented as operationally verified.

**Related documentation:**

- [Corporate Wi-Fi — VLAN 60](../networking/corporate-wifi-vlan60.md)
- [IoT Network — VLAN 70](../networking/iot-vlan70.md)
- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)

---

# 5. Linux, Docker, and Container Infrastructure

### 26. What is the main NOC server configuration?

The principal infrastructure computer is a Dell OptiPlex 3020 running Debian GNU/Linux 13.

Its documented specifications include:

| Component | Specification |
|---|---|
| Processor | Intel Core i5-4590 |
| Memory | Approximately 8 GB |
| Operating system | Debian 13 |
| IPv4 address | `192.168.10.12/24` |
| Network segment | VLAN 10 |

This computer hosts the principal Docker environment and several infrastructure services.

### 27. Why is Docker used in the project?

Docker provides an organized environment for deploying infrastructure applications as containers.

The project uses containers to host monitoring services, management interfaces, DNS applications, databases, and web components.

This approach separates application environments and simplifies the organization of service dependencies.

Containerization does not automatically provide high availability, complete security isolation, or persistent data protection.

### 28. Which containers were running during evidence collection?

The November 6 inventory recorded ten running containers:

1. `reverse-proxy`
2. `zabbix-web`
3. `zabbix-server`
4. `uptime-kuma`
5. `zabbix-db`
6. `grafana`
7. `zabbix-agent`
8. `site-estatico`
9. `pihole`
10. `portainer`

These names come from the recorded Docker inventory.

The snapshot confirms their running state at collection time, not continuous operation.

### 29. What are the differences between Docker Compose and Portainer?

Docker Compose defines and manages multi-container applications through declarative configuration files.

Portainer provides a graphical interface for inspecting and managing Docker environments.

In the laboratory, the two tools complement each other.

Compose describes deployment structure, while Portainer provides operational visibility into containers, images, and networks.

### 30. Why are Nginx and Apache both present?

They perform different functions.

Nginx is used as a reverse proxy, providing a centralized access layer for selected web services.

Apache HTTP Server is used to host a static corporate website through the `site-estatico` container.

This organization separates the responsibility of routing web requests from serving the website content.

### 31. What is MariaDB used for?

MariaDB provides database storage for the Zabbix monitoring environment.

The documented Docker deployment contains a dedicated `zabbix-db` container.

Zabbix Server processes monitoring information, while the database supports the storage requirements of the monitoring platform.

The project's architecture distinguishes the database from the monitoring interface and visualization tools.

### 32. Can the Docker infrastructure be reproduced directly from GitHub?

The repository contains sanitized Docker Compose files and supporting configuration examples.

However, these files are not presented as a complete, independently validated, one-command reproduction of the laboratory.

Local certificates, secrets, persistent application data, machine-specific settings, and other prerequisites are excluded from the public configuration.

A new deployment requires review and adaptation of those dependencies.

**Related documentation:**

- [Docker Infrastructure and Services](../containers/docker-services.md)
- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Docker Compose Configuration](../../docker_configs/docker-compose.yml)

---

# 6. Monitoring and Observability

### 33. Why are Zabbix and Grafana used together?

Zabbix is responsible for collecting and processing monitoring information through configured hosts, interfaces, items, templates, and triggers.

Grafana provides a separate visualization layer through its Zabbix integration.

Combining these tools allows infrastructure metrics to be collected centrally and displayed through dashboards organized by network equipment, operating systems, and services.

Grafana does not replace the underlying monitoring data collection performed by Zabbix.

### 34. How extensive was the Zabbix monitoring environment?

The November 6 system information screenshot records:

| Metric | Value |
|---|---:|
| Registered hosts | 12 |
| Total items | 1,820 |
| Enabled items | 1,698 |
| Unsupported items | 113 |
| Triggers in problem state | 34 |

These are historical system measurements.

The presence of unsupported items and active problems demonstrates that the monitoring environment still contained operational issues requiring investigation.

### 35. How are Cisco devices and operating systems monitored?

The Cisco router and switch are represented through SNMP monitoring interfaces.

The Linux and Windows systems use Zabbix Agent interfaces for system monitoring.

SNMP provides access to supported network-device metrics, while agents collect operating-system information.

The available dashboards include CPU usage, memory consumption, network traffic, interface status, and service indicators.

### 36. Was the Cisco switch SNMP problem resolved?

The November 4 troubleshooting record documents an SNMP connectivity problem caused by inconsistent community values between the switch and Zabbix.

The configuration was aligned, a host-level `{$SNMP_COMMUNITY}` macro was configured, and the monitoring configuration cache was reloaded.

The documented result was restored SNMP availability and interface discovery.

This is a recorded troubleshooting case, distinct from problems for which no completed resolution was documented.

### 37. Why did some Grafana workstation panels display `No data`?

The November 6 Grafana evidence includes eight Windows workstations.

Three were displayed as `ONLINE`, while five panels showed `No data`.

A missing value does not necessarily mean that the corresponding computer was powered off.

Possible explanations include unavailable monitoring agents, address mismatches, item configuration problems, or missing data within the selected time range.

The collected evidence does not establish one definitive cause for every panel.

### 38. How can DHCP affect Zabbix monitoring?

The laboratory uses DHCP for workstation addressing.

The evidence collection identified six differences between photographed workstation addresses and the addresses registered in Zabbix.

If a monitored host changes its IP address while the Zabbix host configuration retains the previous address, agent communication can be affected.

This is a relevant explanation for some monitoring inconsistencies, but it does not prove the cause of every unavailable host.

### 39. What do the 113 unsupported Zabbix items indicate?

An unsupported item is a monitoring item that cannot currently provide valid data through its configured collection method.

Possible causes include incompatible keys, unsupported device metrics, incorrect interfaces, insufficient permissions, or configuration errors.

The November 6 screenshot records 113 unsupported items.

However, the screenshot does not individually identify the causes of those items. A specific diagnosis requires inspecting the affected monitoring configurations.

### 40. Why is Uptime Kuma used if Zabbix already monitors availability?

The two applications provide complementary monitoring functions.

Zabbix supports infrastructure metrics, triggers, and host-level monitoring.

Uptime Kuma focuses on availability checks and their event history for selected targets.

The laboratory's Uptime Kuma screenshot records four configured monitors. It does not establish that every container, workstation, or network device was monitored individually through that application.

**Related documentation:**

- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)
- [Cisco SNMP Troubleshooting](../monitoring/snmp-troubleshooting.md)
- [DNS and Availability Services](../services/dns-and-availability.md)

---

# 7. Enterprise Infrastructure Services

### 41. What is Asterisk used for?

Asterisk provides the laboratory's IP telephony functionality.

The documented configuration uses SIP/PJSIP for endpoint registration and call signaling, with RTP supporting voice media transport.

The server is associated with VLAN 50 and is hosted on a dedicated Linux computer.

The technical documentation also describes an internal dialplan for extension routing and testing.

### 42. Which telephone extensions are configured?

The documented telephone environment contains two Grandstream devices:

| Extension | Department | IP address |
|---|---|---|
| 1001 | Sales | `192.168.50.10` |
| 1002 | IT | `192.168.50.11` |

The November 6 photographs confirm the presence of both physical devices and their displayed network addresses.

The exact telephone models were not reliably established from the available photographs.

### 43. Were successful telephone calls independently verified?

The technical records describe the Asterisk configuration, extensions, and dialplan.

An earlier technical report identifies the extensions as available during its observation.

However, the collected evidence does not include independent call recordings or call-detail records proving successful execution of every configured test.

Therefore, the configuration is documented without claiming a complete end-to-end telephony validation.

### 44. What is the purpose of FreeRADIUS?

FreeRADIUS provides centralized network authentication functionality.

The documented server configuration includes RADIUS and authentication technologies such as EAP-PEAP and MSCHAPv2.

It runs alongside Asterisk on the Linux computer associated with VLAN 50.

The available technical records describe the authentication architecture but do not independently verify successful end-to-end authentication from the corporate wireless equipment.

### 45. What does Pi-hole contribute to the infrastructure?

Pi-hole provides DNS filtering and query visibility.

The November 6 dashboard records:

| Metric | Observed value |
|---|---:|
| DNS queries | 12,293 |
| Blocked queries | 1,827 |
| Blocked percentage | 14.9% |
| Active clients | 13 |

These figures describe the selected dashboard period.

They do not establish complete DNS filtering coverage across every VLAN or client.

### 46. Does Uptime Kuma guarantee service availability?

No.

The collected Uptime Kuma dashboard displays four configured monitors, with all four shown as `Up` at the time of the screenshot.

The application also contains historical availability events, including unsuccessful checks.

A positive availability indicator only represents the configured monitoring conditions and reporting period.

It does not guarantee continuous availability or the correct operation of every application function.

**Related documentation:**

- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)
- [DNS Filtering and Service Availability](../services/dns-and-availability.md)

---

# 8. Security, Troubleshooting, and Project Evidence

### 47. Does a green monitoring indicator prove that a service is working correctly?

Not necessarily.

A green indicator usually means that a particular monitoring condition was satisfied.

For example, a service may respond to an HTTP request while another application function remains unavailable.

Infrastructure monitoring results should be interpreted together with service-specific checks, configuration evidence, logs, and operational tests.

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
- Implementation details not established by the available evidence.

Answers should be updated when new validated information is added to the project.

For detailed configurations, diagrams, inventories, and screenshots, consult the technical documents linked throughout this FAQ.

**Enterprise NOC — From Scratch**  
*From physical infrastructure to network operations.*
