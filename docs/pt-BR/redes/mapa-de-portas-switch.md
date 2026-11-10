# Cisco Catalyst C9200L — Mapeamento de Portas

**Enterprise NOC — From Scratch**

[English](../../networking/switch-port-map.md) | **Português (Brasil)**

---

## Visão Geral

Este documento apresenta o mapeamento histórico das interfaces do switch **Cisco Catalyst C9200L-24T-4G**, utilizado na infraestrutura do Enterprise NOC.

O equipamento disponibiliza conectividade Ethernet para estações de trabalho departamentais, servidores Linux, telefonia IP, infraestrutura Wi-Fi corporativa e dispositivos IoT.

O inventário das interfaces utiliza a configuração do Cisco IOS XE coletada em **4 de novembro de 2026**, juntamente com os registros dos equipamentos presentes no laboratório.

| Característica | Informação |
|---|---|
| Fabricante | Cisco |
| Modelo | Catalyst C9200L-24T-4G |
| Sistema Operacional | Cisco IOS XE |
| Versão Registrada do IOS XE | 17.15 |
| Referência da Configuração | 04/11/2026 |
| Segmentação da Rede | VLANs 10, 20, 30, 40, 50, 60 e 70 |

A captura de configuração representa os parâmetros registrados no switch durante a coleta das evidências. Não estabelece o estado operacional atual de todas as interfaces.

## 1. Inventário das Interfaces

A tabela apresenta as atribuições de VLANs e as descrições documentadas das interfaces.

| Interface | Segmento ou Equipamento Documentado | VLAN Atribuída | Configuração Registrada |
|---|---|---|---|
| Gi1/0/1 | Cisco Catalyst C8200L | Não especificada explicitamente | Trunk |
| Gi1/0/2–3 | TI e NOC | 10 | Access |
| Gi1/0/4–6 | Contabilidade | 20 | Access |
| Gi1/0/7–8 | Financeiro | 30 | Access |
| Gi1/0/9–10 | Vendas | 40 | Access |
| Gi1/0/11 | Debian — Asterisk e FreeRADIUS | 50 | VLAN de acesso 50 configurada; modo operacional não estabelecido |
| Gi1/0/12–13 | Telefones IP Grandstream | 50 | Access |
| Gi1/0/14 | TP-Link Archer AX53 — IoT | 70 | Access |
| Gi1/0/15 | TP-Link Archer AX53 — Wi-Fi Corporativo | 60 | Access |
| Gi1/0/16–24 | Sem atribuição específica de equipamento estabelecida | — | Sem comandos específicos de configuração registrados |
| Gi1/1/1–4 | Interfaces Uplink SFP | — | Sem comandos específicos de configuração registrados |

A tabela reúne a configuração registrada do switch e as atribuições dos equipamentos identificados na documentação da rede.

A configuração de uma interface não comprova isoladamente a existência de conexão física, o estado do enlace ou a comunicação bem-sucedida com o equipamento associado.

## 2. Trunk para o Roteador — Gi1/0/1

A interface `Gi1/0/1` está associada ao roteador Cisco Catalyst C8200L.

A configuração histórica apresenta:

```cisco
interface GigabitEthernet1/0/1
 description TRUNK-PARA-ROTEADOR
 switchport mode trunk
```

Esse registro estabelece que a interface estava configurada como trunk no switch.

A configuração coletada não contém uma lista explícita de VLANs permitidas nem a definição de uma VLAN nativa personalizada nessa interface.

Embora a arquitetura documente as VLANs 10 a 70, o inventário de VLANs não deve ser interpretado como uma lista explicitamente configurada de VLANs permitidas no trunk.

A interface correspondente no roteador, suas subinterfaces VLAN e a configuração completa do roteamento entre VLANs não estão incluídas nos registros coletados.

## 3. Interfaces de Acesso Departamentais

As atribuições departamentais documentadas estão organizadas da seguinte maneira:

| Departamento | VLAN | Interfaces do Switch |
|---|---|---|
| TI e NOC | 10 | Gi1/0/2–3 |
| Contabilidade | 20 | Gi1/0/4–6 |
| Financeiro | 30 | Gi1/0/7–8 |
| Vendas | 40 | Gi1/0/9–10 |

A captura de configuração identifica parâmetros de portas de acesso para essas interfaces.

Um exemplo registrado no segmento de Contabilidade é:

```cisco
interface GigabitEthernet1/0/4
 description PCS-CONTABILIDADE
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
```

Esses comandos descrevem a configuração registrada das interfaces.

Não representam medições independentes da disponibilidade física dos enlaces nem comprovação de comunicação ponta a ponta.

## 4. VoIP e Autenticação — VLAN 50

A VLAN 50 está associada à infraestrutura de telefonia e autenticação do laboratório.

Os equipamentos documentados incluem:

- Servidor Debian Linux com Asterisk e FreeRADIUS.
- Dois telefones IP Grandstream.

As atribuições das interfaces são:

| Interface | Equipamento | VLAN |
|---|---|---|
| Gi1/0/11 | Servidor Asterisk e FreeRADIUS | 50 |
| Gi1/0/12 | Telefone IP Grandstream | 50 |
| Gi1/0/13 | Telefone IP Grandstream | 50 |

### 4.1 Interface Gi1/0/11

A configuração histórica apresenta:

```cisco
interface GigabitEthernet1/0/11
 description SERVIDOR-DEBIAN-VOIP-E-RADIUS
 switchport access vlan 50
 spanning-tree portfast trunk
```

Diferentemente das demais interfaces departamentais de acesso, a configuração não apresenta explicitamente:

```cisco
switchport mode access
```

A presença de `spanning-tree portfast trunk` também difere da configuração registrada nas portas de acesso utilizadas pelas estações de trabalho.

Consequentemente, a captura histórica estabelece a VLAN de acesso configurada, mas não comprova isoladamente o modo operacional efetivo da interface.

A configuração foi preservada conforme registrada, sem classificar a interface como uma porta access ou trunk confirmada.

## 5. Wi-Fi Corporativo — VLAN 60

A rede Wi-Fi corporativa está associada a um TP-Link Archer AX53 dedicado.

| Característica | Informação Documentada |
|---|---|
| Equipamento | TP-Link Archer AX53 |
| Segmento | Wi-Fi Corporativo |
| VLAN | 60 |
| Interface do Switch | Gi1/0/15 |
| Configuração da Interface | Access VLAN 60 |

A captura do switch documenta a atribuição da VLAN.

As evidências coletadas não estabelecem o modo interno de operação do equipamento wireless, a configuração DHCP, o funcionamento do NAT ou o endereçamento IP dos clientes.

Esses parâmetros são tratados conforme as evidências disponíveis na documentação específica da rede wireless.

## 6. Rede IoT — VLAN 70

O ambiente IoT inclui um TP-Link Archer AX53 separado, associado a um dispositivo Amazon Alexa.

| Característica | Informação Documentada |
|---|---|
| Equipamento | TP-Link Archer AX53 dedicado |
| Segmento | IoT |
| VLAN | 70 |
| Interface do Switch | Gi1/0/14 |
| Configuração da Interface | Access VLAN 70 |

A configuração do switch Cisco associa a interface `Gi1/0/14` à VLAN 70.

O endereçamento interno e o modo de operação do equipamento wireless não são estabelecidos pela configuração do switch.

A atribuição da VLAN não comprova isoladamente que os clientes wireless utilizavam endereços de uma sub-rede específica da VLAN 70.

## 7. Interfaces Adicionais do Switch

A captura de configuração não contém comandos específicos de configuração para:

- `Gi1/0/16` até `Gi1/0/24`.
- `Gi1/1/1` até `Gi1/1/4`.

A ausência desses comandos não estabelece se as interfaces estavam fisicamente conectadas, disponíveis, desabilitadas ou operacionalmente inativas.

Os registros históricos não constituem um inventário completo do estado das interfaces.

## 8. Escopo das Configurações e Evidências

Este documento reúne a configuração registrada das interfaces do switch e as atribuições correspondentes dos equipamentos de rede.

A captura de 4 de novembro de 2026 apresenta evidências de:

- Atribuições de VLANs.
- Configuração das portas de acesso departamentais.
- Trunk voltado ao roteador.
- Interfaces associadas aos equipamentos VoIP, Wi-Fi corporativo e IoT.
- Configuração particular da interface `Gi1/0/11`.

As evidências disponíveis não constituem:

- Um relatório atual do estado das interfaces.
- Comprovação da conectividade física de todas as portas documentadas.
- Uma exportação completa da configuração do Cisco C8200L.
- Comprovação da comunicação entre todas as VLANs.
- Verificação da aplicação das ACLs do roteador.
- Um mapa físico completo do cabeamento.

A configuração original foi coletada antes das alterações posteriores relacionadas ao monitoramento SNMP e não deve ser interpretada como a configuração final do switch.

## 9. Documentação Relacionada

- [Redes e Arquitetura](README.md)
- [Topologia Lógica Consolidada](topologia-logica-consolidada.md)
- [Segmentação por VLANs](vlans.md)
- [Cisco Catalyst C8200L](roteador-c8200l.md)
- [Registro de Configuração do Switch](registro-switch-vlans-2026-11-04.md)
- [Wi-Fi Corporativo — VLAN 60](wifi-corporativo-vlan60.md)
- [Rede IoT — VLAN 70](iot-vlan70.md)
- [Infraestrutura Física](../evidencias/infraestrutura-fisica.md)

---

**Referência da configuração:** 04/11/2026  
**Tipo de documento:** Mapeamento histórico das interfaces do switch.
