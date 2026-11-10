# Runbook — Falhas em Serviços Docker

[English](../../../noc-operations/runbooks/docker-service-failure.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** CNT / SYS / WEB · **Tipo de documento:** Runbook de diagnóstico operacional  
**Ambiente:** Computador NOC Debian 13; Docker, Compose, Portainer e aplicações de infraestrutura

## 1. Objetivo e evidências

Investigar container parado, reiniciando, não saudável, inacessível ou com resposta inadequada. As capturas de Docker e Portainer de 06/11/2026 mostravam **dez containers em execução**, sem garantir disponibilidade permanente. O inventário registra `reverse-proxy`, `zabbix-web`, `zabbix-server`, `uptime-kuma`, `zabbix-db`, `grafana`, `zabbix-agent`, `site-estatico`, `pihole` e `portainer`.

O Compose público sanitizado inclui a stack principal; **Pi-hole e Portainer têm exemplos Compose separados**. Não presumir projeto Docker único ou todos os requisitos presentes no repositório.

## 2. Segurança e limites das alterações

- Obter autorização para o host e serviço afetados. Começar por comandos de leitura.
- **Não executar** `docker compose down -v`, `docker system prune`, atualização de imagem, reset de banco ou exclusão de volume durante a triagem.
- Reinício pode interromper usuários e apagar evidência transitória; somente após avaliação, autorização e plano de reversão.
- `docker inspect` e exportações do ambiente podem expor senhas; coletar apenas campos necessários e manter dados sensíveis fora do GitHub.
- Container em execução ou porta publicada não comprova saúde funcional.

## 3. Dependências dos serviços

| Camada | Serviço documentado |
|---|---|
| Banco Zabbix | `zabbix-db` (exemplo MariaDB 11.4); o Zabbix depende do banco |
| Motor de monitoramento | `zabbix-server`; processa/coleta métricas |
| Interface Zabbix | `zabbix-web`; depende da aplicação e do banco |
| Visualização | `grafana`; integração com fonte/plugin Zabbix |
| Proxy e web | `reverse-proxy` (Nginx) e `site-estatico` (Apache) |
| Disponibilidade | `uptime-kuma` monitora alvos configurados |
| DNS | `pihole` publicou porta 53 TCP/UDP no inventário |
| Gerenciamento | `portainer` exibe containers e redes |
| Agente | `zabbix-agent` integra a stack de monitoramento |

O **portal público GitHub Pages** e o site de laboratório hospedado pelo Apache `site-estatico` são componentes diferentes: suas implantações e disponibilidades não devem ser confundidas.

## 4. Triagem inicial

Registrar horário, sintoma, container envolvido, comportamento da aplicação, alterações recentes e dependências.

~~~bash
docker version
docker info --format '{{.ServerVersion}}'
docker ps --all --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
docker ps --filter name=zabbix
~~~

Se o daemon Docker não responder, inspecionar host:

~~~bash
systemctl status docker --no-pager
journalctl -u docker --since '-30 min' --no-pager
df -h
free -h
~~~

Problema no daemon pode afetar vários containers; falha de aplicação pode ser isolada.

## 5. Inspeção do container identificado

Substituir `<CONTAINER>` por nome **confirmado**; não usar nomes não confiáveis ou segredos no comando.

~~~bash
docker logs --tail 100 --timestamps <CONTAINER>
docker inspect --format '{{.State.Status}} {{.State.ExitCode}} {{.State.OOMKilled}} {{if .State.Health}}{{.State.Health.Status}}{{else}}no-healthcheck{{end}}' <CONTAINER>
docker port <CONTAINER>
docker stats --no-stream
~~~

Interpretação:

| Resultado | Investigação |
|---|---|
| `Exited`, código de saída diferente de zero | Examinar erro e dependências |
| `Restarting` | Investigar loop, configuração e dependências indisponíveis |
| `OOMKilled=true` | Verificar pressão de memória antes de mudar limites |
| `running` com health check falhando | Analisar verificação de saúde e testes da aplicação |
| `running` sem health check | Estado não prova prontidão da aplicação |
| Proxy retorna erro | Separar conectividade proxy da aplicação de destino |

Alguns containers no Compose público não possuem health check explícito. Não atribuir saúde presumida.

## 6. Inspeção de Compose e redes

Trabalhar no **diretório correto** da implantação, após confirmar sua localização. Não exportar configuração interpolada contendo segredos para relatórios públicos.

~~~bash
docker network ls
docker volume ls
docker compose ps
docker compose config --quiet
~~~

Os dois últimos comandos dependem do diretório correto e das variáveis privadas necessárias. Conferir redes do container sem expor todo o ambiente:

~~~bash
docker inspect --format '{{json .NetworkSettings.Networks}}' <CONTAINER>
~~~

Compartilhar rede Docker não comprova automaticamente conectividade a todos os serviços ou VLANs.

Executar teste funcional autorizado conforme o serviço. Conexão TCP válida não prova processamento Zabbix, correção do MariaDB ou filtragem DNS.

## 7. Decisão de correção

**Somente após causa identificada e mudança autorizada:**

- Resolver dependência ausente ou falta de espaço por procedimento controlado.
- Restaurar configuração aprovada conhecida se divergência for confirmada.
- Considerar reinício controlado do serviço afetado **apenas** quando responsável aceitar interrupção.
- Recriar containers ou alterar imagens somente com backup, persistência, migração e reversão avaliados.

Nunca apagar `zabbix-db` ou volumes persistentes como método comum de reinício. Tags `latest` do inventário não estabelecem versões fixas; evitar pulls não controlados.

## 8. Validação e encerramento

1. Confirmar estado do container, saúde real da aplicação e serviços dependentes.
2. Verificar logs novos após correção.
3. Testar URL, DNS ou operação de monitoramento esperada por cliente autorizado.
4. Conferir Zabbix/Grafana/Uptime Kuma quando aplicável; dashboard complementa, não substitui teste da aplicação.
5. Registrar mudança, recuperação, alertas remanescentes, horários e capacidade de reversão.

## 9. Registro de incidentes

Guardar container, projeto Compose, host, dependências, estado inicial/final, logs sanitizados, portas/redes, sintoma, causa confirmada versus hipótese, ação autorizada e validação funcional. Não alegar uma nova recuperação sem evidências.

## 10. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Serviços Docker e inventário de dez containers](../../containers/servicos-docker.md)
- [Compose principal sanitizado](../../../../docker_configs/docker-compose.yml)
- [Compose Pi-hole](../../../../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Compose Portainer](../../../../docker_configs/lab-ti/portainer/docker-compose.yml)
- [Runbook DNS](falhas-resolucao-dns.md)
- [Runbook de utilização de recursos](utilizacao-recursos-sistema.md)

**Limite:** Este documento apenas descreve o procedimento; não comprova nova falha, reinício ou recuperação executada.