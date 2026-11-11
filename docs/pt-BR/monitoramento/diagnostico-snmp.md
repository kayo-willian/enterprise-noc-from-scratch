# Cisco Catalyst C9200L — Diagnóstico SNMP

[English](../../monitoring/snmp-troubleshooting.md) | **Português (Brasil)**

**Intervenção registrada:** 4 de novembro de 2026 · **Equipamento:** Cisco Catalyst C9200L · **Protocolo:** SNMPv2c · **Monitoramento:** Zabbix 7.0 LTS / Grafana

Este registro apresenta **três resultados documentados de troubleshooting**, não a disponibilidade atual do switch ou a resolução de alertas posteriores.

## Caso 1 — Interface SNMP Indisponível

**Sintoma:** Após cadastrar o C9200L no Zabbix, a interface SNMP permanecia indisponível e não era possível coletar as métricas do switch.

**Investigação registrada:**
1. Verificar a conectividade IP entre o servidor Linux de monitoramento e o switch.
2. Conferir a acessibilidade SNMP e executar consultas pelo terminal Linux.
3. Comparar a configuração SNMP do switch com o cadastro do host no Zabbix.

**Causa confirmada:** O host Zabbix herdava uma comunidade SNMP diferente da configurada no switch.

**Correção:** Alinhar as comunidades, configurar a macro `{$SNMP_COMMUNITY}` no host e recarregar o cache de configuração do Zabbix Server:

```bash
docker exec zabbix-server zabbix_server -R config_cache_reload
```

**Resultado registrado:** A interface SNMP ficou disponível; a coleta de métricas e a descoberta automática das interfaces foram restabelecidas.

## Caso 2 — Uptime Incorreto

**Sintoma:** O widget de uptime mostrava `0`, embora o switch estivesse funcionando.

**Causa registrada:** O item selecionado retornava valor incorreto para este equipamento Cisco IOS-XE.

**Alteração do item:**

| Item anterior | Item substituto |
|---|---|
| `system.hw.uptime[hrSystemUptime.0]` | `system.net.uptime[sysUpTime.0]` |

**Resultado registrado:** O dashboard passou a apresentar o uptime informado pelo switch.

## Caso 3 — Widgets de Eventos Vazios

**Sintoma:** Alguns widgets de eventos estavam vazios mesmo com o monitoramento operacional.

**Causa confirmada:** Os filtros selecionavam apenas o switch recém-cadastrado, que não apresentava problemas ativos naquele momento.

**Correção:** Ampliar os filtros para incluir a infraestrutura do NOC, não somente o switch.

**Resultado registrado:** Os widgets passaram a apresentar registros de monitoramento e alertas operacionais relevantes.

## O que as Três Investigações Demonstram

O registro de **4 de novembro de 2026** é importante porque separa **três falhas diferentes**:

**1. Falha de coleta SNMP:** após cadastrar o C9200L, a interface SNMP permanecia indisponível. Foram consideradas conectividade IP, consultas SNMP a partir do Linux, configuração do switch e comunidade herdada no host Zabbix. A **divergência confirmada de comunidade** foi corrigida pela macro `{$SNMP_COMMUNITY}` e atualização do cache de configuração Zabbix. O resultado registrado foi retorno da descoberta de interfaces e da coleta. Apenas testar ping não identificaria a divergência de configuração.

**2. Métrica de uptime incorreta:** o switch operava, mas o widget mostrava **0**. O problema era o item selecionado, não indisponibilidade comprovada. A substituição de `system.hw.uptime[hrSystemUptime.0]` por `system.net.uptime[sysUpTime.0]` normalizou o uptime exibido no caso histórico. Um SNMP acessível não garante compatibilidade de todos os itens com o dispositivo.

**3. Widgets vazios:** os filtros consideravam apenas o switch recém-adicionado, sem problemas ativos naquele momento. Ampliar os alvos para o ambiente NOC fez aparecer alertas relevantes. Lista de problemas vazia pode resultar de **filtro/visão**, não falha de coleta.

São **resultados de correções documentadas**, não novos testes. O relatório não inclui captura de pacotes ou SNMP walk bruto. Não confundir esses casos com os itens não suportados ou painéis Windows `No data` de 6 de novembro. Comunidades reais permanecem fora da documentação pública.

## Observações Operacionais

- Conectividade IP não garante coleta SNMP; comunidade e macro Zabbix precisam corresponder.
- As chaves dos itens devem ser compatíveis com as métricas do equipamento; validar os valores após a alteração.
- Widgets vazios podem refletir o filtro aplicado, não falha de coleta.
- A implantação registrada utilizou **SNMPv2c**. SNMPv3 com autenticação e criptografia é preferível em produção.
- As comunidades reais e configurações sensíveis do switch não estão incluídas neste estudo de caso público.

**Fonte:** Relatório técnico de implementação de 4 de novembro de 2026. Itens Zabbix não suportados, agentes indisponíveis e painéis `No data` posteriores permanecem observações distintas.

**Evidências relacionadas:** [Zabbix](zabbix.md) · [Grafana](grafana.md) · [Registro do switch](../redes/registro-switch-vlans-2026-11-04.md)
