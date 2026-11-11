# Cisco Catalyst C9200L — Registro de Configuração

**Enterprise NOC — From Scratch**

[English](../../networking/switch-vlan-snapshot-2026-11-04.md) | **Português (Brasil)**

## Coleta

| Característica | Registro histórico |
|---|---|
| Equipamento | Cisco Catalyst C9200L-24T-4G |
| Sistema operacional | Cisco IOS XE 17.15 |
| Comando | `show running-config` |
| Data | 04/11/2026 |
| Método | Console serial a partir do computador Linux Asterisk/FreeRADIUS |

Esta captura **antecede alterações posteriores de monitoramento SNMP**; não representa a configuração atual completa do switch nem um relatório do estado das interfaces.

![Roteador Cisco, switch e patch panel](../../assets/images/physical/cisco-router-switch-patch-panel.jpg)

## VLANs registradas

| VLAN | Segmento | Interfaces atribuídas |
|---|---|---|
| 10 | TI / NOC | Gi1/0/2–3 |
| 20 | Contabilidade | Gi1/0/4–6 |
| 30 | Financeiro | Gi1/0/7–8 |
| 40 | Vendas | Gi1/0/9–10 |
| 50 | VoIP / Autenticação | Gi1/0/11–13 |
| 60 | Wi-Fi corporativo | Gi1/0/15 |
| 70 | IoT | Gi1/0/14 |

O inventário por interface está no [mapa de portas](mapa-de-portas-switch.md). O modelo Archer AX53 da VLAN 70 vem do inventário dos equipamentos, não dos comandos IOS XE.

## Trechos de configuração

### Trunk para o roteador — Gi1/0/1

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

Não foi registrada lista explícita de VLANs permitidas nem VLAN nativa personalizada. A interface do C8200L e as subinterfaces do roteador não integram a captura.

### Porta de acesso da Contabilidade — Gi1/0/4

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

### Servidor de voz — Gi1/0/11

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

A Gi1/0/11 **não** apresenta `switchport mode access` explícito nos comandos coletados. `spanning-tree portfast trunk` não determina seu modo de comutação efetivo.

As interfaces Gi1/0/16–24 e Gi1/1/1–4 não apresentam comandos específicos na captura; seu estado físico ou operacional não está estabelecido.

### Spanning Tree

```cisco
spanning-tree mode rapid-pvst
spanning-tree extend system-id
```

O Rapid PVST+ está configurado, e diversas portas de acesso utilizam PortFast. Não há saída operacional para estabelecer root bridge, portas bloqueadas ou estado de convergência.

## Interpretando o Spanning Tree e as Portas

Os comandos `spanning-tree mode rapid-pvst` e `spanning-tree extend system-id` comprovam que o **Rapid PVST+ foi configurado** no export histórico. A finalidade do protocolo é evitar loops em Layer 2, considerando a árvore de encaminhamento por VLAN; porém esses comandos globais **não identificam** bridge raiz, caminhos alternativos/bloqueados ou eventos de convergência. Isso exigiria saídas operacionais datadas.

Na porta de Contabilidade `Gi1/0/4` constam `switchport mode access`, `switchport access vlan 20` e `spanning-tree portfast`. O PortFast costuma ser usado em portas de endpoints confiáveis para acelerar a transição de encaminhamento; o comando não comprova ausência de loops na rede.

**Exceção — Gi1/0/11:** `switchport access vlan 50` e `spanning-tree portfast trunk` aparecem juntos, **sem `switchport mode access` explícito**. O PortFast não estabelece o modo efetivo da interface. Confirmar access ou trunk exigiria consulta operacional autorizada e configuração atual da porta. Isso não está no snapshot de 4 de novembro.

O snapshot é **registro de configuração**, enquanto os dashboards posteriores Zabbix/Grafana são **registros de telemetria**. Estados `UP`/`DOWN` ou gráficos de tráfego devem ser associados aos identificadores reais das portas antes de concluir algo sobre os links físicos. O [mapa de portas](mapa-de-portas-switch.md) mantém os comandos exatos.


## Evidências posteriores de monitoramento

As capturas abaixo do Zabbix e Grafana documentam métricas do switch coletadas **após** o registro de configuração original.

![Dashboard do switch Catalyst no Zabbix](../../assets/images/monitoring/zabbix/zabbix_dashboard3.png)

![Dashboard do switch Catalyst no Grafana](../../assets/images/monitoring/grafana/grafana_dashboard_switch1.png)

Os dashboards incluem métricas de interfaces e hardware, mas não substituem uma exportação de configuração SNMP. Alguns painéis do Grafana repetem nomes de interfaces; esses rótulos não são contabilizados como interfaces físicas independentes.

**Limites:** O registro do switch não comprova ACLs no roteador, roteamento entre todas as VLANs, endereçamento dos clientes wireless ou estado físico dos enlaces.

## Referências

[Visão geral de Redes](README.md) · [Mapa de portas](mapa-de-portas-switch.md) · [Inventário de VLANs](vlans.md) · [Roteador](roteador-c8200l.md) · [Topologia lógica](topologia-logica-consolidada.md) · [Infraestrutura física](../evidencias/infraestrutura-fisica.md) · [Zabbix](../monitoramento/zabbix.md) · [Grafana](../monitoramento/grafana.md)
