# Cisco Catalyst C9200L — Configuration Snapshot

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](../pt-BR/redes/registro-switch-vlans-2026-11-04.md)

## Capture

| Attribute | Historical record |
|---|---|
| Equipment | Cisco Catalyst C9200L-24T-4G |
| Operating system | Cisco IOS XE 17.15 |
| Command | `show running-config` |
| Date | November 4, 2026 |
| Collection method | Serial console from the Linux Asterisk/FreeRADIUS computer |

This snapshot **predates subsequent SNMP monitoring changes**; it is not the switch's complete current configuration or an interface-status report.

![Cisco router, switch and patch panel](../assets/images/physical/cisco-router-switch-patch-panel.jpg)

## Recorded VLANs

| VLAN | Segment | Assigned interfaces |
|---|---|---|
| 10 | IT / NOC | Gi1/0/2–3 |
| 20 | Accounting | Gi1/0/4–6 |
| 30 | Finance | Gi1/0/7–8 |
| 40 | Sales | Gi1/0/9–10 |
| 50 | VoIP / Authentication | Gi1/0/11–13 |
| 60 | Corporate Wi-Fi | Gi1/0/15 |
| 70 | IoT | Gi1/0/14 |

The detailed per-port inventory is maintained in the [switch port map](switch-port-map.md). The VLAN 70 Archer AX53 model is identified in the equipment inventory, not by the IOS XE commands.

## Configuration excerpts

### Router-facing trunk — Gi1/0/1

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

No explicit allowed-VLAN list or custom native VLAN is recorded. The C8200L interface and router-side VLAN subinterfaces are outside this capture.

### Accounting access port — Gi1/0/4

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

### Voice server — Gi1/0/11

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Gi1/0/11 does **not** have an explicit `switchport mode access` in the collected statements. The `spanning-tree portfast trunk` command does not determine its effective switching mode.

Interfaces Gi1/0/16–24 and Gi1/1/1–4 have no interface-specific statements in the snapshot; their physical or operational status is not established.

### Spanning Tree

```cisco
spanning-tree mode rapid-pvst
spanning-tree extend system-id
```

Rapid PVST+ is configured, and several access ports use PortFast. No operational output establishes the root bridge, blocked interfaces, or convergence state.

## Rapid PVST+ and Switchport Configuration

The commands `spanning-tree mode rapid-pvst` and `spanning-tree extend system-id` establish **Rapid PVST+ configuration** in this historical export. Rapid PVST+ is intended to prevent Layer 2 forwarding loops while maintaining per-VLAN spanning-tree behavior, but these global statements **do not identify** the actual root bridge, alternate/blocked paths or convergence events. Those require dated operational show-command output.

The captured accounting port `Gi1/0/4` declares `switchport mode access`, `switchport access vlan 20` and `spanning-tree portfast`. PortFast is commonly applied to trusted endpoint-facing interfaces to speed the forwarding transition; it should not be interpreted as proof that all access links were free of loops.

**Important exception — Gi1/0/11:** `switchport access vlan 50` and `spanning-tree portfast trunk` occur together, with **no explicit `switchport mode access`**. The PortFast command does not establish the effective interface mode. Confirming whether the live port is access or trunk would require an authorized operational interface-mode check and the current configuration. Neither was included in the November 4 capture.

The historical snapshot is a **configuration record**, whereas later Zabbix/Grafana panels are **telemetry records**. A displayed `UP`/`DOWN` interface or historical throughput graph should be reconciled with an actual port identifier before drawing conclusions about physical links. The [port map](switch-port-map.md) retains the exact interface statements.


## Later monitoring evidence

The Zabbix and Grafana screenshots below document switch metrics collected **after** the original configuration capture.

![Catalyst switch dashboard in Zabbix](../assets/images/monitoring/zabbix/zabbix_dashboard3.png)

![Catalyst switch dashboard in Grafana](../assets/images/monitoring/grafana/grafana_dashboard_switch1.png)

The dashboards include interface and hardware metrics but are not a substitute for an SNMP configuration export. Some Grafana panels repeat interface labels; those labels are not counted as independent physical interfaces.

**Limits:** The switch record does not verify router ACLs, successful inter-VLAN routing, wireless client addressing, or physical link state.

## References

[Networking overview](README.md) · [Switch port map](switch-port-map.md) · [VLAN inventory](vlans.md) · [Router](router-c8200l.md) · [Logical topology](consolidated-logical-topology.md) · [Physical infrastructure](../evidence/physical-infrastructure.md) · [Zabbix](../monitoring/zabbix-monitoring.md) · [Grafana](../monitoring/grafana-monitoring.md)
