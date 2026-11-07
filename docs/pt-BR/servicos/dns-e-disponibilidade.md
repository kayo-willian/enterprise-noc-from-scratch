# Filtragem DNS e Disponibilidade dos Serviços

[English](../../services/dns-and-availability.md) | [Português (Brasil)](dns-e-disponibilidade.md)

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

A existência de portas publicadas e containers não comprova, isoladamente, o acesso bem-sucedido a partir de todas as redes do laboratório.

Para consultar o inventário completo, acesse [Infraestrutura Docker e Serviços](../containers/servicos-docker.md).

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

As estatísticas de bloqueio não comprovam, isoladamente, que determinado computador estivesse infectado, que ocorreu um ataque ou que todo tráfego indesejado foi impedido.

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

Entretanto, um endereço IPv4 na lista de clientes não comprova, isoladamente, a identidade ou as especificações de hardware do dispositivo correspondente.

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

Esses valores precisam ser interpretados conforme o período de monitoramento e os parâmetros de relatório configurados na aplicação.

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

Ela não comprova que todos os dez containers Docker ou todos os equipamentos da infraestrutura fossem monitorados individualmente pelo Uptime Kuma.

A aplicação complementa o Zabbix, sem substituir o monitoramento mais abrangente da infraestrutura.

## 5. Relação com Zabbix e Grafana

O laboratório utiliza aplicações complementares para infraestrutura e monitoramento:

| Aplicação | Responsabilidade |
|---|---|
| Pi-hole | Filtragem DNS e registro das consultas |
| Uptime Kuma | Verificações de disponibilidade de serviços e equipamentos |
| Zabbix | Métricas de infraestrutura, itens de monitoramento e triggers |
| Grafana | Visualização dos dados de monitoramento |

As ferramentas apresentam perspectivas diferentes da mesma infraestrutura.

Uma verificação bem-sucedida no Uptime Kuma não garante, isoladamente, que todos os itens correspondentes do Zabbix estejam funcionando ou que todos os painéis do Grafana apresentem dados válidos.

Documentações relacionadas:

- [Monitoramento com Zabbix](../monitoramento/zabbix.md)
- [Monitoramento com Grafana](../monitoramento/grafana.md)

## 6. Configuração de Implantação

A configuração sanitizada do Docker Compose do Pi-hole está disponível no repositório:

[Docker Compose do Pi-hole](../../../docker_configs/lab-ti/pihole/docker-compose.yml)

O container Uptime Kuma está descrito no Compose principal da infraestrutura:

[Docker Compose da Infraestrutura](../../../docker_configs/docker-compose.yml)

As configurações públicas não incluem segredos de autenticação nem configurações DNS específicas da instituição.

Esses arquivos documentam a estrutura de implantação, enquanto as capturas coletadas comprovam a presença das aplicações no laboratório.

## 7. Evidências e Limitações

| Evidência | O que demonstra |
|---|---|
| `pihole_dashboard.png` | Consultas DNS, estatísticas de bloqueio, atividade dos clientes e estado ativo do serviço |
| `pihole_dashboard_tops.png` | Atividade de domínios e estatísticas dos clientes |
| `UpTimeKuma.png` | Quatro monitores configurados, estados observados e histórico de eventos |
| Inventário dos containers Docker | Presença dos containers Pi-hole e Uptime Kuma na infraestrutura |

As evidências não comprovam isoladamente:

- Disponibilidade contínua das duas aplicações.
- Cobertura completa da filtragem DNS em todas as VLANs.
- Visibilidade de todas as consultas DNS dos clientes.
- Cumprimento de um acordo de nível de serviço.
- Funcionamento bem-sucedido de todas as aplicações Docker.
- Ausência de incidentes anteriores.

As capturas representam o ambiente documentado em 6 de novembro de 2026.

## 8. Documentação Relacionada

- [Infraestrutura Docker e Serviços](../containers/servicos-docker.md)
- [Monitoramento com Zabbix](../monitoramento/zabbix.md)
- [Monitoramento com Grafana](../monitoramento/grafana.md)
- [Inventário de Computadores e Servidores](../estacoes/inventario-de-computadores.md)

**Data da coleta das evidências:** 6 de novembro de 2026.

**Escopo da documentação:** Filtragem DNS, monitoramento de disponibilidade e evidências históricas do laboratório.
