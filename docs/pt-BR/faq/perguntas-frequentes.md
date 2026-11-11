# Enterprise NOC — Perguntas Frequentes (FAQ)

[English](../../faq/technical-faq.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch  
**Organização:** Tapajós Inovações  
**Ambiente:** Laboratório físico de infraestrutura empresarial  
**Idiomas da documentação:** Inglês e português brasileiro  

---

## Apresentação

Este FAQ reúne respostas para as principais dúvidas técnicas sobre o projeto Enterprise NOC — From Scratch.

O conteúdo abrange a infraestrutura física, equipamentos Cisco, servidores Linux, containers Docker, monitoramento, serviços corporativos, diagnóstico de problemas e evidências da implementação.

O objetivo é explicar não apenas quais tecnologias fazem parte do ambiente, mas também suas funções, integração, decisões técnicas e limitações documentadas.

O FAQ complementa a documentação do projeto. Ele não substitui os registros de configuração, inventários ou procedimentos operacionais.

## Índice

1. Fundamentos do Projeto
2. Infraestrutura Física e Hardware
3. Redes Cisco e VLANs
4. Redes Wireless e IoT
5. Linux, Docker e Infraestrutura de Containers
6. Monitoramento e Observabilidade
7. Serviços de Infraestrutura Corporativa
8. Segurança, Troubleshooting e Evidências

---

# 1. Fundamentos do Projeto

### 01. O que é o Enterprise NOC — From Scratch?

Laboratório físico de infraestrutura corporativa com redes Cisco, Linux, Docker, VoIP, DNS e monitoramento centralizado. O repositório reúne configurações, inventários, registros de diagnóstico e evidências datadas.

### 02. A Tapajós Inovações é uma empresa real?

Não. A Tapajós Inovações é o cenário empresarial fictício; os equipamentos e os registros do laboratório são reais.

### 03. Por que o projeto foi desenvolvido em torno de um NOC?

Para integrar implantação de redes, disponibilidade dos serviços, monitoramento e diagnóstico em um mesmo ambiente documentado. O modelo NOC organiza essas atividades operacionais.

### 04. Quais problemas empresariais o projeto procura resolver?

O cenário fictício apresenta quatro problemas: cabeamento instável, Wi-Fi sem proteção adequada, telefonia IP instável e monitoramento insuficiente. São requisitos do cenário, não falhas atuais comprovadas.

### 05. A infraestrutura foi desenvolvida para utilização em produção?

Não há certificação de ambiente produtivo. O projeto demonstra implantação e monitoramento em equipamentos físicos de laboratório; produção exigiria validação própria de segurança, backup, resiliência e operação.

### 06. Qual é o período abrangido pela documentação?

Os registros abrangem outubro e novembro de 2026, incluindo a configuração do switch de 4 de novembro e os inventários e dashboards coletados em 6 de novembro. Cada registro corresponde à sua data de coleta.

**Documentação relacionada:**

- [README do Projeto](../../../README.pt-BR.md)
- [Visão Geral da Infraestrutura](../arquitetura/visao-geral-da-infraestrutura.md)
- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)

---

# 2. Infraestrutura Física e Hardware

### 07. Quais equipamentos físicos de rede são utilizados?

Os principais equipamentos de rede são:

- Roteador Cisco Catalyst C8200L.
- Switch Cisco Catalyst C9200L.
- Equipamentos wireless TP-Link Archer AX53.
- Patch panel de categoria 6.
- Rack de rede e cabeamento Ethernet estruturado.

O laboratório também possui computadores Linux, estações Windows, telefones IP Grandstream e um dispositivo Amazon Alexa.

Cada componente desempenha uma função específica na infraestrutura física ou lógica.

### 08. Qual é a função do rack e do patch panel?

O rack centraliza e organiza os equipamentos de rede, o cabeamento e os componentes de suporte da infraestrutura.

O patch panel fornece pontos de terminação para o cabeamento estruturado e permite organizar as conexões por meio de patch cords.

A separação entre o cabeamento fixo e as conexões aos equipamentos facilita a manutenção, a organização e a identificação dos pontos de rede.

As fotografias documentam a instalação, mas não constituem um laudo completo de certificação de todos os cabos.

### 09. Qual padrão de cabeamento Ethernet foi utilizado?

O laboratório utiliza a pinagem T568A na confecção manual dos cabos Ethernet.

A sequência dos condutores é:

| Pino | Cor do fio |
|---|---|
| 1 | Branco/Verde |
| 2 | Verde |
| 3 | Branco/Laranja |
| 4 | Azul |
| 5 | Branco/Azul |
| 6 | Laranja |
| 7 | Branco/Marrom |
| 8 | Marrom |

Em um cabo direto confeccionado nesse padrão, as duas extremidades utilizam a mesma sequência T568A.

A identificação T568A registra a ordem dos condutores; o inventário fotográfico não é um laudo elétrico dos enlaces.

### 10. Quantos computadores fazem parte do laboratório?

O inventário da infraestrutura registra dez computadores:

| Departamento ou Função | Computadores |
|---|---:|
| TI / NOC | 2 |
| Contabilidade | 3 |
| Financeiro | 2 |
| Vendas | 2 |
| Servidor Asterisk / FreeRADIUS | 1 |
| **Total** | **10** |

Oito computadores executam Windows, enquanto dois desempenham funções de infraestrutura Linux.

As especificações individuais foram registradas quando estavam disponíveis nas evidências coletadas.

### 11. Os dois computadores Linux possuem configurações idênticas?

Os computadores possuem características de hardware semelhantes, incluindo modelos Dell OptiPlex 3020, processadores Intel Core i5-4590 e aproximadamente 8 GB de memória RAM.

Entretanto, possuem funções diferentes.

O computador principal do NOC executa Debian GNU/Linux 13 (Trixie) e hospeda o ambiente Docker.

O segundo computador executa o ambiente Debian forky/sid registrado no inventário e disponibiliza Asterisk e FreeRADIUS.

Portanto, não devem ser tratados como sistemas com versões idênticas do sistema operacional.

### 12. O que as fotografias da infraestrutura comprovam?

As fotografias documentam a presença e a organização física dos equipamentos no momento da coleta.

Elas mostram o rack, os equipamentos Cisco, o patch panel, o cabeamento estruturado e determinadas estações de trabalho.

As fotografias documentam a instalação física; roteamento, políticas de acesso e disponibilidade pertencem aos respectivos registros técnicos.

Essas propriedades dependem de configurações e testes operacionais correspondentes.

**Documentação relacionada:**

- [Infraestrutura Física](../evidencias/infraestrutura-fisica.md)
- [Inventário de Computadores](../estacoes/inventario-de-computadores.md)
- [Registro de Coleta de Evidências](../evidencias/registro-coleta-2026-11-06.md)

---

# 3. Redes Cisco e VLANs

### 13. Qual é a função do roteador e do switch Cisco?

O C8200L é o roteador da arquitetura; o C9200L documenta comutação, VLANs e o trunk voltado ao roteador. Não foi coletada a configuração completa do C8200L. Veja [roteador](../redes/roteador-c8200l.md) e [registro do switch](../redes/registro-switch-vlans-2026-11-04.md).

### 14. Por que a infraestrutura utiliza sete VLANs?

As VLANs **10/20/30/40/50/60/70** separam TI/NOC, Contabilidade, Financeiro, Vendas, VoIP/Autenticação, Wi-Fi corporativo e IoT em camada 2. Veja o [inventário de VLANs](../redes/vlans.md).

### 15. Qual é a função do trunk entre o roteador e o switch?

Um trunk pode transportar várias VLANs identificadas por tags. A interface `Gi1/0/1` do switch está configurada como trunk para o roteador; a lista de VLANs permitidas e a interface correspondente no roteador não foram coletadas. Veja o [registro do switch](../redes/registro-switch-vlans-2026-11-04.md).

### 16. Como as interfaces do switch estão distribuídas?

A captura de 4 de novembro atribui `Gi1/0/2–3` à VLAN 10, `4–6` à 20, `7–8` à 30, `9–10` à 40, `11–13` à 50, `14` à 70 e `15` à 60. Veja o [mapa de portas](../redes/mapa-de-portas-switch.md).

### 17. Por que a interface Gi1/0/11 recebe uma observação especial?

A `Gi1/0/11` contém `switchport access vlan 50` e `spanning-tree portfast trunk`, mas não apresenta `switchport mode access` explícito. A captura não estabelece seu modo operacional efetivo. Veja o [mapa de portas](../redes/mapa-de-portas-switch.md).

### 18. Como os endereços IP são atribuídos às estações?

As estações utilizam DHCP. Os gateways observados foram `192.168.10.1`, `.20.1`, `.30.1` e `.40.1`; o servidor e os pools DHCP não foram estabelecidos. Veja [VLANs](../redes/vlans.md).

### 19. As VLANs departamentais estão completamente isoladas?

As VLANs do switch separam os segmentos em camada 2. O isolamento completo em camada 3 e a aplicação das ACLs não foram verificados; essas restrições permanecem requisitos arquiteturais. Veja [VLANs](../redes/vlans.md).

### 20. O roteamento entre VLANs e o NAT estão completamente documentados?

Não. Há registros do C8200L físico, do trunk no lado do switch e dos gateways observados, mas não das subinterfaces completas do roteador, regras NAT ou testes de roteamento ponta a ponta. Veja [C8200L](../redes/roteador-c8200l.md).

**Documentação relacionada:**

- [Segmentação por VLANs](../redes/vlans.md)
- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)
- [Cisco Catalyst C8200L](../redes/roteador-c8200l.md)
- [Mapa de Portas do Switch](../redes/mapa-de-portas-switch.md)
- [Registro de Configuração do Switch](../redes/registro-switch-vlans-2026-11-04.md)

---

# 4. Redes Wireless e IoT

### 21. Por que são utilizados dois TP-Link Archer AX53?

Eles atendem funções distintas: Wi-Fi corporativo (VLAN 60) e IoT (VLAN 70). São dois Archer AX53 físicos separados.

### 22. Quais interfaces do switch conectam as redes wireless?

O C9200L registra Wi-Fi corporativo em `Gi1/0/15` (VLAN 60) e IoT em `Gi1/0/14` (VLAN 70). Veja o [mapa de portas](../redes/mapa-de-portas-switch.md).

### 23. Como a Amazon Alexa está integrada à infraestrutura?

A Amazon Alexa está associada ao Archer AX53 de IoT, ligado ao C9200L na VLAN 70. O endereço IP da Alexa e a conectividade em nível de aplicação não foram registrados. Veja [IoT](../redes/iot-vlan70.md).

### 24. Os roteadores wireless funcionam em modo access point?

As configurações não foram coletadas. O modo AP pode conectar clientes à VLAN upstream; o modo roteador/NAT pode usar sub-redes próprias. Nenhum modo foi confirmado. Veja [Wi-Fi](../redes/wifi-corporativo-vlan60.md) e [IoT](../redes/iot-vlan70.md).

### 25. A autenticação do Wi-Fi corporativo utiliza FreeRADIUS?

Há um serviço FreeRADIUS documentado na VLAN 50, mas não há configuração de cliente RADIUS no AX53 ou logs de autenticação wireless para confirmar essa integração. Veja [Asterisk/FreeRADIUS](../servicos/asterisk-freeradius.md).

**Documentação relacionada:**

- [Wi-Fi Corporativo — VLAN 60](../redes/wifi-corporativo-vlan60.md)
- [Rede IoT — VLAN 70](../redes/iot-vlan70.md)
- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)

---

# 5. Linux, Docker e Infraestrutura de Containers

### 26. Qual é a configuração do computador principal do NOC?

O NOC utiliza um Dell OptiPlex 3020 com Intel i5-4590, aproximadamente 8 GB de RAM, Debian 13 e `192.168.10.12/24`. Ele hospeda os serviços principais de Docker/monitoramento. Veja o [inventário](../estacoes/inventario-de-computadores.md).

### 27. Por que o Docker é utilizado no projeto?

Docker executa aplicações de infraestrutura em containers, e o Compose define serviços e dependências. Isso não implica alta disponibilidade. Veja [serviços Docker](../containers/servicos-docker.md).

### 28. Quais containers estavam em execução durante a coleta?

Em 6 de novembro, dez containers foram registrados em execução: `reverse-proxy`, `zabbix-web`, `zabbix-server`, `uptime-kuma`, `zabbix-db`, `grafana`, `zabbix-agent`, `site-estatico`, `pihole` e `portainer`. Veja o [inventário Docker](../containers/servicos-docker.md).

### 29. Qual é a diferença entre Docker Compose e Portainer?

O Compose define implantações de containers em YAML; o Portainer fornece uma interface gráfica de administração Docker. Ambos estão presentes no laboratório.

### 30. Por que Nginx e Apache são utilizados simultaneamente?

Nginx funciona como proxy reverso; Apache serve o site corporativo estático pelo container `site-estatico`. Veja [serviços Docker](../containers/servicos-docker.md).

### 31. Qual é a função do MariaDB?

MariaDB armazena os dados de monitoramento do Zabbix no container `zabbix-db`. Veja [serviços Docker](../containers/servicos-docker.md).

### 32. É possível reproduzir toda a infraestrutura Docker diretamente pelo GitHub?

Não como implantação verificada em um único comando. Os arquivos Compose públicos foram sanitizados e não incluem segredos locais, certificados, dados persistentes e requisitos específicos dos hosts. Veja [serviços Docker](../containers/servicos-docker.md).

**Documentação relacionada:**

- [Infraestrutura Docker e Serviços](../containers/servicos-docker.md)
- [Inventário de Computadores](../estacoes/inventario-de-computadores.md)
- [Configuração Docker Compose](../../../docker_configs/docker-compose.yml)

---

# 6. Monitoramento e Observabilidade

### 33. Por que Zabbix e Grafana são utilizados juntos?

Zabbix coleta e processa itens de monitoramento; Grafana os apresenta por meio da integração com o Zabbix. Veja [Zabbix](../monitoramento/zabbix.md) e [Grafana](../monitoramento/grafana.md).

### 34. Qual era a dimensão do ambiente de monitoramento Zabbix?

A captura de 6 de novembro registrou **12 hosts, 1.820 itens, 1.698 habilitados, 113 não suportados e 34 triggers em estado de problema**. Veja as [evidências do Zabbix](../monitoramento/zabbix.md).

### 35. Como os equipamentos Cisco e os sistemas operacionais são monitorados?

Equipamentos Cisco utilizam interfaces SNMP no Zabbix; hosts Linux/Windows utilizam interfaces Zabbix Agent. Os dashboards apresentam CPU, memória, tráfego e estado de interfaces. Veja [Zabbix](../monitoramento/zabbix.md).

### 36. O problema de SNMP do switch Cisco foi resolvido?

Sim, no **caso SNMP registrado em 4 de novembro**: a divergência da comunidade foi corrigida, configurou-se `{$SNMP_COMMUNITY}` e o cache de monitoramento foi atualizado, restabelecendo a descoberta. Isso não implica correção de outros alertas posteriores. Veja o [caso SNMP](../monitoramento/diagnostico-snmp.md).

### 37. Por que alguns computadores apareciam como `No data` no Grafana?

Em 6 de novembro, três painéis de estações mostravam `ONLINE` e cinco `No data`. A ausência de valores pode envolver agentes, endereçamento, itens ou intervalo selecionado; as capturas não estabelecem causa única. Veja [Grafana](../monitoramento/grafana.md).

### 38. Como o DHCP pode afetar o monitoramento do Zabbix?

Seis endereços IPv4 divergiam entre os registros das estações e os cadastros do Zabbix. Alterações por DHCP podem contribuir, sem comprovar causa comum. Veja o [inventário](../estacoes/inventario-de-computadores.md).

### 39. O que significam os 113 itens não suportados no Zabbix?

Os **113 itens não suportados** não forneciam dados válidos nas configurações de coleta registradas. A captura não estabelece a causa individual de cada item; o diagnóstico deve ser feito por item. Veja [Zabbix](../monitoramento/zabbix.md).

### 40. Por que utilizar Uptime Kuma se o Zabbix já monitora disponibilidade?

Zabbix coleta métricas e alertas de infraestrutura; Uptime Kuma verifica alvos específicos e registra eventos. O dashboard coletado do Kuma tinha quatro monitores. Veja [DNS e disponibilidade](../servicos/dns-e-disponibilidade.md).

**Documentação relacionada:**

- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)
- [Troubleshooting SNMP](../monitoramento/diagnostico-snmp.md)
- [DNS e Disponibilidade](../servicos/dns-e-disponibilidade.md)

---

# 7. Serviços de Infraestrutura Corporativa

### 41. Para que o Asterisk é utilizado?

Asterisk disponibiliza telefonia IP SIP/PJSIP no servidor Debian de voz da VLAN 50. Veja [Asterisk/FreeRADIUS](../servicos/asterisk-freeradius.md).

### 42. Quais ramais telefônicos estão configurados?

Os ramais **1001 (Vendas)** e **1002 (TI)** correspondem aos telefones Grandstream em `192.168.50.10` e `192.168.50.11`. Veja [Asterisk](../servicos/asterisk-freeradius.md).

### 43. O funcionamento das chamadas telefônicas foi comprovado?

Não há registros de chamadas ou gravações independentes que comprovem chamadas entre os dois telefones fotografados. As configurações e os ramais estão documentados. Veja [telefonia](../servicos/asterisk-freeradius.md).

### 44. Qual é a função do FreeRADIUS?

FreeRADIUS oferece autenticação de rede no servidor Debian da VLAN 50. A autenticação bem-sucedida de clientes Wi-Fi pelo AX53 não foi comprovada de forma independente. Veja [FreeRADIUS](../servicos/asterisk-freeradius.md).

### 45. O que o Pi-hole acrescenta à infraestrutura?

Pi-hole filtra consultas DNS e registra atividade de clientes/domínios. Em 6 de novembro, o dashboard mostrava **12.293 consultas, 1.827 bloqueadas (14,9%) e 13 clientes ativos** no período exibido. Veja [evidências DNS](../servicos/dns-e-disponibilidade.md).

### 46. O Uptime Kuma garante que os serviços estejam sempre disponíveis?

Não. O Kuma registrava verificações de **quatro alvos**; um resultado positivo não garante saúde contínua das aplicações ou SLA. Veja [monitoramento de disponibilidade](../servicos/dns-e-disponibilidade.md).

**Documentação relacionada:**

- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [Filtragem DNS e Disponibilidade](../servicos/dns-e-disponibilidade.md)

---

# 8. Segurança, Troubleshooting e Evidências

### 47. Um indicador verde no monitoramento comprova que o serviço funciona corretamente?

Não. O indicador verde confirma somente a condição monitorada. Testes funcionais e logs continuam necessários para avaliar o comportamento da aplicação.

### 48. Por que credenciais e configurações sensíveis não são publicadas no GitHub?

O repositório é público.

A publicação de senhas, comunidades SNMP, credenciais de bancos de dados, chaves privadas, segredos de autenticação ou identificadores sensíveis de equipamentos introduziria riscos desnecessários.

Por isso, os exemplos públicos de configuração utilizam valores sanitizados e omitem informações operacionais privadas.

O objetivo é preservar a utilidade técnica da documentação sem expor credenciais ou dados confidenciais.

### 49. Quais atividades de troubleshooting possuem resultados documentados?

O registro de troubleshooting SNMP do Cisco Catalyst C9200L apresenta três casos:

1. Monitoramento SNMP indisponível devido à divergência entre comunidades.
2. Exibição incorreta do uptime do switch devido a um item de monitoramento inadequado.
3. Widgets vazios no dashboard devido a filtros restritivos de hosts.

O documento descreve a investigação, os ajustes realizados e os resultados observados.

Esses casos constituem evidências de atividades reais de diagnóstico técnico.

### 50. Todos os problemas de monitoramento foram documentados como resolvidos?

Não.

As capturas incluem itens não suportados, hosts indisponíveis, inconsistências de endereçamento e painéis do Grafana sem dados.

Algumas situações possuem investigações e resultados documentados, enquanto outras permanecem como observações históricas sem resolução individual comprovada.

O projeto diferencia essas situações em vez de apresentar todos os alertas como incidentes resolvidos.

Procedimentos operacionais e runbooks adicionais fazem parte de uma seção própria de documentação NOC.

### 51. A análise financeira representa os valores realmente gastos no projeto?

Não.

A documentação financeira utiliza cenários de custos e estimativas de referência.

Os cenários diferenciam implantação completa do zero, utilização de equipamentos existentes e despesas recorrentes de operação e manutenção.

A análise depende da consolidação final do inventário e da verificação das premissas financeiras.

Subtotais parciais não devem ser interpretados como gastos reais confirmados.

### 52. Quais são as próximas prioridades do projeto?

O desenvolvimento continua com documentação técnica, revisão da consistência da infraestrutura, análise do monitoramento e elaboração de procedimentos operacionais.

A próxima grande área documental é **NOC Operations & Troubleshooting**.

Ela abordará classificação de incidentes, triagem de alertas, procedimentos de diagnóstico, ações corretivas, validação e registro de ocorrências.

A análise financeira será finalizada depois da consolidação do inventário técnico e das premissas restantes.

---

## Considerações Finais

Este FAQ foi elaborado com base na documentação técnica e nas evidências históricas disponíveis no repositório Enterprise NOC.

O conteúdo diferencia:

- Infraestrutura física e configurações observadas.
- Projetos técnicos e políticas previstas.
- Métricas históricas de monitoramento.
- Resultados documentados de troubleshooting.
- Detalhes de configuração ausentes dos registros históricos coletados.

As respostas devem ser atualizadas quando novas informações tecnicamente validadas forem incorporadas ao projeto.

Para consultar configurações, diagramas, inventários e capturas completas, utilize os documentos técnicos relacionados em cada seção.

**Enterprise NOC — From Scratch**  
*Da infraestrutura física às operações de rede.*
