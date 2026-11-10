# Cisco Catalyst 9200L — Switch Port Mapping

**English | [Português (Brasil)](../pt-BR/redes/mapa-de-portas-switch.md)**

## Overview

This document presents the historical interface mapping of the Cisco Catalyst 9200L switch used in the Enterprise NOC — From Scratch project.

The switch connects departmental workstations, infrastructure servers, IP telephony devices, and wireless network equipment.

**Device:** Cisco Catalyst 9200L  
**Reference:** Technical implementation report — November 4, 2026  
**Scope:** Configuration snapshot from November 4, 2026; not live interface status

## Interface Inventory

| Interface | Connected Segment or Device | Expected VLAN | Configuration |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | 10–70 | Trunk |
| Gi1/0/2–3 | IT & Monitoring | 10 | Access |
| Gi1/0/4–6 | Accounting | 20 | Access |
| Gi1/0/7–8 | Finance | 30 | Access |
| Gi1/0/9–10 | Sales | 40 | Access |
| Gi1/0/11 | Debian Server — VoIP & RADIUS | 50 |VLAN 50 assigned in recorded configuration|
| Gi1/0/12–13 | Grandstream IP Phones | 50 | Access VLAN 50 |
| Gi1/0/14 | TP-Link Archer AX53 — IoT Network | 70 | Access VLAN 70 |
| Gi1/0/15 | TP-Link Archer AX53 — Corporate Wi-Fi | 60 | Access VLAN 60 |
| Gi1/0/16–24 | No device assignment established | — | No interface-specific statements recorded |
| Gi1/1/1–4 | SFP interfaces | — | No interface-specific statements recorded |

**Important:** This inventory combines interface descriptions from the November 4 technical report with the corrected VLAN design. It does not represent a verified running configuration.

## VLAN 60 and VLAN 70

The November 4 switch configuration assigns Gi1/0/14 to VLAN 70 and Gi1/0/15 to VLAN 60. These are recorded interface settings, not a physical-link test.

## Scope of the Port Map

Gi1/0/1 is configured as a trunk. Gi1/0/2–10 and Gi1/0/12–15 have documented access VLANs. Gi1/0/11 contains `switchport access vlan 50` and `spanning-tree portfast trunk`, but no explicit `switchport mode access`; the actual operational mode cannot be established from this snapshot alone.

The absence of interface-specific statements for Gi1/0/16–24 and Gi1/1/1–4 does not prove that those ports were free, disconnected, or disabled. This is a historical configuration inventory, not a current link-state report.
