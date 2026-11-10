# Runbook — Falhas de Conectividade do Zabbix Agent

[English](../../../noc-operations/runbooks/zabbix-agent-connectivity.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** MON · **Tipo de documento:** Runbook de diagnóstico operacional  
**Ambiente:** Servidor de monitoramento Debian na VLAN 10; estações Windows; servidor Linux de VoIP/autenticação na VLAN 50

## 1. Objetivo e limites das evidências

Utilizar este procedimento quando o Zabbix indicar interface de agente indisponível, ausência de métricas de agente passivo ou coleta intermitente. É essencial distinguir **falha do host**, **falha do agente** e **erro de configuração do monitoramento**. Na captura de 06/11/2026, havia 12 hosts registrados, sete disponíveis e cinco indisponíveis; seis endereços de estações divergiam entre os registros. Isso não comprova uma causa única nem uma correção posterior.

O computador NOC principal foi registrado em `192.168.10.12/24` (Debian 13); o servidor Asterisk/FreeRADIUS em `192.168.50.2/24`. Estações usam DHCP. Os IPs são **observações históricas**, não destinos presumidamente atuais.

## 2. Segurança e pré-requisitos

- Obter autorização e acesso administrativo legítimo ao segmento envolvido.
- Identificar o **nome do host no Zabbix**, endereço IP/DNS cadastrado, tipo de interface, erro exato do item, último valor válido e sentido esperado da conexão.
- Começar por inspeção sem alterações. Não reiniciar agentes, modificar firewall, desabilitar proteções ou alterar endereçamento na triagem inicial.
- Não publicar segredos, regras excessivamente permissivas, identificadores privados nem logs sensíveis.

## 3. Delimitação do sintoma

| Observação | Interpretação a investigar |
|---|---|
| Ping falha e outros serviços também | Possível falha do host ou caminho; bloqueio ICMP isolado não é conclusivo |
| Host acessível, TCP 10050 indisponível | Agente passivo sem listener, filtragem ou destino incorreto |
| TCP 10050 acessível, itens falhando | Permissões, lista de servidores permitidos, chave ou configuração do item |
| Itens ativos falham, passivos funcionam | Comunicação ativa com servidor/proxy, hostname ou caminho TCP 10051 |
| Grafana indica `No data` e Zabbix possui valores | Problema na visualização, fonte de dados, consulta ou período |

## 4. Sequência de diagnóstico não disruptivo

### Etapa A — Conferir o cadastro no Zabbix

Em **Coleta de dados → Hosts**, comparar o endereço cadastrado na interface de agente com o endereço **observado atualmente** na máquina. Identificar se o item é **Zabbix agent** (passivo) ou **Zabbix agent (active)** e consultar a mensagem de erro e o horário da última coleta.

Em uma estação Windows (PowerShell local):

~~~powershell
ipconfig /all
Get-Service 'Zabbix Agent','Zabbix Agent 2' -ErrorAction SilentlyContinue
Get-NetTCPConnection -State Listen -LocalPort 10050 -ErrorAction SilentlyContinue
~~~

Em um host Linux:

~~~bash
hostnamectl
ip -br addr
ip route
systemctl status zabbix-agent zabbix-agent2 --no-pager
sudo ss -lntp | grep ':10050'
~~~

Nem todo Linux executa o agente via systemd: a stack principal documentada também possui um **container** `zabbix-agent`.

### Etapa B — Inspecionar o servidor de monitoramento

No host Docker Debian, consultar containers e logs recentes:

~~~bash
docker ps --filter name=zabbix
docker logs --tail 80 zabbix-server
docker logs --tail 80 zabbix-agent
~~~

O Compose público registra as portas **10050** (agente) e **10051** (servidor). Portas publicadas não comprovam comunicação ponta a ponta.

### Etapa C — Testar o caminho real

De um terminal Linux autorizado no lado do monitoramento, substituir o endereço pelo **IP atual confirmado**:

~~~bash
ping -c 3 <IP_ATUAL_CONFIRMADO>
nc -vz -w 3 <IP_ATUAL_CONFIRMADO> 10050
~~~

Se a ferramenta estiver instalada e o agente autorizar, realizar consulta de leitura:

~~~bash
zabbix_get -s <IP_ATUAL_CONFIRMADO> -p 10050 -k agent.ping
~~~

Falha no `ping` não comprova, sozinha, queda do host. Conexão TCP bem-sucedida não comprova a validade de todos os itens. Em verificações ativas, observar o acesso do agente ao servidor/proxy e a correspondência entre hostname configurado e cadastro do host.

### Etapa D — Correlacionar as descobertas

| Resultado | Próxima decisão |
|---|---|
| IP diferente do cadastro | Confirmar identidade da estação e concessão DHCP antes de qualquer ajuste |
| Serviço/container parado | Examinar logs, configuração e responsabilidade pelo serviço antes da recuperação autorizada |
| Acesso negado pelo agente | Conferir lista de servidores autorizados sem reduzir proteção |
| Chave de monitoramento não suportada | Revisar tipo de item, plataforma, versão e logs |
| Vários hosts indisponíveis simultaneamente | Investigar roteamento e dependências compartilhadas antes de alterações individuais |

## 5. Decisão sobre correção

**Este runbook não autoriza mudanças automaticamente.** Após identificar a causa, registrar a configuração a alterar, impactos, autorização e reversão. Corrigir endereço cadastrado no Zabbix somente após identificar corretamente o equipamento e seu IP atual. Não abrir portas amplamente nem desligar firewalls como atalho. Para recorrências do DHCP, avaliar estratégia aprovada de identificação ou endereçamento, sem presumir reservas já existentes.

## 6. Validação da recuperação

1. Confirmar conectividade pelo caminho de gerenciamento esperado.
2. Verificar novo valor **com horário atualizado** em um item de agente.
3. Conferir disponibilidade da interface e estado da trigger original.
4. Validar pelo menos outro item relevante, sem depender apenas do indicador verde.
5. Registrar itens restantes sem suporte/indisponíveis; uma correção não comprova solução para todos os alertas históricos.

## 7. Registro do incidente

Registrar horário/fuso, identidade do equipamento, VLAN, IP atual observado, IP no Zabbix, tipo/erro do item, testes não disruptivos, alteração autorizada, evidências antes/depois, alternativa de reversão, validação e status final.

## 8. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Monitoramento Zabbix e limitações históricas](../../monitoramento/zabbix.md)
- [Inventário de estações e divergências DHCP](../../estacoes/inventario-de-computadores.md)
- [Infraestrutura Docker](../../containers/servicos-docker.md)
- [Runbook Grafana sem dados](grafana-sem-dados.md)

**Escopo documental:** Procedimento de referência com base nos registros datados do laboratório; este arquivo não é um registro de incidente executado.