# Filtragem DNS e Disponibilidade dos Serviços

[English](../../services/dns-and-availability.md) | **Português (Brasil)**

## 1. Visão Geral

O laboratório Enterprise NOC — From Scratch utiliza Pi-hole e Uptime Kuma para disponibilizar filtragem DNS, visualização de atividades de rede e monitoramento de disponibilidade dos serviços.

As duas aplicações são executadas como containers Docker no computador principal da infraestrutura, utilizando Debian GNU/Linux 13.

Os serviços documentados possuem funções diferentes:

| Serviço | Função principal |
|---|---|
| Pi-hole | Filtragem DNS, estatísticas de consultas e bloqueio de domínios |
| Uptime Kuma | Monitoramento de disponibilidade e histórico de eventos |

Esta documentação utiliza capturas coletadas em **6 de novembro de 2026**.

Todas as estatísticas exibidas representam observações históricas, não dados de monitoramento em tempo real.

## 2. Arquitetura da Infraestrutura

O servidor principal da infraestrutura foi identificado com o endereço IPv4 `192.168.10.12/24` durante a coleta.

O ambiente Docker inclui:

| Container | Imagem | Acesso documentado |
|---|---|---|
| `pihole` | `pihole/pihole:latest` | DNS nas portas TCP/UDP 53; interface web na porta 8080 do host |
| `uptime-kuma` | `louislam/uptime-kuma:1` | Interface web na porta 3001 do host |

Essas aplicações complementam o ambiente de monitoramento com Zabbix e Grafana.

O proxy reverso documentado também fornece acesso web interno a serviços.

As portas publicadas descrevem a configuração Docker, não testes de acesso em todas as VLANs.

Para consultar o inventário completo, acesse [Infraestrutura Docker e Serviços](../containers/servicos-docker.md).

### 2.1. Caminho da Consulta DNS e Dependências dos Serviços

Um cliente só utiliza o Pi-hole quando a configuração do seu resolvedor direciona consultas ao serviço. Na implantação documentada, o host Debian publica DNS TCP/UDP **53**; o container Pi-hole avalia as requisições pelas regras de filtragem e pelos servidores upstream configurados.

1. O cliente recebe ou configura um resolvedor DNS. As evidências públicas **não** comprovam opções DHCP de DNS aplicadas a todas as VLANs.
2. O cliente envia a consulta ao resolvedor. Quando o Pi-hole a recebe, pode responder com registros/cache disponíveis, aplicar bloqueios ou consultar os resolvedores upstream configurados.
3. A aplicação acessa separadamente o endereço retornado. **Resolver DNS com sucesso não comprova que HTTP, HTTPS ou o backend Docker esteja acessível.**

O [Compose do Pi-hole](../../../docker_configs/lab-ti/pihole/docker-compose.yml) publica `53:53/tcp`, `53:53/udp` e a porta `8080` do host para interface web; a senha administrativa e os upstreams são informados por **variáveis de ambiente locais**. Assim, é possível examinar a declaração do serviço sem expor credenciais no repositório.

Essa distinção ajuda a investigar indisponibilidades: bloqueio intencional de domínio, timeout do resolvedor, falha de roteamento e erro de aplicação web exigem **correções diferentes**.


## 3. Pi-hole — Filtragem DNS

O Pi-hole disponibiliza filtragem de domínios baseada em DNS e visibilidade sobre consultas realizadas pelos clientes que utilizam o serviço.

O laboratório utiliza essa aplicação como parte de sua infraestrutura de serviços de rede.

### 3.1 Evidência do Dashboard

![Dashboard de filtragem DNS do Pi-hole](../../assets/images/services/pihole_dashboard.png)

O dashboard coletado apresenta as seguintes estatísticas:

| Métrica | Valor observado |
|---|---:|
| Total de consultas DNS | 12.293 |
| Consultas DNS bloqueadas | 1.827 |
| Percentual bloqueado | 14,9% |
| Domínios nas listas de bloqueio | 75.952 |
| Clientes ativos | 13 |
| Estado do serviço | Ativo |

O painel também apresenta:

- Atividade de consultas DNS ao longo do tempo.
- Atividade dos clientes.
- Distribuição dos tipos de consultas.
- Informações dos servidores DNS upstream.
- Estatísticas de filtragem DNS.

Os contadores representam o período apresentado pela interface do Pi-hole.

Não devem ser interpretados como totais permanentes nem como medições de desempenho de longo prazo.

### 3.2 Funcionamento do Bloqueio DNS

O Pi-hole avalia as consultas DNS utilizando regras de filtragem e listas de domínios configuradas.

Uma consulta DNS bloqueada indica que a solicitação correspondeu a uma regra de bloqueio ou outra condição de filtragem configurada.

As estatísticas representam correspondências com regras de filtragem DNS, não diagnósticos de infecção, incidentes de ataque ou cobertura integral de tráfego.

Da mesma forma, a quantidade de domínios cadastrados nas listas não representa o número de domínios efetivamente bloqueados durante o período observado.

### 3.3 Atividade dos Clientes e Domínios

![Estatísticas de domínios e clientes no Pi-hole](../../assets/images/services/pihole_dashboard_tops.png)

A segunda captura apresenta quatro tabelas:

- Domínios permitidos mais consultados.
- Domínios bloqueados mais consultados.
- Clientes com maior quantidade de consultas.
- Clientes com maior quantidade de consultas bloqueadas.

Essas informações demonstram que o Pi-hole registrou atividades DNS de diferentes clientes durante o período observado.

Diversos clientes aparecem identificados por endereços IPv4 privados de diferentes segmentos departamentais e de redes sem fio.

Esses registros constituem evidências complementares da atividade DNS no laboratório.

Os endereços IPv4 da lista identificam clientes DNS apresentados pelo Pi-hole; as especificações de hardware pertencem ao inventário de estações.

**Observação sobre privacidade:** esta captura contém histórico de consultas DNS e endereços dos clientes. A divulgação pública exige considerar a privacidade dos usuários da rede.

## 4. Uptime Kuma — Disponibilidade dos Serviços

O Uptime Kuma realiza verificações de disponibilidade e mantém registros históricos dos eventos relacionados aos serviços e equipamentos monitorados.

A captura coletada apresenta quatro monitores configurados.

### 4.1 Dashboard de Monitoramento

![Dashboard de monitoramento do Uptime Kuma](../../assets/images/services/UpTimeKuma.png)

O dashboard apresenta o seguinte resumo:

| Estado | Quantidade de monitores |
|---|---:|
| Ligado | 4 |
| Desligado | 0 |
| Manutenção | 0 |
| Desconhecido | 0 |
| Pausado | 0 |

Os alvos monitorados apresentados são:

| Monitor | Componente |
|---|---|
| Grafana NOC | Aplicação de monitoramento Grafana |
| Portal Web Zabbix | Interface web do Zabbix |
| Roteador Cisco C8200L | Equipamento de roteamento |
| Site Institucional | Portal web corporativo |

A barra lateral apresenta indicadores de `100%` para os quatro monitores.

Os indicadores de `100%` correspondem ao intervalo e às regras de relatório exibidos na captura.

Não constituem comprovação de um acordo de nível de serviço ou de disponibilidade ininterrupta.

### 4.2 Histórico de Eventos

A captura também apresenta uma tabela com mudanças de estado registradas antes da data da coleta.

Entre os registros observados estão:

- Verificações HTTP bem-sucedidas com resposta `200 OK`.
- Falhas anteriores de conectividade com o roteador Cisco.
- Um evento de conexão reiniciada relacionado ao Grafana.
- Registros posteriores de verificações bem-sucedidas.

Essas informações demonstram que o Uptime Kuma registra tanto verificações positivas quanto falhas.

Consequentemente, o estado atual `Ligado` não deve ser interpretado como prova de que um serviço nunca apresentou interrupções.

### 4.3 Escopo do Monitoramento

A captura confirma quatro monitores cadastrados e apresentados na interface.

A captura do Uptime Kuma registra quatro monitores específicos, não uma cobertura individual de todos os containers ou equipamentos.

A aplicação complementa o Zabbix, sem substituir o monitoramento mais abrangente da infraestrutura.

## 5. Relação com Zabbix e Grafana

O Pi-hole registra filtragem DNS; o Uptime Kuma verifica serviços selecionados. O Zabbix coleta métricas de infraestrutura e o Grafana as apresenta. Cada ferramenta possui escopo distinto; veja [Zabbix](../monitoramento/zabbix.md) e [Grafana](../monitoramento/grafana.md).

## 6. Configuração de Implantação

A configuração sanitizada do Docker Compose do Pi-hole está disponível no repositório:

[Docker Compose do Pi-hole](../../../docker_configs/lab-ti/pihole/docker-compose.yml)

O container Uptime Kuma está descrito no Compose principal da infraestrutura:

[Docker Compose da Infraestrutura](../../../docker_configs/docker-compose.yml)

As configurações públicas não incluem segredos de autenticação nem configurações DNS internas.

Esses arquivos documentam a estrutura de implantação, enquanto as capturas coletadas comprovam a presença das aplicações no laboratório.

## 7. Correlação de Incidentes e Validação

### Por que Essas Ferramentas São Complementares

O **Pi-hole** registra consultas DNS e aplica regras de filtragem. O **Uptime Kuma** consulta um conjunto limitado de alvos e registra mudanças de estado. O **Zabbix** coleta métricas e triggers de hosts/rede; o **Grafana** visualiza os dados selecionados. Combinar os sinais pode delimitar falhas, mas nenhuma ferramenta sozinha comprova a saúde de toda a cadeia de aplicações.

Se um usuário não consegue abrir o portal corporativo, a investigação deve separar:

| Verificação | Questão técnica | Evidência necessária |
|---|---|---|
| Resolvedor do cliente | O cliente usa o DNS esperado? | Configuração atual e resposta da consulta |
| Pi-hole | A consulta foi bloqueada, não respondida ou encaminhada? | Resposta/log datado, regra correspondente ou estado do upstream |
| Rede e proxy | O nome resolvido chega ao Nginx e ao upstream correto? | Testes autorizados de conectividade e HTTPS |
| Aplicação | O `site-estatico` entrega o conteúdo solicitado? | Estado do container, logs relevantes e resposta HTTP funcional |
| Uptime Kuma / Zabbix | Houve falha no mesmo período e alertas relacionados? | Histórico e timestamps correlacionados |

### Anomalias Históricas Não São Causas Comprovadas

O histórico capturado no Uptime Kuma inclui **verificações malsucedidas de conectividade com o roteador Cisco** e um **evento de conexão reiniciada do Grafana**, seguidos de verificações bem-sucedidas. Isso comprova **falhas registradas**, mas não demonstra causas-raiz, procedimentos de correção, duração do impacto ou solução permanente. Os quatro monitores atuais em `Up` não apagam eventos anteriores.

Da mesma forma, 1.827 consultas DNS bloqueadas comprovam atividade de filtragem, **não** 1.827 incidentes de segurança. Os 75.952 domínios da lista representam entradas de filtragem, não solicitações efetivamente bloqueadas.

### Verificações Futuras Somente de Leitura

Estes comandos são **exemplos de diagnóstico autorizado**, não testes executados nesta revisão. Substituir placeholders por informações atuais verificadas e evitar divulgar consultas reais de usuários.

```bash
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
docker logs --tail 100 pihole
docker logs --tail 100 uptime-kuma
```

Com `dig` instalado, é possível consultar um nome permitido no resolvedor Pi-hole atualmente autorizado:

```bash
dig @<VERIFIED_DNS_SERVER_IP> example.org A +time=2 +tries=1
```

Uma resposta HTTP `200 OK` e uma resposta DNS são verificações distintas. Confirmar tipo de monitor, estado esperado, intervalo de medição e rede de origem antes de interpretar percentuais do Uptime Kuma como disponibilidade.

**Runbooks:** [Falhas de resolução DNS](../operacoes-noc/runbooks/falhas-resolucao-dns.md) · [Falhas de serviços Docker](../operacoes-noc/runbooks/falhas-servicos-docker.md). Eles descrevem procedimentos de diagnóstico; não comprovam que novos incidentes foram reproduzidos.


## 8. Escopo das Evidências Históricas

| Evidência | O que demonstra |
|---|---|
| `pihole_dashboard.png` | Consultas DNS, estatísticas de bloqueio, atividade dos clientes e estado ativo do serviço |
| `pihole_dashboard_tops.png` | Atividade de domínios e estatísticas dos clientes |
| `UpTimeKuma.png` | Quatro monitores configurados, estados observados e histórico de eventos |
| Inventário dos containers Docker | Presença dos containers Pi-hole e Uptime Kuma na infraestrutura |

As capturas de 6 de novembro documentam consultas DNS e quatro monitores do Uptime Kuma. Elas não estabelecem cobertura DNS de todas as VLANs, disponibilidade contínua ou SLA comprovado.

## 9. Documentação Relacionada

- [Infraestrutura Docker e Serviços](../containers/servicos-docker.md)
- [Monitoramento com Zabbix](../monitoramento/zabbix.md)
- [Monitoramento com Grafana](../monitoramento/grafana.md)
- [Inventário de Computadores e Servidores](../estacoes/inventario-de-computadores.md)

**Data da coleta das evidências:** 6 de novembro de 2026.

