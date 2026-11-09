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

The wireless router's operating mode, client addressing, DHCP configuration, and authentication settings require further verification.

The intended network architecture restricts unauthorized access between the corporate wireless network and other internal VLANs.

## IoT Network — VLAN 70

VLAN 70 is dedicated to Internet of Things (IoT) connectivity.

The network includes an Amazon Alexa connected over Wi-Fi to a dedicated TP-Link Archer AX53.

The wireless router connects to the Cisco Catalyst C9200L through Ethernet.

The switch configuration snapshot from November 4, 2026, assigns interface `Gi1/0/14` to VLAN 70.

The wireless router's operating mode, internal addressing, DHCP behavior, and NAT configuration remain pending verification.

The IoT network is intended to remain isolated from sensitive corporate infrastructure.

The exact routing and access control implementation has not yet been validated.


## Documentation Status

**Status:** In Progress

Additional technical documentation will cover:

- Physical network topology.
- VLAN assignments and switch interfaces.
- Trunk and access port configurations.
- Routing and access control policies.
- Wireless network configuration.
- Connectivity and isolation tests.

Configuration details will be documented after verification against the laboratory equipment.
