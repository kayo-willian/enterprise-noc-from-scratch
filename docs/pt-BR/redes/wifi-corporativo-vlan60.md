# Wi-Fi Corporativo — VLAN 60

> **Projeto:** Enterprise NOC — From Scratch  
> **Ambiente:** Laboratório físico de redes corporativas  
> **Segmento:** VLAN 60 — Wi-Fi Corporativo  
> **Equipamento identificado:** TP-Link Archer AX53 (Wi-Fi 6 AX3000)  
> **Datas das evidências:** 04 e 06 de novembro de 2026  
> **Documentação atualizada:** 09 de novembro de 2026  
> **Registro:** Equipamento físico e VLAN do switch documentados em 04–06/11/2026

## 1. Visão Geral

O laboratório Enterprise NOC possui um segmento de rede destinado à conectividade sem fio corporativa.

A VLAN 60 foi designada para o Wi-Fi corporativo, permitindo a separação lógica dessa rede em relação às estações departamentais, à infraestrutura administrativa, aos serviços de telefonia e aos dispositivos IoT.

As evidências disponíveis identificam um **TP-Link Archer AX53** como equipamento associado à rede wireless corporativa.

Este documento reúne as informações identificadas sobre o equipamento, a configuração registrada no switch e a arquitetura de rede pretendida.

Não se presume que a autenticação wireless, o roteamento ou as restrições de segurança tenham sido integralmente implementados.

## 2. Identificação do Equipamento

Uma fotografia coletada em 06/11/2026 permitiu identificar o equipamento abaixo.

| Característica | Identificação |
|---|---|
| Fabricante | TP-Link |
| Modelo | Archer AX53 |
| Geração wireless | Wi-Fi 6 |
| Classe do produto | AX3000 |
| Função na rede | Conectividade Wi-Fi corporativa |
| Segmento associado | VLAN 60 |
| Modo de operação | Não verificado |
| Configuração ativa de segurança | Não verificada |

O equipamento foi identificado por evidência física, não por suposição baseada no inventário.

A fotografia original contém informações sensíveis, incluindo credenciais wireless e identificadores exclusivos do equipamento. Por esse motivo, ela não foi incluída nesta documentação pública.

## 3. Integração com o Switch

O registro de configuração do Cisco Catalyst C9200L, coletado em 04/11/2026, associa a interface `Gi1/0/15` à VLAN 60.

| Componente | Informação documentada |
|---|---|
| Switch | Cisco Catalyst C9200L |
| Interface | `Gi1/0/15` |
| VLAN atribuída | 60 |
| Finalidade | Wi-Fi corporativo |
| Roteador | Cisco Catalyst C8200L |
| Conexão do equipamento | Rede wireless associada à VLAN 60 |

O registro comprova a atribuição da VLAN no momento da coleta da configuração do switch.

O registro datado identifica a atribuição da VLAN no switch. O modo operacional e os parâmetros de uplink do equipamento wireless não constam das configurações coletadas.

## 4. Arquitetura da Rede

A arquitetura pretendida estabelece um segmento independente para a conectividade wireless corporativa.

A infraestrutura diferencia:

- VLAN 10 — Administração de TI e NOC.
- VLANs 20–40 — Estações dos departamentos.
- VLAN 50 — Telefonia e serviços de autenticação.
- VLAN 60 — Wi-Fi corporativo.
- VLAN 70 — Dispositivos IoT.

O registro do switch documenta a VLAN 60 como segmento dedicado.

Porém, não permite determinar se o Archer AX53 estava operando em modo access point, roteador ou outra modalidade compatível.

A fotografia e a captura do switch não incluem os parâmetros de DHCP, NAT, endereçamento dos clientes ou modo de operação do roteador wireless.

## 5. Segmentação e Controle de Acesso

A VLAN 60 corresponde ao Wi-Fi corporativo, separado das redes departamentais e da VLAN 70 (IoT). O projeto lógico restringe a comunicação não autorizada entre VLANs e prevê exceções para serviços internos necessários. A configuração da porta do switch demonstra a segmentação, mas não equivale a um teste de aplicação das ACLs.

## 6. Autenticação e Serviços

O FreeRADIUS integra o servidor Linux documentado na VLAN 50. A existência desse serviço não demonstra que o Archer AX53 esteja utilizando RADIUS para autenticar clientes Wi-Fi. Os registros de 04–06/11 não incluem configuração de SSID, criptografia, endereçamento dos clientes, DHCP, NAT ou modo operacional do equipamento wireless; esses detalhes não são atribuídos à implantação.

## 7. Monitoramento

Os registros do Zabbix e Grafana documentam o monitoramento da infraestrutura Cisco. As capturas coletadas não apresentam monitoramento direto do Archer AX53. Por isso, o equipamento wireless é descrito como componente da rede, não como alvo de monitoramento comprovado.

## 8. Escopo do Registro

Esta página reúne a identificação do TP-Link Archer AX53, a função da VLAN 60 e a atribuição registrada no switch C9200L. Não são atribuídos ao laboratório testes de clientes wireless, autenticações RADIUS ou regras ACL/firewall que não constam das evidências.

## 9. Documentação Relacionada

- [Roteador Cisco Catalyst C8200L](roteador-c8200l.md)
- [Rede IoT — VLAN 70](iot-vlan70.md)
- [Registro do switch Cisco Catalyst C9200L](registro-switch-vlans-2026-11-04.md)
- [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
- [Serviços Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)

