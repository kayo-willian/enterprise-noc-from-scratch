# Monitoramento com Zabbix

[English](../../monitoring/zabbix-monitoring.md) | [Português (Brasil)](zabbix.md)

## 1. Visão Geral

O laboratório Enterprise NOC — From Scratch utiliza o Zabbix para monitorar equipamentos de rede, servidores Linux, estações Windows, serviços de infraestrutura e tráfego de rede.

O ambiente de monitoramento integra equipamentos físicos Cisco com serviços hospedados em sistemas Linux e containers Docker.

Esta documentação utiliza capturas de tela coletadas em **6 de novembro de 2026**.

As imagens representam o ambiente no momento da coleta e não constituem monitoramento em tempo real.

## 2. Arquitetura de Monitoramento

O ambiente Zabbix está hospedado no computador principal da infraestrutura, executando Debian GNU/Linux 13.

A implantação Docker inclui:

| Componente | Finalidade |
|---|---|
| Zabbix Server | Coleta e processamento de dados de monitoramento |
| Zabbix Web | Interface web e dashboards |
| Zabbix Agent | Coleta de informações dos sistemas |
| MariaDB | Armazenamento dos dados do Zabbix |

A infraestrutura monitorada inclui:

- Roteador Cisco Catalyst C8200L.
- Switch Cisco Catalyst C9200L.
- Servidor Debian de infraestrutura.
- Servidor Debian com Asterisk e FreeRADIUS.
- Oito estações Windows.

Os equipamentos Cisco são monitorados por interfaces SNMP, enquanto os sistemas operacionais documentados utilizam interfaces do Zabbix Agent.

Os dashboards também apresentam informações sobre serviços e verificações HTTP.

Para consultar a implantação dos containers, acesse [Infraestrutura Docker e Serviços](../containers/servicos-docker.md).

## 3. Informações do Sistema Zabbix

![Informações do sistema Zabbix](../../assets/images/monitoring/zabbix/zabbix_info_system.png)

A página de informações do sistema apresenta os seguintes valores:

| Parâmetro | Valor observado |
|---|---:|
| Versão do Zabbix Server | 7.0.32 |
| Versão do Zabbix Frontend | 7.0.32 |
| Hosts cadastrados | 12 |
| Hosts habilitados | 12 |
| Templates | 356 |
| Total de itens | 1.820 |
| Itens habilitados | 1.698 |
| Itens desabilitados | 9 |
| Itens não suportados | 113 |
| Total de triggers | 1.082 |
| Triggers habilitadas | 1.073 |
| Triggers desabilitadas | 9 |
| Triggers em estado de problema | 34 |
| Cluster de alta disponibilidade | Inativo |

A captura confirma que o Zabbix Server estava em execução no momento do registro.

Entretanto, os 113 itens não suportados e as 34 triggers em estado de problema indicam que o ambiente ainda apresentava pendências de investigação.

A quantidade de itens não suportados não permite identificar, isoladamente, a causa de cada falha.

## 4. Evidências dos Dashboards

As seis capturas representam partes consecutivas dos dashboards de monitoramento.

A sequência original foi preservada.

### 4.1 Dashboard Unificado da Infraestrutura

![Dashboard unificado do Zabbix](../../assets/images/monitoring/zabbix/zabbix_dashboard1.png)

O dashboard unificado apresenta informações sobre:

- Disponibilidade dos hosts.
- Severidade dos alarmes.
- Monitoramento de aplicações e serviços.
- Métricas da infraestrutura Cisco.
- Utilização de recursos dos servidores Linux.
- Indicadores dos serviços Asterisk.

Durante a coleta, o painel de disponibilidade apresentou:

| Situação | Hosts |
|---|---:|
| Disponíveis | 7 |
| Indisponíveis | 5 |
| Total | 12 |

O detalhamento das interfaces mostrou cinco interfaces passivas de Zabbix Agent disponíveis e cinco indisponíveis, além de duas interfaces SNMP disponíveis.

Os indicadores de serviços também apresentavam verificações positivas para o site corporativo, Pi-hole, Grafana, Zabbix Web, Portainer e Asterisk.

Esses resultados representam observações pontuais, não garantias de disponibilidade contínua.

### 4.2 Interfaces do Roteador Cisco e Tráfego das VLANs

![Monitoramento das interfaces do roteador Cisco](../../assets/images/monitoring/zabbix/zabbix_dashboard2.png)

Esta seção apresenta informações associadas ao roteador Cisco Catalyst C8200L.

O dashboard inclui:

- Estado das interfaces e subinterfaces.
- Tráfego das interfaces WAN e trunk.
- Visualização do tráfego relacionado às VLANs.
- Gráficos de throughput durante o período observado.

Os indicadores das interfaces aparecem como operacionais na captura.

Essas informações demonstram a coleta de métricas, mas não verificam isoladamente todas as políticas de roteamento e controle de acesso.

### 4.3 Monitoramento do Cisco Catalyst 9200L

![Dashboard de monitoramento do Cisco Catalyst 9200L](../../assets/images/monitoring/zabbix/zabbix_dashboard3.png)

O dashboard do switch apresenta informações sobre:

- Utilização de CPU.
- Utilização de memória RAM.
- Sensores de temperatura.
- Indicadores de ventilação e alimentação.
- Estado das interfaces Ethernet.
- Distribuição do tráfego pelas interfaces.

A captura apresenta interfaces identificadas como `up` e `down`.

Uma interface em estado `down` não representa necessariamente uma falha. Portas sem dispositivos conectados ou administrativamente desabilitadas podem permanecer nesse estado normalmente.

Alguns rótulos estão truncados na captura. A identificação exata das interfaces depende da conferência dos itens cadastrados no monitoramento.

### 4.4 Tráfego de Rede, Desempenho e Eventos

![Monitoramento de tráfego, desempenho e incidentes](../../assets/images/monitoring/zabbix/zabbix_dashboard4.png)

Esta seção apresenta informações complementares sobre a infraestrutura:

- Throughput do núcleo da rede e dos servidores.
- Tráfego das portas relacionadas aos setores.
- Desempenho de resposta do site corporativo.
- Utilização de CPU e RAM dos sistemas monitorados.
- Registros de eventos e incidentes.

O painel de eventos apresenta registros de incidentes e eventos resolvidos.

Essas informações demonstram o acompanhamento de eventos no período observado, mas não comprovam que todos os problemas registrados foram solucionados definitivamente.

### 4.5 Utilização de Recursos da Infraestrutura

![Indicadores de utilização de recursos no Zabbix](../../assets/images/monitoring/zabbix/zabbix_dashboard5.png)

Esta seção apresenta indicadores de consumo de recursos dos equipamentos monitorados.

O dashboard inclui:

- Indicadores de utilização de CPU.
- Indicadores de utilização de memória RAM.
- Classificação de consumo de recursos entre computadores e servidores.

A captura apresenta também indicadores diferentes associados ao mesmo nome de switch.

É necessário conferir os itens de origem desses indicadores antes de interpretá-los como medições independentes.

A imagem foi preservada como evidência da configuração do dashboard observada em 6 de novembro de 2026.

### 4.6 Throughput e Monitoramento das Estações Windows

![Throughput e monitoramento das estações Windows](../../assets/images/monitoring/zabbix/zabbix_dashboard6.png)

A última captura da sequência apresenta:

- Throughput de internet e roteamento central.
- Distribuição de tráfego pelas subinterfaces das VLANs.
- Tráfego de download das estações Windows.
- Tráfego de upload das estações Windows.

Os gráficos demonstram a existência de séries históricas de tráfego para determinadas interfaces e estações.

Entretanto, não comprovam cobertura completa de monitoramento para todos os computadores.

## 5. Cadastro e Disponibilidade dos Hosts

### 5.1 Hosts Cadastrados

![Lista de hosts cadastrados no Zabbix](../../assets/images/monitoring/zabbix/zabbix_hosts.png)

A página de configuração apresenta doze hosts:

- Oito estações Windows.
- Servidor principal de infraestrutura e Zabbix.
- Servidor Linux com Asterisk e FreeRADIUS.
- Roteador Cisco Catalyst C8200L.
- Switch Cisco Catalyst C9200L.

Os computadores Windows e servidores Linux estão associados ao monitoramento por Zabbix Agent.

Os equipamentos Cisco utilizam interfaces SNMP na porta UDP 161.

### 5.2 Disponibilidade e Incidentes

![Disponibilidade dos hosts e registros de incidentes](../../assets/images/monitoring/zabbix/zabbix_hosts2.png)

A segunda captura da lista complementa a anterior.

Ela apresenta:

- Indicadores de disponibilidade.
- Interfaces de monitoramento cadastradas.
- Status dos hosts.
- Acesso aos dados recentes e gráficos.
- Contadores de incidentes.

Embora os doze hosts estivessem habilitados, nem todas as interfaces de monitoramento estavam disponíveis.

**Um host habilitado no Zabbix não significa necessariamente que seu agente esteja acessível.**

## 6. Divergências de Endereçamento

A comparação entre as interfaces cadastradas no Zabbix e as fotografias do comando `ipconfig` identificou seis divergências.

| Estação | IPv4 fotografado | IPv4 cadastrado no Zabbix |
|---|---|---|
| TI 2 | `192.168.10.13` | `192.168.10.11` |
| Contabilidade 2 | `192.168.20.12` | `192.168.20.10` |
| Contabilidade 3 | `192.168.20.13` | `192.168.20.12` |
| Financeiro 1 | `192.168.30.10` | `192.168.30.13` |
| Vendas 1 | `192.168.40.11` | `192.168.40.14` |
| Vendas 2 | `192.168.40.10` | `192.168.40.13` |

As estações Contabilidade 1 e Financeiro 2 apresentavam endereços coincidentes nas fontes comparadas.

Essas divergências podem contribuir para problemas de disponibilidade dos agentes ou ausência de dados de monitoramento.

Os registros não determinam uma causa única para todas as falhas; configurações dos agentes, endereçamento dos hosts, firewall, conectividade e itens cadastrados podem afetar a coleta.

Os endereços fotografados representam registros históricos de 6 de novembro de 2026.

Para consultar o inventário das estações, acesse [Inventário de Computadores e Servidores](../estacoes/inventario-de-computadores.md).

## 7. Limites Históricos do Monitoramento

As evidências identificaram situações que ainda exigem verificação:

| Área | Observação |
|---|---|
| Disponibilidade dos agentes | Cinco hosts foram identificados como indisponíveis |
| Itens de monitoramento | 113 itens não suportados |
| Estado das triggers | 34 triggers em estado de problema |
| Endereçamento das estações | Seis divergências entre fotografias e cadastros |
| Interfaces do switch | Algumas interfaces foram apresentadas como down |
| Rótulos dos dashboards | Alguns indicadores precisam de conferência dos itens de origem |
| Disponibilidade histórica | Não foi comprovada disponibilidade contínua dos serviços |

Essas limitações foram mantidas na documentação, em vez de serem omitidas.

Elas representam oportunidades de diagnóstico e demonstram a importância de validar as configurações de monitoramento com o estado real da infraestrutura.

### Considerações sobre DHCP e monitoramento

O ambiente do laboratório utiliza endereçamento dinâmico (DHCP) para estações de trabalho.

Por esse motivo, os endereços IP observados nas capturas podem diferir daqueles registrados anteriormente no Zabbix.

Essa característica pode ocasionar inconsistências temporárias no monitoramento quando os hosts são identificados por endereços IP que não acompanham as mudanças de concessão DHCP.

Consequentemente, estados de indisponibilidade e ausência de métricas devem ser interpretados considerando o contexto do laboratório e a data de coleta das evidências.

As capturas documentam o comportamento observado naquele momento e não representam uma avaliação definitiva da disponibilidade dos equipamentos.

## 8. Integração com Grafana

O Zabbix também funciona como fonte de dados para os dashboards do Grafana utilizados no laboratório.

O ambiente Grafana apresenta visualizações relacionadas a:

- Estações Windows.
- Interfaces do roteador Cisco.
- Interfaces do switch Cisco.
- Servidores Linux.
- Asterisk.
- Serviços web e containers.

As capturas do Grafana e as limitações dos dados apresentados serão documentadas separadamente.

## 9. Resumo das Evidências

| Evidência | Nome original |
|---|---|
| Dashboard unificado | `zabbix_dashboard1.png` |
| Interfaces do roteador e VLANs | `zabbix_dashboard2.png` |
| Monitoramento do switch Cisco | `zabbix_dashboard3.png` |
| Tráfego, desempenho e eventos | `zabbix_dashboard4.png` |
| Consumo de recursos | `zabbix_dashboard5.png` |
| Throughput da infraestrutura | `zabbix_dashboard6.png` |
| Cadastro dos hosts | `zabbix_hosts.png` |
| Disponibilidade e incidentes | `zabbix_hosts2.png` |
| Informações do sistema | `zabbix_info_system.png` |

Todas as capturas foram coletadas em **6 de novembro de 2026**.

Esta documentação descreve o ambiente observado e suas limitações. Não afirma disponibilidade ininterrupta, cobertura completa de monitoramento ou resolução de todos os problemas da infraestrutura.
