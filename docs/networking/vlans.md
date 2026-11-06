# VLAN Segmentation

## Overview

The enterprise network uses VLANs (Virtual Local Area Networks) to logically separate departments, infrastructure services, and wireless networks.

This segmentation provides a structured network environment and separates traffic between different functional areas.

## VLAN Configuration

| VLAN ID | Name | Purpose |
|---|---|---|
| 10 | IT & Monitoring | IT workstations and network monitoring infrastructure |
| 20 | Accounting | Accounting department workstations |
| 30 | Finance | Financial department workstations |
| 40 | Sales | Sales department workstations |
| 50 | VoIP | IP telephony and Asterisk PBX services |
| 60 | Corporate Wi-Fi | Corporate wireless network |
| 70 | IoT | Internet of Things devices |

## Network Equipment

The network infrastructure includes Cisco Catalyst equipment:

- **Cisco Catalyst C8200L:** Router used for network connectivity and inter-VLAN routing.
- **Cisco Catalyst 9200L:** Switch used to connect devices across the segmented network.

## Documentation Status

**Status:** In Progress

Detailed switch configurations, trunk interfaces, VLAN assignments, routing configuration, and connectivity tests will be documented in future updates.

The VLAN 60 and VLAN 70 assignments reflect the current design and are pending final configuration verification.
