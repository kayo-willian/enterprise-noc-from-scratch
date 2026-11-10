# Runbook — Grafana Panel Displays No Data

**English** | [Português (Brasil)](../../pt-BR/operacoes-noc/runbooks/grafana-sem-dados.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** MON · **Status:** Proposed runbook; historical missing-data cases not declared resolved  
**Environment:** Grafana OSS container with Zabbix integration; Debian Docker NOC host

## 1. Purpose and historical evidence

Use this runbook when a Grafana panel displays `No data`, an unexpected gap, or an incorrect host/interface label. Grafana visualizes monitoring information but is **not** the source of truth for device state. On November 6, 2026, the Windows workstation dashboard showed **three `ONLINE` and five `No data`** status panels. Some Cisco switch panels repeated the label `Gi1/0/1 TRUNK-ROUTER`. Neither observation establishes a shared root cause.

The repository also documents Zabbix's **113 unsupported items**, five unavailable hosts, and DHCP/address differences. These may be relevant to an investigation but are not proof of the cause of any particular panel.

## 2. Safety and preparation

- Obtain authorized read access to Grafana, Zabbix and the Debian host.
- Record dashboard URL, panel title/UID where available, selected time range, host/template variables and screenshot timestamp.
- Use read-only panel inspection first. Do not edit queries, dashboards, datasource credentials, permissions, or Zabbix hosts during initial triage.
- Never publish cookies, API keys, database passwords, private dashboards, or unrestricted datasource exports.

## 3. Diagnose by scope

| Symptom | Investigation path |
|---|---|
| Every panel is empty | Grafana datasource/plugin availability, Zabbix API and overall timeframe |
| One panel is empty | Query, metric/item, field reduction, transformation or panel filter |
| Only one workstation is missing | Check its Zabbix host, address, agent, selected items and last data |
| Historical graphs exist, current status absent | Compare item timestamps, query function, time filters and trigger state |
| Switch label is repeated | Confirm item/interface mapping; do not reassign physical ports from panel text |
| `No data` at short time range only | Examine sample collection interval and broader approved time range |

## 4. Verification sequence

### A. Check Grafana itself

From Grafana, open the affected dashboard and inspect:

1. Selected organization, dashboard and host variables.
2. Absolute start/end time, timezone and refresh setting.
3. Panel **Inspect → Query / Data / Error** views (labels may vary with version).
4. Query datasource, selected Zabbix host, item, transformations and reduction.
5. Whether another panel using the same datasource has fresh values.

A panel may show an empty result when a filter selects a host or item absent in the chosen interval.

### B. Compare with Zabbix

In the authorized Zabbix frontend, inspect **Monitoring → Latest data** for the exact host/item referenced in the Grafana query. Confirm:

- The host exists and is enabled.
- The configured interface matches its current address, accounting for DHCP.
- The item is enabled and supported.
- The item has a recent valid timestamp in the same investigation interval.
- The selected Zabbix group, application/template and item key match the Grafana selection.

If Zabbix has no recent data, diagnose collection before editing Grafana. If Zabbix has fresh data but Grafana does not, investigate datasource, query, filters, plugin compatibility, transformations and time ranges.

### C. Inspect local container health

On the Debian host, use read-only Docker commands:

~~~bash
docker ps --filter name=grafana
docker ps --filter name=zabbix
docker logs --tail 100 --timestamps grafana
docker logs --tail 80 --timestamps zabbix-server
~~~

For a limited HTTP reachability check on the host (not proof of valid queries):

~~~bash
curl -I --max-time 5 http://127.0.0.1:3000/login
~~~

The public Compose example sets `GF_INSTALL_PLUGINS: alexanderzobnin-zabbix-app` and Grafana port **3000**. This proves only the documented deployment configuration; current plugin state and exact version must be inspected, not guessed.

### D. Trace data flow

~~~text
Monitored Cisco / Linux / Windows host
       |
       | SNMP or Zabbix Agent
       v
Zabbix Server and its stored metrics
       |
       | Configured Grafana Zabbix datasource
       v
Grafana query -> selection / transformation -> panel
~~~

Test each layer separately. A successful Grafana HTTP response does not prove Zabbix connectivity or a correct panel query. Likewise, a valid Zabbix value does not guarantee the panel's filters and visual encoding.

## 5. Root cause versus hypothesis

| Finding | Plausible conclusion |
|---|---|
| Stale Zabbix host IP and failed agent checks | Collection path may be invalid; confirm before changing host interface |
| `Unsupported` item in Zabbix | Investigate item type, key or device/agent support |
| Zabbix item updated, Grafana query selects another host | Query/variable selection mismatch |
| Raw panel data exists, visualization empty | Transformation, thresholds, field mapping or display config |
| Query timeout/API error | Investigate Grafana plugin, network access and Zabbix API |
| Duplicate switch labels | Mapping/label issue until interface indices are verified |

## 6. Approved remediation

Only after confirming a cause, propose a minimally scoped change: correct panel variable, item selection or transformation; fix the underlying unsupported item; update an accurately identified host interface; or repair a demonstrated datasource/plugin fault. Obtain approval and export/version the existing dashboard **without credentials** before changes. Do not mask an underlying monitoring outage by replacing actual measurements with static values.

## 7. Recovery validation

1. Confirm the exact Zabbix item has a fresh valid value.
2. Refresh the affected Grafana panel and inspect its new query/data response.
3. Check both a short relevant interval and a broader interval consistent with item sampling.
4. Verify labels identify the intended host/interface and that units are meaningful.
5. Record before/after timestamps, query changes, remaining exceptions and final incident status.

## 8. Documentation record

Preserve dashboard/panel identifiers, time range, Zabbix host/item, last data time, original error, investigated layers, authorized change, verified measurement, and screenshot references. Do not classify the five November 6 `No data` panels as repaired absent later evidence.

## 9. References

- [Incident management](../incident-management.md)
- [Grafana dashboards and limits](../../monitoring/grafana-monitoring.md)
- [Zabbix monitoring and unsupported items](../../monitoring/zabbix-monitoring.md)
- [Zabbix Agent runbook](zabbix-agent-connectivity.md)
- [SNMP troubleshooting case study](../../monitoring/snmp-troubleshooting.md)
- [Docker infrastructure](../../containers/docker-services.md)

**Status:** Recommended diagnostic process; no new panel fix is claimed.