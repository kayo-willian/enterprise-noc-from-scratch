# Evidence collection record — November 6, 2026

**English** | [Português (BR)](../pt-BR/evidencias/registro-coleta-2026-11-06.md)

> **Project:** Enterprise NOC — From Scratch  
> **Record type:** preliminary evidence collection inventory  
> **Status:** evidence review and selection for publication

## Overview

On November 6, 2026, physical and logical infrastructure evidence was collected from the lab. The materials include photographs of equipment, screenshots of workstations and monitoring tools, hardware records, and technical documents.

The original files are preserved in private working storage. Images and configurations will only be added to the repository after reviewing their contents and redacting institutional identifiers or sensitive information.

## Documented components

| Area | Collected evidence |
|---|---|
| Physical infrastructure | Rack, Cisco C8200L router, Catalyst 9200L switch, patch panel, cabling, and workstations. |
| Workstations | Records for eight Windows computers and two Linux machines with distinct roles in the lab. |
| Networking | Department-level IP configuration screenshots and a historical switch configuration captured before SNMP was enabled. |
| Telephony and authentication | Two Grandstream IP phones and technical documentation for the Asterisk/FreeRADIUS server. |
| Containers | Docker/Portainer records showing ten running containers at the time of collection. |
| Observability | Zabbix, Grafana, and Uptime Kuma screenshots, including infrastructure and service dashboards. |
| Additional services | Evidence of Pi-hole, a reverse proxy, and a containerized web service. |

## Limitations and findings under review

- Some workstation IP addresses in the photographs differ from the addresses registered in Zabbix on the collection date.
- The collected material includes unavailable hosts, unsupported items, and panels showing no data. These are point-in-time observations and do not establish continuous availability.
- Images must be reviewed to remove institutional information, credentials, asset identifiers, and other internal details before publication.
- The historical switch configuration does not replace a current export of the device's configuration.
- Models and specifications that cannot be read or confirmed from the evidence will remain **unverified** in the inventory.

## Next steps

1. Select the most representative photographs and screenshots for each area.
2. Prepare publication-safe copies while retaining the private originals.
3. Consolidate the inventory of computers, network devices, and services.
4. Link each piece of evidence to the corresponding technical documentation page.
5. Update the project's README and track remaining work through Issues.

---

**Note:** This record documents the existence and general scope of collected evidence. It does not certify continuous operation, comprehensive security testing, or validation of every configuration.
