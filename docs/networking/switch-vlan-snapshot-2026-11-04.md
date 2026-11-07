# Cisco Catalyst 9200L — VLAN and Port Configuration

[English](switch-vlan-snapshot-2026-11-04.md) | [Português (Brasil)](../pt-BR/redes/registro-switch-vlans-2026-11-04.md)

## 1. Overview

The Enterprise NOC — From Scratch laboratory uses a Cisco Catalyst C9200L switch to connect departmental workstations, Linux servers, IP telephones, and wireless networking equipment.

This document describes the VLAN assignments and interface configuration identified in a Cisco IOS XE `show running-config` capture collected on **November 4, 2026**.

The configuration was obtained through a serial console connection from the Linux computer assigned to Asterisk and FreeRADIUS.

**Evidence limitation:** The capture predates the switch's SNMP monitoring configuration. Therefore, it must not be interpreted as the complete or current running configuration.

## 2. Network Equipment

The documented infrastructure includes:

| Equipment | Model | Function |
|---|---|---|
| Router | Cisco Catalyst C8200L | Routing between network segments |
| Switch | Cisco Catalyst C9200L-24T-4G | Ethernet switching and VLAN segmentation |
| Structured cabling | Category 6 patch panel | Physical network termination |
| Wireless router | TP-Link Archer AX53 | Corporate Wi-Fi |
| Additional wireless equipment | Model not verified | IoT network |

The switch configuration identifies Cisco IOS XE version `17.15` and a provisioned `c9200l-24t-4g` platform.

### Physical Evidence

![Cisco networking equipment and structured cabling](../assets/images/physical/cisco-router-switch-patch-panel.jpg)

The photograph documents the physical presence of the Cisco router, Catalyst switch, and structured cabling components.

The photograph does not independently prove the operational state of every connected interface.

## 3. VLAN Segmentation

The switch configuration contains the following VLAN assignments:

| VLAN | Department or purpose | Switch interfaces |
|---|---|---|
| 10 | IT and NOC infrastructure | Gi1/0/2–3 |
| 20 | Accounting | Gi1/0/4–6 |
| 30 | Finance | Gi1/0/7–8 |
| 40 | Sales | Gi1/0/9–10 |
| 50 | VoIP and Asterisk/FreeRADIUS server | Gi1/0/11–13 |
| 60 | Corporate Wi-Fi | Gi1/0/15 |
| 70 | IoT network | Gi1/0/14 |

The VLAN assignments above come directly from the collected switch configuration.

The existence and operation of every VLAN across the complete network require additional validation using VLAN status and routing information.

### 3.1 Logical Organization

```text
                      Cisco C8200L
                          Router
                            |
                         802.1Q
                            |
                     Gi1/0/1 — Trunk
                            |
                     Cisco C9200L
                          Switch
                            |
          +-----------------+------------------+
          |                 |                  |
       VLAN 10           VLAN 20            VLAN 30
       IT / NOC         Accounting           Finance
          |
       VLAN 40           VLAN 50            VLAN 60
        Sales           VoIP/RADIUS       Corporate Wi-Fi

                         VLAN 70
                           IoT
```

This diagram represents the documented logical segmentation.

It is not a complete physical cable map or proof of every routed communication path.

## 4. Switch Port Mapping

The following table reproduces the interface assignments identified in the November 4 configuration.

| Interface | Configuration | Description / Intended connection |
|---|---|---|
| Gi1/0/1 | Trunk | Connection to Cisco router |
| Gi1/0/2 | Access VLAN 10 | IT / NOC computers |
| Gi1/0/3 | Access VLAN 10 | IT / NOC computers |
| Gi1/0/4 | Access VLAN 20 | Accounting computers |
| Gi1/0/5 | Access VLAN 20 | Accounting computers |
| Gi1/0/6 | Access VLAN 20 | Accounting computers |
| Gi1/0/7 | Access VLAN 30 | Finance computers |
| Gi1/0/8 | Access VLAN 30 | Finance computers |
| Gi1/0/9 | Access VLAN 40 | Sales computers |
| Gi1/0/10 | Access VLAN 40 | Sales computers |
| Gi1/0/11 | VLAN 50 assigned; operating mode requires verification | Debian Asterisk/FreeRADIUS server |
| Gi1/0/12 | Access VLAN 50 | VoIP / Grandstream |
| Gi1/0/13 | Access VLAN 50 | VoIP / Grandstream |
| Gi1/0/14 | Access VLAN 70 | IoT wireless equipment |
| Gi1/0/15 | Access VLAN 60 | Corporate Wi-Fi |

Interfaces Gi1/0/16 through Gi1/0/24 and Gi1/1/1 through Gi1/1/4 appear without specific interface configuration statements in this snapshot.

This does not establish whether those interfaces were physically connected, administratively disabled, or operationally down.

### 4.1 Router Trunk

The collected configuration contains:

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

This establishes that Gi1/0/1 was configured as a trunk interface.

The capture does not explicitly define an allowed VLAN list or a custom native VLAN on that interface.

The router-side trunk and VLAN subinterface configuration were not included in this evidence.

### 4.2 Departmental Access Ports

The following example represents the recorded configuration for an Accounting workstation port:

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

Equivalent access-port configurations appear for the IT, Finance, Sales, VoIP, corporate Wi-Fi, and IoT segments.

### 4.3 Special Case: Gi1/0/11

The Asterisk/FreeRADIUS server interface contains:

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Unlike the other departmental interfaces, this configuration does not explicitly include:

```cisco
switchport mode access
```

The presence of `spanning-tree portfast trunk` also differs from the configuration used on the other workstation ports.

**The operational switching mode of Gi1/0/11 requires verification.**

This document preserves the original configuration without silently modifying or interpreting it as a standard access-port configuration.

## 5. Observed IP Addressing

Network photographs and Linux inventory records collected on November 6 provide the following addressing information.

| VLAN | Network observed or inferred from /24 host addressing | Documented examples |
|---|---|---|
| 10 | 192.168.10.0/24 | Main NOC: 192.168.10.12; IT 2: 192.168.10.13 |
| 20 | 192.168.20.0/24 | Accounting: 192.168.20.11–13 |
| 30 | 192.168.30.0/24 | Finance: 192.168.30.10–11 |
| 40 | 192.168.40.0/24 | Sales: 192.168.40.10–11 |
| 50 | 192.168.50.0/24 | Asterisk: 192.168.50.2; VoIP: 192.168.50.10–11 |
| 60 | Not established | Corporate wireless network |
| 70 | Not established | IoT network |

The `/24` networks are derived from the observed host addresses and subnet masks.

The collected workstation evidence also identifies `.1` as the default gateway in the documented departmental networks.

The available evidence does not include the current router configuration required to verify the gateway interfaces, DHCP settings, ACLs, or inter-VLAN routing policies.

### Addressing Consistency

The November 6 audit identified six differences between photographed Windows workstation addresses and the host interfaces registered in Zabbix.

The photographed addresses are retained as historical evidence.

The discrepancies are discussed in:

- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)

## 6. Spanning Tree

The collected configuration includes:

```cisco
spanning-tree mode rapid-pvst
spanning-tree extend system-id
```

Rapid PVST+ was configured on the switch.

Most documented access interfaces also contain `spanning-tree portfast`.

This configuration evidence does not include a complete spanning-tree operational status report.

The root bridge, blocked interfaces, and complete spanning-tree topology were not independently verified.

## 7. Switch Monitoring

The original switch configuration was collected before SNMP monitoring was enabled.

Later evidence from Zabbix and Grafana shows switch monitoring dashboards containing:

- CPU utilization.
- Memory utilization.
- Hardware sensors.
- Interface status.
- Traffic measurements.
- Interface errors.

### Zabbix Evidence

![Cisco Catalyst switch monitoring in Zabbix](../assets/images/monitoring/zabbix/zabbix_dashboard3.png)

### Grafana Evidence

![Cisco Catalyst switch monitoring in Grafana](../assets/images/monitoring/grafana/grafana_dashboard_switch1.png)

These screenshots demonstrate that monitoring data was available at the time of collection.

They do not provide the complete final SNMP configuration.

Some Grafana interface panels also contain repeated labels, which require verification against the underlying monitoring items.

## 8. Known Limitations

| Component | Limitation |
|---|---|
| Router configuration | Complete current running configuration not available |
| Inter-VLAN routing | Detailed routing configuration not independently verified |
| ACLs | Effective access-control policies not established |
| DHCP | Complete DHCP configuration not available |
| Switch management | Management address requires confirmation against current configuration |
| VLAN 60 | Complete wireless addressing and authentication not verified |
| VLAN 70 | IoT equipment model and addressing not verified |
| Gi1/0/11 | Operational interface mode requires confirmation |
| SNMP | November 4 configuration predates monitoring activation |
| Physical cabling | Complete end-to-end cable and patch-panel mapping not verified |

These limitations are preserved to distinguish documented configuration from assumptions.

## 9. Related Documentation

- [Physical Infrastructure](../evidence/physical-infrastructure.md)
- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)
- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)

**Switch configuration captured:** November 4, 2026.

**Additional infrastructure evidence:** November 6, 2026.

**Documentation status:** Historical configuration snapshot, not a verified final running configuration.
