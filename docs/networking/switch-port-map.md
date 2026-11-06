# Cisco Catalyst 9200L — Switch Port Mapping

**English | [Português (Brasil)](../pt-BR/redes/mapa-de-portas-switch.md)**

## Overview

This document presents the preliminary interface mapping of the Cisco Catalyst 9200L switch used in the Enterprise NOC — From Scratch project.

The switch connects departmental workstations, infrastructure servers, IP telephony devices, and wireless network equipment.

**Device:** Cisco Catalyst 9200L  
**Reference:** Technical implementation report — November 4, 2026  
**Status:** Preliminary mapping — pending final verification

## Interface Inventory

| Interface | Connected Segment or Device | Expected VLAN | Configuration |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | 10–70 | Trunk |
| Gi1/0/2–3 | IT & Monitoring | 10 | Access |
| Gi1/0/4–6 | Accounting | 20 | Access |
| Gi1/0/7–8 | Finance | 30 | Access |
| Gi1/0/9–10 | Sales | 40 | Access |
| Gi1/0/11 | Debian Server — VoIP & RADIUS | 50 | Access |
| Gi1/0/12–13 | Grandstream IP Phones | 50 | To verify |
| Gi1/0/14 | Intelbras — IoT Network | 70 | To verify |
| Gi1/0/15 | Intelbras — Corporate Wi-Fi | 60 | To verify |
| Gi1/0/16–24 | Spare / Reserved | To verify | To verify |
| Gi1/1/1–4 | SFP Uplink Interfaces | To verify | To verify |

**Important:** This inventory combines interface descriptions from the November 4 technical report with the corrected VLAN design. It does not represent a verified running configuration.

## VLAN 60 and VLAN 70 — Pending Verification

The original implementation report contains inconsistent VLAN assignments for the wireless and IoT interfaces.

The current intended segmentation is:

- **VLAN 60:** Corporate Wi-Fi.
- **VLAN 70:** IoT network.

The physical assignments of Gi1/0/14 and Gi1/0/15 must be checked against the actual switch configuration.

## Configuration Verification

The following read-only Cisco IOS-XE commands can be used to inspect the switch:

```text
show interfaces status
show vlan brief
show interfaces trunk
show interfaces switchport
show running-config interface GigabitEthernet1/0/14
show running-config interface GigabitEthernet1/0/15
```

Verification should establish:

- Interface operational status.
- Access and trunk port assignments.
- Actual VLAN membership.
- Trunk allowed VLANs.
- Connected devices and interface descriptions.
- Any differences between the documentation and running configuration.

## Documentation Status

**Status:** In Progress

This document will be updated after the physical connections and switch configuration have been verified.

Sensitive information will be excluded from public configuration examples.
