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

A infraestrutura física inclui os seguintes equipamentos:

- **Cisco Catalyst C8200L:** Roteador corporativo.
- **Cisco Catalyst 9200L:** Switch corporativo.
- **Roteador Intelbras (VLAN 60):** Fornece conectividade à rede sem fio corporativa.
- **Roteador Intelbras (VLAN 70):** Fornece conectividade aos dispositivos IoT.

Os dois roteadores Intelbras são do mesmo modelo, que será identificado durante o levantamento final dos equipamentos.

## Rede Wi-Fi Corporativa — VLAN 60

A VLAN 60 é dedicada à conectividade sem fio corporativa.

A implementação no laboratório inclui:

- Um roteador Intelbras.
- Um esquema de endereçamento na faixa `10.0.0.0`, ainda pendente de confirmação da máscara.
- Restrições de acesso envolvendo ACLs.
- Controle de acesso baseado em RADIUS.

O segmento sem fio foi projetado para permanecer isolado da rede principal, conforme as políticas de acesso do laboratório.

A máscara de sub-rede, o modelo do roteador, as regras de ACL e a configuração RADIUS ainda precisam ser documentados e verificados.

## Rede IoT — VLAN 70

A VLAN 70 é dedicada aos dispositivos de Internet das Coisas (IoT).

O ambiente inclui:

- Um roteador Intelbras.
- Um dispositivo Amazon Alexa com tela.
- Uma lâmpada inteligente controlada por comandos de voz da Alexa.

O segmento IoT demonstra a integração de dispositivos inteligentes em uma infraestrutura de rede segmentada, semelhante à de ambientes corporativos.

A configuração específica do roteador e as políticas de acesso dos dispositivos IoT ainda precisam ser verificadas.

## Status da Documentação

**Status:** Em andamento

A documentação técnica adicional contemplará:

- Topologia física da rede.
- Atribuição das VLANs e interfaces do switch.
- Configurações das portas trunk e access.
- Políticas de roteamento e controle de acesso.
- Configuração das redes sem fio.
- Testes de conectividade e isolamento.

Os detalhes das configurações serão documentados após a verificação nos equipamentos do laboratório.
