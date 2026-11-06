# Enterprise NOC — Do Zero

**[English](README.md) | Português (Brasil)**

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

## Visão Geral

Projeto de infraestrutura corporativa de TI de ponta a ponta, abrangendo o planejamento, a implantação física, a configuração, a integração e o monitoramento de uma rede empresarial simulada.

O ambiente integra equipamentos físicos de rede, cabeamento estruturado, estações de trabalho, servidores Linux, aplicações conteinerizadas, segurança de redes e monitoramento centralizado por meio de um Centro de Operações de Rede (NOC).

O objetivo é documentar a implementação de uma infraestrutura de padrão corporativo, desde seus componentes físicos até sua administração e monitoramento.

## Escopo do Projeto

### 1. Infraestrutura Física

- Montagem e organização do rack de rede.
- Cabeamento estruturado e confecção manual de cabos Ethernet.
- Instalação do patch panel e organização dos cabos.
- Distribuição elétrica e organização física dos equipamentos.
- Montagem de computadores e inventário de hardware.

### 2. Redes Corporativas

- Roteador Cisco Catalyst C8200L.
- Switch Cisco Catalyst 9200L.
- Segmentação de rede em sete VLANs.
- Roteamento, controle de acesso e conectividade.
- Rede Wi-Fi corporativa.
- Rede IoT dedicada com dispositivos inteligentes.

### 3. Servidores Linux e Conteinerização

- Administração de servidores Linux.
- Docker e Docker Compose.
- Gerenciamento de containers com Portainer.
- Serviços de rede e DNS interno.
- Serviços web e configuração de proxy reverso.
- Integração de serviços e armazenamento persistente.

### 4. Centro de Operações de Rede (NOC)

- Monitoramento centralizado com Zabbix.
- Visualização da infraestrutura com Grafana.
- Monitoramento de disponibilidade com Uptime Kuma.
- Monitoramento de equipamentos Cisco via SNMP.
- Dashboards de monitoramento e telemetria de rede.
- Diagnóstico e resolução de problemas operacionais.

### 5. Serviços Adicionais de Infraestrutura

- Telefonia IP com Asterisk PBX.
- Controle de acesso à rede baseado em RADIUS.
- Infraestrutura Wi-Fi corporativa.
- Conectividade IoT e integração de dispositivos inteligentes.

Os detalhes das configurações e as evidências de implementação serão documentados conforme sua disponibilidade e verificação.

## Análise de Custos da Infraestrutura

O projeto também contempla uma análise financeira da infraestrutura, considerando três cenários:

| Cenário | Descrição |
|---|---|
| **A — Implantação do Zero** | Aquisição dos equipamentos, infraestrutura física, instalação e configuração. |
| **B — Equipamentos Existentes** | Implantação e configuração utilizando equipamentos já pertencentes à organização. |
| **C — Operação e Manutenção** | Custos recorrentes necessários para manter e administrar a infraestrutura. |

As estimativas serão fundamentadas em premissas documentadas, especificações dos equipamentos e referências de preços de mercado.

## Objetivos do Projeto

- Construir e documentar uma infraestrutura de TI de padrão corporativo.
- Aplicar conhecimentos de redes e administração Linux em um ambiente físico.
- Integrar serviços de infraestrutura e plataformas de monitoramento.
- Desenvolver competências práticas de diagnóstico e operação.
- Produzir documentação técnica, diagramas e evidências de implementação.
- Analisar os recursos e custos envolvidos na implantação da infraestrutura.

## Minhas Contribuições

Minhas principais contribuições práticas incluem a implantação e integração dos serviços conteinerizados, o desenvolvimento dos dashboards de monitoramento e a resolução de problemas relacionados à infraestrutura e à observabilidade.

O repositório documenta o ambiente completo do laboratório, diferenciando o trabalho de implementação individual dos demais componentes do projeto.

## Status de Desenvolvimento

**Status:** Em Desenvolvimento Ativo  
**Documentação:** Em Andamento  
**Período de Desenvolvimento do Laboratório:** Até 17 de novembro de 2026

Este repositório está sendo desenvolvido de forma incremental.

Documentações técnicas, exemplos de configuração, diagramas, evidências de implementação e análises financeiras serão adicionados conforme a evolução do projeto.

O ambiente é utilizado para fins educacionais e de demonstração técnica, não representando uma implantação em produção.

---

**Infraestrutura corporativa, da implantação física às operações de rede.**
