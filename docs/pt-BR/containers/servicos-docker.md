# Infraestrutura Docker e Serviços

[English](../../containers/docker-services.md) | [Português (Brasil)](servicos-docker.md)

## 1. Visão Geral

O laboratório Enterprise NOC — From Scratch utiliza Docker para hospedar serviços de infraestrutura, monitoramento e rede.

O ambiente de containers é executado no computador principal de TI, um Dell OptiPlex 3020 com processador Intel Core i5-4590, aproximadamente 8 GB de memória RAM e Debian GNU/Linux 13 (Trixie).

Durante a coleta de evidências, o computador foi identificado com o endereço IPv4 `192.168.10.12/24`.

Este documento descreve o ambiente Docker observado em 6 de novembro de 2026, utilizando a saída do comando `docker ps` e capturas do Portainer.

## 2. Ambiente Docker

![Resumo do ambiente no Portainer](../../assets/images/docker/portainer-environment-summary.png)

O dashboard do Portainer apresentou os seguintes recursos:

| Recurso | Quantidade observada |
|---|---:|
| Ambientes Docker | 1 |
| Stacks | 3 |
| Containers | 10 |
| Containers em execução | 10 |
| Containers parados | 0 |
| Imagens de containers | 11 |
| Volumes | 4 |
| Redes Docker | 6 |

Quatro containers foram identificados como saudáveis, sem indicação de containers não saudáveis no momento da coleta.

Esses valores representam uma observação específica, não estatísticas de disponibilidade contínua.

## 3. Inventário dos Containers

![Containers em execução no Portainer](../../assets/images/docker/portainer-running-containers.png)

A saída do comando `docker ps` identificou dez containers em execução.

| Container | Imagem | Finalidade |
|---|---|---|
| `reverse-proxy` | `nginx:alpine` | Proxy reverso |
| `zabbix-web` | `zabbix/zabbix-web-apache-mysql:ubuntu-7.0-latest` | Interface web do Zabbix |
| `zabbix-server` | `zabbix/zabbix-server-mysql:ubuntu-7.0-latest` | Servidor de monitoramento Zabbix |
| `uptime-kuma` | `louislam/uptime-kuma:1` | Monitoramento de disponibilidade |
| `zabbix-db` | `mariadb:11.4` | Banco de dados do Zabbix |
| `grafana` | `grafana/grafana-oss:latest` | Dashboards e visualização de métricas |
| `zabbix-agent` | `zabbix/zabbix-agent:ubuntu-7.0-latest` | Agente de monitoramento Zabbix |
| `site-estatico` | `httpd:alpine` | Hospedagem de site estático |
| `pihole` | `pihole/pihole:latest` | Filtragem e gerenciamento DNS |
| `portainer` | `portainer/portainer-ce:latest` | Gerenciamento de containers |

As tags das imagens foram reproduzidas conforme o registro coletado. Tags como `latest` não permitem determinar, isoladamente, a versão exata instalada.

## 4. Portas Publicadas

As seguintes portas do host foram identificadas na saída do comando `docker ps`:

| Container | Porta(s) publicada(s) no host |
|---|---|
| `reverse-proxy` | 80, 443 |
| `zabbix-web` | 8082 |
| `zabbix-server` | 10051 |
| `uptime-kuma` | 3001 |
| `zabbix-db` | Nenhuma porta publicada no host |
| `grafana` | 3000 |
| `zabbix-agent` | 10050 |
| `site-estatico` | 8081 |
| `pihole` | 53 TCP/UDP, 8080 |
| `portainer` | 8000, 9000, 9443 |

As portas representam a configuração observada durante a coleta. As portas publicadas são registros de configuração, não resultados de testes de acesso em todas as VLANs.

## 5. Redes Docker

![Redes Docker no Portainer](../../assets/images/docker/portainer-docker-networks.png)

O Portainer registrou seis redes Docker.

O ambiente utiliza mecanismos padrão de rede do Docker e redes associadas às stacks de aplicações implantadas.

O relatório do sistema Linux também identifica interfaces bridge do Docker e sub-redes privadas utilizadas pelos containers.

A captura registra as redes Docker configuradas, não uma matriz de testes de conectividade entre aplicações.

## 6. Organização dos Serviços

Os containers documentados atendem a diferentes funções.

### Infraestrutura e Acesso às Aplicações

- Nginx disponibiliza [funcionalidades de proxy reverso](../servicos/nginx-proxy-reverso/README.md).
- Apache HTTP Server hospeda um site estático.
- Portainer permite gerenciar os containers.

### Monitoramento e Observabilidade

- Zabbix Server coleta e processa dados de monitoramento.
- Zabbix Web disponibiliza a interface de monitoramento.
- Zabbix Agent fornece dados para monitoramento.
- Grafana apresenta dashboards e visualizações.
- Uptime Kuma monitora a disponibilidade dos serviços.

### Serviços Complementares

- MariaDB [armazena os dados utilizados pelo Zabbix](../servicos/mariadb-zabbix/README.md).
- Pi-hole disponibiliza funcionalidades relacionadas ao DNS.

Os serviços Asterisk e FreeRADIUS são documentados separadamente, pois são executados em outro computador Linux.

## 7. Arquitetura, Integração dos Serviços e Decisões Técnicas

A infraestrutura reúne **dez containers observados em um host físico Debian** e **outro computador Linux dedicado a Asterisk/FreeRADIUS**. Essa separação está registrada nos inventários de containers e do servidor de telefonia/autenticação; o servidor VoIP não deve ser contado como container Docker.

### Caminho de uma Requisição na Infraestrutura

A configuração publicada permite compreender o fluxo de acesso aos serviços:

1. O cliente resolve o **nome DNS interno** pelo resolvedor configurado. O Pi-hole pode responder ou filtrar consultas dos clientes que o utilizam; as evidências não comprovam que todas as VLANs adotaram esse resolvedor.
2. O cliente acessa o host Debian pelas portas **HTTP 80 ou HTTPS 443**, publicadas pelo container `reverse-proxy`.
3. O Nginx seleciona o host virtual em [`lab.conf`](../../../docker_configs/reverse-proxy/conf.d/lab.conf) e encaminha a requisição para o container apropriado. Por exemplo, `grafana.noc.example.test` aponta para `grafana:3000` e `zabbix.noc.example.test` para `zabbix-web:8080`.
4. O Zabbix Web depende do restante da stack Zabbix e do MariaDB; receber resposta HTTP da interface não equivale a comprovar que todos os itens estão sendo coletados. O Grafana apresenta métricas da integração Zabbix definida no exemplo.

Os nomes apresentados são **exemplos sanitizados**, não registros DNS públicos reais. O Nginx público contempla hosts virtuais de **portal, Zabbix, Grafana e Uptime Kuma**; não publica regras de proxy para Pi-hole ou Portainer. O registro do laboratório também menciona esses outros serviços, portanto o exemplo público não é um export completo.

### Importância das Dependências no Compose

| Relação | Implicação técnica | O que está documentado |
|---|---|---|
| Health check de `db` → `zabbix-server` | O processamento do Zabbix depende do banco; o Compose espera a inicialização do MariaDB | **Dependência declarada**, não coleta correta de todos os itens |
| `db` e `zabbix-server` → `zabbix-web` | A inicialização da interface segue os pré-requisitos da stack | Ordem de inicialização, **não** prontidão funcional |
| `zabbix-server` → `zabbix-agent` | O agente está configurado para interagir com o servidor identificado | Configuração, **não** sucesso de coleta em todos os hosts |
| `reverse-proxy` → aplicações web | O encaminhamento exige alcance dos upstreams pelos nomes dos containers | Rotas declaradas, **não** acesso testado de todas as VLANs |
| Plugin Grafana → Zabbix | Os dashboards podem visualizar os dados coletados pelo Zabbix | Configuração do plugin e painéis observados |

Concentrar serviços em um host facilita inventário, inspeção dos logs e acompanhamento de dependências, mas também cria um **domínio de falha compartilhado**. Alta disponibilidade ou tempo de recuperação não foram comprovados. Os volumes persistentes preservam dados nas operações normais de substituição de containers quando utilizados corretamente; isso **não** equivale a um backup validado.

Algumas imagens utilizam tags mutáveis, como `latest`. Uma implantação reproduzível exigiria verificar versões ou digests específicos, que não podem ser deduzidos apenas do inventário histórico.

## 8. Fluxo de Diagnóstico e Validação

Os comandos abaixo são **referências para futuras verificações**, não testes executados nesta revisão. Utilizar um host autorizado e confirmar os caminhos reais das stacks antes de agir.

```bash
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
docker network ls
docker volume ls
```

Ao inspecionar um serviço, distinguir o processo em execução do health check opcional:

```bash
docker inspect --format '{{.State.Status}} {{if .State.Health}}{{.State.Health.Status}}{{else}}no-healthcheck{{end}}' zabbix-db
docker logs --tail 100 zabbix-server
```

Uma validação deve examinar **a aplicação e suas dependências**: diante de falha no Zabbix Web, consultar interface, Zabbix Server e MariaDB; diante de falha no portal, verificar resolução DNS, rota Nginx e `site-estatico`. Porta publicada ou container `running` é observação inicial, não teste funcional conclusivo.

**Limites das investigações registradas:** as capturas mostram dez containers em execução e quatro health checks saudáveis, mas não apresentam uso individual de CPU/RAM, testes de conectividade por VLAN, validação TLS, exercícios de recuperação ou causa-raiz comprovada de indisponibilidades. Registrar novas saídas com data e hora e remover segredos antes de publicar.

**Procedimentos operacionais:** [Runbook de falhas Docker](../operacoes-noc/runbooks/falhas-servicos-docker.md) · [Runbook de resolução DNS](../operacoes-noc/runbooks/falhas-resolucao-dns.md). Esses documentos descrevem métodos de diagnóstico; não afirmam que houve um incidente em 6 de novembro. 

## 9. Escopo das Evidências

As evidências coletadas confirmam a presença de dez containers Docker em execução em 6 de novembro de 2026.

As capturas do Portainer também documentam o gerenciamento de containers, a configuração de redes e as quantidades de recursos.

O inventário datado não registra as seguintes propriedades operacionais:

- Disponibilidade contínua dos serviços.
- Acesso bem-sucedido a partir de todas as VLANs.
- Segurança completa das aplicações.
- Funcionamento correto de todos os itens de monitoramento.
- Alta disponibilidade ou redundância.

O inventário apresenta containers, portas e redes na data de coleta, sem tratar essas configurações como resultados de testes das aplicações.

## 10. Configuração do Docker Compose

Os arquivos Docker Compose a seguir são exemplos públicos sanitizados, baseados nos registros do laboratório. Não representam uma exportação integral da implantação nem incluem os arquivos privados necessários para reproduzi-la.

- [Stack de Monitoramento e Infraestrutura](../../../docker_configs/docker-compose.yml)
- [Pi-hole](../../../docker_configs/lab-ti/pihole/docker-compose.yml)
- [Portainer](../../../docker_configs/lab-ti/portainer/docker-compose.yml)

### Pré-requisitos dos exemplos públicos e limites de reprodução

O [Compose principal](../../../docker_configs/docker-compose.yml) referencia diretórios locais montados a partir de `docker_configs/`: `alertscripts/`, `externalscripts/`, `site-estatico-html/` e `reverse-proxy/certs/`. Esses caminhos **não estão incluídos nos arquivos versionados**. Portanto, um clone novo não contém os certificados TLS privados, scripts locais do Zabbix ou arquivos do site interno exigidos por essas montagens. Iniciar o Compose com caminhos ausentes não fornece esse conteúdo e pode criar diretórios vazios no host.

Os arquivos [`.env.example`](../../../docker_configs/.env.example) e [`.env.example` do Pi-hole](../../../docker_configs/lab-ti/pihole/.env.example) mostram nomes de variáveis e valores demonstrativos, **não credenciais reais**. Arquivos `.env` locais, dados persistentes e chaves TLS não devem ser publicados no Git. O volume `portainer_data` do Portainer é um **volume nomeado do Docker**, não uma pasta do repositório. O site público no GitHub Pages, em `docs/`, e o conteúdo local montado em `site-estatico` são implantações distintas; os exemplos publicados não comprovam que tenham arquivos idênticos.

Para reproduzir a stack, é necessário conferir caminhos existentes no host, segredos, versões das imagens, exposição de portas e parâmetros de TLS/DNS antes da execução. Os arquivos públicos são uma **referência sanitizada de configuração**, não uma implantação de produção pronta para executar.

### Proxy Reverso e Portal Corporativo

O laboratório possui um proxy reverso Nginx e um
container Apache HTTP Server responsável pelo portal corporativo.

A configuração coletada contém rotas para Zabbix,
Grafana, Uptime Kuma, Portainer, Pi-hole e o portal.

A versão pública documenta atualmente as rotas
do portal, Zabbix, Grafana e Uptime Kuma.

Arquivos de configuração:

- [Configuração Principal do Nginx](../../../docker_configs/reverse-proxy/nginx.conf)
- [Regras do Proxy Reverso](../../../docker_configs/reverse-proxy/conf.d/lab.conf)

Os arquivos públicos utilizam domínios e caminhos de
certificados demonstrativos.

O ambiente original utilizava nomes DNS internos
e certificados TLS.

Chaves privadas e configurações específicas da
instituição não estão incluídas.

O portal estático é hospedado pelo container
`site-estatico`, utilizando a imagem `httpd:alpine`
e a porta `8081` no host Docker.

Esses arquivos são versões sanitizadas das configurações coletadas.
Credenciais e configurações DNS específicas da instituição foram removidas.

**Data da coleta das evidências:** 6 de novembro de 2026.
