# Runbook — Cisco Interface Unavailable or Degraded

**English** | [Português (Brasil)](../../pt-BR/operacoes-noc/runbooks/interface-cisco-indisponivel.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Category:** NET / PHY / MON · **Document type:** Operational troubleshooting runbook  
**Hardware:** Cisco Catalyst C9200L switch and C8200L router

## 1. Purpose and evidence

This runbook investigates an interface marked down, unusual error counts, loss of VLAN connectivity, or an inconsistent SNMP status. The November 4 switch snapshot records `Gi1/0/1` as router-facing trunk; `Gi1/0/2–3` for VLAN 10; `Gi1/0/4–6` for VLAN 20; `Gi1/0/7–8` for VLAN 30; `Gi1/0/9–10` for VLAN 40; `Gi1/0/11–13` associated with VLAN 50; `Gi1/0/14` with VLAN 70; `Gi1/0/15` with VLAN 60. This is a **historical configuration**, not a live port-state map.

Grafana screenshots contain both `UP` and `DOWN` states and some repeated labels. A displayed label does not establish the identity of every physical interface. A spare port being down is not an incident.

## 2. Safety and authorization

- Use authorized read-only Cisco CLI access, approved monitoring dashboards, and the current physical topology.
- Never unplug, re-patch, `shutdown`, change access/trunk mode, modify spanning tree or change ACLs as a diagnostic shortcut.
- Before any remedial change, capture the relevant configuration securely, understand downstream impact and obtain authorization plus a rollback plan.
- Public documentation must not expose passwords, SNMP communities, management secrets or full unsanitized configurations.

## 3. Define expected operation

| Interface group | Recorded use | Diagnostic distinction |
|---|---|---|
| `Gi1/0/1` | Trunk towards C8200L | Check trunk state, intended VLAN carriage, downstream impact |
| `Gi1/0/2–10` | Departmental access | Confirm specific workstation and intended VLAN |
| `Gi1/0/11` | Asterisk/FreeRADIUS VLAN 50 association | Mode **not established** by the captured statements |
| `Gi1/0/12–13` | Grandstream phones | Confirm endpoints and PoE/power arrangement from current equipment |
| `Gi1/0/14` | IoT Archer AX53 | VLAN 70 in dated switch snapshot |
| `Gi1/0/15` | Corporate Archer AX53 | VLAN 60 in dated switch snapshot |

The router-side physical interface and exact routed subinterfaces remain outside the captured router configuration. Do not invent their names.

## 4. Diagnostic sequence

### A. Correlate alerts

Record time, device hostname, monitored interface index/description, historical traffic, and precise impact. Verify whether the switch port is expected to be physically connected **now**. Compare Zabbix interface discovery with Grafana's panel query before trusting its label.

### B. Read-only Cisco switch inspection

Execute in authorized EXEC mode; replace the example with the confirmed affected port:

~~~text
show interfaces status
show interfaces GigabitEthernet1/0/1
show interfaces trunk
show vlan brief
show interfaces counters errors
show spanning-tree interface GigabitEthernet1/0/1 detail
show mac address-table interface GigabitEthernet1/0/1
show logging
~~~

Use specific interface commands rather than dumping a full configuration to public logs. Not every command is applicable on every device, software version or privilege level.

### C. Interpret states

| Observation | Possible meaning / required check |
|---|---|
| `administratively down` | Interface intentionally disabled; confirm owner and intended state |
| `notconnect` or physical link absent | Endpoint power, cable, transceiver or physical path may matter |
| Link up but VLAN traffic missing | Verify access VLAN, trunk tagging, MAC learning and upstream routing |
| CRC/input errors increasing | Investigate physical medium, connectors and interface quality |
| STP state restricting forwarding | Confirm spanning-tree role/topology before treating as fault |
| Monitoring `DOWN`, CLI interface up | Check SNMP index, collection timestamp, filters and Grafana labeling |

CRC counters and link status should be evaluated over time; a nonzero historical counter alone does not prove current failure.

### D. Special case: VLAN 50 server port

The November 4 `Gi1/0/11` snapshot contains `switchport access vlan 50` and `spanning-tree portfast trunk` without an explicit `switchport mode access`. Inspect the **current** operational mode and configuration before inferring whether the port is an access or trunk port. Do not silently normalize this historical discrepancy.

### E. Validate Layer 3 separately

If physical and VLAN states appear correct, test from **authorized endpoints** using their current addresses, gateway settings and approved service paths. The recorded departmental gateways are `192.168.10.1`, `192.168.20.1`, `192.168.30.1` and `192.168.40.1`; these are dated endpoint observations, not verified current router interfaces. A successful link does not prove inter-VLAN connectivity or ACL enforcement.

## 5. Response decision and escalation

Do not change the switch or router until impact and likely fault domain have been confirmed. Escalate if the trunk serves multiple departments, if a routing/ACL change is considered, if a hardware fault is suspected, or if access to current configurations is unavailable. A switch SNMP collection issue belongs first to monitoring triage when forwarding still operates.

## 6. Recovery validation

1. Confirm the interface's intended **current** role and physical state.
2. Verify expected VLAN/trunk behavior with authorized read-only checks.
3. Confirm that the affected endpoint/service works through an appropriate functional test.
4. Confirm new valid monitoring samples and accurate mapping of SNMP interface to panel.
5. Record changed configuration (if any), validation times, remaining errors and rollback availability.

## 7. Evidence and classification

Record port ID, device, VLAN, time zone, old/new status, relevant read-only output, affected users/services, confirmed cause versus hypotheses, authorized action, post-change checks and final incident category. Do not turn an unused-port `DOWN` into an invented outage.

## 8. References

- [Incident management](../incident-management.md)
- [Switch port map](../../networking/switch-port-map.md)
- [Cisco configuration snapshot](../../networking/switch-vlan-snapshot-2026-11-04.md)
- [Router evidence](../../networking/router-c8200l.md)
- [SNMP troubleshooting: three recorded cases](../../monitoring/snmp-troubleshooting.md)
- [Consolidated topology](../../networking/consolidated-logical-topology.md)

**Evidence boundary:** CLI examples are recommendations; no new inspection or correction is claimed.