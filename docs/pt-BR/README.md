# Documentação Técnica

**Enterprise NOC — From Scratch**

[English](../README.md) | **Português (Brasil)**

Índice da documentação de arquitetura, infraestrutura física, serviços, monitoramento, operações NOC e análise de custos da infraestrutura.

## Arquitetura e Redes

- [Visão geral da infraestrutura](arquitetura/visao-geral-da-infraestrutura.md)
- [Visão geral de redes](redes/README.md)
- [Topologia lógica](redes/topologia-logica-consolidada.md)
- [Segmentação por VLANs](redes/vlans.md)
- [Roteador Cisco C8200L](redes/roteador-c8200l.md)
- [Mapa de portas do C9200L](redes/mapa-de-portas-switch.md)
- [Registro de configuração do C9200L](redes/registro-switch-vlans-2026-11-04.md)
- [Wi-Fi corporativo — VLAN 60](redes/wifi-corporativo-vlan60.md)
- [Rede IoT — VLAN 70](redes/iot-vlan70.md)

## Infraestrutura Física e Evidências

- [Rack, equipamentos e cabeamento](evidencias/infraestrutura-fisica.md)
- [Coleta de evidências — 6 de novembro de 2026](evidencias/registro-coleta-2026-11-06.md)
- [Inventário de computadores e servidores](estacoes/inventario-de-computadores.md)

## Monitoramento e Observabilidade

- [Monitoramento Zabbix](monitoramento/zabbix.md)
- [Dashboards Grafana](monitoramento/grafana.md)
- [Diagnóstico SNMP do C9200L](monitoramento/diagnostico-snmp.md)

## Linux, Containers e Serviços de Infraestrutura

- [Docker, Compose e containers](containers/servicos-docker.md)
- [Asterisk e FreeRADIUS](servicos/asterisk-freeradius.md)
- [Filtragem DNS e disponibilidade](servicos/dns-e-disponibilidade.md)

## Operações NOC e Diagnóstico

- [Gerenciamento de incidentes](operacoes-noc/gerenciamento-de-incidentes.md)
- [Exercícios de incidentes e validação da recuperação](operacoes-noc/simulacao-e-validacao-de-incidentes.md)
- [Runbook de interfaces Cisco](operacoes-noc/runbooks/interface-cisco-indisponivel.md)
- [Runbook de resolução DNS](operacoes-noc/runbooks/falhas-resolucao-dns.md)
- [Runbook de serviços Docker](operacoes-noc/runbooks/falhas-servicos-docker.md)
- [Runbook de painéis Grafana sem dados](operacoes-noc/runbooks/grafana-sem-dados.md)
- [Runbook de recursos dos sistemas](operacoes-noc/runbooks/utilizacao-recursos-sistema.md)
- [Runbook de conectividade do Zabbix Agent](operacoes-noc/runbooks/conectividade-zabbix-agent.md)

## Análise de Custos da Infraestrutura

- [Análise de custos completa — Português (BRL)](custos/enterprise-noc-orcamento-final-brl-2026.md)
- [Planilha financeira — Português (BRL)](custos/enterprise-noc-orcamento-final-brl-2026.xlsx)
- [Análise de custos completa — English (USD)](../costs/enterprise-noc-final-budget-usd-2026.md)
- [Planilha financeira — English (USD)](../costs/enterprise-noc-final-budget-usd-2026.xlsx)

## Referências do Projeto e Site Público

- [Perguntas frequentes técnicas](faq/perguntas-frequentes.md)
- [Arquitetura e manutenção do site](site/README.md)

## Arquivos de Configuração

- [Docker Compose](../../docker_configs/docker-compose.yml)
- [Compose do Pi-hole](../../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Compose do Portainer](../../docker_configs/lab-ti/portainer/docker-compose.yml)
- [Proxy reverso Nginx](../../docker_configs/reverse-proxy/conf.d/lab.conf)

## Recursos Complementares

- [Site público](index.html)
- [README principal](../../README.pt-BR.md)
