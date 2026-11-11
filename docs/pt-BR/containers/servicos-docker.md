# Linux e Docker — Serviços de Infraestrutura

[English](../../containers/docker-services.md) | **Português (Brasil)**

**Evidências:** 6 de novembro de 2026 · **Host:** Dell OptiPlex 3020, Intel Core i5-4590, aproximadamente 8 GB RAM, Debian GNU/Linux 13 (Trixie), IPv4 observado `192.168.10.12/24`.

Este documento distingue o **inventário de containers em execução** registrado por `docker ps` e Portainer da **configuração Compose sanitizada** publicada no repositório. Os arquivos públicos descrevem a estrutura de implantação, não uma reprodução integral e validada do laboratório.

## Inventário Docker

![Resumo do ambiente no Portainer](../../assets/images/docker/portainer-environment-summary.png)

| Recurso do Portainer | Registro de 6 de novembro |
|---|---:|
| Ambientes Docker | 1 |
| Stacks | 3 |
| Containers / em execução / parados | 10 / 10 / 0 |
| Imagens de containers | 11 |
| Volumes | 4 |
| Redes | 6 |
| Containers indicados como saudáveis | 4 |
| Containers indicados como não saudáveis | 0 |

Os quatro resultados *healthy* correspondem às verificações de saúde informadas pelo Portainer, não a testes funcionais independentes de todos os containers.

![Containers em execução](../../assets/images/docker/portainer-running-containers.png)

| Container | Imagem registrada | Função | Portas publicadas no host |
|---|---|---|---|
| `reverse-proxy` | `nginx:alpine` | Proxy reverso Nginx | 80, 443 |
| `zabbix-web` | `zabbix/zabbix-web-apache-mysql:ubuntu-7.0-latest` | Interface Zabbix | 8082 |
| `zabbix-server` | `zabbix/zabbix-server-mysql:ubuntu-7.0-latest` | Métricas e triggers | 10051 |
| `uptime-kuma` | `louislam/uptime-kuma:1` | Verificações de disponibilidade | 3001 |
| `zabbix-db` | `mariadb:11.4` | Banco de dados Zabbix | Nenhuma |
| `grafana` | `grafana/grafana-oss:latest` | Dashboards | 3000 |
| `zabbix-agent` | `zabbix/zabbix-agent:ubuntu-7.0-latest` | Agente Zabbix | 10050 |
| `site-estatico` | `httpd:alpine` | Portal corporativo estático | 8081 |
| `pihole` | `pihole/pihole:latest` | Filtragem DNS | 53 TCP/UDP, 8080 |
| `portainer` | `portainer/portainer-ce:latest` | Administração Docker | 8000, 9000, 9443 |

As imagens e portas foram registradas no inventário. A tag `latest` **não** identifica uma versão exata do aplicativo; uma porta publicada **não** comprova acesso por todas as VLANs.

## Implantação e Dependências

Os arquivos Compose públicos estão organizados por grupos de serviços:

| Configuração pública | Serviços declarados | Configurações relevantes |
|---|---|---|
| [Stack principal](../../../docker_configs/docker-compose.yml) | `db`, `zabbix-server`, `zabbix-web`, `zabbix-agent`, `grafana`, `uptime-kuma`, `reverse-proxy`, `site-estatico` | Bridge `zabbix-net`, volumes de dados e dependências |
| [Pi-hole](../../../docker_configs/lab-ti/pihole/docker-compose.yml) | `pihole` | DNS TCP/UDP 53, web 8080, volumes de configuração |
| [Portainer](../../../docker_configs/lab-ti/portainer/docker-compose.yml) | `portainer` | Socket Docker, volume persistente `portainer_data`, portas administrativas |

Os três grupos públicos declaram os **dez nomes de containers** encontrados no inventário histórico. Essa correspondência não significa que apenas esses arquivos reproduzam o ambiente: dados locais, DNS, certificados e credenciais também eram necessários.

### Stack Principal

O `docker-compose.yml` público documenta estas relações e opções:

- **MariaDB (`db`):** imagem `mariadb:11.4`, bind mount `./zabbix-db-data:/var/lib/mysql`, health check de conexão/inicialização, buffer InnoDB de `512M` e limite de `300` conexões no exemplo.
- **Zabbix Server:** aguarda `service_healthy` do banco, utiliza as mesmas variáveis de conexão, monta scripts externos/de alertas somente para leitura e publica TCP `10051`.
- **Zabbix Web:** depende da saúde do banco e do início do server; a porta interna `8080` é publicada como `8082` no host.
- **Zabbix Agent:** configuração de coleta passiva com servidor `zabbix-server`; TCP `10050` publicado.
- **Grafana:** exemplo com plugin `alexanderzobnin-zabbix-app` e persistência de `/var/lib/grafana` via `./grafana-data`.
- **Uptime Kuma:** persistência de `/app/data` por `./uptime-kuma-data`; interface publicada em `3001`.
- **Proxy Nginx:** depende de Zabbix Web, Grafana, Uptime Kuma e site estático; expõe `80`/`443`, montando regras e caminhos dos certificados.
- **Site estático:** Apache `httpd:alpine` serve `./site-estatico-html` em modo somente leitura, na porta `80` do container / `8081` do host.

São **opções presentes na configuração pública sanitizada**, não comprovação de que o sistema local ainda utiliza exatamente esses valores.

### Pi-hole e Portainer

O exemplo do Pi-hole exige os valores locais de `PIHOLE_ADMIN_PASSWORD` e `PIHOLE_DNS_UPSTREAMS`, define o modo de escuta DNS como `ALL` e monta `./etc-pihole` e `./etc-dnsmasq.d`. Esse modo de escuta não comprova filtragem DNS em todas as VLANs.

O exemplo do Portainer monta `/var/run/docker.sock` e o volume `portainer_data`. O acesso ao socket Docker é administrativamente sensível; não publicar credenciais reais no exemplo.

## Redes e Proxy Reverso

![Redes Docker no Portainer](../../assets/images/docker/portainer-docker-networks.png)

O Portainer registrou **seis redes Docker**. O Compose principal declara uma bridge nomeada `zabbix-net`; os outros grupos Compose são separados. Não foi coletado um mapeamento completo de participação nas redes ou testes de conectividade entre todos os containers.

Arquivos públicos do Nginx:

- [Configuração principal](../../../docker_configs/reverse-proxy/nginx.conf)
- [Hosts virtuais e upstreams](../../../docker_configs/reverse-proxy/conf.d/lab.conf)

| Hostname demonstrativo | Destino do proxy |
|---|---|
| `portal.noc.example.test` | `site-estatico:80` |
| `zabbix.noc.example.test` | `zabbix-web:8080` |
| `grafana.noc.example.test` | `grafana:3000` |
| `status.noc.example.test` | `uptime-kuma:3001` |

Os arquivos declaram listeners HTTP/HTTPS e caminhos demonstrativos de certificados (`/etc/nginx/certs/lab.crt` e `lab.key`). As regras sanitizadas **não incluem** hosts virtuais para Pi-hole ou Portainer, apesar de esses serviços constarem no inventário; a configuração coletada do laboratório e o exemplo público possuem escopos diferentes. As regras publicadas não estabelecem redirecionamento automático de HTTP para HTTPS.

Certificados reais, senhas de banco, DNS interno e dados persistentes não estão publicados. A execução da stack exige os pré-requisitos locais e uma avaliação das interfaces expostas.

## Limites das Evidências

Os registros `docker ps` / Portainer de 6 de novembro estabelecem dez containers em execução, portas publicadas e quantidades de recursos. **Não** comprovam uptime contínuo, saúde completa de cada aplicação, acesso entre VLANs, alta disponibilidade, recuperação de backup ou hardening de produção.

- **Evidências Zabbix/Grafana:** [Zabbix](../monitoramento/zabbix.md) · [Grafana](../monitoramento/grafana.md).
- **DNS e disponibilidade:** [Pi-hole e Uptime Kuma](../servicos/dns-e-disponibilidade.md).
- **Serviços em outro computador Linux:** [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md).
- **Inventário Linux/estações:** [Inventário de Computadores e Servidores](../estacoes/inventario-de-computadores.md).
