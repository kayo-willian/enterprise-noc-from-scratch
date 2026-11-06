# Enterprise NOC — From Scratch

**English | [Português (Brasil)](README.pt-BR.md)**

<p align="center">
  <img src="https://img.shields.io/badge/NOC-Infrastructure-0F172A?style=flat-square" alt="NOC Infrastructure">
  <img src="https://img.shields.io/badge/Status-In%20Development-2563EB?style=flat-square" alt="Development Status">
  <img src="https://img.shields.io/github/license/kayo-willian/enterprise-noc-from-scratch?style=flat-square" alt="MIT License">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Cisco-1BA0D7?style=flat-square&amp;logo=cisco&amp;logoColor=white" alt="Cisco">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&amp;logo=linux&amp;logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&amp;logo=docker&amp;logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Zabbix-D40000?style=flat-square&amp;logo=zabbix&amp;logoColor=white" alt="Zabbix">
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&amp;logo=grafana&amp;logoColor=white" alt="Grafana">
</p>

## Overview

An end-to-end enterprise IT infrastructure project covering the design, physical deployment, configuration, integration, and monitoring of a simulated corporate network.

The environment combines physical networking equipment, structured cabling, workstations, Linux servers, containerized applications, network security, and centralized monitoring through a Network Operations Center (NOC).

The objective is to document the implementation of an enterprise-style infrastructure, from its physical components to its daily administration and monitoring.

## Project Scope

### 1. Physical Infrastructure

- Network rack assembly and organization.
- Structured cabling and manual Ethernet cable termination.
- Patch panel installation and cable management.
- Power distribution and physical equipment organization.
- Workstation assembly and hardware inventory.

### 2. Enterprise Networking

- Cisco Catalyst C8200L router.
- Cisco Catalyst 9200L switch.
- VLAN segmentation across seven logical networks.
- Routing, access control, and network connectivity.
- Corporate wireless networking.
- Dedicated IoT network with smart devices.

### 3. Linux Servers & Containerization

- Linux server administration.
- Docker and Docker Compose.
- Container management with Portainer.
- Network services and internal DNS.
- Web services and reverse proxy configuration.
- Service integration and persistent storage.

### 4. Network Operations Center

- Centralized monitoring with Zabbix.
- Infrastructure visualization with Grafana.
- Service availability monitoring with Uptime Kuma.
- Cisco equipment monitoring through SNMP.
- Monitoring dashboards and network telemetry.
- Troubleshooting and operational diagnostics.

### 5. Additional Infrastructure Services

- IP telephony with Asterisk PBX.
- RADIUS-based network access control.
- Corporate Wi-Fi infrastructure.
- IoT connectivity and smart device integration.

Configuration details and implementation evidence will be documented as they become available and are verified.

## Infrastructure Cost Analysis

The project also includes a financial analysis of the infrastructure, considering three scenarios:

| Scenario | Description |
|---|---|
| **A — From Scratch** | Acquisition of equipment, physical infrastructure, installation, and configuration. |
| **B — Existing Equipment** | Deployment and configuration using hardware already owned by the organization. |
| **C — Operations & Maintenance** | Recurring costs associated with maintaining and operating the infrastructure. |

Cost estimates will be based on documented assumptions, equipment specifications, and market references.

## Project Objectives

- Build and document an enterprise-style IT infrastructure.
- Apply networking and Linux administration concepts in a physical environment.
- Integrate infrastructure services and monitoring platforms.
- Develop practical troubleshooting and operational skills.
- Produce technical documentation, diagrams, and implementation evidence.
- Analyze the resources and costs involved in infrastructure deployment.

## My Contributions

My primary hands-on contributions include the deployment and integration of containerized services, development of monitoring dashboards, and troubleshooting of infrastructure and monitoring issues.

The repository documents the broader laboratory environment while distinguishing individual implementation work from other project components.

## Development Status

**Status:** Active Development  
**Documentation:** In Progress  
**Laboratory Development Period:** Through November 17, 2026

This repository is being developed incrementally.

Technical documentation, configuration examples, diagrams, implementation evidence, and financial analysis will be added as the project evolves.

The laboratory environment is used for educational and technical demonstration purposes. It does not represent a production deployment.

---

**Enterprise infrastructure, from physical deployment to network operations.**
