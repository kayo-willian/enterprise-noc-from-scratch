# Enterprise Infrastructure — Architecture Overview

**English | [Português (Brasil)](../pt-BR/architecture/infrastructure-overview.md)**

## Overview

This document presents the logical architecture of the Enterprise NOC — From Scratch project.

The infrastructure combines physical networking equipment, segmented corporate networks, Linux servers, containerized services, and centralized monitoring.

## Network Architecture

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

    V10 --- NOC["Linux Server<br/>Docker & Monitoring"]

    V50 --- PBX["Asterisk PBX<br/>RADIUS Services"]

    V60 --- WIFI["Intelbras Router<br/>Corporate Wireless"]

    V70 --- IOT["Intelbras Router<br/>IoT Network"]

    IOT --- ALEXA["Alexa with Display"]
    ALEXA -.->|"Voice Control"| LIGHT["Smart Light Bulb"]
```

> **Note:** This is a logical architecture diagram. It does not represent exact switch port assignments, cabling paths, or verified physical connections.

## Monitoring Architecture

```mermaid
flowchart LR
    CISCO["Cisco Network Devices"]
    ZABBIX["Zabbix Server"]
    DB[("MariaDB")]
    WEB["Zabbix Web / API"]
    GRAFANA["Grafana"]

    ZABBIX <-->|"SNMP"| CISCO
    ZABBIX --> DB
    WEB --> DB
    GRAFANA -->|"Zabbix Data Source"| WEB
```

Zabbix collects infrastructure metrics, MariaDB stores monitoring data, and Grafana provides additional visualization through the Zabbix data source.

Uptime Kuma is also deployed as a separate service for availability monitoring.

## Physical Infrastructure

The laboratory includes a network rack, patch panel, structured cabling, power distribution, and manually assembled workstations.

A detailed physical topology will be documented after the final equipment and cabling inventory.

## Verification Status

**Status:** Preliminary architecture documentation.

The following details require further verification:

- Exact physical switch port assignments.
- Intelbras router models and operating modes.
- Wireless and IoT network configurations.
- Final workstation inventory.
- Updated monitoring service configuration.

This document will be updated as the infrastructure evolves.
