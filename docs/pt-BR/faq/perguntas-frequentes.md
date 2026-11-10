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

O Enterprise NOC — From Scratch é um projeto prático de infraestrutura empresarial desenvolvido em laboratório físico de treinamento.

Ele integra equipamentos de rede Cisco, estações de trabalho, servidores Linux, aplicações conteinerizadas, telefonia IP, serviços DNS e monitoramento centralizado.

O projeto documenta a implantação da infraestrutura, a segmentação da rede, a integração entre serviços, as observações operacionais e as atividades de diagnóstico técnico.

### 02. A Tapajós Inovações é uma empresa real?

Não. A Tapajós Inovações é uma organização fictícia criada para estabelecer os requisitos empresariais e contextualizar o projeto.

Entretanto, o laboratório de infraestrutura é real.

Os equipamentos, a instalação física, os inventários e as capturas de monitoramento representam atividades técnicas realizadas no ambiente de treinamento.

O cenário empresarial fictício não deve ser confundido com uma implantação corporativa em produção.

### 03. Por que o projeto foi desenvolvido em torno de um NOC?

Um Network Operations Center (NOC), ou Centro de Operações de Rede, permite centralizar a observação da disponibilidade, dos eventos operacionais e do desempenho da infraestrutura.

O projeto utiliza esse conceito para integrar administração de redes, monitoramento e troubleshooting.

Em vez de apresentar configurações isoladas, a infraestrutura demonstra como equipamentos de rede, sistemas operacionais, aplicações e plataformas de monitoramento se relacionam.

### 04. Quais problemas empresariais o projeto procura resolver?

O cenário empresarial simulado apresenta quatro desafios:

- Cabeamento estruturado com problemas de confiabilidade.
- Rede wireless com controles de segurança insuficientes.
- Instabilidade na telefonia IP interna.
- Ausência de monitoramento centralizado da infraestrutura.

O projeto responde a essas necessidades por meio de cabeamento estruturado, segmentação de redes, serviços dedicados e monitoramento centralizado.

Esses problemas fazem parte dos requisitos iniciais da empresa fictícia. Não representam falhas comprovadamente contínuas no laboratório físico.

### 05. A infraestrutura foi desenvolvida para utilização em produção?

O ambiente foi desenvolvido para educação técnica e implementação prática de infraestrutura.

Ele demonstra conceitos de redes empresariais utilizando equipamentos e serviços reais, mas não é apresentado como uma infraestrutura certificada para produção.

Uma implantação em produção exigiria validações adicionais de segurança, procedimentos de backup, requisitos de disponibilidade, revisão de configurações e testes operacionais.

### 06. Qual é o período abrangido pela documentação?

O repositório contém registros técnicos produzidos em outubro e novembro de 2026.

Entre as principais evidências estão a configuração do switch Cisco coletada em 04/11 e os inventários, registros de serviços e capturas de monitoramento de 06/11.

O período documentado de desenvolvimento do laboratório se estende até 17/11/2026.

Cada fotografia, captura ou configuração representa seu respectivo momento de coleta, não necessariamente o estado atual da infraestrutura.

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

A identificação do padrão não comprova, isoladamente, o desempenho elétrico de todos os cabos confeccionados.

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

Entretanto, fotografias isoladas não comprovam roteamento funcional entre todas as VLANs, aplicação correta das políticas de acesso, funcionamento de todas as interfaces ou disponibilidade contínua dos serviços.

Essas propriedades dependem de configurações e testes operacionais correspondentes.

**Documentação relacionada:**

- [Infraestrutura Física](../evidencias/infraestrutura-fisica.md)
- [Inventário de Computadores](../estacoes/inventario-de-computadores.md)
- [Registro de Coleta de Evidências](../evidencias/registro-coleta-2026-11-06.md)

---

# 3. Redes Cisco e VLANs

### 13. Qual é a função do roteador e do switch Cisco?

O Cisco Catalyst C8200L é a plataforma de roteamento associada à comunicação entre os segmentos da rede corporativa.

O Cisco Catalyst C9200L fornece comutação Ethernet e segmentação por VLANs para estações, servidores, telefones IP e equipamentos wireless.

A configuração do switch contém uma interface trunk associada à conexão com o roteador.

A configuração completa do lado do roteador não foi incluída nas evidências disponíveis.

### 14. Por que a infraestrutura utiliza sete VLANs?

As VLANs permitem separar logicamente departamentos e serviços da infraestrutura em camada 2.

A organização documentada é:

| VLAN | Finalidade |
|---|---|
| 10 | TI / NOC |
| 20 | Contabilidade |
| 30 | Financeiro |
| 40 | Vendas |
| 50 | VoIP e autenticação |
| 60 | Wi-Fi corporativo |
| 70 | IoT |

Essa estrutura organiza o tráfego e estabelece uma base para a aplicação de políticas de acesso.

A separação por VLAN, isoladamente, não garante segurança entre redes que possuem roteamento.

### 15. Qual é a função do trunk entre o roteador e o switch?

Uma interface trunk pode transportar tráfego associado a diferentes VLANs utilizando identificação por tags.

A configuração coletada do Catalyst C9200L identifica a interface `Gi1/0/1` como trunk conectado ao roteador.

Isso sustenta a arquitetura prevista para múltiplas VLANs.

Entretanto, a configuração do lado do switch não comprova, isoladamente, a configuração correspondente no roteador nem a comunicação bem-sucedida entre todas as VLANs.

### 16. Como as interfaces do switch estão distribuídas?

A configuração de 04/11 registra atribuições para os departamentos e serviços da infraestrutura.

As interfaces `Gi1/0/2–3` estão associadas à VLAN 10, `Gi1/0/4–6` à VLAN 20, `Gi1/0/7–8` à VLAN 30 e `Gi1/0/9–10` à VLAN 40.

As demais atribuições documentadas incluem a VLAN 50 para telefonia, `Gi1/0/14` para IoT e `Gi1/0/15` para Wi-Fi corporativo.

O mapeamento detalhado é mantido em documento específico.

### 17. Por que a interface Gi1/0/11 recebe uma observação especial?

A configuração histórica da interface `Gi1/0/11` apresenta:

```cisco
switchport access vlan 50
spanning-tree portfast trunk
```

Diferentemente das outras interfaces de acesso documentadas, ela não apresenta o comando explícito `switchport mode access`.

Além disso, possui uma instrução de PortFast para trunk.

Por isso, a documentação preserva a associação à VLAN 50 sem afirmar um modo operacional que não tenha sido estabelecido de forma independente.

### 18. Como os endereços IP são atribuídos às estações?

O laboratório utiliza DHCP para o endereçamento dos computadores.

As configurações de rede coletadas identificam gateways padrão como:

| VLAN | Gateway observado |
|---|---|
| 10 | `192.168.10.1` |
| 20 | `192.168.20.1` |
| 30 | `192.168.30.1` |
| 40 | `192.168.40.1` |

Esses valores correspondem às configurações observadas nas estações.

Os registros disponíveis não estabelecem a configuração completa do servidor DHCP, os pools de endereços ou eventuais mecanismos de relay.

### 19. As VLANs departamentais estão completamente isoladas?

A arquitetura prevista restringe a comunicação não autorizada entre departamentos e limita o acesso aos recursos administrativos.

Entretanto, uma configuração de VLAN não equivale à comprovação de uma política de controle de acesso.

As evidências disponíveis do roteador não incluem uma configuração completa de ACLs nem testes abrangentes de comunicação entre VLANs.

Por isso, o isolamento departamental é documentado como requisito arquitetural, e não como uma implementação de segurança integralmente validada.

### 20. O roteamento entre VLANs e o NAT estão completamente documentados?

Não.

As evidências identificam o roteador Cisco, o trunk no lado do switch, o projeto das VLANs, os gateways observados e os dashboards de monitoramento do roteador.

Entretanto, não incluem o `running-config` completo do C8200L.

As subinterfaces exatas, regras de NAT, configuração de conectividade externa e comunicação entre todas as VLANs não foram estabelecidas de forma independente pelos registros coletados.

**Documentação relacionada:**

- [Segmentação por VLANs](../redes/vlans.md)
- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)
- [Cisco Catalyst C8200L](../redes/roteador-c8200l.md)
- [Mapa de Portas do Switch](../redes/mapa-de-portas-switch.md)
- [Registro de Configuração do Switch](../redes/registro-switch-vlans-2026-11-04.md)

---

# 4. Redes Wireless e IoT

### 21. Por que são utilizados dois TP-Link Archer AX53?

A infraestrutura separa a conectividade wireless corporativa da conectividade IoT.

Um TP-Link Archer AX53 está associado à VLAN 60, enquanto outro equipamento dedicado está associado à VLAN 70.

Os dois dispositivos representam segmentos físicos wireless distintos no projeto do laboratório.

Essa separação permite documentar e administrar as funções das redes de maneira independente.

### 22. Quais interfaces do switch conectam as redes wireless?

A configuração do Catalyst C9200L de 04/11 identifica:

| Interface | VLAN | Função |
|---|---|---|
| `Gi1/0/15` | 60 | Wi-Fi corporativo |
| `Gi1/0/14` | 70 | Conectividade IoT |

Essas atribuições aparecem na configuração registrada do switch.

A evidência do switch, isoladamente, não comprova a configuração wireless completa ou a aplicação efetiva das políticas de isolamento.

### 23. Como a Amazon Alexa está integrada à infraestrutura?

O laboratório possui uma Amazon Alexa associada à rede wireless dedicada aos dispositivos IoT.

A conectividade documentada é:

```text
Amazon Alexa
     |
   Wi-Fi
     |
TP-Link Archer AX53
     |
  Ethernet
     |
Cisco Catalyst C9200L
     |
   VLAN 70
```

A topologia descreve a relação física entre o dispositivo wireless e o switch.

Ela não estabelece, isoladamente, o endereço IP da Alexa ou sua conectividade completa com aplicações externas.

### 24. Os roteadores wireless funcionam em modo access point?

As evidências coletadas não estabelecem os modos de operação dos equipamentos.

Um dispositivo configurado como access point pode conectar seus clientes ao segmento de rede associado.

Já um equipamento funcionando como roteador pode utilizar NAT e disponibilizar uma sub-rede própria aos clientes.

Sem a exportação das configurações correspondentes, a documentação não atribui nenhum desses comportamentos aos equipamentos instalados.

### 25. A autenticação do Wi-Fi corporativo utiliza FreeRADIUS?

A infraestrutura possui um servidor FreeRADIUS e uma arquitetura documentada de autenticação de rede.

Entretanto, as evidências coletadas não demonstram de forma independente autenticação bem-sucedida entre o Archer AX53 fotografado e o FreeRADIUS.

A presença dos dois componentes não comprova uma integração RADIUS wireless concluída.

O comportamento da autenticação precisa ser sustentado por configurações e registros de transações antes de ser apresentado como operacionalmente validado.

**Documentação relacionada:**

- [Wi-Fi Corporativo — VLAN 60](../redes/wifi-corporativo-vlan60.md)
- [Rede IoT — VLAN 70](../redes/iot-vlan70.md)
- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)

---

# 5. Linux, Docker e Infraestrutura de Containers

### 26. Qual é a configuração do computador principal do NOC?

O computador principal da infraestrutura é um Dell OptiPlex 3020 executando Debian GNU/Linux 13.

As especificações documentadas incluem:

| Componente | Especificação |
|---|---|
| Processador | Intel Core i5-4590 |
| Memória | Aproximadamente 8 GB |
| Sistema operacional | Debian 13 |
| Endereço IPv4 | `192.168.10.12/24` |
| Segmento | VLAN 10 |

Esse computador hospeda o principal ambiente Docker e diversos serviços de infraestrutura.

### 27. Por que o Docker é utilizado no projeto?

O Docker oferece uma estrutura organizada para executar aplicações de infraestrutura em containers.

O projeto utiliza containers para hospedar serviços de monitoramento, interfaces de gerenciamento, aplicações DNS, bancos de dados e componentes web.

Essa abordagem separa os ambientes das aplicações e facilita a organização das dependências.

A conteinerização não fornece automaticamente alta disponibilidade, isolamento completo de segurança ou proteção dos dados persistentes.

### 28. Quais containers estavam em execução durante a coleta?

O inventário de 06/11 registrou dez containers ativos:

1. `reverse-proxy`
2. `zabbix-web`
3. `zabbix-server`
4. `uptime-kuma`
5. `zabbix-db`
6. `grafana`
7. `zabbix-agent`
8. `site-estatico`
9. `pihole`
10. `portainer`

Os nomes foram obtidos do inventário Docker registrado.

A captura comprova o estado de execução naquele momento, não a continuidade da operação.

### 29. Qual é a diferença entre Docker Compose e Portainer?

O Docker Compose permite definir e administrar aplicações compostas por múltiplos containers utilizando arquivos declarativos de configuração.

O Portainer fornece uma interface gráfica para inspecionar e gerenciar ambientes Docker.

No laboratório, as duas ferramentas possuem funções complementares.

O Compose descreve a estrutura de implantação, enquanto o Portainer facilita a visualização operacional de containers, imagens e redes.

### 30. Por que Nginx e Apache são utilizados simultaneamente?

Eles possuem funções diferentes.

O Nginx é utilizado como proxy reverso, disponibilizando uma camada centralizada de acesso a determinados serviços web.

O Apache HTTP Server hospeda um site corporativo estático através do container `site-estatico`.

Essa organização separa o encaminhamento das requisições web da disponibilização do conteúdo do site.

### 31. Qual é a função do MariaDB?

O MariaDB fornece armazenamento de banco de dados para o ambiente Zabbix.

A implantação Docker documentada possui um container específico chamado `zabbix-db`.

O Zabbix Server processa as informações de monitoramento, enquanto o banco de dados atende às necessidades de armazenamento da plataforma.

A arquitetura separa o banco de dados da interface de monitoramento e das ferramentas de visualização.

### 32. É possível reproduzir toda a infraestrutura Docker diretamente pelo GitHub?

O repositório disponibiliza arquivos Docker Compose sanitizados e exemplos de configurações.

Entretanto, esses arquivos não são apresentados como uma reprodução completa do laboratório, validada para execução automática com um único comando.

Certificados locais, credenciais, dados persistentes das aplicações, parâmetros específicos das máquinas e outros pré-requisitos foram excluídos da configuração pública.

Uma nova implantação exige análise e adaptação dessas dependências.

**Documentação relacionada:**

- [Infraestrutura Docker e Serviços](../containers/servicos-docker.md)
- [Inventário de Computadores](../estacoes/inventario-de-computadores.md)
- [Configuração Docker Compose](../../../docker_configs/docker-compose.yml)

---

# 6. Monitoramento e Observabilidade

### 33. Por que Zabbix e Grafana são utilizados juntos?

O Zabbix é responsável pela coleta e pelo processamento das informações de monitoramento por meio de hosts, interfaces, itens, templates e triggers.

O Grafana fornece uma camada de visualização através de sua integração com o Zabbix.

A combinação permite centralizar a coleta das métricas e apresentá-las em dashboards organizados por equipamentos de rede, sistemas operacionais e serviços.

O Grafana não substitui a coleta de informações realizada pelo Zabbix.

### 34. Qual era a dimensão do ambiente de monitoramento Zabbix?

A captura das informações do sistema em 06/11 registra:

| Métrica | Valor |
|---|---:|
| Hosts cadastrados | 12 |
| Total de itens | 1.820 |
| Itens habilitados | 1.698 |
| Itens não suportados | 113 |
| Triggers em estado de problema | 34 |

Esses números representam uma observação histórica do sistema.

A presença de itens não suportados e problemas ativos demonstra que o ambiente ainda apresentava situações operacionais que exigiam investigação.

### 35. Como os equipamentos Cisco e os sistemas operacionais são monitorados?

O roteador e o switch Cisco aparecem no monitoramento por meio de interfaces SNMP.

Os sistemas Linux e Windows utilizam interfaces do Zabbix Agent para o monitoramento do sistema operacional.

O SNMP fornece acesso a métricas suportadas pelos equipamentos de rede, enquanto os agentes coletam informações dos sistemas.

Os dashboards incluem consumo de CPU, memória, tráfego, estado de interfaces e indicadores de serviços.

### 36. O problema de SNMP do switch Cisco foi resolvido?

O registro de troubleshooting de 04/11 documenta um problema de conectividade SNMP causado pela divergência entre os valores de comunidade configurados no switch e no Zabbix.

As configurações foram alinhadas, a macro `{$SNMP_COMMUNITY}` foi definida no host e o cache de configuração do monitoramento foi recarregado.

O resultado documentado foi a recuperação da disponibilidade SNMP e da descoberta de interfaces.

Esse é um caso de troubleshooting registrado, diferente de problemas que não possuem resolução documentada.

### 37. Por que alguns computadores apareciam como `No data` no Grafana?

As evidências do Grafana de 06/11 incluem oito estações Windows.

Três apareciam como `ONLINE`, enquanto cinco painéis exibiam `No data`.

A ausência de dados não significa necessariamente que o computador estivesse desligado.

Possíveis explicações incluem indisponibilidade do agente, divergências de endereçamento, problemas na configuração dos itens ou ausência de informações no intervalo consultado.

Os registros disponíveis não estabelecem uma causa definitiva para todos os painéis.

### 38. Como o DHCP pode afetar o monitoramento do Zabbix?

O laboratório utiliza DHCP para atribuir endereços IP às estações.

A coleta identificou seis divergências entre os endereços fotografados nos computadores e os endereços registrados nos respectivos hosts do Zabbix.

Quando um computador recebe outro endereço IP e o cadastro no Zabbix mantém o endereço anterior, a comunicação com o agente pode ser afetada.

Essa é uma explicação relevante para parte das inconsistências, mas não comprova a causa de todos os hosts indisponíveis.

### 39. O que significam os 113 itens não suportados no Zabbix?

Um item não suportado é um item de monitoramento que não consegue fornecer dados válidos através do método configurado.

Entre as possíveis causas estão chaves incompatíveis, métricas não suportadas, interfaces incorretas, permissões insuficientes e problemas de configuração.

A captura de 06/11 registra 113 itens nessa condição.

Entretanto, a imagem não identifica individualmente as causas. Um diagnóstico específico depende da análise da configuração dos itens afetados.

### 40. Por que utilizar Uptime Kuma se o Zabbix já monitora disponibilidade?

As duas aplicações oferecem funcionalidades complementares.

O Zabbix permite monitorar métricas da infraestrutura, triggers e condições dos hosts.

O Uptime Kuma concentra-se em verificações de disponibilidade e no histórico de eventos dos alvos selecionados.

A captura do laboratório registra quatro monitores configurados no Uptime Kuma. Isso não demonstra que todos os containers, computadores ou equipamentos de rede fossem monitorados individualmente pela ferramenta.

**Documentação relacionada:**

- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)
- [Troubleshooting SNMP](../monitoramento/diagnostico-snmp.md)
- [DNS e Disponibilidade](../servicos/dns-e-disponibilidade.md)

---

# 7. Serviços de Infraestrutura Corporativa

### 41. Para que o Asterisk é utilizado?

O Asterisk fornece a funcionalidade de telefonia IP do laboratório.

A configuração documentada utiliza SIP/PJSIP para registro dos dispositivos e sinalização de chamadas, enquanto o RTP é utilizado para o transporte de mídia de voz.

O servidor está associado à VLAN 50 e executa em um computador Linux dedicado.

A documentação também descreve um dialplan interno para encaminhamento entre ramais e testes.

### 42. Quais ramais telefônicos estão configurados?

O ambiente documentado possui dois telefones Grandstream:

| Ramal | Departamento | Endereço IP |
|---|---|---|
| 1001 | Vendas | `192.168.50.10` |
| 1002 | TI | `192.168.50.11` |

As fotografias de 06/11 comprovam a presença física dos dispositivos e os endereços apresentados em suas telas.

Os modelos exatos dos telefones não foram estabelecidos com segurança pelas fotografias disponíveis.

### 43. O funcionamento das chamadas telefônicas foi comprovado?

Os registros técnicos descrevem a configuração do Asterisk, os ramais e o dialplan.

Um relatório técnico anterior identifica os ramais como disponíveis durante sua observação.

Entretanto, as evidências coletadas não incluem gravações independentes ou registros detalhados que comprovem a execução bem-sucedida de todos os testes configurados.

Por isso, a implementação é documentada sem afirmar uma validação completa de telefonia ponta a ponta.

### 44. Qual é a função do FreeRADIUS?

O FreeRADIUS fornece funcionalidades de autenticação centralizada de rede.

A configuração documentada inclui RADIUS e tecnologias de autenticação como EAP-PEAP e MSCHAPv2.

Ele executa junto ao Asterisk no computador Linux associado à VLAN 50.

Os registros técnicos descrevem a arquitetura de autenticação, mas não comprovam independentemente uma autenticação completa realizada a partir do equipamento wireless corporativo.

### 45. O que o Pi-hole acrescenta à infraestrutura?

O Pi-hole fornece filtragem DNS e visibilidade sobre consultas realizadas pelos clientes.

O dashboard de 06/11 registra:

| Métrica | Valor observado |
|---|---:|
| Consultas DNS | 12.293 |
| Consultas bloqueadas | 1.827 |
| Percentual bloqueado | 14,9% |
| Clientes ativos | 13 |

Esses valores correspondem ao período exibido no dashboard.

Eles não comprovam que todos os clientes e VLANs utilizavam obrigatoriamente a filtragem DNS.

### 46. O Uptime Kuma garante que os serviços estejam sempre disponíveis?

Não.

O dashboard coletado mostra quatro monitores configurados, todos apresentados como `Up` no momento da captura.

A aplicação também possui registros históricos de verificações de disponibilidade, incluindo ocorrências sem sucesso.

Um indicador positivo representa apenas as condições de monitoramento configuradas e o período correspondente.

Ele não garante disponibilidade contínua nem funcionamento correto de todas as funcionalidades de uma aplicação.

**Documentação relacionada:**

- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [Filtragem DNS e Disponibilidade](../servicos/dns-e-disponibilidade.md)

---

# 8. Segurança, Troubleshooting e Evidências

### 47. Um indicador verde no monitoramento comprova que o serviço funciona corretamente?

Não necessariamente.

Um indicador verde geralmente representa o atendimento de uma condição específica de monitoramento.

Por exemplo, uma aplicação pode responder a uma requisição HTTP enquanto outra funcionalidade permanece indisponível.

Os resultados de monitoramento devem ser interpretados em conjunto com verificações específicas dos serviços, configurações, logs e testes operacionais.

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
- Detalhes de implementação não estabelecidos pelas evidências disponíveis.

As respostas devem ser atualizadas quando novas informações tecnicamente validadas forem incorporadas ao projeto.

Para consultar configurações, diagramas, inventários e capturas completas, utilize os documentos técnicos relacionados em cada seção.

**Enterprise NOC — From Scratch**  
*Da infraestrutura física às operações de rede.*
