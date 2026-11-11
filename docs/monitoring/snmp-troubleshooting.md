# Cisco Catalyst C9200L — SNMP Troubleshooting

**English** | [Português (Brasil)](../pt-BR/monitoramento/diagnostico-snmp.md)

**Recorded intervention:** November 4, 2026 · **Device:** Cisco Catalyst C9200L · **Protocol:** SNMPv2c · **Monitoring:** Zabbix 7.0 LTS / Grafana

This record describes **three documented troubleshooting outcomes**, not current switch availability or the resolution of later monitoring alerts.

## Case 1 — SNMP Interface Unavailable

**Symptom:** After the C9200L was registered in Zabbix, the SNMP interface remained unavailable and switch metrics could not be collected.

**Investigation recorded:**
1. Check IP connectivity between the monitoring Linux server and switch.
2. Check SNMP accessibility and run queries from the Linux terminal.
3. Compare switch SNMP configuration with the Zabbix host configuration.

**Confirmed cause:** The Zabbix host inherited an SNMP community different from the value configured on the switch.

**Correction:** Align the community values, configure the host-level `{$SNMP_COMMUNITY}` macro and reload the Zabbix Server configuration cache:

```bash
docker exec zabbix-server zabbix_server -R config_cache_reload
```

**Recorded result:** The SNMP interface became available; switch metric collection and automatic interface discovery resumed.

## Case 2 — Incorrect Switch Uptime

**Symptom:** The uptime widget showed `0` although the switch was running.

**Recorded cause:** The selected monitoring item returned an incorrect value for this Cisco IOS-XE device.

**Item changed:**

| Previous item | Replacement item |
|---|---|
| `system.hw.uptime[hrSystemUptime.0]` | `system.net.uptime[sysUpTime.0]` |

**Recorded result:** The dashboard began displaying the uptime value reported by the switch.

## Case 3 — Empty Event Widgets

**Symptom:** Some dashboard event widgets were empty while monitoring was operational.

**Confirmed cause:** The widget filters selected only the recently added switch, which had no active problems at the time.

**Correction:** Broaden the filters to include the NOC infrastructure rather than the switch alone.

**Recorded result:** The widgets displayed relevant monitoring entries and operational alerts.

## What the Three Investigations Demonstrate

The **November 4, 2026** troubleshooting record is valuable because it distinguishes **three different faults**:

**1. SNMP collection failure:** after the C9200L was registered, the SNMP interface was unavailable. The investigation considered IP connectivity, SNMP queries from Linux, the switch's SNMP settings and the community inherited by the Zabbix host. The **confirmed community mismatch** was corrected through the host macro `{$SNMP_COMMUNITY}` and a Zabbix configuration-cache reload. The recorded result was restored interface discovery and metric collection. IP reachability alone would not have identified the configuration mismatch.

**2. Wrong uptime metric:** the switch was operational but the uptime widget displayed **0**. The issue concerned the selected monitoring item, not a demonstrated switch outage. Replacing `system.hw.uptime[hrSystemUptime.0]` with `system.net.uptime[sysUpTime.0]` restored the displayed reported uptime in the historical case. A reachable SNMP endpoint does not guarantee that every item matches the device's supported metrics.

**3. Empty event widgets:** the filters were restricted to the newly registered switch, which had no active problems at that moment. Expanding the target set to the NOC environment displayed relevant alerts. An empty problem list may indicate a **view/filter condition**, not a collection failure.

These are **recorded corrective outcomes**, not newly reproduced tests. The report does not include packet captures or raw SNMP walk transcripts. Do not conflate them with later unsupported items or Windows `No data` panels on November 6. The original community values remain excluded from public documentation.

## Operational Notes

- Reachable IP does not guarantee functional SNMP collection; community values and Zabbix macros must match.
- Item keys need to be compatible with the device metrics; validate values after changing an item.
- Empty problem widgets can reflect filter scope rather than a collection fault.
- The recorded deployment used **SNMPv2c**. SNMPv3 with authentication and encryption is preferable for production systems.
- Actual community strings and sensitive switch configuration are not included in this public case study.

**Source:** November 4, 2026 technical implementation report. Later Zabbix unsupported items, unavailable agents and Grafana `No data` panels remain separate observations.

**Related evidence:** [Zabbix](zabbix-monitoring.md) · [Grafana](grafana-monitoring.md) · [Switch snapshot](../networking/switch-vlan-snapshot-2026-11-04.md)
