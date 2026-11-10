# Segmentação de Rede com VLANs

**[English](../../networking/vlans.md) | Português (Brasil)**

## Visão Geral

A infraestrutura corporativa utiliza VLANs (Virtual Local Area Networks) para separar logicamente departamentos, serviços de infraestrutura, conectividade sem fio e dispositivos IoT.

A arquitetura da rede contempla sete VLANs, proporcionando segmentação lógica para diferentes necessidades operacionais.

## Inventário de VLANs

| VLAN ID | Nome | Finalidade |
|---|---|---|
| 10 | TI e Monitoramento | Infraestrutura de TI e serviços de monitoramento |
| 20 | Contabilidade | Departamento de contabilidade |
| 30 | Financeiro | Departamento financeiro |
| 40 | Vendas | Departamento de vendas |
| 50 | VoIP | Telefonia IP e serviços de PBX |
| 60 | Wi-Fi Corporativo | Conectividade sem fio corporativa |
| 70 | IoT | Dispositivos inteligentes e conectividade IoT |

## Infraestrutura de Rede

A infraestrutura física inclui:

- **Cisco Catalyst C8200L:** Infraestrutura de roteamento corporativo.
- **Cisco Catalyst C9200L:** Switch Ethernet gerenciável.
- **TP-Link Archer AX53 (VLAN 60):** Conectividade Wi-Fi corporativa.
- **TP-Link Archer AX53 (VLAN 70):** Conectividade wireless dedicada aos dispositivos IoT.

As redes Wi-Fi corporativa e IoT utilizam roteadores wireless separados do mesmo modelo.

## Rede Wi-Fi Corporativa — VLAN 60

A VLAN 60 é destinada à conectividade sem fio corporativa.

A rede utiliza um TP-Link Archer AX53, identificado por evidência física coletada em 06/11/2026.

O registro de configuração do Cisco Catalyst C9200L, coletado em 04/11/2026, atribui a interface `Gi1/0/15` à VLAN 60.

A captura do switch registra a atribuição da VLAN, mas não inclui o modo de operação do equipamento wireless, o endereçamento dos clientes, o DHCP nem a autenticação.

A arquitetura de rede pretende restringir acessos não autorizados entre o Wi-Fi corporativo e as demais VLANs internas.

## Rede IoT — VLAN 70

A VLAN 70 é destinada à conectividade de dispositivos de Internet das Coisas (IoT).

A rede inclui uma Amazon Alexa conectada via Wi-Fi a um TP-Link Archer AX53 dedicado ao ambiente IoT.

O roteador wireless conecta-se ao switch Cisco Catalyst C9200L por Ethernet.

O registro de configuração do switch, coletado em 04/11/2026, atribui a interface `Gi1/0/14` à VLAN 70.

A captura do switch registra a atribuição da VLAN, mas não inclui o modo de operação, o endereçamento interno, o DHCP ou as regras NAT do roteador wireless.

O projeto lógico da rede IoT separa os dispositivos desse segmento dos recursos corporativos sensíveis.

O isolamento descrito corresponde à política lógica do projeto, não a um resultado comprovado de testes das ACLs.

## Escopo do Registro

Este inventário consolida o projeto lógico e a configuração histórica do switch Cisco coletada em 04/11/2026. Os parâmetros específicos dos roteadores wireless são descritos apenas quando constam das evidências. A ausência de exportações dessas configurações não é apresentada como tarefa de publicação pendente.
