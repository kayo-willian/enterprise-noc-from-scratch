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

## Contexto Empresarial — Tapajós Inovações

O **Enterprise NOC — From Scratch** é um projeto de infraestrutura de redes corporativas desenvolvido a partir do cenário de uma empresa fictícia chamada **Tapajós Inovações**.

A empresa representa o cliente simulado de uma iniciativa de modernização de redes, fornecendo o contexto empresarial para o planejamento, a implementação e a documentação de um Centro de Operações de Rede (NOC).

### O Desafio Empresarial

O cenário empresarial fictício da Tapajós Inovações apresenta quatro desafios de infraestrutura:

- **Cabeamento estruturado sem certificação:** Problemas físicos de conectividade e interrupções frequentes na comunicação.
- **Rede sem fio desprotegida:** Ambiente Wi-Fi aberto e sem controle adequado de acesso.
- **Telefonia IP instável:** Interrupções recorrentes nas comunicações internas por VoIP.
- **Ausência de monitoramento centralizado:** Visibilidade limitada sobre o desempenho da infraestrutura, a disponibilidade dos serviços e os incidentes operacionais.

Esses problemas representam o cenário empresarial inicial, não necessariamente o estado atual do laboratório.

### A Solução Proposta

O projeto busca desenvolver e documentar uma infraestrutura corporativa integrada, incluindo:

- Roteamento Cisco Catalyst C8200L e comutação Cisco Catalyst C9200L.
- Segmentação por VLANs, com acesso administrativo centralizado e isolamento dos setores.
- Segmentos dedicados às redes Wi-Fi corporativa e IoT.
- Infraestrutura e serviços baseados em Linux.
- Telefonia IP com Asterisk e autenticação de rede com FreeRADIUS.
- Serviços em containers administrados por Docker e Docker Compose.
- Monitoramento centralizado utilizando Zabbix, Grafana e Uptime Kuma.
- Filtragem DNS e gerenciamento de serviços internos com Pi-hole.
- Documentação técnica, inventários da infraestrutura e evidências operacionais.

### Escopo do Projeto

**A Tapajós Inovações é uma empresa fictícia.** O projeto é desenvolvido em um laboratório físico de treinamento, utilizando equipamentos reais de rede, servidores Linux, estações Windows e serviços de infraestrutura implantados.

Este repositório documenta a infraestrutura desenvolvida para esse cenário, incluindo sua implementação, evidências coletadas, limitações e melhorias em andamento.

O objetivo é demonstrar conhecimentos práticos em engenharia de redes, administração Linux, monitoramento de infraestrutura, diagnóstico de problemas e documentação técnica por meio de um laboratório corporativo integrado.

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

O registro de implementação está organizado por capturas de configuração datadas, inventário de equipamentos e evidências de monitoramento.

## Análise de Custos da Infraestrutura

O projeto também contempla uma análise financeira da infraestrutura, considerando três cenários:

| Cenário | Descrição |
|---|---|
| **A — Implantação do Zero** | Aquisição dos equipamentos, infraestrutura física, instalação e configuração. |
| **B — Equipamentos Existentes** | Implantação e configuração utilizando equipamentos já pertencentes à organização. |
| **C — Operação e Manutenção** | Custos recorrentes necessários para manter e administrar a infraestrutura. |

A análise de custos é uma simulação financeira delimitada por premissas e referências de mercado; subtotais parciais não representam valores efetivamente gastos.

## Objetivos do Projeto

- Construir e documentar uma infraestrutura de TI de padrão corporativo.
- Aplicar conhecimentos de redes e administração Linux em um ambiente físico.
- Integrar serviços de infraestrutura e plataformas de monitoramento.
- Desenvolver competências práticas de diagnóstico e operação.
- Produzir documentação técnica, diagramas e evidências de implementação.
- Analisar os recursos e custos envolvidos na implantação da infraestrutura.

## Documentação Técnica

- [Arquitetura](docs/pt-BR/arquitetura/visao-geral-da-infraestrutura.md) · [VLANs](docs/pt-BR/redes/vlans.md) · [Configuração do switch](docs/pt-BR/redes/registro-switch-vlans-2026-11-04.md)
- [Roteador C8200L](docs/pt-BR/redes/roteador-c8200l.md) · [Wi-Fi corporativo](docs/pt-BR/redes/wifi-corporativo-vlan60.md) · [Mapa de portas](docs/pt-BR/redes/mapa-de-portas-switch.md)
- [Estações](docs/pt-BR/estacoes/inventario-de-computadores.md) · [Docker](docs/pt-BR/containers/servicos-docker.md)
- [Zabbix](docs/pt-BR/monitoramento/zabbix.md) · [Grafana](docs/pt-BR/monitoramento/grafana.md) · [Diagnóstico SNMP](docs/pt-BR/monitoramento/diagnostico-snmp.md)
- [Asterisk / FreeRADIUS](docs/pt-BR/servicos/asterisk-freeradius.md) · [Pi-hole / Uptime Kuma](docs/pt-BR/servicos/dns-e-disponibilidade.md) · [Infraestrutura física](docs/pt-BR/evidencias/infraestrutura-fisica.md)
- [Portal de documentação GitHub Pages](https://kayo-willian.github.io/enterprise-noc-from-scratch/pt-BR/)

### DHCP e registros de monitoramento

As estações do laboratório utilizam DHCP. Seus endereços IP podem variar entre as datas de coleta e os cadastros anteriores no Zabbix. Hosts indisponíveis e painéis `No data` nas capturas de 06/11 representam estados históricos de monitoramento; mudanças de endereço podem explicar parte das divergências, sem comprovar a causa de todos os alertas.

## Minhas Contribuições

Minhas principais contribuições práticas incluem a implantação e integração dos serviços conteinerizados, o desenvolvimento dos dashboards de monitoramento e a resolução de problemas relacionados à infraestrutura e à observabilidade.

O repositório documenta o ambiente completo do laboratório, diferenciando o trabalho de implementação individual dos demais componentes do projeto.

## Status de Desenvolvimento

**Status:** Em Desenvolvimento Ativo  
**Documentação:** Registros técnicos datados publicados  
**Período de Desenvolvimento do Laboratório:** Até 17 de novembro de 2026

Este repositório está sendo desenvolvido de forma incremental.

As configurações e capturas disponíveis são documentadas como observações históricas. Informações ausentes das evidências não são apresentadas como configurações implantadas ou testadas.

O ambiente é utilizado para fins educacionais e de demonstração técnica, não representando uma implantação em produção.

---

**Infraestrutura corporativa, da implantação física às operações de rede.**
