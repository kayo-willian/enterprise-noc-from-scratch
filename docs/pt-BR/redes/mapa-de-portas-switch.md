# Cisco Catalyst 9200L — Mapeamento de Portas

**[English](../../networking/switch-port-map.md) | Português (Brasil)**

## Visão Geral

Este documento apresenta o mapeamento preliminar das interfaces do switch Cisco Catalyst 9200L utilizado no projeto Enterprise NOC — Do Zero.

O equipamento conecta estações de trabalho dos departamentos, servidores de infraestrutura, dispositivos de telefonia IP e equipamentos de redes sem fio.

**Equipamento:** Cisco Catalyst 9200L  
**Referência:** Relatório técnico de implantação — 4 de novembro de 2026  
**Status:** Mapeamento preliminar — aguardando verificação final

## Inventário de Interfaces

| Interface | Segmento ou Equipamento | VLAN Prevista | Configuração |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | 10–70 | Trunk |
| Gi1/0/2–3 | TI e Monitoramento | 10 | Access |
| Gi1/0/4–6 | Contabilidade | 20 | Access |
| Gi1/0/7–8 | Financeiro | 30 | Access |
| Gi1/0/9–10 | Vendas | 40 | Access |
| Gi1/0/11 | Servidor Debian — VoIP e RADIUS | 50 | Access |
| Gi1/0/12–13 | Telefones IP Grandstream | 50 | A verificar |
| Gi1/0/14 | Intelbras — Rede IoT | 70 | A verificar |
| Gi1/0/15 | Intelbras — Wi-Fi Corporativo | 60 | A verificar |
| Gi1/0/16–24 | Livres / Reservadas | A verificar | A verificar |
| Gi1/1/1–4 | Interfaces SFP de Uplink | A verificar | A verificar |

**Importante:** Este inventário combina as descrições das interfaces presentes no relatório de 4 de novembro com o projeto de VLANs corrigido. Não representa uma configuração em execução já verificada.

## VLAN 60 e VLAN 70 — Verificação Pendente

O relatório original apresenta uma inconsistência na atribuição das VLANs relacionadas às redes sem fio e IoT.

A segmentação prevista atualmente é:

- **VLAN 60:** Wi-Fi Corporativo.
- **VLAN 70:** Rede IoT.

As atribuições físicas das interfaces Gi1/0/14 e Gi1/0/15 deverão ser verificadas diretamente na configuração do switch.

## Verificação das Configurações

Os seguintes comandos de consulta do Cisco IOS-XE podem ser utilizados:

```text
show interfaces status
show vlan brief
show interfaces trunk
show interfaces switchport
show running-config interface GigabitEthernet1/0/14
show running-config interface GigabitEthernet1/0/15
```

A verificação deverá confirmar:

- Estado operacional das interfaces.
- Configuração das portas access e trunk.
- VLANs efetivamente atribuídas.
- VLANs permitidas nos trunks.
- Equipamentos conectados e descrições das interfaces.
- Divergências entre a documentação e a configuração em execução.

## Status da Documentação

**Status:** Em andamento

Este documento será atualizado após a verificação das conexões físicas e das configurações do switch.

Informações sensíveis serão removidas dos exemplos de configuração destinados ao repositório público.
