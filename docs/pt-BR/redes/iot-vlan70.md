# Rede IoT — VLAN 70

**Projeto:** Enterprise NOC — From Scratch  
**Segmento:** VLAN 70 — Internet das Coisas (IoT)  
**Equipamento de rede:** TP-Link Archer AX53 dedicado (Wi-Fi 6 AX3000)  
**Dispositivo conectado:** Amazon Alexa  
**Switch:** Cisco Catalyst C9200L  
**Registro:** 09/11/2026

## 1. Visão Geral

A VLAN 70 é o segmento dedicado aos dispositivos IoT do laboratório Enterprise NOC. Uma Amazon Alexa conecta-se por Wi-Fi a um TP-Link Archer AX53 separado, interligado por Ethernet ao switch Cisco Catalyst C9200L. O Wi-Fi corporativo da VLAN 60 utiliza outro Archer AX53; são dois equipamentos wireless físicos distintos.

## 2. Conectividade

```text
Amazon Alexa
    |
    | Wi-Fi
    v
TP-Link Archer AX53 — IoT
    |
    | Ethernet
    v
Cisco Catalyst C9200L
Gi1/0/14 — Access VLAN 70
    |
    | Trunk para o roteador: Gi1/0/1
    v
Cisco Catalyst C8200L
```

A configuração do switch de 04/11 registra `Gi1/0/14` em access VLAN 70 e `Gi1/0/1` como trunk para o roteador. A ligação wireless–switch e a associação da Alexa descrevem a topologia física do laboratório. O desenho não presume que o endereço IP da Alexa pertença diretamente à sub-rede da VLAN 70.

## 3. Segmentação da Rede

| VLAN | Segmento | Função |
|---|---|---|
| 60 | Wi-Fi corporativo | Conectividade wireless corporativa |
| 70 | IoT | Conectividade dedicada à Alexa e a dispositivos inteligentes |

A arquitetura separa os equipamentos IoT das redes administrativas e departamentais. A atribuição da VLAN consta do registro do switch; esse registro não comprova, por si só, a aplicação das ACLs do roteador.

## 4. Endereçamento IP e Modo de Operação

As evidências coletadas não incluem exportação de configuração do Archer AX53 IoT. Em modo access point, os clientes Wi-Fi podem participar diretamente da rede IP da VLAN 70. Em modo roteador com NAT, os clientes podem utilizar uma sub-rede independente atrás do equipamento.

O modo efetivo, endereço da Alexa, serviço DHCP, regras NAT e gateway da rede IoT não são atribuídos à implantação sem configuração correspondente. Esses parâmetros estão **fora do escopo da captura histórica**, e não representam tarefas editoriais abertas para concluir esta página.

## 5. Monitoramento

As capturas disponíveis apresentam a infraestrutura Cisco monitorada por Zabbix e Grafana. O inventário de monitoramento publicado não apresenta métricas diretas do Archer AX53 IoT ou da Alexa. A VLAN 70 é documentada conforme a segmentação lógica do switch e a conectividade IoT do laboratório.

## 6. Escopo das Evidências

A página reúne o registro datado da configuração do C9200L e o inventário dos equipamentos de rede. Descreve a ligação implantada e diferencia os detalhes presentes nas evidências dos parâmetros não incluídos nas exportações coletadas. SSIDs, senhas, segredos RADIUS e identificadores exclusivos não são publicados.

## Documentação Relacionada

- [Segmentação por VLANs](vlans.md)
- [Mapa de Portas do Switch](mapa-de-portas-switch.md)
- [Registro de Configuração do Switch](registro-switch-vlans-2026-11-04.md)
- [Roteador Cisco C8200L](roteador-c8200l.md)
- [Wi-Fi Corporativo — VLAN 60](wifi-corporativo-vlan60.md)
- [Infraestrutura Física](../evidencias/infraestrutura-fisica.md)
