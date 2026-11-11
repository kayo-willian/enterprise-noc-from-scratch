# Segmentação por VLANs

**Enterprise NOC — From Scratch**

[English](../../networking/vlans.md) | **Português (Brasil)**

## Inventário de VLANs e endereçamento

A configuração do Cisco C9200L coletada em 4 de novembro de 2026 registra sete VLANs. O endereçamento dos equipamentos vem do inventário de 6 de novembro, não de uma exportação completa da configuração do roteador.

| VLAN | Segmento | Portas do switch | Rede documentada | Gateway registrado |
|---|---|---|---|---|
| 10 | TI / NOC | Gi1/0/2–3 | `192.168.10.0/24` | `192.168.10.1` (estação de TI) |
| 20 | Contabilidade | Gi1/0/4–6 | `192.168.20.0/24` | `192.168.20.1` (estação) |
| 30 | Financeiro | Gi1/0/7–8 | `192.168.30.0/24` | `192.168.30.1` (estação) |
| 40 | Vendas | Gi1/0/9–10 | `192.168.40.0/24` | `192.168.40.1` (estação) |
| 50 | VoIP / Autenticação | Gi1/0/11–13 | `192.168.50.0/24` | `192.168.50.1` (servidor de voz) |
| 60 | Wi-Fi corporativo | Gi1/0/15 | Sub-rede dos clientes não estabelecida | Não estabelecido |
| 70 | IoT | Gi1/0/14 | Sub-rede dos clientes não estabelecida | Não estabelecido |

**Os gateways são observações dos equipamentos**, não atribuições verificadas a interfaces do C8200L. As redes `/24` foram obtidas dos endereços e máscaras coletados.

## Equipamentos documentados

| VLAN | Exemplos do inventário |
|---|---|
| 10 | Servidor NOC Debian 13 `192.168.10.12`, estação de TI `192.168.10.13` |
| 20 | Estações da Contabilidade `192.168.20.11–13` |
| 30 | Estações do Financeiro `192.168.30.10–11` |
| 40 | Estações de Vendas `192.168.40.10–11` |
| 50 | Asterisk/FreeRADIUS `192.168.50.2`; telefones Grandstream `192.168.50.10–11` |
| 60 | TP-Link Archer AX53 corporativo |
| 70 | Outro Archer AX53 para IoT e Amazon Alexa |

O trunk voltado ao roteador está configurado no switch, em `Gi1/0/1`. A lista de VLANs permitidas não está explicitamente indicada na captura. Na `Gi1/0/11`, a VLAN 50 foi atribuída, mas o modo operacional efetivo não foi estabelecido.

## Projeto de segurança e evidências

As VLANs separam domínios de broadcast na camada 2. O tráfego entre VLANs exige roteamento em camada 3; **a atribuição de VLANs não comprova a aplicação de ACLs**.

| Segmento | Requisito de controle de acesso |
|---|---|
| TI / NOC | Administração e monitoramento autorizados |
| Contabilidade / Financeiro / Vendas | Separação departamental com exceções autorizadas |
| Voz / Autenticação | Comunicação necessária aos serviços de voz e autenticação |
| Wi-Fi corporativo | Restringir acesso não autorizado aos sistemas internos |
| IoT | Separar dispositivos inteligentes dos recursos corporativos sensíveis |

Os registros não incluem exportação completa das ACLs do C8200L nem teste de isolamento ponta a ponta.

Os Archer AX53 das VLANs 60 e 70 são equipamentos físicos separados. Seus modos de operação, redes IP dos clientes, DHCP e NAT não foram coletados. Em modo roteador, clientes wireless podem utilizar sub-redes privadas atrás desses equipamentos, distintas da rede VLAN upstream.

As estações utilizam DHCP. Endereços do inventário de 6 de novembro podem divergir dos registros anteriores do Zabbix; nenhuma reserva estática é presumida.

## Referências

[Visão geral de Redes](README.md) · [Topologia lógica](topologia-logica-consolidada.md) · [Registro do switch](registro-switch-vlans-2026-11-04.md) · [Mapa de portas](mapa-de-portas-switch.md) · [Roteador](roteador-c8200l.md) · [Wi-Fi corporativo](wifi-corporativo-vlan60.md) · [IoT](iot-vlan70.md) · [Inventário de computadores](../estacoes/inventario-de-computadores.md)
