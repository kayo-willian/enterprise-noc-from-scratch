# Cisco Catalyst 9200L — SNMP Troubleshooting

**English | [Português (Brasil)](../pt-BR/monitoring/snmp-troubleshooting.md)**

## Overview

This case study documents troubleshooting activities performed during the integration of a Cisco Catalyst 9200L switch into an enterprise NOC monitoring environment.

The infrastructure uses Zabbix 7.0 LTS for monitoring and Grafana for data visualization.

**Equipment:** Cisco Catalyst 9200L  
**Monitoring protocol:** SNMPv2c  
**Monitoring platform:** Zabbix 7.0 LTS  
**Date:** November 4, 2026

## Incident 1 — SNMP Monitoring Unavailable

### Problem

After registering the Catalyst 9200L in Zabbix, the SNMP interface remained unavailable.

Monitoring requests failed, preventing the collection of equipment metrics.

### Investigation

The troubleshooting process involved:

1. Verifying IP connectivity between the Linux monitoring server and the switch.
2. Checking SNMP accessibility.
3. Testing SNMP queries from the Linux terminal.
4. Reviewing the switch configuration.
5. Inspecting the SNMP community configured in Zabbix.

### Root Cause

The switch and Zabbix were configured with different SNMP community values.

The Zabbix host inherited a community value that did not match the switch configuration.

### Resolution

The SNMP configuration was aligned between both systems.

A host-level `{$SNMP_COMMUNITY}` macro was configured in Zabbix.

The monitoring server configuration cache was subsequently reloaded:

```bash
docker exec zabbix-server zabbix_server -R config_cache_reload
```

### Result

The SNMP interface became available, enabling metric collection and automatic interface discovery.

## Incident 2 — Incorrect Switch Uptime

### Problem

The monitoring dashboard displayed an uptime value of zero, even though the switch was operational.

### Root Cause

The configured monitoring item used an uptime metric that returned an incorrect value for the Cisco IOS-XE device.

### Resolution

The monitoring item was changed from:

`system.hw.uptime[hrSystemUptime.0]`

To:

`system.net.uptime[sysUpTime.0]`

### Result

The dashboard began displaying the switch's reported uptime correctly.

## Incident 3 — Empty Dashboard Widgets

### Problem

Some monitoring widgets displayed empty results despite the monitoring infrastructure being operational.

### Root Cause

The affected widgets were configured to display information only from the newly registered switch.

The switch had no active problems, resulting in empty alarm lists.

### Resolution

The dashboard filters were adjusted to include the broader NOC environment.

### Result

The widgets began displaying relevant monitoring information and operational alerts.

## Technical Lessons Learned

- IP connectivity does not guarantee successful application-layer monitoring.
- SNMP credentials and monitoring macros must be consistent.
- Monitoring items must be validated against the equipment's supported metrics.
- Dashboard filters can affect the visibility of operational information.
- Monitoring changes require functional verification.

## Security Considerations

The original laboratory implementation used SNMPv2c.

For production environments, SNMPv3 with authentication and encryption should be considered.

Internal IP addresses, SNMP community values, and other sensitive configuration details are excluded from this public case study.

## Documentation Status

**Status:** Documented from the November 4, 2026 technical implementation report.

Additional evidence may be incorporated after verification.
