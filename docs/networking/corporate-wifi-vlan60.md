# Corporate Wi-Fi — VLAN 60

> **Project:** Enterprise NOC — From Scratch  
> **Environment:** Physical enterprise networking laboratory  
> **Network segment:** VLAN 60 — Corporate Wi-Fi  
> **Identified equipment:** TP-Link Archer AX53 (Wi-Fi 6 AX3000)  
> **Evidence dates:** November 4 and 6, 2026  
> **Documentation updated:** November 9, 2026  
> **Status:** Equipment identified; wireless configuration and integration pending verification

## 1. Overview

The Enterprise NOC laboratory includes a dedicated network segment for corporate wireless connectivity.

VLAN 60 is designated for corporate Wi-Fi, separating this network from departmental workstations, administrative infrastructure, voice services, and IoT devices.

The available evidence identifies a **TP-Link Archer AX53** as the equipment associated with the corporate wireless environment.

This document records the available hardware and switching evidence, the intended network architecture, and the remaining verification requirements.

It does not assume that wireless authentication, routing, or security restrictions have been fully implemented.

## 2. Identified Wireless Equipment

A photograph collected on November 6, 2026, identifies the following equipment:

| Attribute | Identification |
|---|---|
| Manufacturer | TP-Link |
| Model | Archer AX53 |
| Wireless generation | Wi-Fi 6 |
| Product class | AX3000 |
| Intended role | Corporate wireless connectivity |
| Associated network segment | VLAN 60 |
| Operating mode | Not verified |
| Active wireless security configuration | Not verified |

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
| Router configuration | Not independently verified |

This record establishes the VLAN assignment visible in the historical switch configuration.

It does not independently prove that the TP-Link device was physically connected to this exact interface at the time of the November 6 photographs.

The device's operating mode and uplink configuration also remain unverified.

## 4. Network Architecture

The intended corporate wireless architecture separates wireless devices from other internal network segments.

The laboratory distinguishes:

- VLAN 10 — IT and NOC administration.
- VLANs 20–40 — Departmental workstations.
- VLAN 50 — Voice and authentication services.
- VLAN 60 — Corporate Wi-Fi.
- VLAN 70 — IoT devices.

The available switch evidence documents VLAN 60 as a dedicated segment.

However, it does not establish whether the Archer AX53 operated in access point mode, router mode, or another supported configuration.

Consequently, DHCP behavior, NAT, wireless client addressing, and end-to-end VLAN membership require additional verification.

## 5. Intended Security Policy

The intended security model restricts communication between corporate wireless clients and other internal VLANs.

Administrative access should remain limited to authorized devices and services.

Any permitted communication between VLAN 60 and internal services must be explicitly defined according to operational requirements.

These restrictions are architectural requirements.

**The available evidence does not confirm that corresponding ACLs or firewall rules were actively enforced.**

## 6. Authentication and FreeRADIUS

The laboratory includes a separately documented FreeRADIUS service hosted in VLAN 50.

The existence of this service does not, by itself, establish that the corporate wireless network uses RADIUS authentication.

The following details remain unverified:

- The wireless authentication method actually configured.
- Whether the deployed Archer AX53 hardware and firmware support the intended authentication integration.
- Whether a RADIUS client is configured for the wireless infrastructure.
- Whether authentication requests successfully reach FreeRADIUS.
- Whether wireless client authentication was validated.

If enterprise authentication is implemented, the wireless equipment's capabilities and authentication flow must be verified before documenting the integration as operational.

No RADIUS credentials, shared secrets, or wireless passwords are included in this repository.

## 7. Monitoring and Troubleshooting

The available evidence documents monitoring of the main Cisco networking infrastructure through Zabbix and Grafana.

It does not independently establish direct monitoring of the TP-Link Archer AX53.

Potential verification activities include:

| Area | Verification objective |
|---|---|
| Physical connectivity | Confirm the actual switch interface connected to the wireless device |
| VLAN assignment | Confirm the operational VLAN and interface configuration |
| Operating mode | Identify whether the equipment operates as an access point or router |
| IP addressing | Identify the wireless client subnet, gateway, and DHCP source |
| Authentication | Determine the configured wireless security and authentication mechanisms |
| Network isolation | Validate intended restrictions between VLANs |
| Monitoring | Determine whether wireless device or client metrics are collected |

These are pending verification activities, not completed operational tests.

## 8. Known Limitations

The following information is not established by the available evidence:

1. Active SSID configuration.
2. Wireless encryption and authentication settings.
3. Actual operating mode of the Archer AX53.
4. Physical connection between the identified device and switch interface `Gi1/0/15`.
5. DHCP and NAT behavior.
6. Operational enforcement of VLAN isolation.
7. Successful integration with FreeRADIUS.
8. Direct wireless equipment monitoring.

These limitations are intentionally retained to distinguish documented equipment from verified configuration.

## 9. Related Documentation

- [Cisco Catalyst C8200L router](router-c8200l.md)
- [Cisco Catalyst C9200L VLAN snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Physical infrastructure](../evidence/physical-infrastructure.md)
- [Asterisk and FreeRADIUS services](../services/asterisk-freeradius.md)
- [Zabbix monitoring](../monitoring/zabbix-monitoring.md)

---

**Documentation principle:** The available evidence identifies the wireless equipment and the VLAN assignment recorded on the switch. It does not establish the complete operational configuration or validate the intended security policies.
