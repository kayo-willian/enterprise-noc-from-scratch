# Runbook — Falhas de Resolução DNS

[English](../../../noc-operations/runbooks/dns-resolution-failure.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** DNS / NET / CNT · **Status:** Runbook proposto; não constitui nova ocorrência comprovada  
**Ambiente:** Container Pi-hole no host Debian NOC, VLANs departamentais, proxy reverso e serviços web

## 1. Objetivo e ambiente registrado

Este runbook separa falhas de consulta DNS de problemas de conectividade IP, aplicações, bloqueios DNS intencionais e roteamento. O registro de 06/11 identifica o host Debian `192.168.10.12/24` e o container Pi-hole com porta **53** TCP/UDP publicada. O dashboard mostrava **12.293 consultas**, **1.827 bloqueadas**, **14,9% bloqueadas** e **13 clientes ativos** no período exibido. Esses valores são históricos e não comprovam que todas as VLANs utilizavam Pi-hole.

Nome resolvendo não prova que a aplicação funciona. Da mesma forma, falha de acesso a um site não significa necessariamente erro DNS.

## 2. Segurança e pré-requisitos

- Obter autorização para analisar DNS dos clientes e o resolver corporativo. Utilizar endereços atuais confirmados.
- Começar por verificações de leitura. Não desativar filtragem, substituir DNS corporativo, remover blocklists nem limpar caches compartilhados sem mudança autorizada e reversão.
- Logs e consultas DNS podem expor dados sensíveis; sanitizar antes de publicar.
- Identificar se o destino é nome público, interno, bloqueio intencional ou nome exclusivo de rede Docker.

## 3. Sintomas e possibilidades

| Sintoma | Distinção inicial |
|---|---|
| Nome falha e IP responde | Caminho DNS, registro ou filtragem provavelmente relevantes |
| Nome e IP falham | Possível roteamento, enlace, firewall ou aplicação |
| `NXDOMAIN` | Nome ausente no DNS consultado; revisar zona/registro esperado |
| `SERVFAIL` | Possível problema do resolver, upstream ou delegação |
| `REFUSED` ou timeout | Política, bloqueio, servidor inacessível ou listener ausente |
| Um cliente afetado, outros saudáveis | Resolver/DHCP/cache do cliente ou segmento |
| Um domínio específico bloqueado | Regra Pi-hole intencional ou exceção indevida |

## 4. Sequência de diagnóstico

### A. DNS e rota do cliente

No Linux:

~~~bash
ip -br addr
ip route
cat /etc/resolv.conf
getent ahostsv4 example.org
~~~

Se o comando existir:

~~~bash
resolvectl status
~~~

No Windows (PowerShell):

~~~powershell
ipconfig /all
Resolve-DnsName example.org
~~~

Comparar servidor DNS utilizado com o projeto autorizado. Os documentos públicos não estabelecem a opção DNS distribuída por DHCP em todas as VLANs.

### B. Consulta direta ao resolver confirmado

Com `dig` instalado, substituir pelo IP **atual e autorizado** do servidor e escolher nome de teste permitido:

~~~bash
dig @<IP_DNS_CONFIRMADO> example.org A +time=2 +tries=1
dig @<IP_DNS_CONFIRMADO> example.org AAAA +time=2 +tries=1
~~~

Conferir `SERVER`, `status`, respostas e tempo. Comparar com outro resolver expressamente autorizado pode delimitar a falha, mas não autoriza contornar bloqueios corporativos.

Porta publicada pelo Docker não comprova acesso real na rede. Se consultas UDP falharem, conferir o caminho TCP autorizado:

~~~bash
dig +tcp @<IP_DNS_CONFIRMADO> example.org A +time=2 +tries=1
~~~

### C. Inspecionar Pi-hole e Docker sem alterar

No host Debian:

~~~bash
docker ps --filter name=pihole
docker logs --tail 80 pihole
docker port pihole
sudo ss -lntup | grep ':53'
~~~

Esses comandos mostram porta e mensagens recentes para investigar conflitos de bind, problemas upstream ou política. O Pi-hole pode pertencer a uma **stack Compose diferente** da principal de Zabbix/Grafana.

### D. Verificação funcional

Testar nome permitido conhecido e, somente quando autorizado, um caso de bloqueio esperado. Bloqueio intencional do Pi-hole não é incidente. Para aplicações internas, validar tanto a resolução quanto o **endpoint da aplicação**, por exemplo requisição HTTPS aprovada através do proxy.

## 5. Decisão e correção

| Diagnóstico confirmado | Possível resposta autorizada |
|---|---|
| Resolver incorreto distribuído via DHCP | Corrigir configuração de origem após avaliar abrangência e concessões |
| Container Pi-hole indisponível | Inspecionar logs/dependências e planejar recuperação controlada |
| Upstream DNS indisponível | Restaurar configuração aprovada após verificação |
| Registro interno ausente | Corrigir zona/registro com controle da alteração |
| Bloqueio intencional da blocklist | Não remover sem análise e exceção aprovada |
| DNS responde, HTTP não | Encaminhar para diagnóstico da aplicação/proxy |

Nunca alterar entradas Pi-hole, configurações de clientes ou mapeamentos Docker sem aprovação e plano de reversão.

## 6. Validação da recuperação

1. Confirmar resolver correto nos clientes afetados.
2. Verificar resposta nova de nome permitido, registrando servidor e horário.
3. Testar a aplicação separadamente.
4. Conferir processamento atual no Pi-hole, não apenas contadores históricos.
5. Testar cliente afetado e controle, quando problema abranger departamento; registrar restrições remanescentes.

## 7. Registro do incidente

Registrar cliente/VLAN, DNS recebido via DHCP, tipo de domínio de teste (público/interno/bloqueado), horário, servidor consultado, código de resposta, tempo, comparação entre clientes, mudança efetiva, validação e impacto residual. Sanitizar nomes reais quando necessário.

## 8. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Pi-hole e Uptime Kuma](../../servicos/dns-e-disponibilidade.md)
- [Infraestrutura Docker](../../containers/servicos-docker.md)
- [Limites de DHCP e roteador](../../redes/roteador-c8200l.md)
- [Falhas de serviços Docker](falhas-servicos-docker.md)

**Status:** Procedimento proposto; nenhuma nova falha DNS ou correção é apresentada como executada.