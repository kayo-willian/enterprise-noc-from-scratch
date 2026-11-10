# Cisco Catalyst C8200L — Router Architecture and Evidence

> **Project:** Enterprise NOC — From Scratch  
> **Environment:** Physical enterprise networking laboratory  
> **Device:** Cisco Catalyst C8200L-1N-4T  
> **Evidence period:** November 4–6, 2026  
> **Documentation updated:** November 8, 2026  
> **Record:** Router hardware, switch trunk, network roles and monitoring evidence

## 1. Overview

The Cisco Catalyst C8200L is the central routing device in the Enterprise NOC laboratory.

The network combines a physical Cisco router, a Catalyst C9200L switch, departmental VLANs, Linux servers, Windows workstations, and monitoring services.

This document records the available evidence concerning the router's network role, addressing, monitoring, and intended segmentation policies.

**Record scope:** This page consolidates dated network architecture and equipment evidence, not a router running-configuration export.

## 2. Physical Infrastructure

The router is installed in the laboratory's network rack alongside the Cisco Catalyst C9200L switch and structured cabling infrastructure.

The available photographs identify the router as a **Cisco Catalyst C8200L-1N-4T**.

![Cisco router, switch and patch panel](../assets/images/physical/cisco-router-switch-patch-panel.jpg)

The switch configuration snapshot collected on November 4, 2026, identifies interface `Gi1/0/1` as a trunk associated with the router uplink.

This supports the documented network architecture but does not independently establish the configuration of the corresponding physical interface or VLAN subinterfaces on the router.

The switch record identifies `Gi1/0/1` on the C9200L as the router uplink; the corresponding C8200L interface is not named in that record.

## 3. Network Segmentation

The laboratory uses seven documented VLANs.

| VLAN | Network role | Evidence |
|---|---|---|
| 10 | IT / NOC / Administration | Switch configuration and endpoint records |
| 20 | Accounting | Switch configuration and endpoint records |
| 30 | Finance | Switch configuration and endpoint records |
| 40 | Sales | Switch configuration and endpoint records |
| 50 | VoIP / Asterisk / FreeRADIUS | Switch configuration and server records |
| 60 | Corporate Wi-Fi | Switch configuration snapshot |
| 70 | IoT | Switch configuration snapshot |

The November 4 switch snapshot records VLAN assignments and the router-facing trunk.

**Evidence limitation:** VLAN existence and switch port assignments do not, by themselves, demonstrate successful inter-VLAN routing or enforcement of access control policies.

## 4. Observed IP Addressing

Workstation photographs collected on November 6, 2026, include IP configuration output identifying the following default gateways.

| VLAN | Observed default gateway | Evidence source |
|---|---|---|
| 10 | `192.168.10.1` | IT workstation IP configuration |
| 20 | `192.168.20.1` | Accounting workstation IP configuration |
| 30 | `192.168.30.1` | Finance workstation IP configuration |
| 40 | `192.168.40.1` | Sales workstation IP configuration |

The November 4 technical records also identify `192.168.10.1` as the router's management-side address.

These observations establish the gateway settings visible on the endpoints at the time of collection.

They do not independently confirm the router's subinterface configuration, gateway ownership for every VLAN, or successful forwarding between departments.

## 5. Network Segmentation and Access Policy Design

The documented segmentation design distinguishes the IT/NOC administration network from the departmental, wireless, and IoT networks.

### Administrative access

VLAN 10 is designated for administration and monitoring.

The access-policy design permits authorized administrative systems to initiate management connections to services and devices in other VLANs when required.

### Departmental isolation

VLANs 20, 30, and 40 are separated in the access-policy design, except where explicitly authorized services require communication.

### VoIP and authentication services

VLAN 50 hosts the documented Asterisk and FreeRADIUS server.

Access to these services should be restricted according to application requirements.

### Wireless and IoT isolation

VLANs 60 and 70 have restricted access in the access-policy design to internal enterprise resources.

Any necessary exceptions, including communication between a wireless access point and FreeRADIUS, must be defined according to the actual source addresses and service requirements.

**Record scope:** These are architectural access-policy requirements, not a transcription of router ACL entries.

The dated records include switch-side VLAN assignments, but no export of router ACL entries or ACL test results.

## 6. Router Monitoring

The router is represented in the laboratory's Zabbix and Grafana monitoring environment.

The collected evidence includes router availability information and interface-related metrics.

### Grafana — Router Dashboard

![Router monitoring dashboard — Part 1](../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

![Router monitoring dashboard — Part 2](../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

These screenshots document monitoring information available during the collection period.

They do not demonstrate continuous availability, complete interface coverage, or the operational correctness of every routing and security configuration.

The Zabbix host inventory also provides evidence of an SNMP monitoring interface associated with the router.

The recorded Zabbix/Grafana metrics document router monitoring; a router-side SNMP configuration export is outside the collected material.

## 7. DHCP, NAT and External Connectivity

The laboratory workstations use DHCP. Their recorded gateway addresses for VLANs 10, 20, 30 and 40 come from November 6 workstation captures, not from an exported router running configuration. The collection does not identify the DHCP server or relay mechanism, address pools, NAT translations, external interface or default route of the C8200L. No corresponding router commands are represented as deployed.

## 8. Scope of the Router Record

This page documents the physical C8200L equipment, the switch-side trunk (Gi1/0/1), the VLAN design, observed workstation default gateways, and router-related Zabbix/Grafana evidence. It does not claim identification of the router-side physical interface or precise dot1Q subinterfaces. The access-control section describes the segmentation policy, not the proven contents or enforcement of ACLs.

The screenshots establish monitoring observations at their collection time, not uninterrupted availability or a complete running configuration.

## 9. Related Documentation

- [Physical infrastructure](../evidence/physical-infrastructure.md)
- [Cisco switch and VLAN configuration snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Workstation inventory](../endpoints/workstation-inventory.md)
- [Zabbix monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana monitoring](../monitoring/grafana-monitoring.md)

