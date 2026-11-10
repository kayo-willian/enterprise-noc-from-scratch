# Cisco Catalyst C8200L — Arquitetura e Evidências do Roteador

> **Projeto:** Enterprise NOC — From Scratch  
> **Ambiente:** Laboratório físico de redes corporativas  
> **Equipamento:** Cisco Catalyst C8200L-1N-4T  
> **Período das evidências:** 04 a 06 de novembro de 2026  
> **Documentação atualizada:** 08 de novembro de 2026  
> **Registro:** Equipamento físico, trunk no switch, funções da rede e evidências de monitoramento

## 1. Visão Geral

O Cisco Catalyst C8200L desempenha o papel de roteador central na arquitetura do laboratório Enterprise NOC.

A infraestrutura combina um roteador Cisco físico, um switch Catalyst C9200L, VLANs departamentais, servidores Linux, estações Windows e plataformas de monitoramento.

Este documento reúne as evidências disponíveis sobre o papel do roteador, endereçamento, monitoramento e projeto de segmentação.

**Escopo do registro:** Esta página consolida evidências datadas da arquitetura e do equipamento, não uma exportação da configuração em execução do roteador.

## 2. Infraestrutura Física

O roteador está instalado no rack de rede do laboratório, juntamente com o switch Cisco Catalyst C9200L e a infraestrutura de cabeamento estruturado.

As fotografias disponíveis identificam o equipamento como **Cisco Catalyst C8200L-1N-4T**.

![Roteador Cisco, switch e patch panel](../../assets/images/physical/cisco-router-switch-patch-panel.jpg)

A configuração do switch coletada em 04/11/2026 identifica a interface `Gi1/0/1` como trunk associado à interligação com o roteador.

Essa evidência é compatível com a arquitetura documentada, mas não comprova isoladamente a configuração da interface física correspondente ou das subinterfaces VLAN do roteador.

O registro do switch identifica `Gi1/0/1` no C9200L como uplink para o roteador; a interface correspondente do C8200L não é nomeada nesse registro.

## 3. Segmentação da Rede

O laboratório possui sete VLANs documentadas.

| VLAN | Função | Evidência |
|---|---|---|
| 10 | TI / NOC / Administração | Configuração do switch e registros dos computadores |
| 20 | Contabilidade | Configuração do switch e registros dos computadores |
| 30 | Financeiro | Configuração do switch e registros dos computadores |
| 40 | Vendas | Configuração do switch e registros dos computadores |
| 50 | VoIP / Asterisk / FreeRADIUS | Configuração do switch e registros do servidor |
| 60 | Wi-Fi corporativo | Registro de configuração do switch |
| 70 | IoT | Registro de configuração do switch |

O registro do switch de 04/11/2026 apresenta a distribuição das VLANs e a interface trunk voltada ao roteador.

**Limitação da evidência:** A existência das VLANs e suas atribuições no switch não comprovam, isoladamente, o funcionamento do roteamento entre redes nem a aplicação efetiva das políticas de controle de acesso.

## 4. Endereçamento IP Observado

As fotografias dos computadores coletadas em 06/11/2026 apresentam configurações IP com os seguintes gateways padrão.

| VLAN | Gateway observado | Origem da evidência |
|---|---|---|
| 10 | `192.168.10.1` | Configuração IP de estação da TI |
| 20 | `192.168.20.1` | Configuração IP de estações da Contabilidade |
| 30 | `192.168.30.1` | Configuração IP de estações do Financeiro |
| 40 | `192.168.40.1` | Configuração IP de estações de Vendas |

Os registros técnicos de 04/11/2026 também associam o endereço `192.168.10.1` ao roteador.

Essas informações demonstram os gateways configurados nas estações no momento da coleta.

Entretanto, não confirmam isoladamente a configuração das subinterfaces do C8200L, a propriedade de todos os gateways ou a comunicação efetiva entre departamentos.

## 5. Modelo de Segmentação e Controle de Acesso

O modelo de segmentação documentado diferencia a rede administrativa de TI/NOC das redes departamentais, sem fio e IoT.

### Acesso administrativo

A VLAN 10 é destinada à administração e ao monitoramento.

O projeto de controle de acesso prevê que sistemas administrativos autorizados iniciem conexões de gerenciamento com serviços e equipamentos de outras VLANs, quando necessário.

### Isolamento departamental

O projeto de controle de acesso separa as VLANs 20, 30 e 40, exceto quando houver comunicação explicitamente autorizada para determinados serviços.

### Telefonia e autenticação

A VLAN 50 hospeda o servidor documentado de Asterisk e FreeRADIUS.

O acesso aos serviços dessa rede deve respeitar as necessidades das aplicações e dos equipamentos autorizados.

### Isolamento de Wi-Fi e IoT

O projeto de controle de acesso prevê acesso restrito para as VLANs 60 e 70 aos recursos internos da infraestrutura corporativa.

Exceções necessárias, incluindo a comunicação entre um ponto de acesso Wi-Fi e o servidor FreeRADIUS, precisam considerar os endereços de origem reais e os serviços utilizados.

**Escopo do registro:** As regras apresentadas são requisitos do projeto de acesso, não uma transcrição das ACLs do roteador.

O material histórico contém a configuração das VLANs no switch, mas não inclui exportação das ACLs do roteador nem testes registrados dessas regras.

## 6. Monitoramento do Roteador

O roteador aparece no ambiente de monitoramento do laboratório, utilizando Zabbix e Grafana.

As evidências coletadas apresentam informações de disponibilidade e métricas relacionadas às interfaces de rede.

### Grafana — Dashboard do Roteador

![Monitoramento do roteador — Parte 1](../../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

![Monitoramento do roteador — Parte 2](../../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

As capturas demonstram informações disponibilizadas pelo monitoramento durante o período de coleta.

Elas não comprovam disponibilidade contínua, cobertura integral das interfaces ou funcionamento correto de todas as configurações de roteamento e segurança.

O inventário de hosts do Zabbix também apresenta evidência de uma interface de monitoramento SNMP associada ao roteador.

As métricas do Zabbix/Grafana registram o monitoramento do roteador; uma exportação da configuração SNMP do próprio C8200L não integra o material coletado.

## 7. DHCP, NAT e Conectividade Externa

As estações do laboratório utilizam DHCP. Os gateways das VLANs 10, 20, 30 e 40 foram registrados nas capturas das estações em 06/11/2026, não em uma exportação da configuração atual do roteador. A coleta não identifica qual equipamento atende ou retransmite DHCP, os pools, traduções NAT, interface externa ou rota padrão do C8200L. Nenhum comando correspondente é apresentado como implantado.

## 8. Escopo do Registro do Roteador

A página documenta o C8200L físico, o trunk no lado do switch (Gi1/0/1), o projeto de VLANs, os gateways observados nas estações e os registros de Zabbix/Grafana relacionados ao roteador. Não atribui nome à interface física do lado do C8200L nem afirma conhecer as subinterfaces dot1Q. A seção de controle de acesso descreve a política lógica, não o conteúdo ou a aplicação efetiva de ACLs.

As capturas registram estados de monitoramento no momento da coleta, sem representar garantia de disponibilidade contínua ou cópia integral da configuração do roteador.

## 10. Documentação Relacionada

- [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
- [Registro do switch Cisco e das VLANs](registro-switch-vlans-2026-11-04.md)
- [Inventário dos computadores](../estacoes/inventario-de-computadores.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)

