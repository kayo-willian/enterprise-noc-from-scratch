# VLAN Segmentation

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](../pt-BR/redes/vlans.md)

## VLAN and addressing inventory

The November 4, 2026 Cisco C9200L configuration records seven VLANs. Endpoint IP information comes from the November 6 inventory, not from a complete router configuration export.

| VLAN | Segment | Switch ports | Documented network | Recorded gateway |
|---|---|---|---|---|
| 10 | IT / NOC | Gi1/0/2–3 | `192.168.10.0/24` | `192.168.10.1` (IT workstation) |
| 20 | Accounting | Gi1/0/4–6 | `192.168.20.0/24` | `192.168.20.1` (workstation) |
| 30 | Finance | Gi1/0/7–8 | `192.168.30.0/24` | `192.168.30.1` (workstation) |
| 40 | Sales | Gi1/0/9–10 | `192.168.40.0/24` | `192.168.40.1` (workstation) |
| 50 | VoIP / Authentication | Gi1/0/11–13 | `192.168.50.0/24` | `192.168.50.1` (voice server) |
| 60 | Corporate Wi-Fi | Gi1/0/15 | Client subnet not established | Not established |
| 70 | IoT | Gi1/0/14 | Client subnet not established | Not established |

**Gateway values are host observations**, not verified C8200L interface assignments. The `/24` networks are based on collected endpoint addresses and masks.

## Documented equipment

| VLAN | Examples from the inventory |
|---|---|
| 10 | Debian 13 NOC server `192.168.10.12`, IT workstation `192.168.10.13` |
| 20 | Accounting workstations `192.168.20.11–13` |
| 30 | Finance workstations `192.168.30.10–11` |
| 40 | Sales workstations `192.168.40.10–11` |
| 50 | Asterisk/FreeRADIUS `192.168.50.2`; Grandstream phones `192.168.50.10–11` |
| 60 | Corporate TP-Link Archer AX53 |
| 70 | Separate IoT Archer AX53 and Amazon Alexa |

The switch-side trunk is configured on `Gi1/0/1`. The router-facing interface's allowed VLAN list is not explicitly specified in the collected configuration. On `Gi1/0/11`, VLAN 50 is assigned but the effective switchport mode is not established.

## Security design versus evidence

VLANs create separate Layer 2 broadcast domains. Inter-VLAN traffic requires Layer 3 routing; **VLAN assignment alone is not an ACL enforcement test**.

| Segment | Access-policy requirement |
|---|---|
| IT / NOC | Authorized management and monitoring |
| Accounting / Finance / Sales | Departmental separation, with authorized service exceptions |
| Voice / Authentication | Connectivity for voice and authentication services |
| Corporate Wi-Fi | Limit unauthorized access to internal systems |
| IoT | Separate smart devices from sensitive corporate resources |

No complete C8200L ACL export or end-to-end isolation test is present in the records.

The VLAN 60 and 70 Archer AX53 devices are separate physical units. Their operating modes, client IP networks, DHCP, and NAT settings were not captured. In router mode, wireless clients may use private subnets behind those devices rather than the corresponding upstream VLAN networks.

Workstations use DHCP. Addresses in the November 6 inventory may differ from earlier Zabbix registrations; no static reservation is inferred.

## References

[Networking overview](README.md) · [Logical topology](consolidated-logical-topology.md) · [Switch snapshot](switch-vlan-snapshot-2026-11-04.md) · [Port map](switch-port-map.md) · [Router](router-c8200l.md) · [Corporate Wi-Fi](corporate-wifi-vlan60.md) · [IoT](iot-vlan70.md) · [Workstation inventory](../endpoints/workstation-inventory.md)
