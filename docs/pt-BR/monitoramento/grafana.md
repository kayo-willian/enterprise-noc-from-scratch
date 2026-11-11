# Grafana — Dashboards do NOC

[English](../../monitoring/grafana-monitoring.md) | **Português (Brasil)**

**Data das evidências:** 6 de novembro de 2026 · **Implantação:** Grafana em Debian 13 / Docker · **Fonte de dados:** integração Zabbix

O Grafana apresenta métricas coletadas da infraestrutura. As imagens são **capturas datadas**, não um painel em tempo real; configurações completas das fontes de dados e exportações JSON dos dashboards não constam das evidências coletadas.

## Organização dos Dashboards

![Organização dos dashboards Grafana](../../assets/images/monitoring/grafana/grafana_order.png)

| Seção do dashboard | Alvos registrados |
|---|---|
| Aplicações Web e Containers | Site, serviços Docker e verificações HTTP |
| Roteador Cisco | Interfaces e tráfego das VLANs no Catalyst C8200L |
| Switch Cisco | Hardware e interfaces do Catalyst C9200L |
| Servidores e VoIP | Servidor Debian do NOC e host Asterisk/FreeRADIUS |
| Estações Windows e Endpoints | Computadores dos setores, CPU/RAM e tráfego |

## Aplicações Web e Containers

![Aplicações web e containers](../../assets/images/monitoring/grafana/grafana_dashboard_web_containers.png)

Os painéis apresentam status e tempo de resposta HTTP, histórico de desempenho web, disponibilidade de serviços e indicadores de heartbeat dos containers.

- **Resultado HTTP:** `200 OK` para a aplicação web monitorada durante a verificação registrada.
- **Serviços representados:** site corporativo, Pi-hole, Grafana, Zabbix Web e Portainer.
- **Escopo:** serviços selecionados, **não** todos os dez containers do [inventário Docker](../containers/servicos-docker.md). Uma resposta HTTP bem-sucedida não verifica todas as funções da aplicação.

## Cisco Catalyst C8200L — Roteador

![Estado das interfaces e tráfego do roteador](../../assets/images/monitoring/grafana/grafana_dashboard_router1.png)

A primeira captura apresenta indicadores `UP` para interfaces/subinterfaces selecionadas e throughput relacionado às conexões WAN, trunk e VLANs.

![Histórico de throughput do roteador](../../assets/images/monitoring/grafana/grafana_dashboard_router2.png)

A segunda apresenta séries históricas do tráfego das interfaces e subinterfaces VLAN. As medições documentam os caminhos monitorados no intervalo selecionado, não a configuração completa do roteador, a aplicação das ACLs ou largura de banda contínua.

## Cisco Catalyst C9200L — Switch

![Hardware e estado das interfaces do switch](../../assets/images/monitoring/grafana/grafana_dashboard_switch1.png)

Inclui CPU, RAM, temperatura, ventiladores, fontes de alimentação, estado das interfaces e throughput. Há estados `UP` e `DOWN`; uma porta down pode estar ociosa ou administrativamente desabilitada.

**Problema de identificação:** vários painéis apresentam o mesmo rótulo `Gi1/0/1 TRUNK-ROUTER`. As capturas, isoladamente, não associam cada painel a uma interface física distinta.

![Throughput das interfaces do switch](../../assets/images/monitoring/grafana/grafana_dashboard_switch2.png)

Séries históricas de tráfego para interfaces selecionadas de trunk, setores e infraestrutura. Os rótulos dos painéis devem ser conferidos com os itens do monitoramento e o [mapa de portas do switch](../redes/mapa-de-portas-switch.md).

![Erros de interfaces e temperatura do switch](../../assets/images/monitoring/grafana/grafana_dashboard_switch3.png)

Erros das interfaces, leituras relacionadas a CRC e histórico de temperatura fornecem contexto para diagnóstico no período observado.

## Servidores Linux e VoIP

![Servidores Linux Asterisk e Zabbix](../../assets/images/monitoring/grafana/grafana_dashboard_asterisk.png)

| Sistema | Função | Estado exibido |
|---|---|---|
| Host Asterisk / FreeRADIUS | Telefonia IP e autenticação de rede | `ONLINE` |
| Servidor de infraestrutura Zabbix | Stack de monitoramento Debian/Docker | `ONLINE` |

Os painéis incluem CPU, RAM, disponibilidade e histórico do Zabbix Agent. Disponibilidade do host **não** comprova chamadas SIP ou autenticação RADIUS; consulte [Asterisk/FreeRADIUS](../servicos/asterisk-freeradius.md).

## Estações Windows

![Disponibilidade e recursos das estações Windows](../../assets/images/monitoring/grafana/grafana_dashboard_pcs1.png)

Oito estações Windows dos setores aparecem no dashboard:

| Painel de estado | Estações |
|---|---:|
| `ONLINE` | 3 |
| `No data` | 5 |
| **Total** | **8** |

Alguns valores de CPU/RAM aparecem apesar da ausência de status. `No data` significa que a consulta não retornou dados utilizáveis para aquele painel e intervalo; **não** comprova que o computador estava desligado. Possíveis causas incluem itens/consultas, agentes, conectividade e referências de hosts; nenhuma foi confirmada como causa comum.

![Histórico de CPU, RAM e tráfego das estações](../../assets/images/monitoring/grafana/grafana_dashboard_pcs2.png)

Existem séries históricas de CPU, RAM, download e upload para determinadas estações. Algumas legendas repetem identificadores; é preciso verificar a associação entre itens e hosts. Seis IPv4 também divergiam dos cadastros no Zabbix na [comparação de 6 de novembro](zabbix.md#divergências-de-endereçamento).

## Interpretando os Dashboards como Evidência

O Grafana **visualiza** dados coletados pelo Zabbix; os gráficos não comprovam, por si sós, que todos os itens Zabbix funcionaram corretamente. O dashboard está dividido em cinco áreas: aplicações/containers, C8200L, C9200L, servidores Linux/VoIP e estações Windows. Essa organização ajuda a relacionar sintomas de serviço com métricas de rede, host e aplicação.

| Indicador | Leitura técnica | Ainda requer verificação |
|---|---|---|
| HTTP **200 OK** | A verificação web recebeu resposta HTTP bem-sucedida | Outras URLs, redes de origem e funções da aplicação |
| Roteador `UP` e tráfego | Estados e amostras de interfaces selecionadas | Subinterfaces, NAT, roteamento e ACLs no C8200L |
| CPU, RAM, temperatura, ventilação, erros e tráfego do switch | Telemetria disponível em itens selecionados | Correspondência de portas; rótulos repetidos `Gi1/0/1 TRUNK-ROUTER` |
| Servidor Linux `ONLINE` | Disponibilidade de host/agente no período | Chamadas SIP ou autenticação RADIUS |
| Windows `No data` | Consulta do painel sem valor útil | Energia do host, agente, item, consulta e intervalo |

**Valores ausentes exigem duas verificações distintas.** Primeiro, conferir se o item Zabbix possui dados recentes válidos. Se não houver, investigar host/IP, interface de coleta, agent/SNMP e erro do item. Se houver, conferir fonte do Grafana, consulta, período, variáveis e filtros. Não “corrigir” rótulos repetidos antes de identificar o item original. Consulte o [runbook Grafana sem dados](../operacoes-noc/runbooks/grafana-sem-dados.md).

As capturas **não** incluem configurações completas de fontes de dados ou exports JSON dos dashboards; um painel visualmente correto comprova a interface observada, não reprodução integral pelo GitHub. Os valores são de **6 de novembro de 2026**, sem novos testes nesta revisão.

## Pendências de Verificação

| Sintoma registrado | Verificação necessária |
|---|---|
| Cinco painéis Windows com `No data` | Estado do item Zabbix, consulta Grafana, identidade do host e intervalo |
| Rótulos repetidos nas interfaces Cisco | Identidade dos itens/interfaces Zabbix e mapeamento físico das portas |
| Portas `UP`/`DOWN` | Estado operacional esperado conforme a topologia atual |
| Registros históricos de HTTP e disponibilidade | Testes funcionais independentes dos serviços, quando necessários |
| Configuração de dashboards não exportada | Obter fontes de dados e JSON antes de afirmar reprodução completa dos dashboards |

**Registros relacionados:** [Monitoramento Zabbix](zabbix.md) · [Diagnóstico SNMP](diagnostico-snmp.md) · [Serviços Docker](../containers/servicos-docker.md)

As dez capturas originais acima foram preservadas de **6 de novembro de 2026**. Não comprovam resolução posterior dos incidentes.
