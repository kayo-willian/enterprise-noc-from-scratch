# Evidence collection record — November 6, 2026

**English** | [Português (BR)](../pt-BR/evidencias/registro-coleta-2026-11-06.md)

> **Project:** Enterprise NOC — From Scratch  
> **Record type:** dated evidence collection inventory  
> **Status:** technical evidence collection record

## Overview

On November 6, 2026, physical and logical infrastructure evidence was collected from the lab. The materials include photographs of equipment, screenshots of workstations and monitoring tools, hardware records, and technical documents.

The original files are preserved in private working storage. Published documentation uses selected and sanitized copies of the collected material; private credentials and institution-specific identifiers are excluded.

## Documented components

| Area | Collected evidence | Technical record |
|---|---|---|
| Physical infrastructure | Rack, Cisco C8200L router, Catalyst 9200L switch, patch panel, cabling, and workstations. | [Rack and cabling](physical-infrastructure.md) |
| Workstations | Records for eight Windows computers and two Linux machines with distinct roles in the lab. | [Computer inventory](../endpoints/workstation-inventory.md) |
| Networking | Department-level IP configuration screenshots and a historical switch configuration captured before SNMP was enabled. | [Switch configuration](../networking/switch-vlan-snapshot-2026-11-04.md) |
| Telephony and authentication | Two Grandstream IP phones and technical documentation for the Asterisk/FreeRADIUS server. | [VoIP and authentication](../services/asterisk-freeradius.md) |
| Containers | Docker/Portainer records showing ten running containers at the time of collection. | [Docker environment](../containers/docker-services.md) |
| Observability | Zabbix, Grafana, and Uptime Kuma screenshots, including infrastructure and service dashboards. | [Zabbix](../monitoring/zabbix-monitoring.md), [Grafana](../monitoring/grafana-monitoring.md) |
| Additional services | Evidence of Pi-hole, a reverse proxy, and a containerized web service. | [DNS and availability](../services/dns-and-availability.md) |

## Record Dates and Inventory Counts

The [C9200L configuration](../networking/switch-vlan-snapshot-2026-11-04.md) was collected on November 4, 2026. The [physical photographs](physical-infrastructure.md), [computer inventory](../endpoints/workstation-inventory.md), and [monitoring records](../monitoring/zabbix-monitoring.md) refer to the November 6 collection.

The computer inventory covers **eight Windows workstations and two Linux computers**. The twelve hosts registered in Zabbix include those ten computers plus the C8200L router and C9200L switch. The [Zabbix record](../monitoring/zabbix-monitoring.md#workstation-address-discrepancies) lists six differences between photographed workstation IPv4 addresses and host registrations.

## Historical Evidence Boundaries

- Some workstation IP addresses in the photographs differ from the addresses registered in Zabbix on the collection date.
- The collected material includes unavailable hosts, unsupported items, and panels showing no data. These are point-in-time observations and do not establish continuous availability.
- Public image selection excludes credentials, institution-specific information, and private identifiers.
- The historical switch configuration does not replace a current export of the device's configuration.
- The technical inventory includes models and specifications only where captured in the collected evidence.


---

**Note:** This record documents the existence and general scope of collected evidence. It does not certify continuous operation, comprehensive security testing, or validation of every configuration.
