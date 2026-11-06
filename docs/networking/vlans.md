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

The physical network includes the following equipment:

- **Cisco Catalyst C8200L:** Enterprise router.
- **Cisco Catalyst 9200L:** Enterprise switch.
- **Intelbras Wireless Router (VLAN 60):** Provides connectivity to the corporate wireless network.
- **Intelbras Wireless Router (VLAN 70):** Provides connectivity to IoT devices.

Both Intelbras routers use the same hardware model, which will be identified during the final equipment inventory.

## Corporate Wireless Network — VLAN 60

VLAN 60 is dedicated to corporate wireless connectivity.

The laboratory implementation includes:

- An Intelbras wireless router.
- An addressing scheme within the `10.0.0.0` range.
- Access restrictions involving ACLs.
- RADIUS-based access control.

The wireless segment is intended to remain isolated from the main network according to the laboratory's access policies.

The exact subnet mask, router model, ACL rules, and RADIUS configuration are pending documentation and verification.

## IoT Network — VLAN 70

VLAN 70 is dedicated to Internet of Things (IoT) devices.

The environment includes:

- An Intelbras wireless router.
- An Amazon Alexa device with a display.
- A smart light bulb controlled through Alexa voice commands.

The IoT segment demonstrates the integration of smart devices into a segmented enterprise-style network.

The specific router configuration and IoT access policies are pending verification.

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
