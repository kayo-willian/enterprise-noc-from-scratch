# Cisco Catalyst C8200L — Roteador

**Enterprise NOC — From Scratch**

[English](../../networking/router-c8200l.md) | **Português (Brasil)**

## Equipamento e função

| Característica | Registro |
|---|---|
| Modelo | Cisco Catalyst C8200L-1N-4T |
| Função | Infraestrutura central de roteamento |
| Switch associado | Cisco Catalyst C9200L-24T-4G |
| Evidências | Fotografias, registros de rede e capturas Zabbix/Grafana de 4 a 6 de novembro de 2026 |

![Roteador Cisco, switch e patch panel](../../assets/images/physical/cisco-router-switch-patch-panel.jpg)

A configuração do switch coletada em 4 de novembro identifica a conexão voltada ao roteador:

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

**Gi1/0/1 é uma interface do switch C9200L**, não uma interface documentada do roteador. A captura não contém lista explícita de VLANs permitidas nem VLAN nativa personalizada no trunk. Não foram coletadas a porta correspondente do C8200L ou suas subinterfaces `802.1Q`.

## Endereçamento observado

As fotografias das estações e os registros do servidor apresentam os seguintes gateways:

| VLAN | Gateway registrado em | Endereço |
|---|---|---|
| 10 · TI / NOC | Estação de TI | `192.168.10.1` |
| 20 · Contabilidade | Estação de Contabilidade | `192.168.20.1` |
| 30 · Financeiro | Estação do Financeiro | `192.168.30.1` |
| 40 · Vendas | Estação de Vendas | `192.168.40.1` |
| 50 · Voz | Servidor Asterisk/FreeRADIUS | `192.168.50.1` |

Os registros técnicos de 4 de novembro também associam `192.168.10.1` ao roteador. Os demais gateways observados, inclusive o da VLAN 50, **não estabelecem endereços de interfaces específicas do C8200L**.

O laboratório utiliza DHCP nas estações; os registros não identificam integralmente o servidor, relay ou pools DHCP.

## Projeto de controle de acesso

| Segmento | Requisito documentado |
|---|---|
| VLAN 10 | Acesso autorizado à administração e ao monitoramento |
| VLANs 20, 30, 40 | Separação departamental e exceções para serviços autorizados |
| VLAN 50 | Acesso aos serviços de voz e autenticação |
| VLAN 60 | Wi-Fi corporativo com restrições de acesso aos recursos internos |
| VLAN 70 | Conectividade IoT separada e acesso corporativo restrito |

São **requisitos arquiteturais**, não entradas ACL verificadas. As VLANs foram registradas no switch, mas não foram coletados os comandos ACL do roteador nem testes de isolamento ponta a ponta.

## Evidências de monitoramento

O C8200L aparece no inventário de hosts do Zabbix com interface de monitoramento SNMP e nos dashboards históricos do Grafana.

![Dashboard do roteador — Parte 1](../../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

![Dashboard do roteador — Parte 2](../../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

Essas capturas documentam métricas do período de coleta, sem comprovar disponibilidade contínua ou cobertura integral do monitoramento.

## Escopo da configuração

Não foi coletada uma configuração completa do C8200L. Assim, interfaces do roteador, comandos de roteamento, traduções NAT, parâmetros WAN, rota padrão, DHCP, aplicação de ACLs e configuração SNMP **não são apresentados como verificados**. O projeto de rede e os gateways observados permanecem documentados nos respectivos registros.

## Referências

[Visão geral de Redes](README.md) · [Topologia lógica](topologia-logica-consolidada.md) · [VLANs](vlans.md) · [Registro do switch](registro-switch-vlans-2026-11-04.md) · [Mapa de portas](mapa-de-portas-switch.md) · [Inventário de computadores](../estacoes/inventario-de-computadores.md) · [Zabbix](../monitoramento/zabbix.md) · [Grafana](../monitoramento/grafana.md)
