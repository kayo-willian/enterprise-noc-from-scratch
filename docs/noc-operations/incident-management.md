# NOC Operations — Incident Management

**English** | [Português (Brasil)](../pt-BR/operacoes-noc/gerenciamento-de-incidentes.md)

**Project:** Enterprise NOC — From Scratch  
**Organization:** Tapajós Inovações  
**Environment:** Physical enterprise infrastructure laboratory  
**Document type:** Operational process and incident management framework  
**Scope:** Network infrastructure, Linux servers, monitoring platforms, containers, and corporate services  

---

## 1. Overview

This document defines incident classification, prioritization, triage, escalation, recovery validation and reporting for the Enterprise NOC laboratory. It is an operational reference, not a record of an active production NOC.

The procedures apply to the network, Linux systems, Docker services and monitoring components documented in the repository.

## 2. Operational Environment

The procedures cover the Cisco C8200L/C9200L network, VLANs 10–70, Debian servers, Docker applications, Windows endpoints, IP telephony, DNS and Zabbix/Grafana monitoring. Refer to the [network topology](../networking/consolidated-logical-topology.md) and [service documentation](../containers/docker-services.md) for equipment assignments and dependencies; this process does not duplicate those inventories.

## 3. Events, Alerts, Incidents, and Problems

| Term | Operational meaning |
|---|---|
| **Event** | Observable state change, such as an interface transition or container restart. |
| **Alert** | Monitoring indication that a configured condition was met; requires assessment. |
| **Incident** | Confirmed unplanned service interruption or degradation. |
| **Problem** | Underlying or suspected cause of one or more incidents. |

**Monitoring failure is not necessarily infrastructure failure.** An unavailable agent, unsupported item or empty Grafana panel requires validation before declaring a service outage. Conversely, a responsive monitoring interface does not prove the application is functioning end-to-end.

## 4. Incident Management Objectives

Detect and validate service impact; classify severity; investigate using collected evidence; authorize corrective action; verify recovery; and record the outcome. Each stage is detailed in the incident lifecycle below.

## 5. Incident Classification

Incidents can be categorized according to the affected infrastructure layer.

| Category | Typical Components | Example |
|---|---|---|
| NET | Cisco routing and switching | Confirmed connectivity failure affecting a VLAN |
| MON | Zabbix, Grafana, monitoring agents | Monitoring data collection unavailable |
| SYS | Linux and Windows systems | Host operating-system failure |
| CNT | Docker and containerized applications | Required application container unavailable |
| DNS | Pi-hole and name resolution | Confirmed failure resolving required domains |
| VOIP | Asterisk and IP telephones | Internal extension unable to complete calls |
| AUTH | FreeRADIUS | Confirmed authentication failure |
| WEB | Internal web applications and reverse proxy | Required application unavailable through its expected endpoint |
| PHY | Cabling and physical equipment | Verified physical link or cable fault |

These categories are reference identifiers for organizing incident records.

They do not represent an existing ticketing configuration or a deployed incident management platform.

## 6. Priority and Severity Model

Incident priority should consider two factors:

**Impact:** How many systems, services, or operational functions are affected?

**Urgency:** How quickly must the condition be addressed to prevent or reduce operational disruption?

The documentation uses the following laboratory reference model.

| Priority | Classification | Impact Description | Illustrative Scenario |
|---|---|---|---|
| P1 | Critical | Confirmed widespread disruption of essential infrastructure | Core network connectivity unavailable across multiple required segments |
| P2 | High | Significant degradation or loss of an important shared service | Main DNS service unavailable for dependent clients |
| P3 | Medium | Limited disruption affecting a department or selected system | One workstation cannot access a required internal application |
| P4 | Low | Minor operational issue without demonstrated service disruption | Nonessential dashboard label or visualization requires correction |

### 6.1 Classification Rules

Priority must be assigned from verified impact rather than the visual appearance of an alert.

A red dashboard indicator does not automatically imply a P1 incident.

Likewise, an unavailable monitoring interface does not establish that the corresponding network device or operating system has failed.

### 6.2 Priority Review

An incident's priority may change when new information becomes available.

For example, an initially isolated DNS complaint may require reclassification if investigation confirms that multiple departments are affected.

The reason for any priority change should be recorded.

### 6.3 Response Times

This document does not establish contractual response times, recovery guarantees, or service-level agreements.

No contractual SLA or measured response-time target is assigned to this laboratory process.

## 7. Incident Lifecycle

The reference incident lifecycle consists of seven stages.

```text
EVENT OR REPORT
       |
       v
1. DETECTION
       |
       v
2. TRIAGE
       |
       v
3. CLASSIFICATION
       |
       v
4. INVESTIGATION
       |
       v
5. CORRECTIVE ACTION
       |
       v
6. VALIDATION
       |
       v
7. CLOSURE
       |
       v
DOCUMENTATION AND REVIEW
```

An incident may return to investigation if validation does not confirm recovery.

Escalation may occur at any stage when the available technical resources or permissions are insufficient.

### 7.1 Detection

Potential incidents may be detected through:

- Zabbix monitoring events.
- Grafana dashboards.
- Uptime Kuma availability checks.
- Operating-system logs.
- Network-device status information.
- Reports from laboratory users or administrators.

**Required record:**

- Detection timestamp.
- Monitoring source or reporting channel.
- Affected system.
- Initial observation.
- Available supporting evidence.

### 7.2 Triage

Triage determines whether the reported condition represents:

- A confirmed service incident.
- A monitoring or visualization failure.
- An expected operational state.
- An event requiring additional investigation.

The initial assessment should consider whether the affected service can still perform its expected function.

For example, an unused switch interface marked `DOWN` may represent a normal condition.

A Grafana panel displaying `No data` requires investigation but does not automatically establish that the monitored computer is offline.

### 7.3 Classification

After the initial assessment, record:

- Incident category.
- Affected component.
- Confirmed or suspected impact.
- Assigned priority.
- Current investigation status.

If impact cannot be established, the record should explicitly state that the condition remains under investigation.

### 7.4 Investigation

The investigation should follow a structured technical sequence:

1. Confirm the reported symptom.
2. Identify the relevant infrastructure component.
3. Examine the corresponding monitoring information.
4. Compare observations with independent technical evidence.
5. Check configuration, connectivity, or service status as appropriate.
6. Develop and test possible explanations.
7. Record the findings.

Diagnostic actions should initially favor non-disruptive inspection.

Configuration changes should only be performed when the impact, authorization, and recovery requirements have been assessed.

### 7.5 Corrective Action

Corrective actions depend on the identified failure.

Examples may include:

- Correcting a monitoring host address.
- Adjusting a misconfigured monitoring item.
- Restoring a required application service.
- Correcting an identified network configuration error.
- Resolving an established service dependency issue.

These are examples of possible actions, not claims that they have all been performed in the laboratory.

Before applying a change, the operational record should identify:

- Expected result.
- Affected components.
- Relevant configuration backup or rollback option.
- Possible side effects.
- Required authorization.

### 7.6 Validation

An incident should not be considered resolved merely because an error message disappears.

Validation should confirm that the original symptom is no longer present and that the expected service behavior has returned.

Depending on the incident, evidence may include:

- Successful service connectivity.
- Valid monitoring data.
- Correct network interface state.
- Successful DNS resolution.
- Expected application response.
- Updated monitoring indicators.
- Absence of the original failure during an appropriate observation interval.

The validation method must correspond to the affected service.

For example, restoring Zabbix Agent communication confirms monitoring connectivity, but does not independently prove that every application on the host works correctly.

### 7.7 Closure

A documented incident can be closed when:

- The affected service or monitoring function has been validated.
- The corrective action is recorded.
- The final impact is understood.
- Relevant evidence is preserved.
- Remaining limitations are identified.
- The outcome is assigned an appropriate closure status.

When recovery cannot be verified, the record should not claim successful resolution.

Possible closure descriptions include:

- Resolved and validated.
- Mitigated with remaining limitations.
- Transferred for further investigation.
- Closed as a monitoring false positive.
- Closed as an expected operational condition.

The final classification must be supported by the investigation.

## 8. Escalation Model

Escalation is required when an incident cannot be appropriately investigated or resolved within the current operational scope.

The laboratory does not have a verified production staffing or on-call structure.

The following responsibilities describe technical functions in the reference workflow, not formally assigned positions.

| Function | Responsibility |
|---|---|
| Monitoring and triage | Review alerts, verify symptoms, record initial impact |
| Network administration | Investigate routing, switching, VLANs, and physical connectivity |
| Linux and infrastructure administration | Investigate operating systems, services, storage, and Docker |
| Application administration | Investigate DNS, VoIP, authentication, and internal web applications |
| Technical coordination | Evaluate impact, authorize disruptive actions, and maintain incident records |

### Escalation Criteria

Escalation should be considered when:

- The incident affects multiple network segments.
- The underlying cause remains unclear after initial checks.
- Corrective action may interrupt shared infrastructure.
- The required configuration access is unavailable.
- The incident involves authentication or sensitive infrastructure.
- The failure recurs after an apparently successful recovery.
- Additional equipment-level investigation is necessary.

Escalation does not remove the requirement to preserve the original investigation record.

## 9. Operational Evidence Collection

Incident records should preserve information sufficient to reconstruct the technical investigation.

### 9.1 Minimum Evidence

| Evidence | Purpose |
|---|---|
| Timestamp | Establish the sequence of observations |
| Affected component | Identify the infrastructure resource |
| Initial symptom | Describe what was observed |
| Monitoring reference | Identify related Zabbix, Grafana, or Uptime Kuma information |
| Diagnostic observations | Support or reject possible causes |
| Corrective action | Record what was changed |
| Validation result | Establish whether the expected behavior returned |
| Final status | Distinguish recovery from unresolved conditions |

### 9.2 Timestamps

Incident reports should record the date, time, and timezone of significant observations.

When timestamps are collected from different systems, timezone differences and clock synchronization should be considered.

Historical screenshots must not be presented as current system readings.

### 9.3 Sensitive Information

Public incident reports must not expose:

- Passwords or authentication secrets.
- SNMP community values.
- Private keys.
- Session tokens.
- Personal user information.
- Confidential infrastructure identifiers.

Original evidence should remain separate from sanitized copies prepared for the public repository.

## 10. Historical Troubleshooting Evidence

Three completed Cisco SNMP troubleshooting cases were recorded on **November 4, 2026**: monitoring unavailable because of a community mismatch; incorrect switch uptime; and dashboard widgets without expected values. The investigation, corrective steps and recorded results are maintained in the [SNMP troubleshooting case study](../monitoring/snmp-troubleshooting.md).

These cases are historical interventions, not executions of the hypothetical procedures in this document.

## 11. Historical Monitoring Conditions

The **November 6, 2026** evidence includes six differences between workstation addresses and Zabbix registrations, Grafana panels displaying `No data`, and Cisco interface `UP`/`DOWN` indicators. None is sufficient on its own to establish a shared root cause or service incident.

Use the dedicated [Zabbix](../monitoring/zabbix-monitoring.md), [Grafana](../monitoring/grafana-monitoring.md) and [Cisco interface runbook](runbooks/cisco-interface-unavailable.md) records for the observations and diagnostic criteria.

## 12. Incident Record Template

The following reusable template defines a consistent incident record format.

It is not a completed incident report.

```markdown
# Incident Report — [Incident ID]

## Identification

- Incident ID:
- Date:
- Detection time and timezone:
- Category:
- Priority:
- Affected component:
- Network segment:
- Detection source:
- Responsible technical function:

## Initial Observation

Describe the reported symptom and how it was detected.

## Operational Impact

Identify affected systems, services, and users.

Separate confirmed impact from suspected impact.

## Investigation

Record the diagnostic actions in chronological order.

| Time | Action | Observation |
|---|---|---|
| | | |
| | | |

## Root Cause

Describe the identified cause.

If the cause was not established, record the current investigation status.

## Corrective Action

Describe the changes or recovery actions actually performed.

## Validation

- Validation procedure:
- Expected result:
- Observed result:
- Supporting evidence:

## Final Status

- Outcome:
- Closure date and time:
- Remaining limitations:
- Follow-up actions:

## Lessons Learned

Document relevant technical findings and prevention opportunities.

## Evidence References

List sanitized logs, screenshots, configuration records,
or related repository documents.
```

### Incident Identification

A possible identifier format is:

`NOC-YYYYMMDD-001`

This is a reporting template, not a claim that a numbered ticketing system was deployed.

## 13. Illustrative Incident Classification

The following examples illustrate how the reference process classifies operational situations.

They are **hypothetical scenarios**, not additional incidents claimed to have occurred in the laboratory.

| Scenario | Initial Classification | Required Verification |
|---|---|---|
| Multiple VLANs lose access to required network resources | Potential P1 | Confirm scope, gateway reachability, and affected services |
| Internal DNS becomes unavailable for several departments | Potential P2 | Confirm DNS failure and dependent-client impact |
| One Windows workstation becomes unreachable | Potential P3 | Distinguish host failure from monitoring failure |
| An unused switch port is displayed as `DOWN` | May not be an incident | Confirm the port's expected operational state |
| Grafana displays `No data` for one panel | Monitoring investigation | Check data source, query, item, and host availability |
| A dashboard label is incorrect but metrics remain valid | Potential P4 | Confirm data integrity and display-only impact |

Final priority must be determined from the actual impact and urgency.

## 14. Operational Review and Improvement

Review recurring incidents, monitoring false positives, incomplete records and the effectiveness of corrective actions. Report counts, recurrence or response time as operational metrics only when supported by dated incident records.

## 15. Relationship With Technical Runbooks

Incident management defines the lifecycle, priority and escalation model. The following six bilingual runbooks document recommended read-only diagnostics, interpretation, authorization requirements and validation criteria for the infrastructure.

| Technical subject | Runbook |
|---|---|
| Zabbix Agent connectivity | [Investigate agent and host address](runbooks/zabbix-agent-connectivity.md) |
| Cisco interface unavailable | [Investigate link, VLAN and interface mapping](runbooks/cisco-interface-unavailable.md) |
| DNS resolution failures | [Investigate Pi-hole, DNS path and filtering](runbooks/dns-resolution-failure.md) |
| Docker service failures | [Investigate Docker, Compose and dependencies](runbooks/docker-service-failure.md) |
| High CPU, memory or disk | [Investigate resource consumption](runbooks/host-resource-utilization.md) |
| Grafana `No data` | [Trace collection versus visualization](runbooks/grafana-no-data.md) |

The companion [Incident Simulation and Recovery Validation](incident-simulation-and-validation.md) document describes controlled exercise planning, authorization, baseline collection, result classification and evidence requirements.

**Publication of a runbook is not proof that its hypothetical diagnostic steps have been executed.** Previously recorded SNMP cases remain separately cited historical troubleshooting evidence.

## 16. Documentation Scope

This document describes a reference incident-management process and links to six diagnostic runbooks and an exercise catalog. It does not establish a staffed production NOC, a ticketing platform, a contracted SLA, or completed recoveries beyond the separate historical case records.

## 17. Related Documentation

- [Consolidated Logical Network Topology](../networking/consolidated-logical-topology.md)
- [Cisco Catalyst C8200L Router](../networking/router-c8200l.md)
- [Switch Port Mapping](../networking/switch-port-map.md)
- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Docker Infrastructure](../containers/docker-services.md)
- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)
- [SNMP Troubleshooting](../monitoring/snmp-troubleshooting.md)
- [DNS Filtering and Availability](../services/dns-and-availability.md)
- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)
- [Technical FAQ](../faq/technical-faq.md)

---

**Document classification:** NOC incident-management reference process.  
**Historical evidence references:** November 4–6, 2026.  
**Related NOC procedures:** Six bilingual technical runbooks and the incident simulation and recovery validation framework, linked in Section 15.

**Enterprise NOC — From Scratch**  
*From physical infrastructure to network operations.*
