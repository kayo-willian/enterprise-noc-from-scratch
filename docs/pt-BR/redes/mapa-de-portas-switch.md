# Cisco Catalyst 9200L — Mapeamento de Portas

**[English](../../networking/switch-port-map.md) | Português (Brasil)**

## Visão Geral

Este documento apresenta o mapeamento histórico das interfaces do switch Cisco Catalyst 9200L utilizado no projeto Enterprise NOC — Do Zero.

O equipamento conecta estações de trabalho dos departamentos, servidores de infraestrutura, dispositivos de telefonia IP e equipamentos de redes sem fio.

**Equipamento:** Cisco Catalyst 9200L  
**Referência:** Relatório técnico de implantação — 4 de novembro de 2026  
**Escopo:** Captura de configuração de 04/11/2026; não representa o estado atual dos enlaces

## Inventário de Interfaces

| Interface | Segmento ou Equipamento | VLAN Prevista | Configuração |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | 10–70 | Trunk |
| Gi1/0/2–3 | TI e Monitoramento | 10 | Access |
| Gi1/0/4–6 | Contabilidade | 20 | Access |
| Gi1/0/7–8 | Financeiro | 30 | Access |
| Gi1/0/9–10 | Vendas | 40 | Access |
| Gi1/0/11 | Servidor Debian — VoIP e RADIUS | 50 | VLAN 50 atribuída conforme configuração registrada |
| Gi1/0/12–13 | Telefones IP Grandstream | 50 | Access VLAN 50 |
| Gi1/0/14 | TP-Link Archer AX53 — Rede IoT | 70 | Access VLAN 70 |
| Gi1/0/15 | TP-Link Archer AX53 — Wi-Fi Corporativo | 60 | Access VLAN 60 |
| Gi1/0/16–24 | Sem equipamento identificado na captura | — | Sem comandos específicos registrados |
| Gi1/1/1–4 | Interfaces SFP | — | Sem comandos específicos registrados |

**Importante:** Este inventário combina as descrições das interfaces presentes no relatório de 4 de novembro com o projeto de VLANs corrigido. Não representa uma configuração em execução já verificada.

## VLAN 60 e VLAN 70

O registro do switch de 04/11/2026 atribui Gi1/0/14 à VLAN 70 e Gi1/0/15 à VLAN 60. São configurações registradas, não testes dos enlaces físicos.

## Escopo do Mapeamento

Gi1/0/1 está configurada como trunk. Gi1/0/2–10 e Gi1/0/12–15 possuem VLANs de acesso documentadas. A interface Gi1/0/11 registra `switchport access vlan 50` e `spanning-tree portfast trunk`, sem `switchport mode access` explícito; não é possível determinar o modo operacional apenas pela captura.

A ausência de comandos específicos para Gi1/0/16–24 e Gi1/1/1–4 não comprova que as portas estavam livres, desconectadas ou desabilitadas. Este é um inventário de configuração histórica, não um relatório do estado atual dos enlaces.
