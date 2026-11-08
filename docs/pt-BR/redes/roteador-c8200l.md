# Cisco Catalyst C8200L — Arquitetura e Evidências do Roteador

> **Projeto:** Enterprise NOC — From Scratch  
> **Ambiente:** Laboratório físico de redes corporativas  
> **Equipamento:** Cisco Catalyst C8200L-1N-4T  
> **Período das evidências:** 04 a 06 de novembro de 2026  
> **Documentação atualizada:** 08 de novembro de 2026  
> **Situação:** Parcialmente documentado — validações pendentes

## 1. Visão Geral

O Cisco Catalyst C8200L desempenha o papel de roteador central na arquitetura do laboratório Enterprise NOC.

A infraestrutura combina um roteador Cisco físico, um switch Catalyst C9200L, VLANs departamentais, servidores Linux, estações Windows e plataformas de monitoramento.

Este documento reúne as evidências disponíveis sobre o papel do roteador, endereçamento, monitoramento e políticas de segmentação pretendidas.

**Importante:** A configuração atual do roteador não foi disponibilizada nas evidências analisadas. Por isso, distinguimos informações observadas de configurações que ainda não puderam ser verificadas.

## 2. Infraestrutura Física

O roteador está instalado no rack de rede do laboratório, juntamente com o switch Cisco Catalyst C9200L e a infraestrutura de cabeamento estruturado.

As fotografias disponíveis identificam o equipamento como **Cisco Catalyst C8200L-1N-4T**.

![Roteador Cisco, switch e patch panel](../../assets/images/physical/cisco-router-switch-patch-panel.jpg)

A configuração do switch coletada em 04/11/2026 identifica a interface `Gi1/0/1` como trunk associado à interligação com o roteador.

Essa evidência é compatível com a arquitetura documentada, mas não comprova isoladamente a configuração da interface física correspondente ou das subinterfaces VLAN do roteador.

O nome da interface utilizada no lado do C8200L permanece sem confirmação.

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
| 50 | Não confirmado de forma independente neste conjunto | Validação pendente |
| 60 | Não verificado | Validação pendente |
| 70 | Não verificado | Validação pendente |

Os registros técnicos de 04/11/2026 também associam o endereço `192.168.10.1` ao roteador.

Essas informações demonstram os gateways configurados nas estações no momento da coleta.

Entretanto, não confirmam isoladamente a configuração das subinterfaces do C8200L, a propriedade de todos os gateways ou a comunicação efetiva entre departamentos.

## 5. Política de Controle de Acesso Pretendida

O modelo de segmentação previsto diferencia a rede administrativa de TI/NOC das redes departamentais, sem fio e IoT.

### Acesso administrativo

A VLAN 10 é destinada à administração e ao monitoramento.

A política pretendida permite que sistemas administrativos autorizados iniciem conexões de gerenciamento com serviços e equipamentos de outras VLANs, quando necessário.

### Isolamento departamental

As VLANs 20, 30 e 40 devem permanecer isoladas entre si, exceto quando houver comunicação explicitamente autorizada para determinados serviços.

### Telefonia e autenticação

A VLAN 50 hospeda o servidor documentado de Asterisk e FreeRADIUS.

O acesso aos serviços dessa rede deve respeitar as necessidades das aplicações e dos equipamentos autorizados.

### Isolamento de Wi-Fi e IoT

As VLANs 60 e 70 devem possuir acesso restrito aos recursos internos da infraestrutura corporativa.

Exceções necessárias, incluindo a comunicação entre um ponto de acesso Wi-Fi e o servidor FreeRADIUS, precisam considerar os endereços de origem reais e os serviços utilizados.

**Estado de implementação:** As regras descritas representam a política pretendida, e não ACLs comprovadamente aplicadas.

As evidências disponíveis não confirmam as entradas exatas das ACLs, interfaces de aplicação, direção das regras, ordem de avaliação ou testes de bloqueio bem-sucedidos.

## 6. Monitoramento do Roteador

O roteador aparece no ambiente de monitoramento do laboratório, utilizando Zabbix e Grafana.

As evidências coletadas apresentam informações de disponibilidade e métricas relacionadas às interfaces de rede.

### Grafana — Dashboard do Roteador

![Monitoramento do roteador — Parte 1](../../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

![Monitoramento do roteador — Parte 2](../../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

As capturas demonstram informações disponibilizadas pelo monitoramento durante o período de coleta.

Elas não comprovam disponibilidade contínua, cobertura integral das interfaces ou funcionamento correto de todas as configurações de roteamento e segurança.

O inventário de hosts do Zabbix também apresenta evidência de uma interface de monitoramento SNMP associada ao roteador.

A configuração completa do SNMP e suas restrições de acesso ainda não foram verificadas de forma independente.

## 7. DHCP, NAT e Conectividade Externa

A participação do roteador nos serviços DHCP, na distribuição de endereços IP, no NAT e na conectividade externa faz parte das verificações previstas para a infraestrutura.

Entretanto, as evidências disponíveis não permitem confirmar:

- Se os pools DHCP estão configurados diretamente no C8200L.
- Se existe utilização de DHCP Relay.
- Quais são os escopos e exclusões de endereços DHCP.
- Qual configuração NAT está efetivamente aplicada.
- Como está configurada a interface externa.
- Qual é a tabela completa de roteamento e a rota padrão utilizada.

Nenhum exemplo de configuração será apresentado como efetivamente implementado sem evidências correspondentes.

## 8. Possibilidades de Validação

Verificações futuras podem utilizar registros já disponíveis, histórico de monitoramento e testes autorizados de conectividade.

| Área | Objetivo da validação |
|---|---|
| Roteamento entre VLANs | Identificar as interfaces utilizadas e confirmar o encaminhamento autorizado |
| Gateways | Confirmar os endereços e os equipamentos responsáveis por cada gateway |
| ACLs | Verificar se as restrições de acesso pretendidas estão sendo aplicadas |
| DHCP | Identificar o mecanismo responsável pela distribuição dos endereços |
| NAT | Determinar se existe tradução de endereços configurada e operacional |
| SNMP | Confirmar os parâmetros de monitoramento e as métricas esperadas |
| Troubleshooting | Registrar falhas observadas e suas respectivas evidências |

Os testes de conectividade devem considerar firewalls dos computadores e o comportamento dos serviços antes de atribuir falhas exclusivamente às ACLs.

Uma resposta ICMP bem-sucedida também não comprova, isoladamente, que todos os serviços necessários estejam acessíveis.

## 9. Limitações Conhecidas

Na data desta atualização:

1. A configuração atual do roteador não está disponível.
2. As subinterfaces VLAN e os parâmetros de encapsulamento do roteador não foram verificados.
3. As políticas de ACL pretendidas ainda não foram comprovadas por configurações e testes controlados.
4. A implementação dos serviços DHCP e NAT permanece sem confirmação.
5. As evidências de monitoramento representam registros históricos, não garantia de disponibilidade contínua.
6. A interface física do roteador utilizada na ligação com o switch não foi identificada nos registros disponíveis.

Essas limitações são mantidas na documentação para preservar a precisão técnica.

## 10. Documentação Relacionada

- [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
- [Registro do switch Cisco e das VLANs](registro-switch-vlans-2026-11-04.md)
- [Inventário dos computadores](../estacoes/inventario-de-computadores.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)

---

**Princípio da documentação:** Este registro descreve a infraestrutura observada no laboratório e sua arquitetura de rede pretendida. Configurações não verificadas não são apresentadas como implementadas ou validadas.
