# Incident Simulation and Recovery Validation

**English** | [Português (Brasil)](../pt-BR/operacoes-noc/simulacao-e-validacao-de-incidentes.md)

**Project:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Area:** NOC Operations & Troubleshooting  
**Document type:** **Exercise scenario catalog and reporting template** — not an execution log  
**Infrastructure:** Cisco C8200L/C9200L, VLANs 10–70, Debian services, Docker, Zabbix, Grafana and Uptime Kuma

## 1. Purpose

Incident response skills must include more than interpreting screenshots. This document provides an auditable method to design **safe, controlled and reversible** laboratory exercises, validate recovery and retain evidence. The scenarios are reference exercises, not recorded recoveries. Dated execution records, if any, must remain separate from this catalog.

The actual November 4, 2026 Cisco SNMP troubleshooting cases are separately documented as historical interventions. The November 6 Zabbix/Grafana screenshots show monitoring conditions, not records of the scenarios in this catalog being executed.

## 2. Exercise categories: distinguish the evidence

| Label | Meaning | Publication rule |
|---|---|---|
| **TABLETOP** | Discussion using diagrams and hypothetical events | Describe as a scenario walkthrough, not a technical test |
| **READ-ONLY** | Observe existing host/service status and compare monitoring without changing production state | Record actual commands, timestamps and results |
| **CONTROLLED LAB TEST** | Authorized, bounded experiment with validated restore steps | Describe only after setup, execution, and recovery evidence are available |
| **HISTORICAL CASE** | Previously recorded troubleshooting with source evidence | Cite its original date and observed result |
| **SCENARIO ONLY** | Reference scenario with no execution record | Do not report it as a passed test |

Do not present TABLETOP or SCENARIO ONLY material as a successful technical recovery.

## 3. Authorization and environment boundaries

Before any test, require:

- An identified technical operator and explicit authorization for the specific infrastructure and exercise scope.
- A precise target host, network segment, service and test duration; no blanket permission for all systems.
- Confirmation that no users or shared infrastructure depend on an uninterrupted service.
- An agreed start/end window, communication channel, abort condition and documented rollback.
- A current configuration backup or recovery point appropriate to the change.
- A safe observation method and sanitized evidence location.
- A post-exercise functional acceptance criterion.

**Prohibited as casual simulation methods:** disconnecting the core router trunk, changing ACLs without a verified revert plan, deleting Docker volumes, wiping files, altering production-like credentials, disabling security protections or exposing sensitive DNS/authentication records.

If isolation or recovery cannot be guaranteed, choose **TABLETOP** or **READ-ONLY** instead.

## 4. Baseline capture

Record the current baseline **before** suggesting a controlled test. Dated 2026-11-06 screenshots may be used for background but are not a substitute for a same-day baseline.

| Area | Baseline evidence |
|---|---|
| Host | Current hostname, VLAN, IP, system state and date/timezone |
| Network | Expected interface/VLAN state and authorized connectivity checks |
| Docker | Current affected-container status, health where defined, logs and dependencies |
| Zabbix | Host/item/trigger names, latest valid item time and error |
| Grafana | Dashboard, exact panel/query, time range and last valid sample |
| Uptime Kuma | Monitor name, check type and recorded status at exercise start |
| Service | Independent functional test: DNS resolution, HTTP response or another appropriate check |

Never consider a dashboard indicator sufficient by itself to demonstrate recovered application functionality.

## 5. Exercise plan matrix

The following **reference scenarios** are designed to avoid unapproved outages.

| ID | Scenario | Safe starting mode | Validation focus | Runbook |
|---|---|---|---|---|
| EX-01 | Agent stopped or stale host address suspected | TABLETOP + current read-only agent checks | Distinguish agent issue from DHCP/host availability | [Zabbix Agent](runbooks/zabbix-agent-connectivity.md) |
| EX-02 | Unexpected switch interface `DOWN` | TABLETOP + non-disruptive Cisco CLI inspection | Verify expected port use and correct SNMP interface mapping | [Cisco Interfaces](runbooks/cisco-interface-unavailable.md) |
| EX-03 | DNS name fails to resolve | TABLETOP + read-only DNS query on authorized names | Separate DNS from routing, blocklists and web application | [DNS Resolution](runbooks/dns-resolution-failure.md) |
| EX-04 | Container reports `Exited` or unavailable | TABLETOP + current Docker health/log inspection | Trace service dependencies and application response | [Docker Service](runbooks/docker-service-failure.md) |
| EX-05 | CPU, RAM or disk warning | TABLETOP + read-only host measurements | Confirm resource pressure independently from dashboard | [Resource Utilization](runbooks/host-resource-utilization.md) |
| EX-06 | Grafana displays `No data` | TABLETOP + panel/Zabbix comparison | Locate whether missing data originates in collection or display | [Grafana](runbooks/grafana-no-data.md) |

A controlled interruption is **optional**, not required to complete the tabletop/read-only documentation. If ever authorized, its exact implementation must be designed and approved for the isolated target; it is not automatically authorized by this document.

## 6. Standard exercise lifecycle

### 6.1 Design

1. Define one precise hypothesis and expected incident category.
2. Specify observable detection criteria and the service functionality that matters.
3. Identify affected network segment and dependencies.
4. Set stop/abort conditions and rollback ownership.
5. Select actual evidence files and reporting format.

### 6.2 Establish baseline

1. Record current date/timezone and target identity.
2. Capture non-disruptive state in Zabbix/Grafana and from the service itself.
3. Verify target is appropriate for the planned exercise.
4. Ensure the approved recovery path is available.

### 6.3 Execute only the approved scope

For a tabletop, discuss actions without touching the infrastructure. For read-only exercises, run only authorized inspection commands and record **actual** output. For any controlled lab test, do not deviate from its approved technical change plan. Stop immediately if unexpected users, VLANs, security controls or data become affected.

### 6.4 Diagnose and document

Differentiate symptoms, confirmed causes and working hypotheses. Preserve observation order and relevant monitoring gaps. Do not infer service loss simply because Zabbix or Grafana lacks data.

### 6.5 Recover and validate

Use the agreed restore procedure where applicable. Compare service behavior with baseline. Confirm expected functional behavior **and** relevant new monitoring values where available. An exercise that cannot be restored safely must be terminated and escalated, not declared successful.

### 6.6 Review

Document why evidence supported or contradicted the hypothesis, what monitoring missed and which runbook should change. State any untested paths explicitly.

## 7. Acceptance criteria

A **controlled lab test** may be marked **PASSED** only when all applicable conditions are supported by timestamped evidence:

- A baseline was captured and the authorized change is known.
- The intended observation was recorded and no disallowed impact occurred.
- The affected functionality was restored to its expected state.
- Relevant monitoring information was collected again or any residual telemetry gap was documented.
- Recovery and rollback actions are traceable.
- No confidential secrets were introduced into the public record.

A TABLETOP exercise has a different outcome: **WALKTHROUGH COMPLETED**, not infrastructure recovery. A READ-ONLY inspection may be **OBSERVATION COMPLETED**, not **incident resolved**.

Possible result labels: `PLANNED`, `NOT EXECUTED`, `WALKTHROUGH COMPLETED`, `OBSERVATION COMPLETED`, `PASSED`, `FAILED`, `ABORTED`, `INCONCLUSIVE`.

## 8. Reusable evidence/report template

~~~markdown
# NOC Exercise — [EX-ID]

## Identification
- Scenario:
- Mode: TABLETOP / READ-ONLY / CONTROLLED LAB TEST
- Status: PLANNED / NOT EXECUTED / ... 
- Responsible operator and approval reference:
- Date, time, timezone:
- Target host, network and service:

## Objective and Hypothesis
- Expected behavior:
- Hypothesized cause or fault:
- Impact boundaries:

## Authorization and Safety
- Confirmed scope:
- Abort criteria:
- Recovery/rollback plan:
- Backup or recovery point:

## Baseline
| Time | Evidence source | Actual value or observation |
|---|---|---|
| | | |

## Execution
| Time | Actual action | Actual output / observation |
|---|---|---|
| | | |

## Diagnosis
- Confirmed observations:
- Hypotheses not proven:
- Identified cause (only if supported):

## Recovery and Verification
- Authorized corrective action (if any):
- Independent functional test:
- Monitoring validation:
- Residual issues:

## Outcome
- Status:
- Justification:
- Sanitized evidence links:
- Lessons learned:
- Action tracking / documentation:
~~~

Do not pre-fill hypothetical console outputs or mark any field as passed without a corresponding test.

## 9. Historical cases versus new exercises

The [Cisco Catalyst C9200L SNMP troubleshooting record](../monitoring/snmp-troubleshooting.md) describes three **historical** investigations from November 4:

1. Mismatched SNMP community and restored collection.
2. Inaccurate switch uptime item and its correction.
3. Empty alert widgets due to restrictive filtering, subsequently adjusted.

These are useful case studies, but they are **not** newly executed EX-01 through EX-06 exercises. The 113 unsupported Zabbix items and Grafana `No data` panels in the November 6 collection must not be described as resolved without later evidence.

## 10. References

- [Incident Management](incident-management.md)
- [Consolidated Network Topology](../networking/consolidated-logical-topology.md)
- [Zabbix Historical Evidence](../monitoring/zabbix-monitoring.md)
- [Grafana Historical Evidence](../monitoring/grafana-monitoring.md)
- [SNMP Historical Troubleshooting](../monitoring/snmp-troubleshooting.md)
- [Evidence Collection](../evidence/evidence-collection-2026-11-06.md)

**Document scope:** Scenario design, safe exercise guidance and reporting format. No execution results are attributed to this catalog.