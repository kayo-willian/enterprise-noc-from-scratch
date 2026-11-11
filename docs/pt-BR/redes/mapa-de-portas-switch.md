# Cisco Catalyst C9200L — Mapa de Portas

**Enterprise NOC — From Scratch**

[English](../../networking/switch-port-map.md) | **Português (Brasil)**

## Inventário das interfaces

A tabela utiliza a configuração do C9200L-24T-4G, IOS XE 17.15, coletada em **4 de novembro de 2026**, junto às funções documentadas dos equipamentos.

| Interface | Conexão documentada | Configuração |
|---|---|---|
| Gi1/0/1 | Cisco C8200L | Trunk voltado ao roteador |
| Gi1/0/2–3 | TI / NOC | Access VLAN 10 |
| Gi1/0/4–6 | Contabilidade | Access VLAN 20 |
| Gi1/0/7–8 | Financeiro | Access VLAN 30 |
| Gi1/0/9–10 | Vendas | Access VLAN 40 |
| Gi1/0/11 | Debian Asterisk / FreeRADIUS | VLAN de acesso 50 atribuída; modo operacional não verificado |
| Gi1/0/12–13 | Telefones IP Grandstream | Access VLAN 50 |
| Gi1/0/14 | TP-Link Archer AX53 dedicado (IoT) | Access VLAN 70 |
| Gi1/0/15 | TP-Link Archer AX53 (Wi-Fi corporativo) | Access VLAN 60 |
| Gi1/0/16–24 | Sem equipamento específico estabelecido | Sem comandos específicos na captura |
| Gi1/1/1–4 | Interfaces uplink SFP | Sem comandos específicos na captura |

A ausência de comandos específicos **não significa** que uma porta estivesse livre, desconectada, desabilitada ou inativa. A tabela registra configurações e conexões previstas, não medições do estado físico dos enlaces.

## Exemplos de interfaces registradas

### Trunk para o roteador — Gi1/0/1

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

A captura não especifica a lista `switchport trunk allowed vlan` nem uma VLAN nativa personalizada. A interface e as subinterfaces correspondentes do roteador não foram coletadas. O inventário de VLANs do projeto não representa uma lista explicitamente permitida no trunk.

### Porta de acesso da Contabilidade — Gi1/0/4

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

### Asterisk / FreeRADIUS — Gi1/0/11

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Diferentemente do exemplo de porta access, a Gi1/0/11 não apresenta `switchport mode access` explícito. `spanning-tree portfast trunk` não comprova o modo operacional efetivo; o registro histórico é preservado sem classificar a porta como access ou trunk confirmado.

## Escopo do registro

As atribuições vêm da captura datada do switch; os modelos AX53 vêm do inventário físico. O documento não verifica isoladamente o funcionamento das portas, o estado dos equipamentos conectados ou a aplicação de ACLs no roteador.

## Referências

[Visão geral de Redes](README.md) · [Registro de configuração do switch](registro-switch-vlans-2026-11-04.md) · [Inventário de VLANs](vlans.md) · [Roteador](roteador-c8200l.md) · [Topologia lógica](topologia-logica-consolidada.md)
