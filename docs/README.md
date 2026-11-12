# Technical Documentation

**Enterprise NOC — From Scratch**

**English** | [Português (Brasil)](pt-BR/README.md)

Documentation index for architecture, physical infrastructure, services, monitoring, NOC operations and infrastructure cost analysis.

## Architecture and Networking

- [Infrastructure overview](architecture/infrastructure-overview.md)
- [Networking overview](networking/README.md)
- [Logical topology](networking/consolidated-logical-topology.md)
- [VLAN segmentation](networking/vlans.md)
- [Cisco C8200L router](networking/router-c8200l.md)
- [C9200L port map](networking/switch-port-map.md)
- [C9200L configuration snapshot](networking/switch-vlan-snapshot-2026-11-04.md)
- [Corporate Wi-Fi — VLAN 60](networking/corporate-wifi-vlan60.md)
- [IoT network — VLAN 70](networking/iot-vlan70.md)

## Physical Infrastructure and Evidence

- [Rack, equipment and cabling](evidence/physical-infrastructure.md)
- [Evidence collection — November 6, 2026](evidence/evidence-collection-2026-11-06.md)
- [Computer and server inventory](endpoints/workstation-inventory.md)

## Monitoring and Observability

- [Zabbix monitoring](monitoring/zabbix-monitoring.md)
- [Grafana dashboards](monitoring/grafana-monitoring.md)
- [C9200L SNMP troubleshooting](monitoring/snmp-troubleshooting.md)

## Linux, Containers and Infrastructure Services

- [Docker, Compose and containers](containers/docker-services.md)
- [Asterisk and FreeRADIUS](services/asterisk-freeradius.md)
- [DNS filtering and availability](services/dns-and-availability.md)

## NOC Operations and Troubleshooting

- [Incident management](noc-operations/incident-management.md)
- [Incident exercises and recovery validation](noc-operations/incident-simulation-and-validation.md)
- [Cisco interface runbook](noc-operations/runbooks/cisco-interface-unavailable.md)
- [DNS resolution runbook](noc-operations/runbooks/dns-resolution-failure.md)
- [Docker service runbook](noc-operations/runbooks/docker-service-failure.md)
- [Grafana no-data runbook](noc-operations/runbooks/grafana-no-data.md)
- [System resource runbook](noc-operations/runbooks/host-resource-utilization.md)
- [Zabbix Agent connectivity runbook](noc-operations/runbooks/zabbix-agent-connectivity.md)

## Infrastructure Cost Analysis

- [Full cost analysis — English (USD)](costs/enterprise-noc-final-budget-usd-2026.md)
- [Financial spreadsheet — English (USD)](costs/enterprise-noc-final-budget-usd-2026.xlsx)
- [Full cost analysis — Português (BRL)](pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.md)
- [Financial spreadsheet — Português (BRL)](pt-BR/custos/enterprise-noc-orcamento-final-brl-2026.xlsx)

## Project Reference and Public Website

- [Technical FAQ](faq/technical-faq.md)
- [Website architecture and maintenance](site/README.md)

## Configuration Files

- [Docker Compose](../docker_configs/docker-compose.yml)
- [Pi-hole Compose](../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Portainer Compose](../docker_configs/lab-ti/portainer/docker-compose.yml)
- [Nginx reverse proxy](../docker_configs/reverse-proxy/conf.d/lab.conf)

## Additional Resources

- [Public website](index.html)
- [Root README](../README.md)
