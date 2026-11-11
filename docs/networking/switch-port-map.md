# Cisco Catalyst C9200L — Switch Port Map

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](../pt-BR/redes/mapa-de-portas-switch.md)

## Interface inventory

The table reflects the C9200L-24T-4G IOS XE 17.15 configuration captured on **November 4, 2026**, combined with documented equipment roles.

| Interface | Documented connection | Configuration |
|---|---|---|
| Gi1/0/1 | Cisco C8200L | Router-facing trunk |
| Gi1/0/2–3 | IT / NOC | Access VLAN 10 |
| Gi1/0/4–6 | Accounting | Access VLAN 20 |
| Gi1/0/7–8 | Finance | Access VLAN 30 |
| Gi1/0/9–10 | Sales | Access VLAN 40 |
| Gi1/0/11 | Debian Asterisk / FreeRADIUS | Access VLAN 50 assigned; operating mode unverified |
| Gi1/0/12–13 | Grandstream IP phones | Access VLAN 50 |
| Gi1/0/14 | Dedicated TP-Link Archer AX53 (IoT) | Access VLAN 70 |
| Gi1/0/15 | TP-Link Archer AX53 (corporate Wi-Fi) | Access VLAN 60 |
| Gi1/0/16–24 | No specific equipment assignment established | No interface-specific statements in the capture |
| Gi1/1/1–4 | SFP uplink interfaces | No interface-specific statements in the capture |

No interface-specific statements **does not mean** a port was free, disconnected, disabled, or down. The table records configuration and intended connection, not physical link-state measurements.

## Recorded interface examples

### Router-facing trunk — Gi1/0/1

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

The capture does not specify a `switchport trunk allowed vlan` list or custom native VLAN. The router-side interface and subinterfaces were not captured. The project VLAN inventory must not be treated as the trunk's explicitly configured allowed list.

### Accounting access port — Gi1/0/4

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

### Asterisk / FreeRADIUS — Gi1/0/11

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Unlike the access-port example, Gi1/0/11 has no explicit `switchport mode access` statement. `spanning-tree portfast trunk` does not prove the effective switchport mode; the historical configuration is retained without classifying the port as confirmed access or trunk.

## Record scope

Assignments are taken from the dated switch capture; the AX53 models come from the equipment inventory. This record does not independently verify port operation, connected-device status, or router ACL enforcement.

## References

[Networking overview](README.md) · [Switch configuration snapshot](switch-vlan-snapshot-2026-11-04.md) · [VLAN inventory](vlans.md) · [Router](router-c8200l.md) · [Logical topology](consolidated-logical-topology.md)
