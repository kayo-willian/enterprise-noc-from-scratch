# Corporate Wi-Fi — VLAN 60

> **Project:** Enterprise NOC — From Scratch  
> **Environment:** Physical enterprise networking laboratory  
> **Network segment:** VLAN 60 — Corporate Wi-Fi  
> **Identified equipment:** TP-Link Archer AX53 (Wi-Fi 6 AX3000)  
> **Evidence dates:** November 4 and 6, 2026  
> **Documentation updated:** November 9, 2026  
> **Record:** Physical equipment and switch VLAN assignment, November 4–6, 2026

## 1. Overview

The Enterprise NOC laboratory includes a dedicated network segment for corporate wireless connectivity.

VLAN 60 is designated for corporate Wi-Fi, separating this network from departmental workstations, administrative infrastructure, voice services, and IoT devices.

The available evidence identifies a **TP-Link Archer AX53** as the equipment associated with the corporate wireless environment.

This page consolidates the dated equipment identification, switch VLAN assignment, network role, and the scope of the collected technical evidence.

It does not assume that wireless authentication, routing, or security restrictions have been fully implemented.

## 2. Identified Wireless Equipment

A photograph collected on November 6, 2026, identifies the following equipment:

| Attribute | Identification |
|---|---|
| Manufacturer | TP-Link |
| Model | Archer AX53 |
| Wireless generation | Wi-Fi 6 |
| Product class | AX3000 |
| Network role | Corporate wireless connectivity |
| Associated network segment | VLAN 60 |

The device was identified from physical evidence rather than an assumed equipment inventory.

The available photograph contains sensitive device information, including wireless credentials and unique identifiers. The original image is therefore not included in this public documentation.

## 3. Switch Integration

The Cisco Catalyst C9200L configuration snapshot collected on November 4, 2026, associates interface `Gi1/0/15` with VLAN 60.

| Component | Documented information |
|---|---|
| Switching equipment | Cisco Catalyst C9200L |
| Interface | `Gi1/0/15` |
| Assigned VLAN | 60 |
| Network purpose | Corporate Wi-Fi |
| Router | Cisco Catalyst C8200L |
| Router connection | Wireless equipment associated with VLAN 60 |

This record establishes the VLAN assignment visible in the historical switch configuration.

The dated switch record identifies the VLAN 60 switch connection. Internal Archer AX53 settings are outside this switch snapshot.

## 4. Network Architecture

The documented architecture assigns wireless devices to a dedicated corporate Wi-Fi segment, VLAN 60.

The laboratory distinguishes:

- VLAN 10 — IT and NOC administration.
- VLANs 20–40 — Departmental workstations.
- VLAN 50 — Voice and authentication services.
- VLAN 60 — Corporate Wi-Fi.
- VLAN 70 — IoT devices.

The available switch evidence documents VLAN 60 as a dedicated segment.

The collected record identifies the device and VLAN assignment, without an Archer AX53 configuration export. Device-specific operating modes and addressing are therefore not presented as installed settings.

## 5. Network Segmentation and Access

VLAN 60 is the corporate wireless segment and is separate from departmental networks and IoT VLAN 70. The logical security design restricts unauthorized cross-VLAN communication, with specific exceptions for approved internal services. The switch assignment documents segmentation but does not constitute an ACL enforcement test.

## 6. Authentication and Services

FreeRADIUS is hosted on the separately documented Linux server in VLAN 50. The presence of FreeRADIUS does not establish that the Archer AX53 uses it for Wi-Fi authentication. Wireless encryption, SSID settings, client IP assignment, DHCP, NAT, and operating mode were not included in the November 4–6 equipment evidence and are not attributed to the deployed configuration.

## 7. Monitoring

The dated Zabbix/Grafana captures document Cisco infrastructure monitoring, without a separate Archer AX53 dashboard. This page describes the wireless device as a network component.

## 8. Record Boundaries

This page consolidates the identified TP-Link Archer AX53 equipment, the VLAN 60 network role, and the dated C9200L switch assignment. It does not claim wireless client tests, RADIUS authentication transactions, or active firewall/ACL behavior absent from the collected evidence.

## 9. Related Documentation

- [Cisco Catalyst C8200L router](router-c8200l.md)
- [IoT network — VLAN 70](iot-vlan70.md)
- [Cisco Catalyst C9200L VLAN snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Physical infrastructure](../evidence/physical-infrastructure.md)
- [Asterisk and FreeRADIUS services](../services/asterisk-freeradius.md)
- [Zabbix monitoring](../monitoring/zabbix-monitoring.md)

