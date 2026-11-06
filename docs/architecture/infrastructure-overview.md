# Enterprise Infrastructure — Architecture Overview

**English | [Português (Brasil)](../pt-BR/arquitetura/visao-geral-da-infraestrutura.md)**

## Overview

This document presents the logical architecture of the **Enterprise NOC — From Scratch** project.

The laboratory simulates an enterprise IT environment, integrating physical network equipment, structured cabling, departmental VLANs, Linux servers, containerized services, and centralized network monitoring.

The architecture is organized into three main areas:

- **Physical Infrastructure:** Network equipment, workstations, rack, and structured cabling.
- **Network Infrastructure:** Cisco routing and switching, VLAN segmentation, corporate Wi-Fi, and IoT connectivity.
- **Systems & Monitoring:** Linux servers, Docker services, and NOC monitoring platforms.

## Logical Network Architecture

```mermaid
flowchart TB
    R["Cisco Catalyst C8200L<br/>Enterprise Router"]
    SW["Cisco Catalyst 9200L<br/>Enterprise Switch"]

    R ---|"802.1Q Trunk"| SW

    SW --- V10["VLAN 10<br/>IT & Monitoring"]
    SW --- V20["VLAN 20<br/>Accounting"]
    SW --- V30["VLAN 30<br/>Finance"]
    SW --- V40["VLAN 40<br/>Sales"]
    SW --- V50["VLAN 50<br/>VoIP"]
    SW --- V60["VLAN 60<br/>Corporate Wi-Fi"]
    SW --- V70["VLAN 70<br/>IoT"]

    V10 --- SERVER["Linux Server<br/>Docker & Monitoring"]
    V50 --- PBX["Asterisk PBX<br/>RADIUS Services"]

    V60 --- WIFI["Intelbras Router<br/>Corporate Wi-Fi"]
    V70 --- IOT["Intelbras Router<br/>IoT Network"]

    IOT --- ALEXA["Alexa with Display"]
    ALEXA -.->|"Voice Control"| LIGHT["Smart Light Bulb"]
```

> **Note:** This diagram represents logical network segmentation, not an exact physical cabling diagram. Switch interface assignments and device connectivity will be verified against the final configurations.

## Network Segmentation

The infrastructure uses seven VLANs to separate different departments and network services.

| VLAN | Segment | Purpose |
|---|---|---|
| 10 | IT & Monitoring | IT infrastructure and monitoring services |
| 20 | Accounting | Accounting workstations |
| 30 | Finance | Financial department workstations |
| 40 | Sales | Sales department workstations |
| 50 | VoIP | IP telephony and associated services |
| 60 | Corporate Wi-Fi | Corporate wireless connectivity |
| 70 | IoT | Smart devices and IoT connectivity |

The wireless infrastructure includes two Intelbras routers of the same model.

The corporate Wi-Fi segment uses an addressing range beginning with `10.0.0.0` and includes access control mechanisms involving ACLs and RADIUS.

Exact addressing, interface assignments, wireless operating modes, and access policies require final verification.

## Monitoring Architecture

```mermaid
flowchart TB
    CISCO["Cisco Network Equipment"]
    ZABBIX["Zabbix Server"]
    DB[("MariaDB")]
    WEB["Zabbix Web / API"]
    GRAFANA["Grafana"]
    KUMA["Uptime Kuma"]
    SERVICES["Monitored Services"]

    CISCO <-->|"SNMPv2c"| ZABBIX

    ZABBIX -->|"Monitoring Data"| DB
    WEB <-->|"Database Access"| DB

    GRAFANA -->|"Zabbix Data Source"| WEB

    KUMA -.->|"Availability Checks"| SERVICES
```

The monitoring architecture combines several complementary components:

- **Zabbix:** Collection of infrastructure metrics and monitoring information.
- **MariaDB:** Storage of Zabbix monitoring data.
- **Grafana:** Visualization of monitoring metrics through the Zabbix integration.
- **Uptime Kuma:** Availability monitoring for selected services.
- **SNMP:** Collection of network equipment information.

The monitoring environment also includes dashboards for analyzing infrastructure status and operational metrics.

## Additional Infrastructure Services

The Linux environment includes containerized applications and infrastructure services such as:

- Docker and Docker Compose.
- Portainer.
- Pi-hole.
- Nginx reverse proxy.
- Internal DNS services.
- Corporate web portal.

The final container inventory, networking configuration, and service dependencies will be documented separately.

## Physical Infrastructure

The laboratory includes:

- Network rack.
- Cisco networking equipment.
- Patch panel.
- Structured Ethernet cabling.
- Manually terminated network cables.
- Rack power distribution.
- Workstations assembled for the simulated departments.

A detailed physical topology and equipment inventory will be prepared after final verification.

## Documentation Status

**Status:** In Progress

The following information remains pending:

- Exact switch interface assignments.
- Final physical cabling diagram.
- Intelbras router models and operating modes.
- Verified Wi-Fi and IoT configurations.
- Complete workstation inventory.
- Final container and service inventory.

This document will be updated as implementation evidence and verified configurations become available.
