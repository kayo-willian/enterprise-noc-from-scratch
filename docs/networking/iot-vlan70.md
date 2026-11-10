# IoT Network — VLAN 70

**Project:** Enterprise NOC — From Scratch  
**Segment:** VLAN 70 — Internet of Things (IoT)  
**Network equipment:** Dedicated TP-Link Archer AX53 (Wi-Fi 6 AX3000)  
**Connected device:** Amazon Alexa  
**Switch:** Cisco Catalyst C9200L  
**Record date:** November 9, 2026

## 1. Overview

VLAN 70 is the dedicated IoT network segment in the Enterprise NOC laboratory. An Amazon Alexa connects by Wi-Fi to a separate TP-Link Archer AX53, which is connected by Ethernet to the Cisco Catalyst C9200L switch. The corporate Wi-Fi segment uses another Archer AX53 on VLAN 60; they are separate physical wireless devices.

## 2. Connectivity

```text
Amazon Alexa
    |
    | Wi-Fi
    v
TP-Link Archer AX53 — IoT
    |
    | Ethernet
    v
Cisco Catalyst C9200L
Gi1/0/14 — Access VLAN 70
    |
    | Router-facing trunk: Gi1/0/1
    v
Cisco Catalyst C8200L
```

The November 4 switch configuration records `Gi1/0/14` with access VLAN 70 and `Gi1/0/1` as the router-facing trunk. The physical Wi-Fi-to-switch connection and Alexa association describe the installed laboratory topology. The diagram does not imply that an Alexa client address resides directly in the VLAN 70 IP subnet.

## 3. Network Segmentation

| VLAN | Segment | Function |
|---|---|---|
| 60 | Corporate Wi-Fi | Corporate wireless connectivity |
| 70 | IoT | Dedicated Alexa and smart-device connectivity |

The network design separates IoT equipment from administrative and departmental resources. The access VLAN assignment is visible in the switch record; the application of router ACL restrictions is not demonstrated by that record.

## 4. IP Addressing and Operating Mode

The collected evidence does not include a configuration export from the IoT Archer AX53. In access point mode, Wi-Fi clients can participate in the VLAN 70 IP network. In router mode with NAT, wireless clients can instead reside on a separate subnet behind the device.

Neither operating mode, the Alexa IP address, the DHCP server, NAT behavior, nor the IoT default gateway is asserted as deployed without configuration evidence. These details are **outside the scope of the historical configuration record**, not outstanding steps required to complete this documentation.

## 5. Observability

The monitoring screenshots record the Cisco network infrastructure through Zabbix and Grafana. Direct metrics from the IoT Archer AX53 or Alexa are not present in the documented monitoring inventory. VLAN 70 is documented as part of the logical switching design and the laboratory IoT connectivity.

## 6. Evidence Scope

This page combines the dated C9200L switch configuration and the laboratory equipment inventory. It documents the implemented connection and distinguishes it from settings not captured in the available configuration exports. No SSIDs, passwords, RADIUS secrets, or unique device identifiers are published.

## Related Documentation

- [VLAN Segmentation](vlans.md)
- [Switch Port Map](switch-port-map.md)
- [Cisco Switch Configuration Snapshot](switch-vlan-snapshot-2026-11-04.md)
- [Cisco C8200L Router](router-c8200l.md)
- [Corporate Wi-Fi — VLAN 60](corporate-wifi-vlan60.md)
- [Physical Infrastructure](../evidence/physical-infrastructure.md)
