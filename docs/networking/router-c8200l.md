# Cisco Catalyst C8200L — Router Architecture and Evidence

> **Project:** Enterprise NOC — From Scratch  
> **Environment:** Physical enterprise networking laboratory  
> **Device:** Cisco Catalyst C8200L-1N-4T  
> **Evidence period:** November 4–6, 2026  
> **Documentation updated:** November 8, 2026  
> **Status:** Partially documented — configuration validation pending

## 1. Overview

The Cisco Catalyst C8200L is the central routing device in the Enterprise NOC laboratory.

The network combines a physical Cisco router, a Catalyst C9200L switch, departmental VLANs, Linux servers, Windows workstations, and monitoring services.

This document records the available evidence concerning the router's network role, addressing, monitoring, and intended segmentation policies.

**Important:** The router's current running configuration was not included in the available evidence. Therefore, the document distinguishes observed information from configurations that have not been independently verified.

## 2. Physical Infrastructure

The router is installed in the laboratory's network rack alongside the Cisco Catalyst C9200L switch and structured cabling infrastructure.

The available photographs identify the router as a **Cisco Catalyst C8200L-1N-4T**.

![Cisco router, switch and patch panel](../assets/images/physical/cisco-router-switch-patch-panel.jpg)

The switch configuration snapshot collected on November 4, 2026, identifies interface `Gi1/0/1` as a trunk associated with the router uplink.

This supports the documented network architecture but does not independently establish the configuration of the corresponding physical interface or VLAN subinterfaces on the router.

The router-side interface name remains unverified.

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
| 50 | Not independently verified in this evidence set | Additional validation required |
| 60 | Not verified | Additional validation required |
| 70 | Not verified | Additional validation required |

The November 4 technical records also identify `192.168.10.1` as the router's management-side address.

These observations establish the gateway settings visible on the endpoints at the time of collection.

They do not independently confirm the router's subinterface configuration, gateway ownership for every VLAN, or successful forwarding between departments.

## 5. Intended Network Access Policy

The intended segmentation model distinguishes the IT/NOC administration network from the departmental, wireless, and IoT networks.

### Administrative access

VLAN 10 is designated for administration and monitoring.

The intended policy permits authorized administrative systems to initiate management connections to services and devices in other VLANs when required.

### Departmental isolation

VLANs 20, 30, and 40 are intended to remain isolated from one another, except where explicitly authorized services require communication.

### VoIP and authentication services

VLAN 50 hosts the documented Asterisk and FreeRADIUS server.

Access to these services should be restricted according to application requirements.

### Wireless and IoT isolation

VLANs 60 and 70 are intended to have restricted access to internal enterprise resources.

Any necessary exceptions, including communication between a wireless access point and FreeRADIUS, must be defined according to the actual source addresses and service requirements.

**Implementation status:** These are intended access policies, not verified ACL rules.

The available records do not establish the exact ACL entries, interface directions, rule order, or successful enforcement of the policy.

## 6. Router Monitoring

The router is represented in the laboratory's Zabbix and Grafana monitoring environment.

The collected evidence includes router availability information and interface-related metrics.

### Grafana — Router Dashboard

![Router monitoring dashboard — Part 1](../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

![Router monitoring dashboard — Part 2](../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

These screenshots document monitoring information available during the collection period.

They do not demonstrate continuous availability, complete interface coverage, or the operational correctness of every routing and security configuration.

The Zabbix host inventory also provides evidence of an SNMP monitoring interface associated with the router.

The router's complete SNMP configuration and access restrictions were not independently verified.

## 7. DHCP, NAT and External Connectivity

The router's possible involvement in DHCP services, address allocation, NAT, and external connectivity is part of the network validation scope.

However, the available evidence does not establish:

- Whether DHCP pools are configured directly on the C8200L.
- Whether DHCP relay is used.
- The configured DHCP scopes and excluded addresses.
- The active NAT configuration.
- The external interface configuration.
- The complete routing table or default route.

No configuration examples are presented as deployed settings without supporting evidence.

## 8. Verification Opportunities

Future verification may use existing configuration records, monitoring history, and authorized connectivity tests.

| Area | Verification objective |
|---|---|
| Inter-VLAN routing | Identify actual routing interfaces and confirm authorized forwarding |
| Gateway addressing | Confirm gateway ownership and interface addresses |
| ACLs | Establish whether intended access restrictions are enforced |
| DHCP | Identify the active address assignment mechanism |
| NAT | Establish whether address translation is configured and operational |
| SNMP | Confirm router monitoring configuration and expected metrics |
| Troubleshooting | Record observed failures and their supporting evidence |

Connectivity tests should consider endpoint firewalls and service behavior before attributing a failed connection to an ACL.

A successful ICMP response also does not prove that every required application is reachable.

## 9. Known Limitations

At the time of this documentation update:

1. The router's current running configuration is unavailable.
2. Its exact VLAN subinterfaces and trunk encapsulation settings have not been verified.
3. Intended ACL policies have not been demonstrated through configuration evidence and controlled tests.
4. DHCP and NAT implementations remain unverified.
5. Monitoring evidence represents historical snapshots rather than continuous operational assurance.
6. The router-side physical interface connected to the switch has not been identified from the available configuration records.

These limitations are documented to preserve technical accuracy.

## 10. Related Documentation

- [Physical infrastructure](../evidence/physical-infrastructure.md)
- [Cisco switch and VLAN configuration snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Workstation inventory](../endpoints/workstation-inventory.md)
- [Zabbix monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana monitoring](../monitoring/grafana-monitoring.md)

---

**Documentation principle:** This page describes an observed laboratory environment and its intended network architecture. Unverified configurations are not represented as implemented or validated.
