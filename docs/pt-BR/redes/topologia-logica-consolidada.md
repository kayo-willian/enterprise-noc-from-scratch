# Topologia Lógica Consolidada

**Enterprise NOC — From Scratch**

[English](../../networking/consolidated-logical-topology.md) | **Português (Brasil)**

## Topologia

O diagrama apresenta as relações de rede registradas no laboratório entre **4 e 6 de novembro de 2026**. As conexões representam associações entre equipamentos, não testes de tráfego ponta a ponta nem o mapeamento individual dos cabos.

```mermaid
flowchart TB
    R["Cisco Catalyst C8200L"]
    SW["Cisco Catalyst C9200L"]
    R ---|"Trunk para o roteador<br/>Switch Gi1/0/1"| SW
    SW --> V10["VLAN 10 · TI / NOC"]
    SW --> V20["VLAN 20 · Contabilidade"]
    SW --> V30["VLAN 30 · Financeiro"]
    SW --> V40["VLAN 40 · Vendas"]
    SW --> V50["VLAN 50 · Voz / Autenticação"]
    SW --> V60["VLAN 60 · Wi-Fi corporativo"]
    SW --> V70["VLAN 70 · IoT"]
    V10 --> NOC["Debian 13<br/>Monitoramento / Docker"]
    V10 --> IT["Estação de TI"]
    V20 --> ACC["3 estações Windows"]
    V30 --> FIN["2 estações Windows"]
    V40 --> SALES["2 estações Windows"]
    V50 --> PBX["Debian forky/sid<br/>Asterisk / FreeRADIUS"]
    V50 --> PHONES["2 telefones IP Grandstream"]
    V60 --> WIFI["TP-Link Archer AX53"]
    V70 --> IOT["TP-Link Archer AX53 dedicado"]
    IOT --> ALEXA["Amazon Alexa"]
```

O trunk `Gi1/0/1` está registrado no lado do switch C9200L. Não foram coletados o identificador da porta correspondente no C8200L nem a configuração completa das subinterfaces do roteador.

## Equipamentos e endereçamento

| Segmento | Equipamentos / exemplos | Rede ou endereço |
|---|---|---|
| VLAN 10 · TI / NOC | Servidor Debian 13; estação de TI | `192.168.10.12`; `192.168.10.13` |
| VLAN 20 · Contabilidade | Três estações Windows | `192.168.20.11–13` |
| VLAN 30 · Financeiro | Duas estações Windows | `192.168.30.10–11` |
| VLAN 40 · Vendas | Duas estações Windows | `192.168.40.10–11` |
| VLAN 50 · Voz | Debian Asterisk / FreeRADIUS | `192.168.50.2/24` |
| VLAN 50 · Telefones | Grandstream, ramais 1001 (Vendas) e 1002 (TI) | `192.168.50.10`; `192.168.50.11` |
| VLAN 60 · Wi-Fi corporativo | TP-Link Archer AX53, switch `Gi1/0/15` | Sub-rede dos clientes não estabelecida |
| VLAN 70 · IoT | Outro Archer AX53, Alexa, switch `Gi1/0/14` | Sub-rede dos clientes não estabelecida |

As redes departamentais documentadas (VLANs 10–50) utilizam máscaras `/24`. O servidor principal do NOC é um Dell OptiPlex 3020 com Debian 13; o servidor de voz foi registrado com Debian forky/sid.

| VLAN | Gateway registrado nos equipamentos |
|---|---|
| 10 | `192.168.10.1` — estação de TI |
| 20 | `192.168.20.1` — estação de Contabilidade |
| 30 | `192.168.30.1` — estação do Financeiro |
| 40 | `192.168.40.1` — estação de Vendas |
| 50 | `192.168.50.1` — servidor Asterisk/FreeRADIUS |

Os gateways observados não identificam todas as interfaces do roteador. As estações utilizam DHCP; foram documentadas seis divergências entre endereços observados e registros de hosts no Zabbix.

## Serviços e monitoramento

O servidor Debian principal hospeda serviços em Docker. O inventário de 6 de novembro registrou **10 containers em execução**, incluindo Zabbix, Grafana, Portainer, Pi-hole e Uptime Kuma; a infraestrutura relacionada inclui MariaDB e serviços web.

Zabbix e Grafana apresentam observações históricas de equipamentos Cisco, hosts e serviços. As capturas também registram hosts indisponíveis e itens não suportados, sem comprovar disponibilidade contínua.

![Roteador Cisco, switch e patch panel](../../assets/images/physical/cisco-router-switch-patch-panel.jpg)

## Arquitetura Operacional da Rede e Fluxos de Monitoramento

O trunk **Gi1/0/1 do C9200L** comprova a associação registrada no lado do switch com o C8200L. Os gateways observados nas VLANs 10–50 descrevem configurações de hosts, mas **não** comprovam interfaces e subinterfaces 802.1Q do roteador, ACLs ou fluxos permitidos entre VLANs. Uma ligação desenhada representa uma associação documentada, não um teste de conectividade concluído.

Um usuário acessando o portal NOC a partir de uma estação departamental dependeria de **quatro camadas**: endereçamento e gateway corretos, caminho Layer 3 permitido até `192.168.10.12`, DNS do serviço e funcionamento do Nginx/backend. Os registros de 4–6 de novembro documentam partes separadas dessa cadeia; não há uma transação validada entre VLANs.

O Archer AX53 corporativo usa **Gi1/0/15 / VLAN 60**. O FreeRADIUS está registrado na **VLAN 50**, em `192.168.50.2`. Trata-se de uma dependência de autenticação pretendida, não de comprovação de que o AX53 atuava como autenticador RADIUS ou que o 802.1X funcionou.

### O Monitoramento Usa Outro Fluxo

```mermaid
flowchart LR
    CISCO["Cisco C8200L / C9200L"] -->|"SNMP"| Z["Zabbix Server"]
    HOSTS["Hosts Debian / Windows"] -->|"Zabbix Agent"| Z
    Z --> DB[("MariaDB")]
    WEB["Zabbix Web / API"] <--> DB
    G["Grafana"] -->|"Fonte de dados Zabbix"| WEB
    K["Uptime Kuma"] -.->|"Verificações independentes"| SERVICES["Serviços selecionados"]
```

O diagrama recupera as **relações entre serviços e monitoramento** presentes antes da consolidação de redes. Representa o fluxo lógico, não captura de pacotes ou garantia de todos os itens. O Zabbix registrava itens não suportados e hosts indisponíveis.

| Evidência | Conclusão permitida | Ainda não demonstrado |
|---|---|---|
| `show running-config` C9200L (4/11) | VLANs, trunk e Spanning Tree | Configuração do roteador, políticas efetivas e todos os estados de link |
| Inventário de sistemas (6/11) | IPs, máscaras e alguns gateways | Pools DHCP e leases atuais |
| Inventário Docker (6/11) | Dez containers em execução e portas publicadas | Alcance dos serviços em cada VLAN |
| Capturas de monitoramento (6/11) | Telemetria e alarmes históricos | Disponibilidade ininterrupta e cobertura completa |

Os comandos e portas permanecem no [snapshot do switch](registro-switch-vlans-2026-11-04.md), e os endereços no [inventário de endpoints](../estacoes/inventario-de-computadores.md). Aqui são referenciados, não duplicados.


## Limites das evidências

- O registro do C9200L documenta VLANs, portas e trunk, mas não comprova aplicação de ACLs no roteador nem todas as rotas entre VLANs.
- A Gi1/0/11 contém `switchport access vlan 50` e `spanning-tree portfast trunk`, sem comando explícito de modo access. O modo efetivo não foi estabelecido.
- Os dois AX53 têm funções diferentes. Seus modos de operação, sub-redes dos clientes, DHCP e NAT não foram coletados; a autenticação entre FreeRADIUS e Wi-Fi não foi verificada.
- Endereços dos equipamentos, estado do Docker e dashboards são registros datados, não garantias de disponibilidade contínua.

## Referências

[Visão geral de Redes](README.md) · [VLANs](vlans.md) · [Roteador](roteador-c8200l.md) · [Mapa de portas](mapa-de-portas-switch.md) · [Registro do switch](registro-switch-vlans-2026-11-04.md) · [Wi-Fi corporativo](wifi-corporativo-vlan60.md) · [IoT](iot-vlan70.md) · [Inventário de computadores](../estacoes/inventario-de-computadores.md) · [Serviços Docker](../containers/servicos-docker.md) · [Asterisk / FreeRADIUS](../servicos/asterisk-freeradius.md) · [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
