# Simulação de Incidentes e Validação da Recuperação

[English](../../noc-operations/incident-simulation-and-validation.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Área:** NOC Operations & Troubleshooting  
**Tipo de documento:** **Catálogo de cenários e modelo de registro de exercícios** — não é histórico de execução  
**Infraestrutura:** Cisco C8200L/C9200L, VLANs 10–70, Debian, Docker, Zabbix, Grafana e Uptime Kuma

## 1. Objetivo

Desenvolver capacidade de resposta a incidentes exige mais do que interpretar screenshots. Este documento define como planejar exercícios **seguros, controlados e reversíveis**, validar a recuperação e preservar evidências. Os cenários descritos são exercícios de referência, não recuperações registradas. Eventuais registros datados de execução permanecem separados deste catálogo.

Os casos SNMP de 04/11/2026 são intervenções históricas descritas separadamente. As capturas Zabbix/Grafana de 06/11 mostram condições de monitoramento, não comprovação de que as simulações abaixo foram executadas.

## 2. Modalidades de exercício e evidências

| Classificação | Significado | Regra para publicação |
|---|---|---|
| **TABLETOP** | Discussão de cenário hipotético usando topologia e documentação | Registrar como análise de cenário, não teste técnico |
| **READ-ONLY** | Observar host/serviço sem alterar seu estado | Registrar comandos, horário e resultados reais |
| **CONTROLLED LAB TEST** | Experimento autorizado e delimitado, com restauração validada | Publicar resultado somente após execução e evidência de recuperação |
| **HISTORICAL CASE** | Troubleshooting anterior com registro original | Citar data e resultado do documento de origem |
| **SCENARIO ONLY** | Cenário de referência sem registro de execução | Não apresentar como teste aprovado |

Um exercício TABLETOP ou SCENARIO ONLY não constitui registro de recuperação técnica.

## 3. Autorização e limites do ambiente

Antes de qualquer teste, exigir:

- Responsável técnico identificado e autorização explícita do laboratório ou instrutor supervisor.
- Host, VLAN, serviço e duração definidos; autorização não é genérica para toda a rede.
- Confirmação de que usuários ou serviços compartilhados não dependem de continuidade durante o teste.
- Janela de início/fim, comunicação, condição de interrupção e reversão documentadas.
- Backup atual ou ponto de recuperação pertinente à mudança.
- Método de observação seguro e local adequado para evidências sanitizadas.
- Critérios funcionais para aceitar recuperação.

**Não utilizar como simulações casuais:** desconectar trunk principal do roteador, alterar ACLs sem reversão comprovada, apagar volumes Docker, destruir arquivos, modificar credenciais, desativar controles de segurança ou expor registros privados de DNS/autenticação.

Se isolamento e recuperação não estiverem garantidos, escolher **TABLETOP** ou **READ-ONLY**.

## 4. Coleta do estado inicial

Registrar baseline **antes** de propor teste controlado. Capturas de 06/11/2026 são contexto histórico, não substituem medições do dia do exercício.

| Área | Evidência inicial |
|---|---|
| Host | Hostname, VLAN, IP, estado e data/fuso atuais |
| Rede | Estado esperado de interface/VLAN e testes autorizados |
| Docker | Estado do container, health check se existir, logs e dependências |
| Zabbix | Host/item/trigger, último valor válido e erro |
| Grafana | Dashboard, painel/consulta, intervalo e última amostra |
| Uptime Kuma | Monitor, tipo de verificação e estado no início |
| Serviço | Teste funcional independente: DNS, HTTP ou outro aplicável |

Não considerar indicador de dashboard, sozinho, prova de recuperação funcional.

## 5. Matriz de exercícios

São **cenários de referência** que não exigem provocar interrupções sem autorização.

| ID | Cenário | Modalidade inicial segura | Foco da validação | Runbook |
|---|---|---|---|---|
| EX-01 | Suspeita de agente parado ou endereço antigo | TABLETOP + inspeção de agente atual | Distinguir falha do agente, DHCP e indisponibilidade do host | [Zabbix Agent](runbooks/conectividade-zabbix-agent.md) |
| EX-02 | Porta do switch aparece `DOWN` inesperadamente | TABLETOP + comandos Cisco de leitura | Confirmar função esperada e mapeamento SNMP | [Interfaces Cisco](runbooks/interface-cisco-indisponivel.md) |
| EX-03 | Nome DNS não resolve | TABLETOP + consulta DNS de leitura autorizada | Separar DNS de rota, blocklist e aplicação | [Resolução DNS](runbooks/falhas-resolucao-dns.md) |
| EX-04 | Container em estado `Exited` ou indisponível | TABLETOP + inspeção atual de logs/saúde | Rastrear dependências e resposta da aplicação | [Docker](runbooks/falhas-servicos-docker.md) |
| EX-05 | Alerta de CPU, RAM ou disco | TABLETOP + medições não disruptivas | Confirmar pressão real independente do gráfico | [Recursos](runbooks/utilizacao-recursos-sistema.md) |
| EX-06 | Grafana exibe `No data` | TABLETOP + comparação painel/Zabbix | Localizar problema na coleta ou visualização | [Grafana](runbooks/grafana-sem-dados.md) |

Interrupção controlada é **opcional** e não necessária para completar a documentação tabletop/read-only. Se houver autorização futura, o método exato será planejado separadamente para o alvo isolado, sem autorização implícita deste arquivo.

## 6. Ciclo do exercício

### 6.1 Planejamento

1. Definir hipótese precisa e categoria do possível incidente.
2. Estabelecer critério observável de detecção e função do serviço a avaliar.
3. Identificar VLAN, host e dependências.
4. Definir critérios de parada e responsável pela reversão.
5. Escolher evidências reais e formato de registro.

### 6.2 Estado inicial

1. Registrar data/fuso e identidade do alvo.
2. Capturar estado não disruptivo no Zabbix/Grafana e no serviço.
3. Confirmar adequação do ambiente ao exercício.
4. Verificar disponibilidade do caminho de restauração aprovado.

### 6.3 Execução somente do escopo aprovado

No tabletop, discutir ações sem tocar na infraestrutura. Na modalidade read-only, executar apenas inspeções autorizadas e registrar a **saída verdadeira**. No teste controlado, não exceder o plano técnico aprovado. Interromper caso serviços inesperados, VLANs, controles de segurança ou dados sejam afetados.

### 6.4 Diagnóstico e documentação

Separar sintomas, causas comprovadas e hipóteses. Preservar ordem temporal e lacunas de monitoramento. Ausência de dados no Zabbix ou Grafana não comprova automaticamente queda do serviço.

### 6.5 Recuperação e validação

Aplicar restauração combinada quando pertinente. Comparar comportamento com baseline. Confirmar funcionalidade **e** novas métricas relevantes quando disponíveis. Um exercício que não possa ser recuperado com segurança deve ser interrompido e escalonado, nunca declarado bem-sucedido.

### 6.6 Revisão

Registrar por que a evidência apoiou ou rejeitou hipótese, o que o monitoramento não identificou e qual runbook deve ser melhorado. Informar explicitamente caminhos ainda não testados.

## 7. Critérios de aceitação

Um **teste controlado** só recebe **PASSED** quando os requisitos pertinentes forem sustentados por evidências com data e horário:

- Baseline registrado e mudança autorizada conhecida.
- Observação pretendida registrada, sem impactos proibidos.
- Funcionalidade afetada restaurada ao estado esperado.
- Coleta de métricas retomada ou lacunas restantes documentadas.
- Ações de recuperação e reversão rastreáveis.
- Nenhum segredo confidencial publicado.

TABLETOP recebe **WALKTHROUGH COMPLETED**, não recuperação da infraestrutura. Inspeção READ-ONLY pode receber **OBSERVATION COMPLETED**, não **incidente resolvido**.

Rótulos possíveis: `PLANNED`, `NOT EXECUTED`, `WALKTHROUGH COMPLETED`, `OBSERVATION COMPLETED`, `PASSED`, `FAILED`, `ABORTED`, `INCONCLUSIVE`.

## 8. Modelo reutilizável de registro

~~~markdown
# Exercício NOC — [EX-ID]

## Identificação
- Cenário:
- Modalidade: TABLETOP / READ-ONLY / CONTROLLED LAB TEST
- Status: PLANNED / NOT EXECUTED / ...
- Operador responsável e autorização:
- Data, horário e fuso:
- Host, rede e serviço:

## Objetivo e Hipótese
- Comportamento esperado:
- Hipótese de causa ou falha:
- Limites do impacto:

## Autorização e Segurança
- Escopo autorizado:
- Critérios para interromper:
- Plano de recuperação/reversão:
- Backup ou ponto de retorno:

## Baseline
| Horário | Origem da evidência | Valor ou observação real |
|---|---|---|
| | | |

## Execução
| Horário | Ação realmente realizada | Saída/observação real |
|---|---|---|
| | | |

## Diagnóstico
- Observações confirmadas:
- Hipóteses não comprovadas:
- Causa identificada (se houver evidência):

## Recuperação e Verificação
- Ação corretiva autorizada (se houver):
- Teste funcional independente:
- Validação do monitoramento:
- Questões restantes:

## Resultado
- Status:
- Justificativa:
- Links das evidências sanitizadas:
- Lições aprendidas:
- Responsável por acompanhamento:
~~~

Não preencher saídas hipotéticas de console nem marcar teste como aprovado sem execução correspondente.

## 9. Casos históricos versus novos exercícios

O [registro de troubleshooting SNMP do Cisco C9200L](../monitoramento/diagnostico-snmp.md) descreve três investigações **históricas** de 04/11:

1. Divergência de comunidade SNMP e restauração da coleta.
2. Item de uptime incorreto e sua correção.
3. Widgets vazios por filtros restritivos, posteriormente ajustados.

São estudos de caso úteis, mas **não** equivalem a novas execuções EX-01 a EX-06. Os 113 itens não suportados e painéis `No data` de 06/11 não devem ser descritos como resolvidos sem evidência posterior.

## 10. Critérios de conclusão da seção NOC

A documentação está estruturalmente concluída quando o gerenciamento de incidentes, os seis runbooks e este método de simulação/validação estiverem publicados em português e inglês, com links válidos.

Isso é **conclusão documental**, não certificação da infraestrutura, tempo de recuperação, estrutura de pessoal, resolução de todos os incidentes ou conformidade com SLA.

Resultados de exercícios registrados separadamente pertencem aos documentos de incidentes ou evidências correspondentes, sem gerar relatórios hipotéticos adicionais.

## 11. Referências

- [Gerenciamento de Incidentes](gerenciamento-de-incidentes.md)
- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)
- [Evidências Históricas Zabbix](../monitoramento/zabbix.md)
- [Evidências Históricas Grafana](../monitoramento/grafana.md)
- [Troubleshooting Histórico SNMP](../monitoramento/diagnostico-snmp.md)
- [Registro da Coleta de Evidências](../evidencias/registro-coleta-2026-11-06.md)

**Escopo documental:** Catálogo de cenários, orientações seguras e modelo de registro. O documento não atribui resultados de execução a esses cenários.