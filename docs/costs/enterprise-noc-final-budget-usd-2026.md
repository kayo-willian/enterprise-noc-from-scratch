# Infrastructure Cost Analysis — Enterprise NOC

**Enterprise NOC — From Scratch**  
**Tapajós Inovações — Fictional Enterprise Environment**

**English (USD)** | [Português (BRL)](../pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.md)

**Spreadsheets:** [English — USD](enterprise-noc-final-budget-usd-2026.xlsx) | [Português — BRL](../pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.xlsx)

| Attribute | Reference |
|---|---|
| Project | Enterprise NOC — From Scratch |
| Financial scope | Infrastructure acquisition, deployment, and operations |
| Budget reference date | November 11, 2026 |
| Currency | U.S. dollars (USD) |
| Base market | Brazilian supplier listings and commercial assumptions |
| Foreign exchange basis | USD 1 = BRL 5.5600 |
| Workbook | `enterprise-noc-final-budget-usd-2026.xlsx` |
| Financial scenarios | A — Full Acquisition; B — Existing Assets; C — Monthly Operations |
| Model structure | 11 worksheets |

> **Financial scope:** This is a reference-cost simulation for replicating an enterprise technology lab, not a record of purchases, paid invoices, executed service contracts, or U.S. supplier quotations. The USD figures are exchange-rate equivalents of Brazilian prices and BRL-denominated planning inputs. The original BRL amounts are retained in the workbook for traceability.

---

## 1. Purpose and Scope

This cost model estimates the financial requirements to acquire, deploy, and operate infrastructure comparable to the **Enterprise NOC — From Scratch** technical environment. It covers Cisco networking, ten physical computers, corporate Wi-Fi and IoT, structured cabling, IP telephony, Linux infrastructure, Docker-based services, monitoring platforms, technical deployment, software licensing, electricity, connectivity, backup, and replacement provisions.

Three distinct investment models are maintained:

| Scenario | Coverage | Cost basis |
|---|---|---|
| **A — Full Acquisition & Deployment** | Purchase of equipment, peripherals, materials, technical services, software provisions, freight, and contingency | Initial capital and deployment estimate |
| **B — Existing Assets & Deployment** | Deployment services and selected consumables where the main hardware is already supplied | Initial services and materials estimate |
| **C — Operations & Maintenance** | Electricity, internet, preventive support, backup storage, and replacement reserve | Recurring monthly estimate |

The workbook calculates monetary results from referenced unit prices, quantities, enabled cost items, service hours, labor rates, and operating assumptions. Optional items remain visible in the source inventory without automatically entering the scenario totals.

### 1.1. Technical Documentation

The financial inventory is linked to the corresponding technical evidence:

- [Infrastructure architecture](../architecture/infrastructure-overview.md)
- [Networking and VLAN documentation](../networking/README.md)
- [Cisco C9200L interface inventory](../networking/switch-port-map.md)
- [Physical rack and cabling evidence](../evidence/physical-infrastructure.md)
- [November 6 evidence collection](../evidence/evidence-collection-2026-11-06.md)
- [Workstation and server inventory](../endpoints/workstation-inventory.md)
- [Docker environment](../containers/docker-services.md)
- [Zabbix monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana dashboards](../monitoring/grafana-monitoring.md)
- [Asterisk and FreeRADIUS](../services/asterisk-freeradius.md)
- [DNS and availability services](../services/dns-and-availability.md)

The technical observations dated November 4–6, 2026 establish equipment identities and documented roles. The financial workbook separately models their hypothetical acquisition and operation at the specified budget reference date.

### 1.2. Price Categories

| Category | Meaning |
|---|---|
| Listed price | An amount retained from a supplier listing or published commercial reference |
| Comparable price | The cost of an alternative model or refurbished system used for replication budgeting |
| Planning assumption | A modeled cost, runtime, service effort, percentage, or allowance rather than an obtained quotation |
| Calculated amount | A formula-driven subtotal, total, or projected cost in the workbook |
| Excluded item | A visible reference with purchase disabled or quantity zero in the baseline scenario |

A device's appearance in the physical inventory does not establish the invoice price, exact commercial SKU, license terms, or procurement conditions. The distinction remains explicit throughout the model.

---

## 2. Workbook Architecture

The English workbook contains **11 worksheets**, with the following responsibilities:

| Worksheet | Financial function |
|---|---|
| **Dashboard** | Consolidated investment results, projections, coverage indicators, and equipment-cost categories |
| **Scenario A** | Full acquisition and deployment components, shipping and contingency |
| **Scenario B** | Deployment using existing assets, additional materials, services and travel |
| **Scenario C** | Monthly operating cost and 12-/36-month projections |
| **Inventory** | Equipment, materials, optional components, source IDs and scenario-specific purchasing |
| **Computers** | Individual records for eight Windows workstations and two Linux servers |
| **Deployment** | Thirty-two technical services, estimated hours and hourly rates |
| **Monthly Operations** | Twelve recurring-cost lines, including excluded optional contracts |
| **Software** | Community editions, Windows licensing provision and optional proprietary services |
| **Assumptions** | Quantities, labor tariffs, electrical power, runtime, exchange rate and percentage allowances |
| **Sources** | Forty-five commercial, technical and planning references; original BRL amounts where applicable |

### 2.1. Calculation Flow

```text
Sources (BRL reference prices) + Assumptions (BRL/USD exchange rate)
                              |
                              v
                   Inventory / Computers
                              |
           +------------------+------------------+
           |                  |                  |
           v                  v                  v
      Scenario A         Scenario B        Monthly Operations
           ^                  ^                  |
           |                  |                  v
    Deployment + Software   Deployment         Scenario C
           |                  |                  |
           +------------------+------------------+
                              |
                              v
                           Dashboard
```

Each scenario maintains its own inclusion conditions. Equipment appearing in the `Inventory` sheet is not automatically purchased in both initial-investment scenarios.

### 2.2. Foreign Exchange Conversion

The workbook uses the following reference exchange rate:

**USD 1.00 = BRL 5.5600 — reference date: November 11, 2026.**

For a BRL-denominated input:

```text
USD equivalent = BRL reference amount / 5.5600
```

For example:

```text
BRL 23,422.08 / 5.5600 = USD 4,212.60 (displayed)
```

The exchange-rate parameter appears as **FX-01** in `Assumptions`. In `Sources`, applicable rows retain the original Brazilian quotation beside the USD equivalent. The converted figures are **not independently sourced prices in U.S. retail or enterprise markets**.

The workbook calculates with unrounded underlying values. Displayed monetary values are rounded to two decimals, so summing rounded line items can differ from the underlying total by a few cents.
---
## 3. Executive Financial Summary

| Indicator | USD equivalent |
|---|---:|
| **Scenario A — Full acquisition and deployment** | **$15,590.49** |
| **Scenario B — Existing assets and deployment** | **$1,339.72** |
| **Scenario C — Monthly operations** | **$194.98** |
| 12 months of operations | $2,339.75 |
| 36 months of operations | $7,019.25 |
| Scenario A + 12 months of operations | $17,930.25 |
| Scenario B + 12 months of operations | $3,679.47 |

**Financial inventory:** 10 computers (8 Windows, 2 Linux), 37 equipment/material lines, 32 deployment activities, 35 operating/financial assumption codes, and 45 source references. The workbook also stores one dedicated FX conversion parameter.

The 12- and 36-month amounts are straight-line projections. They do not model inflation, exchange-rate changes, additional equipment, service-level upgrades, or contractual price escalation.

### 3.1. Investment Categories — Scenario A

| Equipment category | Subtotal (USD) |
|---|---:|
| Cisco Networking | $7,646.53 |
| Workstations | $2,290.02 |
| Wi-Fi and IoT | $233.63 |
| Rack and Power | $179.83 |
| Cabling | $94.83 |
| Telephony | $89.92 |
| Tools | $28.18 |
| Furniture | $0.00 |

The equipment and materials subtotal is **$10,562.93**. This is the acquisition basis before deployment labor, licenses, freight and contingency.

---

## 4. Scenario A — Full Acquisition and Deployment

Scenario A models purchasing equipment, building the infrastructure, installing its software components and setting aside initial delivery and financial provisions.

| Code | Component | Amount (USD) |
|---|---|---:|
| A1 | Equipment and materials | $10,562.93 |
| A2 | Deployment labor | $1,229.68 |
| A3 | Provisioned initial licenses | $2,300.72 |
| A4 | Shipping and distribution | $369.70 |
| A5 | Contingency reserve | $1,127.47 |
| **TOTAL** | **Full acquisition and deployment** | **$15,590.49** |

### 4.1. Equipment and Materials

This component purchases the enabled items in the **Inventory** sheet, including the Cisco C8200L and C9200L, ten desktop computer systems, ten monitors, ten keyboard/mouse sets, two Archer AX53 units, the Alexa reference, rack components, structured-cabling materials, two Grandstream phones, and basic cabling tools.

### 4.2. Technical Deployment

The **Deployment** worksheet contains 32 services covering network planning, cabling, Cisco configuration, Linux, Docker, application installation, monitoring, telephony, verification, diagrams and handover documents. The modeled total is **103.4 hours**, billed at category-specific reference rates. No part of this figure is represented as a time sheet or an executed service agreement.

### 4.3. Software Licensing

Eight Windows 11 Pro retail licenses are provisioned as an acquisition allowance. The open-source components are modeled with a $0 software-use license fee; their integration, operation and administration remain separate costs.

### 4.4. Shipping Allowance

The regional shipping allowance is **3.5%** of the equipment/material base:

```text
Shipping = Equipment and materials × 0.035
         = $10,562.928057… × 0.035
         = $369.70
```

This is a planning allowance, not a freight carrier quotation.

### 4.5. Contingency Reserve

The contingency provision is **8%** of equipment, deployment and initial licenses:

```text
Contingency = (Materials + Deployment + Licenses) × 0.08
            ≈ $1,127.47
```

It is part of the reference budget and does not indicate an actual unplanned expense.

### 4.6. Total Calculation

```text
Materials + Labor + Licenses + Shipping + Contingency
= $15,590.49   (model-calculated USD equivalent)
```

The full-acquisition total is stored in the **Scenario A** worksheet and linked to **Dashboard**.

---

## 5. Scenario B — Deployment Using Existing Assets

Scenario B models a customer-provided hardware environment. The main computers, Cisco equipment, wireless routers and phones are **not purchased again**. Selected consumables, technical deployment and a travel allowance remain included.

| Code | Component | Amount (USD) |
|---|---|---:|
| B1 | Additional materials | $99.25 |
| B2 | Deployment services | $1,229.68 |
| B3 | New operating-system licenses | $0.00 |
| B4 | Technician travel | $10.79 |
| **TOTAL** | **Deployment with existing assets** | **$1,339.72** |

### 5.1. Included Consumables

| Equipment ID | Additional material | Subtotal (USD) |
|---|---|---:|
| EQ-016 | Rack fastening set (20 cage nuts/screws) | $4.43 |
| EQ-018 | CAT6 network cable box (305 m, illustrative) | $77.48 |
| EQ-019 | CAT6 RJ45 connectors (100-pack) | $7.23 |
| EQ-023 | Cable-management hook-and-loop roll | $2.51 |
| EQ-036 | Nylon cable ties (100-pack) | $2.21 |
| EQ-039 | Cable identification labels | $5.39 |

The additional-material subtotal is **$99.25**. The same deployment scope as Scenario A is included because existing equipment does not remove the modeled configuration and installation work.

The **$10.79** travel allowance corresponds to BRL 60.00 converted using FX-01. Software licenses are treated as already supplied in this scenario; no fresh Windows retail-license purchase is added.

The first-year amount, including the recurring cost model, is **$3,679.47**.

---

## 6. Scenario C — Monthly Operations and Maintenance

Scenario C represents a recurring-cost estimate for the documented infrastructure. It includes electrical energy, an internet reference, preventive technical support, backup storage, and an equipment replacement provision.

| Code | Metric | USD amount |
|---|---|---:|
| C1 | Monthly operations | **$194.98** |
| C2 | 12-month operations | $2,339.75 |
| C3 | 36-month operations | $7,019.25 |
| C4 | Electricity per month | $82.78 |
| C5 | Internet / WAN per month | $28.76 |
| C6 | Preventive maintenance per month | $63.85 |
| C7 | Backup and replacement reserves per month | $19.59 |

These expenses do not constitute a contracted 24/7 NOC monitoring or on-call response service.

### 6.1. Preventive Maintenance

The preventive support allocation covers:

- Two hours per month for Linux and container support.
- One hour for Cisco networking and corporate Wi-Fi administration.
- One hour for Grafana/Zabbix dashboard and alert review.
- One hour for backup verification.

The total modeled support time is **5 hours/month** and the monthly labor estimate is approximately **$63.85**.

### 6.2. Internet Service

The monthly broadband reference is **$28.76**, converted from the BRL 159.90 reference in `Sources` (RF-32). It is a local consumer-market benchmark from Santarém, Brazil. Business fiber, dedicated links, fixed IPs and contractual SLAs are outside this base case.

### 6.3. Backup and Replacement Allowances

The operating model includes approximately **$10.79** for external backup storage and **$8.80** as a monthly hardware replacement provision. The latter derives from **1% of equipment acquisition cost per year**, spread across twelve months. These are planning provisions, not payments or proof of an existing backup subscription.

---

## 7. Inventory — Equipment and Materials

The **Inventory** worksheet retains 37 cost lines. Each line includes an equipment identifier, category, item description, commercial reference, quantity, unit, USD unit price, Scenario A/B purchasing switches, calculated subtotals, a pricing classification, source ID and technical scope notes.

The table below lists **every inventory line**. A zero subtotal indicates an item excluded from the respective baseline, even when a reference price is available.

| ID | Category | Item | Qty. | Unit price (USD) | A | B | Subtotal A (USD) | Source |
|---|---|---|---:|---:|:---:|:---:|---:|---|
| EQ-001 | Cisco Networking | Cisco Catalyst C8200L — router | 1 | $4,212.60 | Yes | No | $4,212.60 | RF-01 |
| EQ-002 | Cisco Networking | Cisco Catalyst C9200L-24T-4G — switch | 1 | $3,429.50 | Yes | No | $3,429.50 | RF-02 |
| EQ-003 | Workstations | Physical computers (8 Windows + 2 Linux) | 10 | $156.17 | Yes | No | $1,561.71 | RF-29 |
| EQ-004 | Workstations | Standalone monitor (unless included with desktop) | 10 | $53.96 | Yes | No | $539.55 | RF-26 |
| EQ-005 | Workstations | Keyboard and mouse (unless bundled with desktop) | 10 | $18.88 | Yes | No | $188.76 | RF-25 |
| EQ-006 | Workstations | Extra Docker server (not required) |  | $156.17 | No | No | $0.00 | RF-29 |
| EQ-007 | Wi-Fi and IoT | TP-Link Archer AX53 — corporate Wi-Fi and IoT | 2 | $53.96 | Yes | No | $107.91 | RF-03 |
| EQ-008 | Wi-Fi and IoT | Amazon Alexa with display — comparable | 1 | $125.72 | Yes | No | $125.72 | RF-04 |
| EQ-009 | Wi-Fi and IoT | Smart E27 bulb (optional) |  | $7.67 | No | No | $0.00 | RF-05 |
| EQ-010 | Wi-Fi and IoT | E27 bulb socket (optional) |  | $1.46 | No | No | $0.00 | RF-06 |
| EQ-011 | Rack and Power | 19-inch rack | 1 | $117.01 | Yes | No | $117.01 | RF-07 |
| EQ-012 | Rack and Power | 24-port patch panel | 1 | $36.39 | Yes | No | $36.39 | RF-08 |
| EQ-013 | Rack and Power | Rack power distribution strip (PDU) | 1 | $17.81 | Yes | No | $17.81 | RF-09 |
| EQ-014 | Rack and Power | Horizontal rack cable manager | 1 | $4.19 | Yes | No | $4.19 | RF-10 |
| EQ-015 | Rack and Power | Rack shelf/support (if needed) |  | $9.57 | No | No | $0.00 | RF-11 |
| EQ-016 | Rack and Power | Rack fastening set (20 cage nuts/screws) | 1 | $4.43 | Yes | Yes | $4.43 | RF-12 |
| EQ-017 | Rack and Power | 1200 VA UPS (optional) |  | $143.71 | No | No | $0.00 | RF-34 |
| EQ-018 | Cabling | CAT6 network cable box (305 m, illustrative) | 1 | $77.48 | Yes | Yes | $77.48 | RF-13 |
| EQ-019 | Cabling | CAT6 RJ45 connectors (100-pack) | 1 | $7.23 | Yes | Yes | $7.23 | RF-14 |
| EQ-020 | Cabling | CAT6 RJ45 keystone (single) |  | $1.37 | No | No | $0.00 | RF-15 |
| EQ-021 | Cabling | Surface-mount box/faceplate for keystones |  | $1.29 | No | No | $0.00 | RF-16 |
| EQ-023 | Cabling | Cable-management hook-and-loop roll | 1 | $2.51 | Yes | Yes | $2.51 | RF-17 |
| EQ-024 | Cabling | Cable raceways, conduits and accessories |  | $1.78 | No | No | $0.00 | RF-18 |
| EQ-026 | Telephony | Grandstream IP phones (2 units) | 2 | $44.96 | Yes | No | $89.92 | RF-19 |
| EQ-027 | Telephony | Headsets / telephony accessories |  | $21.58 | No | No | $0.00 | RF-36 |
| EQ-028 | Tools | RJ45 crimping tool | 1 | $13.31 | Yes | No | $13.31 | RF-20 |
| EQ-029 | Tools | Network cable tester | 1 | $7.19 | Yes | No | $7.19 | RF-21 |
| EQ-030 | Tools | Punch-down tool | 1 | $4.94 | Yes | No | $4.94 | RF-22 |
| EQ-031 | Furniture | Workbenches and workstation supports |  | $62.95 | No | No | $0.00 | RF-37 |
| EQ-032 | Furniture | Chairs and monitor supports |  | $35.97 | No | No | $0.00 | RF-38 |
| EQ-033 | Cisco Networking | SFP modules/transceivers |  | $26.98 | No | No | $0.00 | RF-39 |
| EQ-034 | Cisco Networking | Console/serial management cables | 1 | $4.42 | Yes | No | $4.42 | RF-33 |
| EQ-035 | Tools | Cable stripping pliers | 1 | $2.73 | Yes | No | $2.73 | RF-23 |
| EQ-036 | Cabling | Nylon cable ties (100-pack) | 1 | $2.21 | Yes | Yes | $2.21 | RF-24 |
| EQ-037 | Cabling | RJ45 connector boots |  | $4.50 | No | No | $0.00 | RF-40 |
| EQ-038 | Cabling | Ready-made CAT6 patch cable |  | $4.50 | No | No | $0.00 | RF-35 |
| EQ-039 | Cabling | Cable identification labels | 1 | $5.39 | Yes | Yes | $5.39 | RF-41 |

### 7.1. Cisco Infrastructure

The router reference is the **Cisco Catalyst C8200L-1N-4T** and the switch reference is the **Cisco Catalyst C9200L-24T-4G-E** (24 data ports, non-PoE). The non-PoE commercial model aligns with the documented C9200L-24T-4G switch family more closely than a 24P PoE reference. The precise installed SKU, add-on licensing, commercial support and tax treatment are separate considerations.

One USB-to-RJ45 console cable is included in the acquisition scenario. SFP transceivers are retained as optional inventory records with acquisition disabled.

### 7.2. Computers and Peripheral Equipment

All ten physical machines are included as desktop systems using the commercial price of a refurbished OptiPlex 3020-class system. Monitors and keyboard/mouse sets are purchased as separate inventory lines. The main Debian Docker computer and the Debian telephony/authentication computer are **already included** in the ten-system count; an extra Docker server is therefore excluded.

### 7.3. Corporate Wi-Fi and IoT

Two distinct **TP-Link Archer AX53** devices are budgeted, one connected to the VLAN 60 corporate wireless segment and another associated with VLAN 70 IoT. The display-equipped Amazon Alexa is valued using an **Echo Show 5 commercial comparison**. The exact physical Alexa model is not established by that pricing reference. An E27 smart bulb and socket are optional and excluded.

### 7.4. Rack, Cabling and Tools

The financial reproduction includes a 19-inch rack reference, a 24-port CAT6 patch panel, rack power distribution strip, horizontal organizer, mounting kit, CAT6 305 m cable box, connector pack, hook-and-loop material, cable ties and identification labels. Bulk-cable quantities are commercial purchasing units rather than measured installed cable lengths. Optional items include a UPS, shelf, keystones, faceplates, raceways, connector boots and ready-made patch cords.

A basic cable tester is included for continuity checks; its presence is not evidence of CAT6 certification. Crimping, punch-down and stripping tools are treated as reusable acquisition assets.

### 7.5. Telephony and Furniture

Two Grandstream IP phones are included using the GRP2601 as a commercial pricing reference; individual hardware model identification is separate from the documented phone count. Headsets and office furniture retain optional benchmark prices but do not enter the base totals.

---

## 8. Computers — Workstation and Server Inventory

The **Computers** worksheet itemizes the ten physical computers using a unified **{money(tables['Computers']['values'][1][9])}** commercial reference per system. It contains eight Windows workstations and two distinct Linux servers.

| ID | Department / Role | CPU / Reference | RAM | Storage record | Operating system | Desktop reference (USD) |
|---|---|---|---|---|---|---:|
| PC-01 | IT / NOC | Intel Core i5-4590 | ≈ 8 GB | ext4 root: 210.27 GiB | Debian 13 | $156.17 |
| PC-02 | IT | Intel Core i5-4590 (reference) | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-03 | Accounting 1 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-04 | Accounting 2 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-05 | Accounting 3 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-06 | Finance 1 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-07 | Finance 2 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-08 | Sales 1 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-09 | Sales 2 | Intel Core i5-4590 | 8 GB | 224 GB shown | Windows 11 Pro 21H2 | $156.17 |
| PC-10 | Telephony / authentication | Intel Core i5-4590 | ≈ 8 GB | ext4 root: 211.21 GiB | Debian forky/sid | $156.17 |

### 8.1. Windows Desktop Standard

All eight Windows workstations are represented in the budget with:

- **Windows 11 Pro 21H2**
- **8 GB RAM**
- **224 GB displayed storage capacity**

This configuration reflects the laboratory-reported standard used to harmonize the inventory. The PC-02 i5-4590 entry is explicitly classified in the workbook as a hardware-reference assumption based on the predominant desktop configuration, not an independent CPU reading for that workstation. The 224 GB figure is the displayed capacity; it does not independently establish disk type or manufacturer.

### 8.2. Main NOC / Docker Host

The primary infrastructure machine is a **Dell OptiPlex 3020**, **Intel Core i5-4590**, approximately **8 GB RAM**, running **Debian 13 (Trixie)**. Its recorded ext4 root filesystem is approximately **210.27 GiB**. It hosts the Docker-based infrastructure and monitoring stack documented in the project.

### 8.3. Asterisk / FreeRADIUS Server

The voice/authentication machine is a separate **Dell OptiPlex 3020**, **Intel Core i5-4590**, approximately **8 GB RAM**, running **Debian forky/sid** at collection. Its recorded ext4 root filesystem is approximately **211.21 GiB**. Asterisk and FreeRADIUS run on this computer rather than constituting additional computer purchases.

### 8.4. Desktop and Peripheral Acquisition

The desktop price is a refurbished Brazilian listing converted to USD, not a U.S. market quote or an actual depreciation valuation. The from-scratch budget additionally purchases ten monitors and ten wired keyboard/mouse kits. These peripherals are excluded from the desktop reference price to keep the line items separate.

---

## 9. Deployment — Technical Labor Estimate

The **Deployment** worksheet contains **32 services** and **103.4 total modeled technician hours**, using the BRL reference hourly tariffs converted to USD. Services represent scope estimates for reproducing the environment, not actual activity logs.

For each service:

```text
Total hours = Quantity × Hours per unit
Service subtotal (USD) = Total hours × Rate (USD/hour)
```

| ID | Area | Technical service | Hours | Subtotal (USD) |
|---|---|---|---:|---:|
| MO-001 | Cabling | Network-point planning and survey | 2.0 | $19.78 |
| MO-002 | Cabling | Cable pulling and organization | 6.0 | $59.35 |
| MO-003 | Cabling | Hand-assembling RJ45 cables | 4.0 | $39.57 |
| MO-004 | Cabling | Patch-panel termination and labeling | 2.0 | $19.78 |
| MO-005 | Cabling | Basic network-point continuity tests | 2.4 | $23.74 |
| MO-006 | Rack | Rack installation, fastening and organization | 3.0 | $29.68 |
| MO-007 | Workstations | Computer assembly and inspection | 7.5 | $67.45 |
| MO-008 | Workstations | Operating system and driver installation | 7.5 | $67.45 |
| MO-009 | Workstations | IP addressing and connectivity tests | 2.5 | $22.48 |
| MO-010 | Cisco Networking | IPv4, VLAN and segmentation planning | 3.0 | $48.56 |
| MO-011 | Cisco Networking | Cisco Catalyst C9200L configuration | 4.0 | $64.75 |
| MO-012 | Cisco Networking | Cisco Catalyst C8200L configuration | 4.0 | $64.75 |
| MO-013 | Cisco Networking | ACL implementation and tests | 2.0 | $32.37 |
| MO-014 | Wi-Fi and IoT | Configure two TP-Link Archer AX53 devices | 2.0 | $32.37 |
| MO-015 | Wi-Fi and IoT | Alexa device integration | 1.0 | $8.99 |
| MO-016 | Identity | FreeRADIUS deployment and testing | 3.0 | $37.77 |
| MO-017 | Telephony | Asterisk / VoIP deployment | 4.0 | $50.36 |
| MO-018 | Linux / Docker | Linux host installation and basic hardening | 3.0 | $37.77 |
| MO-019 | Linux / Docker | Docker Engine and Compose installation | 2.0 | $25.18 |
| MO-020 | Linux / Docker | MariaDB and Zabbix deployment | 6.0 | $75.54 |
| MO-021 | Observability | Grafana and datasource deployment | 3.0 | $37.77 |
| MO-022 | Observability | NOC dashboard development | 5.0 | $62.95 |
| MO-023 | Observability | Cisco SNMP monitoring | 3.0 | $48.56 |
| MO-024 | Observability | Uptime Kuma deployment | 1.5 | $18.88 |
| MO-025 | Networking / DNS | Pi-hole / internal DNS deployment | 2.0 | $25.18 |
| MO-026 | Web and Security | Nginx reverse-proxy and TLS deployment | 3.0 | $37.77 |
| MO-027 | Web and Security | HTML portal publication and testing | 2.0 | $25.18 |
| MO-028 | Operations | Portainer CE configuration | 1.0 | $12.59 |
| MO-029 | Operations | Backup and persistence planning | 2.0 | $25.18 |
| MO-030 | Testing | End-to-end access and monitoring tests | 4.0 | $43.17 |
| MO-031 | Documentation | Technical diagrams and inventory | 3.0 | $32.37 |
| MO-032 | Documentation | Configuration reports and handover | 3.0 | $32.37 |

**Total modeled deployment:** **103.4 hours — $1,229.68**.

### 9.1. Hourly Tariffs

| Labor category | BRL reference | USD equivalent |
|---|---:|---:|
| Cabling | BRL 55.00/h | $9.89/h |
| Computer assembly | BRL 50.00/h | $8.99/h |
| Linux and infrastructure services | BRL 70.00/h | $12.59/h |
| Cisco networking | BRL 90.00/h | $16.19/h |
| Testing and documentation | BRL 60.00/h | $10.79/h |

These tariffs are configurable model inputs. Network configuration, ACL tests, end-to-end service verification and other deployment tasks appear as **budget scope**, not as proof that a particular test was performed in the historical technical environment.

---

## 10. Software — Licensing and Subscription Costs

The model separates license fees from deployment labor and infrastructure operating costs.

| ID | Software / Service | Licensing basis | Quantity | Initial (USD) | Monthly (USD) | Included |
|---|---|---|---:|---:|---:|:---:|
| SW-001 | Debian GNU/Linux | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-002 | Docker Engine / Compose | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-003 | Portainer Community Edition | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-004 | Zabbix Server / Web / Agent | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-005 | Grafana OSS | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-006 | Uptime Kuma | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-007 | Pi-hole | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-008 | MariaDB Community | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-009 | Nginx Open Source | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-010 | Apache HTTP Server | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-011 | Asterisk | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-012 | FreeRADIUS | Community / open source | 1 | $0.00 | $0.00 | Yes |
| SW-013 | Cisco IOS XE / additional subscriptions and support | SKU-dependent licensing |  | $0.00 | $0.00 | No |
| SW-014 | Windows 11 Pro 21H2 — allowance for 8 workstations | Proprietary license | 8 | $2,300.72 | $0.00 | Yes |
| SW-015 | TLS certificates / PKI | Local, no subscription |  | $0.00 | $0.00 | No |

### 10.1. Initial License Allowance

The only nonzero initial software-license provision in the base model is **eight retail Windows 11 Pro licenses**, at the USD equivalent of the Brazilian price reference:

```text
8 × (BRL 1,599.00 / 5.5600)
= $2,300.72
```

Debian, Docker Engine/Compose, Portainer CE, Zabbix, Grafana OSS, Uptime Kuma, Pi-hole, MariaDB Community, Nginx, Apache, Asterisk and FreeRADIUS are priced with a **$0 community-edition use-license fee**. Installation and support are budgeted separately.

### 10.2. Windows 11 Hardware Support Boundary

The documented Intel Core i5-4590 belongs to Intel's fourth-generation Core line. It is absent from Microsoft's official Windows 11 supported processor list. Including an allowance for a license **does not establish OS hardware compatibility** or compliance with Microsoft's Windows 11 hardware requirements.

### 10.3. Excluded Proprietary Subscriptions

Additional Cisco subscriptions/support, commercial TLS certificates and paid professional support offerings are outside the baseline unless explicitly priced and enabled. A $0 entry for an excluded contract is **not** a claim that its real-world service price is zero.

---

## 11. Monthly Operations — Recurring Cost Lines

The **Monthly Operations** sheet contains twelve cost lines, eight of which are enabled in the base scenario.

| ID | Expense / Service | Quantity | Monthly subtotal (USD) | Enabled |
|---|---|---:|---:|:---:|
| OP-001 | Estimated electricity | 1 | $82.78 | Yes |
| OP-002 | Internet / WAN (local reference) | 1 | $28.76 | Yes |
| OP-003 | Linux and container support | 2 | $25.18 | Yes |
| OP-004 | Cisco and Wi-Fi administration | 1 | $16.19 | Yes |
| OP-005 | Dashboard and alert review | 1 | $12.59 | Yes |
| OP-006 | Backup verification | 1 | $9.89 | Yes |
| OP-007 | Monthly replacement reserve | 1 | $8.80 | Yes |
| OP-008 | External backup storage | 1 | $10.79 | Yes |
| OP-009 | Additional Cisco support contract |  | $0.00 | No |
| OP-010 | Commercial TLS certificate |  | $0.00 | No |
| OP-011 | Professional open-source support |  | $0.00 | No |
| OP-012 | Additional public domain |  | $0.00 | No |

**Monthly total: $194.98.**

### 11.1. Preventive Support

The recurring technical service allocation comprises two hours of Linux/container maintenance and one hour each for Cisco/Wi-Fi administration, dashboard/alert review and backup checks: **five modeled technician hours/month**.

### 11.2. Backup and Replacement Provision

The model allocates a fixed amount for external backup storage and **1% of the initial equipment acquisition total per year** for replacement, divided by 12 months. These are operating provisions; the source evidence does not establish that a particular storage contract or hardware replacement purchase was made.

### 11.3. Excluded Recurring Contracts

Paid Cisco support, commercial TLS certificates, paid open-source support and additional domain charges remain excluded from the monthly baseline. Their zero subtotals are scenario decisions, not generic market price claims.

---

## 12. Electrical Energy Model

Energy expenditure is estimated from device-class average wattages, quantities, operating hours and a Brazilian electricity tariff converted to USD. **No direct electrical measurements are represented in the workbook.**

### 12.1. Modeled Power Inputs

| Device class | Quantity | Average power per unit |
|---|---:|---:|
| Cisco C8200L router | 1 | 55 W |
| Cisco C9200L switch | 1 | 75 W |
| Linux servers | 2 | 70 W |
| Windows workstations | 8 | 55 W |
| Monitors | 10 | 18 W |
| Archer AX53 routers | 2 | 12 W |
| Grandstream phones | 2 | 4 W |
| Alexa device | 1 | 6 W |

### 12.2. Operating Time

| Equipment group | Monthly model |
|---|---:|
| Continuously operated network/servers/wireless/phones/IoT | 720 hours |
| Workstations and monitors | 176 hours |

Continuous equipment corresponds to a **30-day × 24-hour** month. Workstation operation uses **22 business days × 8 hours**.

### 12.3. Estimated Electricity Consumption

```text
Continuous infrastructure:
  55 + 75 + (2 × 70) + (2 × 12) + (2 × 4) + 6
  = 308 W
  308 × 720 / 1000 = 221.76 kWh/month

Windows stations + monitors:
  (8 × 55) + (10 × 18)
  = 620 W
  620 × 176 / 1000 = 109.12 kWh/month

Total modeled consumption:
  221.76 + 109.12 = 330.88 kWh/month
```

The modeled electricity tariff is **BRL 1.391/kWh**, based on an indicative Equatorial Pará residential B1 reference with approximate tax assumptions. It is **not** a measured commercial B3 bill.

```text
330.88 kWh/month × BRL 1.391/kWh
≈ BRL 460.25/month
≈ $82.78/month
```

The workbook stores the resulting USD electricity cost as **$82.78/month**.

---

## 13. Assumptions and Foreign Exchange

`Assumptions` stores **PR-01 through PR-35**, plus **FX-01**. Quantities and electrical inputs retain their original units. BRL-denominated monetary input parameters are converted into USD references using FX-01.

| Code | Parameter | Model value | Unit |
|---|---|---:|---|
| PR-01 | Physical computers | 10 | unit |
| PR-02 | Windows workstations | 8 | unit |
| PR-03 | Linux servers | 2 | unit |
| PR-04 | Monitors in full acquisition | 10 | unit |
| PR-05 | Keyboard/mouse sets | 10 | unit |
| PR-06 | Hourly rate — cabling | $9.89 | USD/h |
| PR-07 | Hourly rate — assembly | $8.99 | USD/h |
| PR-08 | Hourly rate — Linux and services | $12.59 | USD/h |
| PR-09 | Hourly rate — Cisco networking | $16.19 | USD/h |
| PR-10 | Hourly rate — testing and documentation | $10.79 | USD/h |
| PR-11 | Estimated power — C8200L router | 55 | W |
| PR-12 | Estimated power — C9200L switch | 75 | W |
| PR-13 | Average power per Linux server | 70 | W |
| PR-14 | Average power per Windows workstation | 55 | W |
| PR-15 | Average power per monitor | 18 | W |
| PR-16 | Average power per Archer AX53 | 12 | W |
| PR-17 | Power per Grandstream phone | 4 | W |
| PR-18 | Alexa power | 6 | W |
| PR-19 | Continuous rack runtime | 720 | h/month |
| PR-20 | Workstation runtime | 176 | h/month |
| PR-21 | Modeled electricity tariff | $0.2502 | USD/kWh |
| PR-22 | Estimated monthly internet | $28.76 | USD/month |
| PR-23 | Regional shipping allowance | 3.5% | % of materials |
| PR-24 | Contingency reserve | 8% | % of Scenario A subtotal |
| PR-25 | Additional travel in Scenario B | $10.79 | USD |
| PR-26 | Monthly external backup | $10.79 | USD / month |
| PR-27 | Annual replacement reserve | 1% | % hardware/year |
| PR-28 | Windows license quantity | 8 | unit |
| PR-29 | Windows 11 Pro retail license | $287.59 | USD/unit |
| PR-30 | Operating horizon | 12 | months |
| PR-31 | Extended operating horizon | 36 | months |
| PR-32 | Servers operating continuously | 2 | unit |
| PR-33 | Archer AX53 units operating | 2 | unit |
| PR-34 | IP phones operating | 2 | unit |
| PR-35 | Alexa units included | 1 | unit |
| FX-01 | BRL per USD — Nov 11, 2026 | $5.56 | BRL per USD |

### 13.1. Reference Rate and Update Propagation

The model's historical conversion reference is fixed in the spreadsheet at **BRL 5.5600 per USD 1.00**. Monetary inputs and totals are linked to that rate; changes to the FX parameter would alter USD equivalents while leaving documented device counts, technical roles and BRL source quotes unchanged.

The exchange-rate input serves this historical budget. It does not indicate real-time FX access or execution of currency trading.

---

## 14. Sources — Commercial and Planning References

The **Sources** worksheet contains 45 source records. References with supplier URLs originate from Brazilian listings and retained product pages; planning entries explicitly identify their assumption status. The USD unit prices below are workbook-calculated equivalents; source rows also preserve the original BRL quote when applicable.

| ID | Reference item | Provider / Basis | Price (USD) | Original quote / Basis | Source |
|---|---|---|---:|---:|---|
| RF-01 | Cisco Catalyst C8200L-1N-4T router | Xtech | $4,212.60 | BRL 23,422.08 | [Reference](https://xtech.com.br/cisco-catalyst-8200l-with-1-nim-slot-and-4x1g-wan-ports/p/55138/) |
| RF-02 | Cisco Catalyst C9200L-24T-4G-E switch (non-PoE) | FoxTI | $3,429.50 | BRL 19,068.00 | [Reference](https://www.foxti.com.br/products/cisco-catalyst-c9200l-24t-4g-e-24-port-data-switch-with-4x1g-uplinks-network-essentials) |
| RF-03 | TP-Link Archer AX53 Wi-Fi 6 AX3000 | Pichau | $53.96 | BRL 299.99 | [Reference](https://www.pichau.com.br/roteador-tp-link-archer-ax53-wi-fi-6-dual-band-ax3000-4-antenas-preto-archer-ax53) |
| RF-04 | Amazon Echo Show 5 — display model reference | Vivo Store | $125.72 | BRL 699.00 | [Reference](https://z9w115.store.vivo.com.br/marca/amazon/c/) |
| RF-05 | E27 Wi-Fi smart bulb | KaBuM! | $7.67 | BRL 42.66 | [Reference](https://www.kabum.com.br/produto/1043228/lampada-inteligente-led-wi-fi-elw-1001-intelbras) |
| RF-06 | E27 lamp socket with switch | Central Elétrica | $1.46 | BRL 8.12 | [Reference](https://www.lojacentraleletrica.com.br/produto/soquete-porta-lampada-com-chave-pvc-latao-e27) |
| RF-07 | 19-inch 12U wall-mount rack | Solução Cabos | $117.01 | BRL 650.56 | [Reference](https://www.solucaocabos.com.br/mini-rack-de-parede-19--12us-x-570mm-branco/p) |
| RF-08 | CAT6 24-port patch panel | Solução Cabos | $36.39 | BRL 202.35 | [Reference](https://www.solucaocabos.com.br/patch-panel-24-portas-cat6-dc/p) |
| RF-09 | 19-inch rack power strip (8 outlets) | Rack Outdoor | $17.81 | BRL 99.00 | [Reference](https://rackoutdoor.com.br/shop/acessorios/reguas-de-tomadas/regua-de-tomada-para-rack-19-com-8-tomadas-10a-com-protecao/) |
| RF-10 | 1U horizontal rack cable manager | Unicaserv | $4.19 | BRL 23.32 | [Reference](https://www.unicaserv.com.br/linha-metalurgica/acessorios-para-rack/guia-de-cabos-horizontal-fechada-padrao-19-1u-preta) |
| RF-11 | 19-inch 1U fixed rack shelf | Raitek | $9.57 | BRL 53.20 | [Reference](https://www.raitekdistribuidora.com.br/racks-e-acessorios/bandejas) |
| RF-12 | 20-piece cage nut and screw kit | HD Store | $4.43 | BRL 24.62 | [Reference](https://www.hdstore.com.br/kit-porca-gaiola-parafuso-m5-padrao-rack-servidor-pacote-20-pecas) |
| RF-13 | CAT6 copper cable, 305 m | PrimeCabos | $77.48 | BRL 430.80 | [Reference](https://www.primecabos.com/cabo-de-rede/cabo-cat6) |
| RF-14 | 100-pack CAT6 RJ45 connectors | KaBuM! | $7.23 | BRL 40.22 | [Reference](https://www.kabum.com.br/produto/1066948/conector-rj45-plus-cable-cat-6-la-cat6-c-100-pecas) |
| RF-15 | CAT6 keystone | Central Cabos | $1.37 | BRL 7.60 | [Reference](https://www.centralcabos.com.br/redes/keystone/cat6) |
| RF-16 | Surface-mount box for two keystones | Rede Loja | $1.29 | BRL 7.15 | [Reference](https://redeloja.com/produto/1747314101615) |
| RF-17 | Hook-and-loop cable management roll | Unicaserv | $2.51 | BRL 13.97 | [Reference](https://www.unicaserv.com.br/racks-e-acessorios/acessorios-para-racks/organizadores-para-racks) |
| RF-18 | 20 × 10 mm adhesive raceway, 2 m | Sodimac | $1.78 | BRL 9.90 | [Reference](https://www.sodimac.com.br/sodimac-br/product/780771/canaleta-com-adesivo-20x10mm-2-metros/780771/) |
| RF-19 | Grandstream IP phone | KaBuM! | $44.96 | BRL 249.99 | [Reference](https://www.kabum.com.br/produto/194967/telefone-ip-grandstream-2-linhas-visor-lcd-preto-grp2601) |
| RF-20 | RJ45 crimping pliers | LC Ferragens | $13.31 | BRL 74.01 | [Reference](https://www.lcferragens.com.br/produto/alicate-crimpar-vonder-rj-45/) |
| RF-21 | Basic cable tester | FGTEC | $7.19 | BRL 39.99 | [Reference](https://www.fgtec.com.br/perifericos/testador-de-cabo-de-rede-pluscable-rj11-rj45-lt-100) |
| RF-22 | Punch-down tool | Central Cabos | $4.94 | BRL 27.46 | [Reference](https://www.centralcabos.com.br/ferramenta/alicates) |
| RF-23 | Cable stripping pliers | Central Cabos | $2.73 | BRL 15.20 | [Reference](https://www.centralcabos.com.br/ferramenta/alicates) |
| RF-24 | Nylon cable ties, 100-pack | Unicaserv | $2.21 | BRL 12.26 | [Reference](https://www.unicaserv.com.br/infra-estrutura/abracadeiras/abracadeira-de-nylon-3-5mm-x-200mm-branca-cento) |
| RF-25 | Logitech MK120 wired keyboard/mouse set | KaBuM! | $18.88 | BRL 104.95 | [Reference](https://www.kabum.com.br/produto/254649/teclado-e-mouse-logitech-mk120-resistente-a-agua-1000dpi-preto-abnt2-920-004429) |
| RF-26 | BRX 21-inch monitor | TerabyteShop | $53.96 | BRL 299.99 | [Reference](https://www.terabyteshop.com.br/produto/42811/monitor-brx-21-pol-60hz-hdmivga-vesa-preto-mbrx21bk) |
| RF-27 | Alternate Cisco 8200L price | Xtech | $4,212.60 | BRL 23,422.08 | [Reference](https://xtech.com.br/cisco-catalyst-8200l-with-1-nim-slot-and-4x1g-wan-ports/p/55138/) |
| RF-28 | Alternate Cisco 9200L price | Xtech | $6,459.97 | BRL 35,917.41 | [Reference](https://xtech.com.br/Switch-Cisco-Catalyst-9200l-24-Port-Poe-4-X-1g-Network-Advanta-C9200l-24p-4g-A/p/52916/) |
| RF-29 | Refurbished Dell OptiPlex 3020 i5 / 8 GB / 240 GB SSD | Mercado Livre | $156.17 | BRL 868.31 | [Reference](https://lista.mercadolivre.com.br/dell-optiplex-3020) |
| RF-30 | Windows 11 Pro license — retail reference | Microsoft Store Brazil | $287.59 | BRL 1,599.00 | [Reference](https://www.microsoft.com/pt-br/d/windows-11-pro/dg7gmgf0d8h4) |
| RF-31 | Equatorial Pará electricity tariff | Tarifa Aberta / ANEEL | $0.2502 | BRL 1.391/kWh | [Reference](https://tarifaaberta.com.br/distribuidoras/equatorial-pa/) |
| RF-32 | Broadband internet in Santarém | Radar da Telecom | $28.76 | BRL 159.90 | [Reference](https://www.radardatelecom.com/municipio/pa/santarem) |
| RF-33 | 1.80-m FTDI USB-to-RJ45 console cable | Central Cabos | $4.42 | BRL 24.60 | [Reference](https://www.centralcabos.com.br/cabo-console-usb-para-rj45-180-metros/p) |
| RF-34 | 1200 VA UPS | Budget assumption | $143.71 | BRL 799.00 | Planning allowance |
| RF-35 | 2-meter CAT6 patch cord | Budget assumption | $4.50 | BRL 25.00 | Planning allowance |
| RF-36 | Basic telephony headset | Budget assumption | $21.58 | BRL 120.00 | Planning allowance |
| RF-37 | Basic workstation desk | Budget assumption | $62.95 | BRL 350.00 | Planning allowance |
| RF-38 | Basic office chair | Budget assumption | $35.97 | BRL 200.00 | Planning allowance |
| RF-39 | 1 Gbps SFP transceiver | Budget assumption | $26.98 | BRL 150.00 | Planning allowance |
| RF-40 | RJ45 connector boots (pack) | Budget assumption | $4.50 | BRL 25.00 | Planning allowance |
| RF-41 | Adhesive cable identification labels (120-pack) | Mercado Livre (listing) | $5.39 | BRL 29.98 | [Reference](https://lista.mercadolivre.com.br/etiquetas-para-cabos) |
| RF-42 | External backup storage | Budget assumption | $10.79 | BRL 60.00 | Planning allowance |
| RF-43 | Open-source software | Official projects | $0.00 use-license | — | [Reference](https://www.debian.org/) |
| RF-44 | Windows 11 requirements | Microsoft Learn | Technical reference | — | [Reference](https://learn.microsoft.com/pt-br/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors) |
| RF-45 | Maintenance and replacement reserve | Budget assumption | 1%/year | — | Planning allowance |

### 14.1. Source Classification

- **RF-01–RF-33:** primarily vendor product listings, comparable equipment models, and market references. Some rows retain older supplier references; a URL is a source locator, not a guarantee that the listing is currently active.
- **RF-34–RF-40:** optional equipment and accessories with planning-assumption prices and no independent product-level quotation.
- **RF-41:** a price reference for cable identification labels.
- **RF-42:** an estimated recurring external-backup storage allowance.
- **RF-43:** official open-source ecosystem reference; $0 pertains only to the selected community software-use license fees.
- **RF-44:** Microsoft documentation about supported Windows 11 processors; a technical compatibility reference rather than a monetary quotation.
- **RF-45:** a 1% annual replacement reserve assumption, expressed as a percentage rather than a product unit price.

The original Brazilian reference figures are intentionally retained in `Sources`. Supplier taxes, SKU differences, transport conditions, local restrictions, warranties and support subscriptions can materially affect an actual procurement price.

---

## 15. Financial Calculation Rules

### 15.1. Equipment Line Subtotal

```text
If the scenario's purchase flag is enabled:
    Equipment subtotal = Quantity × USD unit reference price
Otherwise:
    Equipment subtotal = 0
```

`Inventory` maintains separate purchase switches and formula results for **Scenario A** and **Scenario B**.

### 15.2. Deployment Service

```text
Labor hours = Quantity × Hours per unit
Service cost (USD) = Labor hours × USD hourly rate
```

The total hours and service cost are aggregated across 32 services. This prevents each scenario from manually maintaining an independent labor total.

### 15.3. Software

```text
Initial license cost =
    Sum of included, nonzero license provisions
```

The Windows retail-license allowance is included in Scenario A. The existing-assets scenario does not add fresh Windows licensing.

### 15.4. Shipping and Contingency

```text
Shipping = Scenario A equipment subtotal × 3.5%

Contingency =
    (Scenario A materials + labor + initial licenses) × 8%
```

### 15.5. Operating Cost

```text
Monthly operations =
    Sum of enabled monthly cost lines

Annual operations = Monthly operations × 12

36-month operations = Monthly operations × 36
```

The model uses underlying unrounded monetary amounts before presentation to two decimal places.

### 15.6. Reference Notation

Cross-sheet formula references use worksheet names and cell addresses. A notation such as:

```text
'Monthly Operations'!G23
```

means the `G23` cell in the `Monthly Operations` worksheet. These references are part of Excel/Calc's calculation syntax; display columns may use human-readable descriptions instead.

---

## 16. Long-Term Cost Projections

| Investment model | Initial amount | 12-month operating estimate | First-year combined estimate |
|---|---:|---:|---:|
| Full acquisition and deployment | {money(a_total)} | {money(annual)} | **{money(a_total+annual)}** |
| Deployment with provided assets | {money(b_total)} | {money(annual)} | **{money(b_total+annual)}** |

The 36-month operations-only projection is **{money(three_year)}**. These projections keep monthly expense and the chosen USD conversion basis constant across the simulated horizon.

Differences in hardware purchasing are confined to the initial investment. Both scenarios are modeled with equivalent ongoing infrastructure requirements once operating.

---

## 17. Scope Boundaries and Budget Limitations

### 17.1. Not an Asset Valuation

The workbook estimates the cost of **replicating** an infrastructure environment. It does not appraise the existing equipment, calculate historical depreciation, or reconstruct original supplier invoices.

### 17.2. Not a U.S. Commercial Quotation

The dollar values are conversions of Brazilian reference prices and planning assumptions using the stated FX rate. No claim is made that the same products can be procured in the United States for those USD amounts.

### 17.3. Vendor and Model Differences

The Cisco network families, two Archer AX53 devices, two Grandstream phones and Linux computer roles are documented technical components. The exact commercial SKU, optional licensing packages, rack dimensions, refurbishing condition, Alexa model and accessories may differ from the financial pricing references.

### 17.4. Services Versus Executed Tests

Deployment rows for interface configuration, ACLs, authentication testing, monitoring and recovery validation are financial service descriptions. Their inclusion in the budget is **not** test evidence. Technical results belong in the dated infrastructure and NOC records.

### 17.5. Energy, Internet and Labor

Device power, electricity tariff, runtime, internet plan, technician hours and hourly tariffs are inputs used for financial forecasting. They are not measured electrical loads or documented supplier service contracts.

### 17.6. Optional and Excluded Items

Optional UPS, SFP modules, rack shelves, keystones, patch cords, headsets, furniture, additional Docker hardware, commercial certificates and vendor subscriptions remain in the model for reference but do not increase the baseline unless enabled.

### 17.7. Software Licensing and Hardware Compatibility

Open-source software-use license fees can be $0 while deployment and maintenance still incur expenses. The Windows license allowance does not overcome the unsupported-hardware status of fourth-generation Intel Core CPUs under Windows 11.

### 17.8. Continuous Service Coverage

The model includes limited preventive maintenance and recurring operating allowances. It does not price a 24/7 NOC staffing model, dedicated business WAN SLA, emergency on-call rotation, full redundancy, or vendor-defined enterprise support contracts.

---

## 18. Budget Consistency and Traceability

| Model element | Cost treatment |
|---|---|
| Eight Windows desktops | Included within ten physical computers |
| Two Linux servers | Included within the same ten computers |
| Docker host | Existing Linux computer; no extra server purchase |
| Ten monitors | Separate equipment acquisition line |
| Ten keyboard/mouse sets | Separate equipment acquisition line |
| Two Archer AX53 devices | Distinct corporate Wi-Fi and IoT devices |
| Two Grandstream phones | Two equipment units |
| Installed vs. comparable models | Physical inventory and pricing basis kept distinct |
| Community software | $0 use-license fee, with implementation labor budgeted |
| Windows proprietary license | Eight-unit allowance in full acquisition |
| Cabling tools | Reusable acquisition assets |
| Network consumables | Scenario-specific purchase flags |
| 32 labor services | Hour-based deployment simulation |
| Electricity | Power-and-runtime consumption estimate |
| Internet | Brazilian retail reference converted to USD |
| External backup | Monthly service-cost allowance |
| Replacement reserve | 1%/year of equipment value, allocated monthly |

This README describes the financial workbook's **November 11, 2026 reference revision**. The `.xlsx` file is the editable source of the calculation model; the figures in this Markdown represent its calculated state at the listed reference rate.

---

## 19. Financial Conclusion

The full-acquisition scenario estimates **{money(a_total)}** for purchasing and deploying the modeled infrastructure. Deployment with customer-provided assets estimates **{money(b_total)}**. The modeled monthly operating expense is **{money(c_total)}**.

The combined first-year amounts are:

- **Full acquisition + 12 months:** **{money(a_total+annual)}**.
- **Existing assets + 12 months:** **{money(b_total+annual)}**.

These figures support comparisons between a complete initial purchase and a services-focused deployment, with a consistent recurring operating model. They are planning estimates and do not establish actual historical expenditures or contractual pricing.

---

## 20. Files and Language Versions

### 20.1. English — USD

- **Financial documentation:** [enterprise-noc-final-budget-usd-2026.md](enterprise-noc-final-budget-usd-2026.md)
- **Financial workbook:** [enterprise-noc-final-budget-usd-2026.xlsx](enterprise-noc-final-budget-usd-2026.xlsx)
- **Currency:** USD
- **Reference date:** November 11, 2026

### 20.2. Português — BRL

- **Documentação financeira:** [enterprise-noc-orcamento-final-brl-2026.md](../pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.md)
- **Planilha:** [enterprise-noc-orcamento-final-brl-2026.xlsx](../pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.xlsx)
- **Moeda:** BRL

---

**Enterprise NOC — From Scratch**  
**Infrastructure Cost Analysis**  
**Reference Revision: November 11, 2026**  
**Language: English (US) · Currency: USD**
