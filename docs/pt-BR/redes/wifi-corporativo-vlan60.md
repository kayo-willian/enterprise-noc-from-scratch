# Wi-Fi Corporativo — VLAN 60

> **Projeto:** Enterprise NOC — From Scratch  
> **Ambiente:** Laboratório físico de redes corporativas  
> **Segmento:** VLAN 60 — Wi-Fi Corporativo  
> **Equipamento identificado:** TP-Link Archer AX53 (Wi-Fi 6 AX3000)  
> **Datas das evidências:** 04 e 06 de novembro de 2026  
> **Documentação atualizada:** 09 de novembro de 2026  
> **Situação:** Equipamento identificado; configuração wireless e integração pendentes de verificação

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
| Função pretendida | Conectividade Wi-Fi corporativa |
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
| Configuração do roteador | Não verificada de forma independente |

O registro comprova a atribuição da VLAN no momento da coleta da configuração do switch.

Entretanto, não comprova isoladamente que o TP-Link identificado estava fisicamente conectado a essa interface durante as fotografias de 06/11/2026.

O modo de operação e a configuração de uplink do equipamento também permanecem sem verificação.

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

Consequentemente, o comportamento DHCP, a utilização de NAT, o endereçamento dos clientes wireless e a associação efetiva à VLAN precisam de confirmação adicional.

## 5. Política de Segurança Pretendida

O modelo de segurança pretendido restringe a comunicação entre dispositivos conectados ao Wi-Fi corporativo e os demais segmentos internos.

O acesso administrativo deve permanecer limitado aos equipamentos e serviços autorizados.

Comunicações necessárias entre a VLAN 60 e os serviços internos precisam ser explicitamente definidas conforme os requisitos da infraestrutura.

Essas restrições representam requisitos de arquitetura.

**As evidências disponíveis não confirmam que ACLs ou regras de firewall correspondentes estejam efetivamente aplicadas.**

## 6. Autenticação e FreeRADIUS

O laboratório possui um serviço FreeRADIUS documentado separadamente, hospedado na VLAN 50.

A existência desse serviço não comprova, por si só, que a rede wireless corporativa utilize autenticação RADIUS.

As seguintes informações permanecem sem confirmação:

- Método de autenticação wireless configurado.
- Compatibilidade do hardware e firmware do Archer AX53 com a integração de autenticação pretendida.
- Existência de um cliente RADIUS configurado na infraestrutura wireless.
- Comunicação efetiva entre o equipamento e o servidor FreeRADIUS.
- Realização de testes de autenticação de clientes wireless.

Caso a autenticação corporativa seja implementada, as capacidades do equipamento e o fluxo de autenticação deverão ser verificados antes de documentar essa integração como operacional.

Nenhuma senha wireless, credencial de autenticação ou segredo compartilhado RADIUS é publicado neste repositório.

## 7. Monitoramento e Diagnóstico

As evidências disponíveis documentam o monitoramento dos principais equipamentos Cisco por meio de Zabbix e Grafana.

Entretanto, não comprovam o monitoramento direto do TP-Link Archer AX53.

As verificações futuras poderão incluir:

| Área | Objetivo da verificação |
|---|---|
| Conectividade física | Confirmar a interface do switch utilizada pelo equipamento wireless |
| VLAN | Confirmar a configuração operacional da interface e da VLAN |
| Modo de operação | Identificar se o equipamento funciona como ponto de acesso ou roteador |
| Endereçamento IP | Identificar a sub-rede, o gateway e a origem do DHCP dos clientes |
| Autenticação | Identificar os mecanismos de segurança e autenticação configurados |
| Isolamento | Validar as restrições pretendidas entre as VLANs |
| Monitoramento | Identificar possíveis métricas coletadas dos equipamentos ou clientes wireless |

Essas atividades representam verificações pendentes, não testes operacionais já concluídos.

## 8. Limitações Conhecidas

As evidências disponíveis não permitem confirmar:

1. Configuração ativa dos SSIDs.
2. Parâmetros de criptografia e autenticação.
3. Modo de operação efetivo do Archer AX53.
4. Conexão física entre o dispositivo identificado e a interface `Gi1/0/15`.
5. Funcionamento dos serviços DHCP e NAT.
6. Aplicação efetiva do isolamento entre VLANs.
7. Autenticação bem-sucedida utilizando FreeRADIUS.
8. Monitoramento direto do equipamento wireless.

Essas limitações são mantidas para diferenciar a identificação física do equipamento das configurações efetivamente validadas.

## 9. Documentação Relacionada

- [Roteador Cisco Catalyst C8200L](roteador-c8200l.md)
- [Registro do switch Cisco Catalyst C9200L](registro-switch-vlans-2026-11-04.md)
- [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
- [Serviços Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)

---

**Princípio da documentação:** As evidências identificam o equipamento wireless e a atribuição da VLAN registrada no switch. Elas não comprovam a configuração operacional completa nem a aplicação efetiva das políticas de segurança pretendidas.
