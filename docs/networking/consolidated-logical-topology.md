# Consolidated Logical Network Topology

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](../pt-BR/redes/topologia-logica-consolidada.md)

## Topology

The diagram shows the network relationships documented in the **November 4–6, 2026** laboratory records. Connections represent equipment associations, not verified end-to-end traffic or a cable-by-cable survey.

```mermaid
flowchart TB
    R["Cisco Catalyst C8200L"]
    SW["Cisco Catalyst C9200L"]
    R ---|"Router-facing trunk<br/>Switch Gi1/0/1"| SW
    SW --> V10["VLAN 10 · IT / NOC"]
    SW --> V20["VLAN 20 · Accounting"]
    SW --> V30["VLAN 30 · Finance"]
    SW --> V40["VLAN 40 · Sales"]
    SW --> V50["VLAN 50 · Voice / Authentication"]
    SW --> V60["VLAN 60 · Corporate Wi-Fi"]
    SW --> V70["VLAN 70 · IoT"]
    V10 --> NOC["Debian 13<br/>Monitoring / Docker"]
    V10 --> IT["IT workstation"]
    V20 --> ACC["3 Windows workstations"]
    V30 --> FIN["2 Windows workstations"]
    V40 --> SALES["2 Windows workstations"]
    V50 --> PBX["Debian forky/sid<br/>Asterisk / FreeRADIUS"]
    V50 --> PHONES["2 Grandstream IP phones"]
    V60 --> WIFI["TP-Link Archer AX53"]
    V70 --> IOT["Dedicated TP-Link Archer AX53"]
    IOT --> ALEXA["Amazon Alexa"]
```

The switch-side `Gi1/0/1` trunk is recorded in the C9200L configuration. Neither the corresponding C8200L port nor the router's complete VLAN subinterfaces were captured.

## Equipment and addressing

| Segment | Equipment / examples | Network or address |
|---|---|---|
| VLAN 10 · IT / NOC | Main Debian 13 server; IT workstation | `192.168.10.12`; `192.168.10.13` |
| VLAN 20 · Accounting | Three Windows workstations | `192.168.20.11–13` |
| VLAN 30 · Finance | Two Windows workstations | `192.168.30.10–11` |
| VLAN 40 · Sales | Two Windows workstations | `192.168.40.10–11` |
| VLAN 50 · Voice | Debian Asterisk / FreeRADIUS | `192.168.50.2/24` |
| VLAN 50 · Phones | Grandstream extensions 1001 (Sales), 1002 (IT) | `192.168.50.10`; `192.168.50.11` |
| VLAN 60 · Corporate Wi-Fi | TP-Link Archer AX53, switch `Gi1/0/15` | Client subnet not established |
| VLAN 70 · IoT | Separate Archer AX53, Alexa, switch `Gi1/0/14` | Client subnet not established |

The documented departmental networks (VLANs 10–50) use `/24` masks. The main NOC computer is a Dell OptiPlex 3020 running Debian 13; the voice server was recorded with Debian forky/sid.

| VLAN | Gateway recorded on equipment |
|---|---|
| 10 | `192.168.10.1` — IT workstation |
| 20 | `192.168.20.1` — Accounting workstation |
| 30 | `192.168.30.1` — Finance workstation |
| 40 | `192.168.40.1` — Sales workstation |
| 50 | `192.168.50.1` — Asterisk/FreeRADIUS server |

Gateway observations do not identify all router interfaces. DHCP is used on workstations; six differences between observed addresses and Zabbix host entries were documented.

## Services and monitoring

The main Debian server hosts Docker-based infrastructure services. The November 6 inventory recorded **10 running containers**, including Zabbix, Grafana, Portainer, Pi-hole and Uptime Kuma; related infrastructure includes MariaDB and web services.

Zabbix and Grafana provide historical monitoring views of Cisco equipment, hosts, and services. The captured dashboards include unavailable hosts and unsupported items; they do not establish uninterrupted availability.

![Cisco router, switch and patch panel](../assets/images/physical/cisco-router-switch-patch-panel.jpg)

## Operational Network Architecture and Monitoring Paths

The C9200L's **Gi1/0/1 trunk** establishes the switch-side association with the C8200L. Endpoint gateways observed in VLANs 10–50 describe configured host routes, but do **not** establish the router-side interfaces, 802.1Q subinterfaces, ACLs or permitted inter-VLAN flows. Likewise, a diagram edge represents a documented association, not a completed connectivity test.

A user reaching the NOC web portal from a departmental workstation would depend on **four distinct layers**: correct workstation addressing and gateway, permitted Layer 3 path to `192.168.10.12`, DNS resolution for the service name and a functioning Nginx/application upstream. The November 4–6 records establish parts of that chain separately; a successful cross-VLAN transaction was not recorded.

The corporate Wi-Fi Archer AX53 is connected on **Gi1/0/15 / VLAN 60**. FreeRADIUS is recorded in **VLAN 50** on `192.168.50.2`. This is an intended authentication dependency, not evidence that the AX53 acted as a RADIUS authenticator or that 802.1X succeeded.

### Monitoring Is a Different Data Path

```mermaid
flowchart LR
    CISCO["Cisco C8200L / C9200L"] -->|"SNMP"| Z["Zabbix Server"]
    HOSTS["Debian / Windows hosts"] -->|"Zabbix Agent"| Z
    Z --> DB[("MariaDB")]
    WEB["Zabbix Web / API"] <--> DB
    G["Grafana"] -->|"Zabbix data source"| WEB
    K["Uptime Kuma"] -.->|"Independent endpoint checks"| SERVICES["Selected services"]
```

This diagram restores the **service-to-monitoring relationships** documented before the networking consolidation. It describes a logical data flow, not a packet capture or a guarantee that all items were supported. The recorded Zabbix deployment contained unsupported items and unavailable hosts.

| Evidence | Supported conclusion | Not yet demonstrated |
|---|---|---|
| C9200L `show running-config` (November 4) | VLAN assignments, trunk, Spanning Tree settings | Router configuration, effective policy enforcement, all link states |
| System/endpoint inventory (November 6) | Host IPs, subnet masks and several gateways | DHCP pools and current lease allocation |
| Docker inventory (November 6) | Ten running containers and published ports | Application reachability from each VLAN |
| Monitoring screenshots (November 6) | Historical telemetry and alert conditions | Uninterrupted availability and complete coverage |

Command transcripts and full per-port records remain in the [switch snapshot](switch-vlan-snapshot-2026-11-04.md); host addresses remain in the [endpoint inventory](../endpoints/workstation-inventory.md). They are linked rather than copied into this architecture page.


## Evidence boundaries

- The C9200L snapshot documents VLANs, port assignments, and a trunk; it does not prove router ACL enforcement or all inter-VLAN paths.
- Gi1/0/11 has `switchport access vlan 50` and `spanning-tree portfast trunk`, but no explicit access-mode statement. Its effective mode is not established.
- The two AX53 devices have different roles. Their operating modes, client subnets, DHCP, and NAT settings were not captured; FreeRADIUS-to-Wi-Fi authentication was not verified.
- Endpoint addressing, Docker status, and monitoring screenshots are dated observations, not continuous service guarantees.

## References

[Networking overview](README.md) · [VLANs](vlans.md) · [Router](router-c8200l.md) · [Switch port map](switch-port-map.md) · [Switch snapshot](switch-vlan-snapshot-2026-11-04.md) · [Corporate Wi-Fi](corporate-wifi-vlan60.md) · [IoT](iot-vlan70.md) · [Workstation inventory](../endpoints/workstation-inventory.md) · [Docker services](../containers/docker-services.md) · [Asterisk / FreeRADIUS](../services/asterisk-freeradius.md) · [Physical infrastructure](../evidence/physical-infrastructure.md)
