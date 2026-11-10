# Runbook — Utilização Elevada de CPU, Memória ou Disco

[English](../../../noc-operations/runbooks/host-resource-utilization.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** SYS / CNT / MON · **Tipo de documento:** Runbook de diagnóstico operacional  
**Ambiente:** Host Debian 13 do NOC, servidor Linux Asterisk/FreeRADIUS, estações Windows e serviços Docker

## 1. Objetivo e contexto histórico

Investigar CPU persistentemente alta, pressão de memória, falta de espaço, esgotamento de inodes ou degradação relacionada a recursos. O inventário de 06/11/2026 registra dois computadores Linux Dell OptiPlex 3020 com Intel Core i5-4590 e aproximadamente 8 GB RAM cada. O principal hospeda a stack Docker de monitoramento; o outro suporta Asterisk/FreeRADIUS. O Grafana apresenta métricas históricas, mas **não demonstra saturação atual nem incidente confirmado**.

Valor elevado em um gráfico não basta: correlacionar duração, impacto, carga esperada e medições independentes. O runbook não estabelece limites universais nem SLA mensurado.

## 2. Regras de segurança

- Obter autorização para inspecionar host, processos e logs.
- Priorizar leitura. Não encerrar processos, reiniciar bancos, apagar logs, aumentar limites, criar swap ou limpar caches apenas para melhorar indicador.
- Sanitizar caminhos, processos e logs antes de divulgação pública.
- O tamanho do sistema de arquivos raiz registrado não comprova a capacidade total do disco físico.

## 3. Matriz de triagem

| Sintoma | Questões relevantes |
|---|---|
| CPU alta | Por quanto tempo? Qual processo? Aplicação está lenta? |
| Load average elevado | Processos aguardam CPU ou I/O? Quantos núcleos há? |
| RAM alta | Cache recuperável ou pressão real de processos/swap? |
| Evento OOM | Qual processo foi encerrado? Havia limite do container? |
| Disco cheio | Qual filesystem/mount? Banco, logs ou dados Docker? |
| Inodes esgotados | Muitos arquivos pequenos impedem criação? |
| Container lento | Host inteiro sob pressão ou limite local do container? |

## 4. Inspeção Linux sem alterações

Executar no host **corretamente identificado**. A disponibilidade de comandos depende dos pacotes instalados.

~~~bash
date -Is
hostnamectl
uptime
nproc
free -h
cat /proc/meminfo | head -n 20
df -hT
df -i
lsblk -f
~~~

Analisar load average junto com `nproc` e intervalo temporal: load elevado não prova CPU alta. Observar memória `available` e swap, sem tratar cache recuperável como memória inutilizável.

Identificar consumidores:

~~~bash
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 15
ps -eo pid,comm,%cpu,%mem --sort=-%mem | head -n 15
~~~

Verificar eventos recentes do kernel com autorização:

~~~bash
journalctl -k --since '-2 hours' --no-pager
~~~

Pesquisar mensagens OOM localmente; não subir logs privados completos ao GitHub.

## 5. Correlação de recursos Docker

No Debian principal:

~~~bash
docker stats --no-stream
docker ps --format 'table {{.Names}}\t{{.Status}}'
docker system df
~~~

`docker system df` consulta uso; **não** confundir com `docker system prune`, que apaga dados. O Compose público utiliza diretórios relativos `./zabbix-db-data` (MariaDB) e `./grafana-data` (Grafana). Não representam caminhos absolutos confirmados da implantação.

Se uma partição estiver pressionada, identificar qual volume/montagem sustenta o serviço e examinar uso sem modificar ou divulgar dados da aplicação. OOM no container não comprova, necessariamente, falta de memória física do host; conferir limites específicos.

## 6. Diagnóstico das estações Windows

Em estações autorizadas:

~~~powershell
Get-ComputerInfo | Select-Object CsName,OsName
Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize
Get-Volume | Select-Object DriveLetter,FileSystem,Size,SizeRemaining
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name,CPU,WorkingSet64
~~~

A propriedade CPU de `Get-Process` representa tempo acumulado, não percentual instantâneo. Uma captura não deve virar afirmação de carga continuamente elevada.

## 7. Causa e resposta autorizada

| Condição confirmada | Ação possível após aprovação |
|---|---|
| Processo consome CPU repetidamente | Examinar logs/carga e corrigir causa; reiniciar só se justificado |
| Pressão de memória sustentada e OOM | Revisar alocação/limites e avaliar ajuste ou mudança de carga |
| Logs ocupam o disco | Revisar retenção e política de rotação em manutenção aprovada |
| Banco/volume lota partição | Rever capacidade e retenção com backup antes da mudança |
| Inodes esgotados | Identificar criação de arquivos; não excluir sem avaliar dono/impacto |
| Dashboard com métrica enganosa | Conferir consulta, unidade, agregação e amostragem |

Não decidir correção apenas por screenshot. Escalonar antes de interromper monitoramento, banco, telefonia ou serviços compartilhados.

## 8. Critérios de validação

1. Medir novamente o recurso **depois** da alteração autorizada, no mesmo host e intervalo adequado.
2. Validar a aplicação separadamente: Zabbix, Grafana ou teste funcional da telefonia, conforme caso.
3. Conferir se pressão e erros deixam de se repetir durante período suficiente.
4. Comparar painéis com medidas locais, considerando atraso, unidades e agregações.
5. Registrar sintoma, duração, causa comprovada, mudança, métricas e riscos remanescentes.

## 9. Registro de evidências

Incluir fuso, host, filesystem/container, medidas iniciais e finais, análise de processos/armazenamento, impacto, autorização, janela de validação e evidências sanitizadas. Não afirmar melhora sem medições comparáveis.

## 10. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Inventário de Linux e Windows](../../estacoes/inventario-de-computadores.md)
- [Infraestrutura Docker](../../containers/servicos-docker.md)
- [Métricas Grafana](../../monitoramento/grafana.md)
- [Falhas de serviços Docker](falhas-servicos-docker.md)

**Escopo documental:** Procedimento de referência com base nos registros datados do laboratório; este arquivo não é um registro de incidente executado.