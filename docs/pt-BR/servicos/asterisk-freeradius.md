# Asterisk e FreeRADIUS — Telefonia e Autenticação

[English](../../services/asterisk-freeradius.md) | **Português (Brasil)**

**Fontes:** relatório Asterisk (30 de outubro de 2026), registros técnicos do FreeRADIUS, inventários Linux/serviços e fotografias dos telefones (6 de novembro de 2026).

Um computador Linux físico dedicado na **VLAN 50** executa Asterisk, FreeRADIUS, Zabbix Agent e OpenSSH. Os estados dos serviços e configurações abaixo são registros históricos; chamadas VoIP e transações wireless 802.1X não foram validadas independentemente de ponta a ponta.

## Servidor Físico

| Item | Configuração registrada |
|---|---|
| Computador | Dell OptiPlex 3020 |
| Processador / memória | Intel Core i5-4590 / aproximadamente 8 GB RAM |
| Sistema operacional | Debian GNU/Linux forky/sid |
| Kernel | `7.2.12+deb14-amd64` |
| Interface de rede | `enp2s0` |
| IPv4 / gateway / VLAN | `192.168.50.2/24` / `192.168.50.1` / 50 |
| Sistema de arquivos raiz | ext4, aproximadamente 211,21 GiB |

| Serviço systemd | Função | Estado registrado em 6 de novembro |
|---|---|---|
| `asterisk` | Telefonia IP | `active (running)` |
| `freeradius` | Autenticação de rede | `active (running)` |
| `zabbix-agent` | Monitoramento | `active (running)` |
| OpenSSH | Administração remota | `active (running)` |

## Asterisk — SIP/PJSIP

**Versão documentada:** `22.10.1`. O Asterisk utiliza PJSIP para cadastro dos terminais e sinalização SIP; RTP transporta áudio. O relatório também descreve IAX2 e AMI, sem estabelecer que foram utilizados em chamadas reais.

| Protocolo | Porta(s) | Finalidade documentada |
|---|---|---|
| SIP / UDP | 5060 | Sinalização e registro |
| RTP / UDP | 10000–20000 | Áudio |
| AMI / TCP | 5038 | Administração; documentada como restrita ao localhost |
| IAX2 / UDP | 4569 | Funcionalidade IAX2 |

### Terminais Grandstream

| Ramal | Setor | IPv4 do telefone |
|---|---|---|
| **1001** | Vendas | `192.168.50.10` |
| **1002** | TI | `192.168.50.11` |

![Telefone Grandstream de TI](../../assets/images/voip/20261106_182149.jpg)

A fotografia do telefone de TI apresenta `192.168.50.11`, correspondente ao ramal 1002 no relatório técnico.

![Telefone Grandstream de Vendas](../../assets/images/voip/20261106_182236.jpg)

A fotografia de Vendas apresenta `192.168.50.10`, correspondente ao ramal 1001. As imagens não permitem identificar os modelos exatos; o relatório anterior descrevia os dois ramais disponíveis, mas não foram coletados registros independentes de chamadas entre eles.

### Plano de Discagem Interno

**Caminho de configuração:** `/etc/asterisk/extensions.conf`

| Ramal | Aplicação documentada | Função |
|---|---|---|
| `1001` | `Dial(PJSIP/1001,30,tT)` | Vendas, timeout de 30 segundos, flags de transferência |
| `1002` | `Dial(PJSIP/1002,30,tT)` | TI, timeout de 30 segundos, flags de transferência |
| `8888` | `Playback(hello-world)` | Teste de reprodução de áudio |
| `9999` | `Echo()` | Teste de áudio/eco bidirecional |

As entradas do plano de discagem são configurações documentadas, não resultados de testes de chamadas comprovados separadamente.

## FreeRADIUS — Autenticação de Rede

**Versão documentada:** `3.2.10`. A configuração descrita utiliza RADIUS, IEEE 802.1X, EAP-PEAP/MSCHAPv2 e integração WPA2/WPA3-Enterprise. O caminho pretendido é dos clientes do Wi-Fi corporativo na **VLAN 60**, por meio do equipamento wireless e roteamento, até o FreeRADIUS **`192.168.50.2`** na VLAN 50.

```text
Cliente Wi-Fi corporativo (VLAN 60)
                 |
       Equipamento wireless
                 |
       Autenticação RADIUS
                 |
    Roteamento para VLAN 50
                 |
       FreeRADIUS 192.168.50.2
```

Não foram coletadas a configuração RADIUS do equipamento wireless ou logs de autenticação bem-sucedida de ponta a ponta.

| Protocolo | Porta | Função |
|---|---|---|
| RADIUS / UDP | 1812 | Autenticação |
| RADIUS / UDP | 1813 | Accounting |

**Diretório de configuração:** `/etc/freeradius/3.0/`.

| Componente | Função registrada |
|---|---|
| `clients.conf` | Clientes RADIUS autorizados |
| `users` | Registros locais de usuários |
| Configuração EAP | Métodos de autenticação |
| `freeradius.service` | Controle do serviço systemd |

Os relatórios originais contêm credenciais e configurações internas, omitidas aqui. **Validar a CA e a identidade do servidor no cliente é necessário para uso seguro de PEAP/MSCHAPv2**; desabilitar essa verificação enfraquece a autenticação.

## Monitoramento e Diagnóstico

O host de serviços é monitorado por Zabbix Agent a partir do servidor de infraestrutura registrado em `192.168.10.12`. O Grafana apresenta CPU/RAM e disponibilidade histórica do host, não chamadas ou transações RADIUS concluídas.

![Monitoramento Grafana do servidor Linux de voz](../../assets/images/monitoring/grafana/grafana_dashboard_asterisk.png)

Comandos de diagnóstico somente de leitura para **verificações locais futuras** (não se afirma ter coletado as saídas):

```bash
systemctl status asterisk --no-pager
systemctl status freeradius --no-pager
systemctl status zabbix-agent --no-pager
```

```bash
asterisk -rx "pjsip show endpoints"
asterisk -rx "core show channels"
asterisk -rx "dialplan show interno"
```

```bash
sudo ss -tulnp
```

Antes de publicar saídas, revisar credenciais e identificadores internos. Os estados, fotografias e dashboards não comprovam disponibilidade contínua, chamadas entre telefones ou autenticação Wi-Fi.

**Relacionado:** [Inventário dos Servidores](../estacoes/inventario-de-computadores.md) · [Zabbix](../monitoramento/zabbix.md) · [Grafana](../monitoramento/grafana.md) · [Serviços Docker](../containers/servicos-docker.md).
