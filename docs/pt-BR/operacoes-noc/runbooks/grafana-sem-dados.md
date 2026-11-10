# Runbook — Painel do Grafana Sem Dados

[English](../../../noc-operations/runbooks/grafana-no-data.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** MON · **Status:** Procedimento proposto; falhas históricas não são declaradas resolvidas  
**Ambiente:** Container Grafana OSS integrado ao Zabbix; host Debian do NOC

## 1. Objetivo e evidências históricas

Utilizar quando um painel do Grafana mostra `No data`, lacunas inesperadas ou identificação incorreta de host/interface. O Grafana visualiza métricas, mas **não determina sozinho o estado real** do equipamento. Em 06/11/2026, os painéis de estado das oito estações Windows mostravam **três `ONLINE` e cinco `No data`**. Alguns painéis do switch Cisco repetiam `Gi1/0/1 TRUNK-ROUTER`. Nenhuma dessas observações comprova uma causa comum.

O repositório também registra **113 itens não suportados**, cinco hosts indisponíveis no Zabbix e divergências de DHCP/endereço. São informações relevantes, não prova da causa de cada painel.

## 2. Segurança e preparação

- Obter acesso autorizado de leitura ao Grafana, Zabbix e host Debian.
- Registrar URL do dashboard, título/UID do painel quando disponível, intervalo, variáveis selecionadas e horário da captura.
- Inspecionar antes de alterar. Não mudar consultas, credenciais, permissões ou cadastros durante triagem inicial.
- Não publicar cookies, chaves de API, senhas de banco, dashboards privados ou exportações sensíveis da fonte de dados.

## 3. Delimitar a ocorrência

| Sintoma | Caminho de investigação |
|---|---|
| Todos os painéis vazios | Fonte/plugin Grafana, API Zabbix e intervalo geral |
| Um único painel vazio | Consulta, item, redução, transformação ou filtro |
| Apenas uma estação ausente | Host no Zabbix, IP, agente, itens e últimos valores |
| Gráfico histórico existe, estado atual não | Horários, função da consulta, filtros e triggers |
| Rótulo do switch repetido | Confirmar mapeamento item/interface; não inferir porta física só pelo texto |
| `No data` apenas em intervalo curto | Conferir frequência de coleta e intervalo maior autorizado |

## 4. Sequência de verificação

### A. Conferir o Grafana

No dashboard afetado:

1. Conferir organização, dashboard e variáveis de host.
2. Conferir início/fim do intervalo, fuso horário e atualização.
3. Utilizar inspeção do painel em **Inspect → Query / Data / Error** (nomes podem mudar por versão).
4. Conferir fonte Zabbix, host, item, transformações e função de redução.
5. Comparar com outro painel que utiliza a mesma fonte e recebe valores novos.

Um filtro que seleciona host/item sem dados no período pode produzir resultado vazio.

### B. Comparar com Zabbix

No frontend autorizado do Zabbix, abrir **Monitoramento → Dados recentes (Latest data)** para o mesmo host/item usado na consulta Grafana. Verificar:

- Host cadastrado e habilitado.
- Interface configurada correspondente ao endereço atual, considerando DHCP.
- Item habilitado e suportado.
- Valor válido com horário recente no intervalo analisado.
- Grupo, template, chave e item equivalentes aos selecionados no Grafana.

Se o Zabbix não tem dados atuais, investigar coleta antes de mexer no painel. Se tem dados, mas o Grafana não exibe, conferir fonte, consulta, filtros, plugin, transformações e tempo.

### C. Inspecionar containers

No host Debian, apenas leitura:

~~~bash
docker ps --filter name=grafana
docker ps --filter name=zabbix
docker logs --tail 100 --timestamps grafana
docker logs --tail 80 --timestamps zabbix-server
~~~

Teste HTTP local limitado (não prova consultas corretas):

~~~bash
curl -I --max-time 5 http://127.0.0.1:3000/login
~~~

O Compose público registra `GF_INSTALL_PLUGINS: alexanderzobnin-zabbix-app` e a porta **3000** do Grafana. Isso documenta configuração, não o estado atual do plugin nem versão instalada; conferir no ambiente.

### D. Percorrer o fluxo dos dados

~~~text
Host Cisco / Linux / Windows
       |
       | SNMP ou Zabbix Agent
       v
Zabbix Server e métricas armazenadas
       |
       | Fonte Zabbix configurada no Grafana
       v
Consulta -> filtro / transformação -> painel
~~~

Testar cada camada. HTTP do Grafana respondendo não comprova Zabbix acessível nem consulta correta. Valor válido no Zabbix não garante configuração correta do painel.

## 5. Causa confirmada ou hipótese

| Descoberta | Interpretação possível |
|---|---|
| IP antigo no Zabbix e agente indisponível | Coleta pode estar apontando para endereço incorreto; confirmar primeiro |
| Item `Unsupported` | Investigar tipo de item, chave ou suporte de dispositivo/agente |
| Zabbix atualizado, consulta Grafana seleciona outro host | Divergência na consulta/variável |
| Dados brutos presentes, gráfico vazio | Transformação, mapeamento, unidade ou formato |
| Timeout ou erro de API | Investigar plugin, rede e API Zabbix |
| Rótulos Cisco duplicados | Problema de mapeamento até conferir índices de interface |

## 6. Correção autorizada

Somente após comprovar a causa, propor alteração mínima: ajustar variável, item ou transformação; corrigir item não suportado; atualizar cadastro de host identificado corretamente; ou reparar falha demonstrada de fonte/plugin. Obter autorização e salvar versão/exportação sanitizada do dashboard antes de mexer. Não esconder falha de coleta substituindo métricas reais por números estáticos.

## 7. Validação da recuperação

1. Confirmar valor recente e válido do item no Zabbix.
2. Atualizar o painel Grafana e inspecionar a resposta da consulta.
3. Comparar intervalo relevante curto com período maior compatível com amostragem.
4. Validar rótulos da interface/host e unidades.
5. Registrar horários antes/depois, alteração da consulta, exceções e estado do incidente.

## 8. Registro da investigação

Preservar identificadores dashboard/painel, intervalo, host/item Zabbix, horário do último valor, erro, camadas investigadas, mudança aprovada, nova medida e capturas. Não classificar os cinco painéis `No data` de 06/11 como corrigidos sem evidência posterior.

## 9. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Dashboards e limitações Grafana](../../monitoramento/grafana.md)
- [Zabbix e itens não suportados](../../monitoramento/zabbix.md)
- [Runbook Zabbix Agent](conectividade-zabbix-agent.md)
- [Caso de troubleshooting SNMP](../../monitoramento/diagnostico-snmp.md)
- [Infraestrutura Docker](../../containers/servicos-docker.md)

**Status:** Processo de diagnóstico recomendado; nenhuma correção nova de painel é afirmada.