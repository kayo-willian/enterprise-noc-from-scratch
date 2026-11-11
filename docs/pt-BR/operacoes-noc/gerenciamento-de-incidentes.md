# Operações NOC — Gerenciamento de Incidentes

[English](../../noc-operations/incident-management.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch  
**Organização:** Tapajós Inovações  
**Ambiente:** Laboratório físico de infraestrutura empresarial  
**Tipo de documento:** Processo operacional e modelo de gerenciamento de incidentes  
**Escopo:** Infraestrutura de rede, servidores Linux, plataformas de monitoramento, containers e serviços corporativos  

---

## 1. Visão Geral

Este documento define classificação, priorização, triagem, escalonamento, validação da recuperação e registro de incidentes no laboratório Enterprise NOC. É uma referência operacional, não um registro de um NOC produtivo em funcionamento.

Os procedimentos abrangem rede, sistemas Linux, serviços Docker e componentes de monitoramento documentados no repositório.

## 2. Ambiente Operacional

Os procedimentos abrangem a rede Cisco C8200L/C9200L, VLANs 10–70, servidores Debian, aplicações Docker, estações Windows, telefonia IP, DNS e monitoramento Zabbix/Grafana. Consulte a [topologia de rede](../redes/topologia-logica-consolidada.md) e a [documentação dos serviços](../containers/servicos-docker.md) para atribuições e dependências; este processo não reproduz os inventários.

## 3. Eventos, Alertas, Incidentes e Problemas

| Termo | Significado operacional |
|---|---|
| **Evento** | Mudança de estado observável, como transição de interface ou reinício de container. |
| **Alerta** | Indicação de monitoramento gerada por uma condição configurada; exige avaliação. |
| **Incidente** | Interrupção ou degradação não planejada de serviço, confirmada. |
| **Problema** | Causa subjacente ou suspeita de um ou mais incidentes. |

**Falha de monitoramento não significa necessariamente falha de infraestrutura.** Agente indisponível, item não suportado ou painel vazio do Grafana precisam ser verificados antes de declarar uma interrupção. Da mesma forma, um indicador ativo não comprova funcionamento ponta a ponta da aplicação.

### Diferenciando Sinal Técnico de Incidente

Esses conceitos estavam detalhados na versão anterior da gestão de incidentes e são importantes para interpretar os screenshots históricos do NOC.

- **Evento:** transição ou amostra observada, como mudança de porta, reinício de container ou ausência de resposta do agente. Pode ser esperado.
- **Alerta:** condição que atingiu regra de monitoramento ou trigger. Indica uma **situação a investigar**, não necessariamente indisponibilidade para usuários.
- **Incidente:** interrupção ou degradação confirmada do serviço esperado. Antes de declarar, identificar função afetada, período e impacto.
- **Problema:** causa subjacente ou suspeita de um ou mais incidentes. Sem diagnóstico, continua sendo hipótese.

**Exemplo — cinco painéis Windows com `No data`:** é uma **observação de monitoramento** Grafana/Zabbix. Não demonstra que cinco PCs estavam desligados, que endereços de agentes ficaram desatualizados ou que filtros estavam incorretos. Deve-se comparar estado do item Zabbix, endereços atuais, alcance do agente e, havendo reclamação, **acesso real da estação à aplicação**.

**Exemplo — porta do switch em `DOWN`:** a relevância depende de haver endpoint ativo esperado. Porta sem uso pode estar down normalmente; perda confirmada de trunk/uplink necessário exigiria análise de impacto. É preciso correlacionar mapa de portas registrado e estado atual.

**Exemplo — divergência de comunidade SNMP:** o [caso de 4 de novembro](../monitoramento/diagnostico-snmp.md) registra uma falha específica de monitoramento, causa, correção e recuperação da descoberta. Não explica automaticamente agentes indisponíveis, itens não suportados ou outros incidentes das capturas de 6 de novembro.

O fluxo NOC deve preservar **sinal observado → impacto verificado → evidência da causa → ação autorizada → validação funcional**, separando fatos e hipóteses. Os seis [runbooks](runbooks/conectividade-zabbix-agent.md) trazem verificações específicas sem duplicar todos os comandos neste documento de gestão.


## 4. Objetivos do Gerenciamento de Incidentes

Detectar e confirmar impacto, classificar gravidade, investigar com evidências, autorizar a correção, verificar a recuperação e registrar o resultado. As etapas estão detalhadas no ciclo de vida abaixo.

## 5. Classificação dos Incidentes

Os incidentes podem ser classificados conforme a camada da infraestrutura afetada.

| Categoria | Componentes | Exemplo |
|---|---|---|
| NET | Roteamento e switching Cisco | Falha confirmada de conectividade em uma VLAN |
| MON | Zabbix, Grafana e agentes | Indisponibilidade na coleta de monitoramento |
| SYS | Sistemas Linux e Windows | Falha do sistema operacional de um host |
| CNT | Docker e aplicações conteinerizadas | Container de aplicação necessária indisponível |
| DNS | Pi-hole e resolução de nomes | Falha comprovada na resolução de domínios necessários |
| VOIP | Asterisk e telefones IP | Ramal interno incapaz de completar chamadas |
| AUTH | FreeRADIUS | Falha de autenticação confirmada |
| WEB | Aplicações internas e proxy reverso | Aplicação indisponível pelo endereço esperado |
| PHY | Cabeamento e equipamentos físicos | Defeito físico comprovado em cabo ou enlace |

Essas categorias são identificadores de referência para organizar registros de incidentes.

Elas não representam uma configuração existente de sistema de chamados ou plataforma de gerenciamento de incidentes já implantada.

## 6. Modelo de Prioridade e Severidade

A prioridade de um incidente deve considerar dois fatores:

**Impacto:** Quantos sistemas, serviços ou funções operacionais foram afetados?

**Urgência:** Com que rapidez a situação precisa ser tratada para evitar ou reduzir prejuízos operacionais?

O modelo de referência utilizado na documentação é:

| Prioridade | Classificação | Descrição do Impacto | Cenário Ilustrativo |
|---|---|---|---|
| P1 | Crítica | Interrupção generalizada e confirmada de infraestrutura essencial | Perda de conectividade da rede central afetando vários segmentos necessários |
| P2 | Alta | Degradação significativa ou indisponibilidade de serviço compartilhado importante | Serviço DNS principal indisponível para clientes dependentes |
| P3 | Média | Interrupção limitada a um departamento ou sistema específico | Uma estação não consegue acessar uma aplicação interna necessária |
| P4 | Baixa | Problema operacional menor sem interrupção comprovada de serviço | Identificação incorreta em um painel secundário do dashboard |

### 6.1 Regras de Classificação

A prioridade deve ser determinada pelo impacto verificado, e não apenas pela aparência visual do alerta.

Um indicador vermelho no dashboard não representa automaticamente um incidente P1.

Da mesma forma, uma interface de monitoramento indisponível não comprova que o equipamento de rede ou sistema operacional correspondente esteja inoperante.

### 6.2 Revisão da Prioridade

A prioridade pode ser modificada quando novas informações forem identificadas.

Por exemplo, uma reclamação inicialmente isolada sobre DNS pode exigir reclassificação quando a investigação confirmar que vários departamentos foram afetados.

O motivo de qualquer alteração deve ser registrado.

### 6.3 Tempos de Resposta

Este documento não estabelece prazos contratuais de atendimento, garantias de recuperação ou acordos de nível de serviço (SLA).

Esta documentação não atribui SLA contratual nem metas de resposta mensuradas ao processo do laboratório.

## 7. Ciclo de Vida dos Incidentes

O ciclo de referência possui sete etapas.

```text
EVENTO OU COMUNICAÇÃO
          |
          v
1. DETECÇÃO
          |
          v
2. TRIAGEM
          |
          v
3. CLASSIFICAÇÃO
          |
          v
4. INVESTIGAÇÃO
          |
          v
5. AÇÃO CORRETIVA
          |
          v
6. VALIDAÇÃO
          |
          v
7. ENCERRAMENTO
          |
          v
DOCUMENTAÇÃO E REVISÃO
```

Um incidente pode retornar à etapa de investigação quando a validação não confirmar a recuperação.

O escalonamento pode ocorrer em qualquer etapa quando os recursos técnicos ou as permissões disponíveis forem insuficientes.

### 7.1 Detecção

Os possíveis incidentes podem ser identificados por:

- Eventos do Zabbix.
- Dashboards do Grafana.
- Verificações de disponibilidade do Uptime Kuma.
- Logs dos sistemas operacionais.
- Informações de estado dos equipamentos de rede.
- Relatos de usuários ou administradores do laboratório.

**Informações necessárias:**

- Data e horário da detecção.
- Origem do alerta ou canal de comunicação.
- Sistema afetado.
- Observação inicial.
- Evidências disponíveis.

### 7.2 Triagem

A triagem determina se a condição observada representa:

- Um incidente de serviço confirmado.
- Uma falha de monitoramento ou visualização.
- Um estado operacional esperado.
- Um evento que necessita de investigação adicional.

A avaliação inicial deve considerar se o serviço afetado continua executando sua função esperada.

Por exemplo, uma interface não utilizada do switch exibida como `DOWN` pode representar uma condição normal.

Um painel do Grafana exibindo `No data` exige investigação, mas não comprova automaticamente que o computador monitorado está desligado.

### 7.3 Classificação

Depois da avaliação inicial, devem ser registrados:

- Categoria do incidente.
- Componente afetado.
- Impacto confirmado ou suspeito.
- Prioridade atribuída.
- Estado da investigação.

Quando o impacto ainda não puder ser determinado, o registro deve indicar explicitamente que a condição permanece em investigação.

### 7.4 Investigação

A investigação deve seguir uma sequência técnica estruturada:

1. Confirmar o sintoma relatado.
2. Identificar o componente relevante da infraestrutura.
3. Examinar as informações de monitoramento correspondentes.
4. Comparar as observações com outras evidências técnicas.
5. Verificar configuração, conectividade ou estado do serviço conforme necessário.
6. Desenvolver e testar possíveis explicações.
7. Registrar os resultados encontrados.

As primeiras ações de diagnóstico devem priorizar verificações não disruptivas.

Modificações de configuração só devem ser realizadas depois da avaliação do impacto, das autorizações e dos requisitos de recuperação.

### 7.5 Ação Corretiva

As ações corretivas dependem da falha identificada.

Entre as possibilidades estão:

- Corrigir o endereço cadastrado de um host no monitoramento.
- Ajustar um item de monitoramento configurado incorretamente.
- Restaurar um serviço de aplicação necessário.
- Corrigir um erro identificado na configuração de rede.
- Resolver um problema comprovado de dependência entre serviços.

Esses são exemplos de ações possíveis, não afirmações de que todas foram executadas no laboratório.

Antes de realizar uma alteração, o registro operacional deve identificar:

- Resultado esperado.
- Componentes afetados.
- Backup da configuração ou alternativa de reversão pertinente.
- Possíveis efeitos colaterais.
- Autorizações necessárias.

### 7.6 Validação

Um incidente não deve ser considerado resolvido apenas porque a mensagem de erro desapareceu.

A validação deve confirmar que o sintoma original não está mais presente e que o comportamento esperado foi restaurado.

Dependendo do incidente, as evidências podem incluir:

- Conectividade bem-sucedida com o serviço.
- Coleta válida de dados de monitoramento.
- Estado correto da interface de rede.
- Resolução DNS funcionando.
- Resposta esperada da aplicação.
- Atualização dos indicadores de monitoramento.
- Ausência da falha original durante um intervalo de observação adequado.

O método de validação deve corresponder ao serviço afetado.

Por exemplo, restaurar a comunicação do Zabbix Agent confirma a conectividade do monitoramento, mas não comprova que todas as aplicações hospedadas no computador estejam funcionando corretamente.

### 7.7 Encerramento

Um incidente documentado pode ser encerrado quando:

- A condição do serviço ou monitoramento foi validada.
- A ação corretiva está registrada.
- O impacto final foi identificado.
- As evidências relevantes foram preservadas.
- As limitações restantes foram identificadas.
- O resultado recebeu uma classificação adequada de encerramento.

Quando não for possível comprovar a recuperação, o registro não deve afirmar uma resolução bem-sucedida.

Entre as possíveis classificações de encerramento estão:

- Resolvido e validado.
- Mitigado, com limitações restantes.
- Encaminhado para investigação adicional.
- Encerrado como falso positivo de monitoramento.
- Encerrado como condição operacional esperada.

A classificação final precisa ser sustentada pelas evidências da investigação.

## 8. Modelo de Escalonamento

O escalonamento ocorre quando um incidente não pode ser investigado ou resolvido adequadamente dentro do escopo operacional disponível.

O laboratório não possui uma estrutura de produção com escala de plantão ou equipes designadas comprovada.

As responsabilidades abaixo descrevem funções técnicas do fluxo de referência, não cargos formalmente atribuídos.

| Função Técnica | Responsabilidade |
|---|---|
| Monitoramento e triagem | Analisar alertas, verificar sintomas e registrar o impacto inicial |
| Administração de redes | Investigar roteamento, switching, VLANs e conectividade física |
| Administração Linux e infraestrutura | Investigar sistemas operacionais, serviços, armazenamento e Docker |
| Administração de aplicações | Investigar DNS, VoIP, autenticação e aplicações web internas |
| Coordenação técnica | Avaliar impactos, autorizar ações disruptivas e manter os registros dos incidentes |

### Critérios de Escalonamento

O escalonamento deve ser considerado quando:

- O incidente afeta múltiplos segmentos da rede.
- A causa permanece desconhecida após as verificações iniciais.
- A ação corretiva pode interromper serviços compartilhados.
- Não existe acesso autorizado à configuração necessária.
- O incidente envolve autenticação ou infraestrutura sensível.
- A falha reaparece após uma recuperação aparentemente bem-sucedida.
- É necessária investigação adicional em equipamentos físicos.

O escalonamento não elimina a necessidade de preservar o histórico da investigação inicial.

## 9. Coleta de Evidências Operacionais

Os registros de incidentes devem preservar informações suficientes para reconstruir a investigação técnica.

### 9.1 Evidências Mínimas

| Evidência | Finalidade |
|---|---|
| Data e horário | Estabelecer a sequência das observações |
| Componente afetado | Identificar o recurso da infraestrutura |
| Sintoma inicial | Descrever o comportamento observado |
| Referência do monitoramento | Identificar informações relacionadas do Zabbix, Grafana ou Uptime Kuma |
| Observações do diagnóstico | Sustentar ou descartar possíveis causas |
| Ação corretiva | Registrar o que foi alterado |
| Resultado da validação | Comprovar se o comportamento esperado retornou |
| Status final | Diferenciar recuperação de condições não resolvidas |

### 9.2 Registro de Horários

Os relatórios de incidentes devem registrar data, horário e fuso horário das observações relevantes.

Quando os registros são provenientes de sistemas diferentes, devem ser consideradas possíveis diferenças de fuso e sincronização dos relógios.

Capturas históricas não devem ser apresentadas como medições atuais dos sistemas.

### 9.3 Informações Sensíveis

Os relatórios públicos não devem expor:

- Senhas e segredos de autenticação.
- Valores de comunidades SNMP.
- Chaves privadas.
- Tokens de sessão.
- Informações pessoais de usuários.
- Identificadores confidenciais da infraestrutura.

As evidências originais devem permanecer separadas das cópias sanitizadas utilizadas no repositório público.

## 10. Evidências Históricas de Troubleshooting

Três casos de diagnóstico SNMP do Cisco foram registrados em **4 de novembro de 2026**: monitoramento indisponível por divergência de comunidade; uptime incorreto do switch; e widgets sem valores esperados. A investigação, as correções e os resultados constam do [estudo de caso SNMP](../monitoramento/diagnostico-snmp.md).

São intervenções históricas, não execuções dos procedimentos hipotéticos deste documento.

## 11. Condições Históricas de Monitoramento

As evidências de **6 de novembro de 2026** incluem seis divergências entre endereços das estações e cadastros no Zabbix, painéis `No data` no Grafana e indicadores `UP`/`DOWN` das interfaces Cisco. Isoladamente, esses registros não estabelecem causa comum ou incidente de serviço.

Consulte os registros específicos de [Zabbix](../monitoramento/zabbix.md), [Grafana](../monitoramento/grafana.md) e o [runbook de interfaces Cisco](runbooks/interface-cisco-indisponivel.md) para as observações e os critérios de diagnóstico.

## 12. Modelo de Registro de Incidentes

O modelo reutilizável a seguir define um formato consistente para registros de incidentes.

Ele não representa um relatório de incidente já concluído.

```markdown
# Relatório de Incidente — [Identificador]

## Identificação

- ID do incidente:
- Data:
- Horário da detecção e fuso:
- Categoria:
- Prioridade:
- Componente afetado:
- Segmento de rede:
- Origem da detecção:
- Função técnica responsável:

## Observação Inicial

Descrever o sintoma relatado e como foi identificado.

## Impacto Operacional

Identificar sistemas, serviços e usuários afetados.

Separar impactos confirmados de impactos suspeitos.

## Investigação

Registrar as ações de diagnóstico em ordem cronológica.

| Horário | Ação | Observação |
|---|---|---|
| | | |
| | | |

## Causa Raiz

Descrever a causa identificada.

Caso não tenha sido determinada, registrar o estado da investigação.

## Ação Corretiva

Descrever as alterações ou ações de recuperação realmente realizadas.

## Validação

- Procedimento de validação:
- Resultado esperado:
- Resultado observado:
- Evidências:

## Status Final

- Resultado:
- Data e horário do encerramento:
- Limitações restantes:
- Ações de acompanhamento:

## Lições Aprendidas

Registrar os conhecimentos técnicos obtidos e oportunidades de prevenção.

## Referências das Evidências

Listar logs sanitizados, capturas, registros de configuração
ou documentos relacionados do repositório.
```

### Identificação dos Incidentes

Um possível formato de identificação é:

`NOC-YYYYMMDD-001`

Esse formato é um modelo de relatório, não uma afirmação de implantação de sistema de chamados numerados.

## 13. Exemplos Ilustrativos de Classificação

Os exemplos abaixo ilustram a classificação de situações operacionais pelo processo de referência.

São **cenários hipotéticos**, não novos incidentes apresentados como ocorrências reais do laboratório.

| Cenário | Classificação Inicial | Verificação Necessária |
|---|---|---|
| Múltiplas VLANs perdem acesso aos recursos necessários | Possível P1 | Confirmar abrangência, gateways e serviços afetados |
| DNS interno fica indisponível para vários departamentos | Possível P2 | Confirmar a falha de resolução e o impacto nos clientes |
| Uma estação Windows deixa de responder | Possível P3 | Diferenciar falha do host de falha de monitoramento |
| Uma porta não utilizada do switch aparece como `DOWN` | Pode não representar incidente | Confirmar o estado operacional esperado |
| Grafana apresenta `No data` em um painel | Investigação de monitoramento | Conferir fonte de dados, consulta, item e host |
| Identificação visual incorreta em um dashboard com métricas válidas | Possível P4 | Confirmar integridade dos dados e impacto apenas visual |

A prioridade final deve ser determinada pelo impacto e pela urgência reais.

## 14. Revisão Operacional e Melhoria Contínua

Revisar recorrência de incidentes, falsos positivos, registros incompletos e eficácia das correções. Quantidades, reincidência e tempos de resposta só devem ser publicados como métricas operacionais quando houver registros datados correspondentes.

## 15. Relação com os Runbooks Técnicos

O gerenciamento de incidentes define ciclo, prioridade e escalonamento. Os seis runbooks bilíngues abaixo documentam diagnósticos não disruptivos, interpretação de resultados, autorização e validação adaptados à infraestrutura.

| Assunto técnico | Runbook |
|---|---|
| Conectividade Zabbix Agent | [Investigar agente e endereçamento](runbooks/conectividade-zabbix-agent.md) |
| Interface Cisco indisponível | [Investigar enlace, VLAN e mapeamento](runbooks/interface-cisco-indisponivel.md) |
| Falhas de resolução DNS | [Investigar Pi-hole, consultas e filtragem](runbooks/falhas-resolucao-dns.md) |
| Falhas de serviços Docker | [Investigar Docker, Compose e dependências](runbooks/falhas-servicos-docker.md) |
| CPU, memória ou disco elevados | [Investigar utilização de recursos](runbooks/utilizacao-recursos-sistema.md) |
| Grafana `No data` | [Distinguir coleta e visualização](runbooks/grafana-sem-dados.md) |

O documento complementar [Simulação de Incidentes e Validação da Recuperação](simulacao-e-validacao-de-incidentes.md) define planejamento, autorização, baseline, classificação de resultados e preservação de evidências.

**A publicação de um runbook não comprova a execução dos procedimentos hipotéticos.** Os casos SNMP anteriores continuam documentados separadamente como troubleshooting histórico.

## 16. Escopo da Documentação

Este documento descreve um processo de referência, associado a seis runbooks de diagnóstico e a um catálogo de exercícios. Não comprova NOC produtivo com equipe, plataforma de chamados, SLA contratado ou recuperações concluídas além dos registros históricos específicos.

## 17. Documentação Relacionada

- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)
- [Roteador Cisco Catalyst C8200L](../redes/roteador-c8200l.md)
- [Mapa de Portas do Switch](../redes/mapa-de-portas-switch.md)
- [Inventário de Computadores](../estacoes/inventario-de-computadores.md)
- [Infraestrutura Docker](../containers/servicos-docker.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)
- [Diagnóstico SNMP](../monitoramento/diagnostico-snmp.md)
- [DNS e Disponibilidade](../servicos/dns-e-disponibilidade.md)
- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [FAQ Técnico](../faq/perguntas-frequentes.md)

---

**Classificação do documento:** Processo de referência de gerenciamento de incidentes NOC.  
**Referências das evidências históricas:** 04 a 06/11/2026.  
**Procedimentos NOC relacionados:** Seis runbooks técnicos bilíngues e o modelo de simulação e validação de incidentes, vinculados na Seção 15.

**Enterprise NOC — From Scratch**  
*Da infraestrutura física às operações de rede.*
