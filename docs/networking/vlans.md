# VLAN Segmentation

English | **[Português (Brasil)](../pt-BR/redes/vlans.md)**

## Overview

The enterprise infrastructure uses VLANs (Virtual Local Area Networks) to logically separate departments, infrastructure services, wireless connectivity, and IoT devices.

The network design includes seven VLANs, providing logical segmentation for different operational requirements.

## VLAN Inventory

| VLAN ID | Name | Purpose |
|---|---|---|
| 10 | IT & Monitoring | IT infrastructure and monitoring services |
| 20 | Accounting | Accounting department |
| 30 | Finance | Finance department |
| 40 | Sales | Sales department |
| 50 | VoIP | IP telephony and PBX services |
| 60 | Corporate Wi-Fi | Corporate wireless connectivity |
| 70 | IoT | Smart devices and IoT connectivity |

## Network Infrastructure

The physical network includes:

- **Cisco Catalyst C8200L:** Enterprise routing infrastructure.
- **Cisco Catalyst C9200L:** Managed Ethernet switch.
- **TP-Link Archer AX53 (VLAN 60):** Corporate wireless connectivity.
- **TP-Link Archer AX53 (VLAN 70):** Dedicated wireless connectivity for IoT devices.

The corporate wireless and IoT networks use separate wireless routers of the same model.

## Corporate Wireless Network — VLAN 60

VLAN 60 is dedicated to corporate wireless connectivity.

The network uses a TP-Link Archer AX53, identified through physical equipment evidence collected on November 6, 2026.

The Cisco Catalyst C9200L configuration snapshot from November 4, 2026, assigns interface `Gi1/0/15` to VLAN 60.

The switch snapshot documents the VLAN assignment; it does not contain the wireless device operating mode, client addressing, DHCP, or authentication configuration.

The access-policy design restricts unauthorized communication between corporate Wi-Fi and other internal VLANs.

## IoT Network — VLAN 70

VLAN 70 is dedicated to Internet of Things (IoT) connectivity.

The network includes an Amazon Alexa connected over Wi-Fi to a dedicated TP-Link Archer AX53.

The wireless router connects to the Cisco Catalyst C9200L through Ethernet.

The switch configuration snapshot from November 4, 2026, assigns interface `Gi1/0/14` to VLAN 70.

The switch snapshot documents the VLAN assignment; it does not contain the wireless router's internal addressing, DHCP, NAT, or operating-mode settings.

The IoT network design separates IoT devices from sensitive corporate resources.

The switch record documents the VLAN assignment; the access-policy requirements are documented separately from router ACL implementation.


## Record Scope

This VLAN inventory consolidates the design and historical Cisco switch configuration collected on November 4, 2026. Device-specific settings are described only where present in the collected evidence. The absence of wireless configuration exports is not presented as a pending publication task.
