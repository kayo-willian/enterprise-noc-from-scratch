# Registro de evidências — 6 de novembro de 2026

[English](../../evidence/evidence-collection-2026-11-06.md) | **Português (BR)**

> **Projeto:** Enterprise NOC — From Scratch  
> **Tipo de registro:** inventário datado da coleta  
> **Situação:** registro técnico da coleta

## Visão geral

Em 6 de novembro de 2026, foi realizada uma coleta de evidências da infraestrutura física e lógica do laboratório. O material reúne fotografias dos equipamentos, capturas de estações de trabalho e ferramentas de monitoramento, registros de hardware e documentos técnicos.

Os arquivos originais são preservados em armazenamento privado de trabalho. A documentação publicada utiliza cópias selecionadas e sanitizadas das evidências, sem credenciais ou identificadores institucionais privados.

## Componentes documentados

| Área | Evidências coletadas | Registro técnico |
|---|---|---|
| Infraestrutura física | Rack, roteador Cisco C8200L, switch Catalyst 9200L, patch panel, cabeamento e estações de trabalho. | [Rack e cabeamento](infraestrutura-fisica.md) |
| Estações | Registros de oito computadores Windows e duas estações Linux com funções distintas no laboratório. | [Inventário de computadores](../estacoes/inventario-de-computadores.md) |
| Redes | Capturas de configuração IP por setor e cópia histórica da configuração do switch, anterior à ativação do SNMP. | [Configuração do switch](../redes/registro-switch-vlans-2026-11-04.md) |
| Telefonia e autenticação | Dois telefones Grandstream e documentação do servidor Asterisk/FreeRADIUS. | [VoIP e autenticação](../servicos/asterisk-freeradius.md) |
| Containers | Registros do Docker/Portainer, com dez containers em execução no instante da coleta. | [Ambiente Docker](../containers/servicos-docker.md) |
| Observabilidade | Capturas de Zabbix, Grafana e Uptime Kuma, incluindo painéis de infraestrutura e serviços. | [Zabbix](../monitoramento/zabbix.md), [Grafana](../monitoramento/grafana.md) |
| Serviços adicionais | Evidências de Pi-hole, proxy reverso e serviço web em container. | [DNS e disponibilidade](../servicos/dns-e-disponibilidade.md) |

## Datas dos Registros e Quantidades do Inventário

A [configuração do C9200L](../redes/registro-switch-vlans-2026-11-04.md) foi coletada em 4 de novembro de 2026. As [fotografias da infraestrutura](infraestrutura-fisica.md), o [inventário de computadores](../estacoes/inventario-de-computadores.md) e os [registros de monitoramento](../monitoramento/zabbix.md) correspondem à coleta de 6 de novembro.

O inventário contém **oito estações Windows e duas máquinas Linux**. Os doze hosts cadastrados no Zabbix correspondem a esses dez computadores e aos equipamentos Cisco C8200L e C9200L. O [registro do Zabbix](../monitoramento/zabbix.md#divergências-de-endereçamento) apresenta seis diferenças entre os endereços IPv4 fotografados nas estações e os cadastros dos hosts.

## Limites Históricos das Evidências

- Alguns endereços IP exibidos nas estações divergem dos cadastrados no Zabbix na data da coleta.
- Há hosts indisponíveis, itens não suportados e painéis sem dados no material capturado; esses estados serão descritos como observações do período, sem afirmar disponibilidade contínua.
- A seleção pública de imagens exclui credenciais, informações institucionais e identificadores privados.
- A configuração histórica do switch não substitui uma exportação atualizada do equipamento.
- O inventário técnico apresenta modelos e especificações somente quando constam das evidências coletadas.


---

**Nota:** este documento registra a existência e o conteúdo geral das evidências coletadas; não constitui certificação de funcionamento contínuo, testes completos de segurança ou validação de todas as configurações.
