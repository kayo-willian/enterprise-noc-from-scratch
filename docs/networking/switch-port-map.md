# Cisco Catalyst C9200L — Switch Port Mapping

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](../pt-BR/redes/mapa-de-portas-switch.md)

---

## Overview

This document presents the historical interface mapping of the **Cisco Catalyst C9200L-24T-4G** switch deployed in the Enterprise NOC infrastructure.

The switch provides Ethernet connectivity for departmental workstations, Linux servers, IP telephony, corporate wireless infrastructure, and IoT equipment.

The interface inventory is based on the Cisco IOS XE configuration captured on **November 4, 2026**, combined with the documented laboratory equipment inventory.

| Attribute | Information |
|---|---|
| Manufacturer | Cisco |
| Model | Catalyst C9200L-24T-4G |
| Operating System | Cisco IOS XE |
| Recorded IOS XE Version | 17.15 |
| Configuration Reference | November 4, 2026 |
| Network Segmentation | VLANs 10, 20, 30, 40, 50, 60, and 70 |

The configuration snapshot represents the switch settings recorded during the evidence collection period. It does not establish the current operational state of every interface.

## 1. Switch Interface Inventory

The following table consolidates the documented VLAN assignments and interface descriptions.

| Interface | Documented Segment or Equipment | VLAN Assignment | Recorded Configuration |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | Not explicitly listed | Trunk |
| Gi1/0/2–3 | IT & NOC | 10 | Access |
| Gi1/0/4–6 | Accounting | 20 | Access |
| Gi1/0/7–8 | Finance | 30 | Access |
| Gi1/0/9–10 | Sales | 40 | Access |
| Gi1/0/11 | Debian — Asterisk & FreeRADIUS | 50 | Access VLAN 50 configured; operating mode not established |
| Gi1/0/12–13 | Grandstream IP Phones | 50 | Access |
| Gi1/0/14 | TP-Link Archer AX53 — IoT | 70 | Access |
| Gi1/0/15 | TP-Link Archer AX53 — Corporate Wi-Fi | 60 | Access |
| Gi1/0/16–24 | No specific equipment assignment established | — | No interface-specific configuration statements recorded |
| Gi1/1/1–4 | SFP Uplink Interfaces | — | No interface-specific configuration statements recorded |

The table combines the recorded switch configuration with the documented network equipment assignments.

Interface configuration does not independently establish physical connectivity, link status, or successful communication with the associated equipment.

## 2. Router-Facing Trunk — Gi1/0/1

Interface `Gi1/0/1` is associated with the Cisco Catalyst C8200L router.

The historical configuration contains:

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

This establishes that the interface was configured as a trunk on the switch.

The collected configuration does not contain an explicit allowed-VLAN list or a custom native VLAN assignment for this interface.

Although the network architecture documents VLANs 10 through 70, the VLAN inventory must not be interpreted as an explicit trunk allowed-VLAN configuration.

The corresponding router interface, VLAN subinterfaces, and complete inter-VLAN routing configuration are not included in the collected records.

## 3. Departmental Access Interfaces

The documented departmental assignments are organized as follows:

| Department | VLAN | Switch Interfaces |
|---|---|---|
| IT & NOC | 10 | Gi1/0/2–3 |
| Accounting | 20 | Gi1/0/4–6 |
| Finance | 30 | Gi1/0/7–8 |
| Sales | 40 | Gi1/0/9–10 |

The configuration snapshot identifies access-port settings for these interfaces.

An example from the Accounting segment is:

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

These statements describe the recorded interface configuration.

They do not represent independent measurements of physical link availability or successful end-to-end communication.

## 4. VoIP and Authentication — VLAN 50

VLAN 50 is associated with the laboratory's voice and authentication infrastructure.

The documented equipment includes:

- Debian Linux server hosting Asterisk and FreeRADIUS.
- Two Grandstream IP telephones.

The interface assignments are:

| Interface | Equipment | VLAN |
|---|---|---|
| Gi1/0/11 | Asterisk and FreeRADIUS server | 50 |
| Gi1/0/12 | Grandstream IP phone | 50 |
| Gi1/0/13 | Grandstream IP phone | 50 |

### 4.1 Interface Gi1/0/11

The historical configuration contains:

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Unlike the other documented departmental access interfaces, this configuration does not explicitly include:

```cisco
switchport mode access
```

The presence of `spanning-tree portfast trunk` also differs from the configuration recorded for the standard workstation access ports.

Consequently, the historical snapshot establishes the configured access VLAN assignment but does not independently establish the interface's effective operating mode.

The configuration is preserved as recorded, without treating the interface as a confirmed access or trunk port.

## 5. Corporate Wi-Fi — VLAN 60

The corporate wireless network is associated with a dedicated TP-Link Archer AX53.

| Attribute | Documented Information |
|---|---|
| Equipment | TP-Link Archer AX53 |
| Network Segment | Corporate Wi-Fi |
| VLAN | 60 |
| Switch Interface | Gi1/0/15 |
| Interface Configuration | Access VLAN 60 |

The switch snapshot documents the VLAN assignment.

The collected evidence does not establish the wireless device's internal operating mode, DHCP configuration, NAT behavior, or client IP addressing.

These parameters are addressed according to the available evidence in the dedicated wireless documentation.

## 6. IoT Network — VLAN 70

The IoT environment includes a separate TP-Link Archer AX53 associated with an Amazon Alexa device.

| Attribute | Documented Information |
|---|---|
| Equipment | Dedicated TP-Link Archer AX53 |
| Network Segment | IoT |
| VLAN | 70 |
| Switch Interface | Gi1/0/14 |
| Interface Configuration | Access VLAN 70 |

The Cisco switch configuration associates `Gi1/0/14` with VLAN 70.

The internal addressing and operating mode of the wireless equipment are not established by the switch configuration.

The VLAN assignment does not independently demonstrate that wireless clients use addresses from a specific VLAN 70 subnet.

## 7. Additional Switch Interfaces

The configuration snapshot does not include specific interface configuration statements for:

- `Gi1/0/16` through `Gi1/0/24`.
- `Gi1/1/1` through `Gi1/1/4`.

The absence of interface-specific configuration statements does not establish whether these ports were physically connected, available, disabled, or operationally down.

The historical records are not a complete interface-status inventory.

## 8. Configuration and Evidence Scope

This document consolidates the recorded switch interface configuration and the corresponding network equipment assignments.

The November 4, 2026, configuration snapshot provides evidence of:

- VLAN assignments.
- Departmental access-port configuration.
- The router-facing trunk.
- Interfaces associated with VoIP, corporate Wi-Fi, and IoT equipment.
- The particular configuration of `Gi1/0/11`.

The available evidence does not constitute:

- A current switch interface-status report.
- Verification of physical connectivity on every documented interface.
- A complete export of the Cisco C8200L configuration.
- Proof of successful communication between all VLANs.
- Verification of router ACL enforcement.
- A complete physical cable map.

The original configuration was collected before subsequent SNMP monitoring changes and must not be treated as the switch's final running configuration.

## 9. Related Documentation

- [Networking & Architecture](README.md)
- [Consolidated Logical Network Topology](consolidated-logical-topology.md)
- [VLAN Segmentation](vlans.md)
- [Cisco Catalyst C8200L](router-c8200l.md)
- [Cisco Switch Configuration Snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Corporate Wi-Fi — VLAN 60](corporate-wifi-vlan60.md)
- [IoT Network — VLAN 70](iot-vlan70.md)
- [Physical Infrastructure](../evidence/physical-infrastructure.md)

---

**Configuration reference:** November 4, 2026  
**Document type:** Historical switch interface mapping.
