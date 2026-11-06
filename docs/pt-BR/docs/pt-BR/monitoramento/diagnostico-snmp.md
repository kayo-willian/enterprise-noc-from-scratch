# Cisco Catalyst 9200L — Diagnóstico e Resolução de Problemas SNMP

**[English](../../monitoring/snmp-troubleshooting.md) | Português (Brasil)**

## Visão Geral

Este estudo de caso documenta as atividades de diagnóstico e resolução de problemas realizadas durante a integração de um switch Cisco Catalyst 9200L ao ambiente de monitoramento de um NOC corporativo.

A infraestrutura utiliza Zabbix 7.0 LTS para monitoramento e Grafana para visualização de dados.

**Equipamento:** Cisco Catalyst 9200L  
**Protocolo de monitoramento:** SNMPv2c  
**Plataforma:** Zabbix 7.0 LTS  
**Data:** 4 de novembro de 2026

## Incidente 1 — Monitoramento SNMP Indisponível

### Problema

Após cadastrar o Catalyst 9200L no Zabbix, a interface SNMP permaneceu indisponível.

As requisições de monitoramento falhavam, impedindo a coleta das métricas do equipamento.

### Investigação

O processo de diagnóstico envolveu:

1. Verificar a conectividade IP entre o servidor Linux e o switch.
2. Verificar a acessibilidade do serviço SNMP.
3. Realizar consultas SNMP pelo terminal Linux.
4. Analisar a configuração do switch.
5. Verificar a comunidade SNMP configurada no Zabbix.

### Causa Raiz

O switch e o Zabbix estavam utilizando valores diferentes para a comunidade SNMP.

O host cadastrado no Zabbix herdava uma comunidade incompatível com a configuração do equipamento.

### Solução

As configurações SNMP foram alinhadas entre os dois sistemas.

Foi configurada a macro `{$SNMP_COMMUNITY}` especificamente para o host no Zabbix.

Posteriormente, o cache de configuração do servidor foi recarregado:

```bash
docker exec zabbix-server zabbix_server -R config_cache_reload
```

### Resultado

A interface SNMP tornou-se disponível, permitindo a coleta de métricas e a descoberta automática das interfaces do switch.

## Incidente 2 — Uptime Incorreto

### Problema

O dashboard apresentava um valor de uptime igual a zero, embora o switch estivesse funcionando normalmente.

### Causa Raiz

O item de monitoramento utilizava uma métrica de uptime que retornava um valor incorreto para o equipamento Cisco IOS-XE.

### Solução

O item foi alterado de:

`system.hw.uptime[hrSystemUptime.0]`

Para:

`system.net.uptime[sysUpTime.0]`

### Resultado

O dashboard passou a apresentar corretamente o uptime informado pelo switch.

## Incidente 3 — Widgets Sem Dados

### Problema

Alguns widgets apresentavam resultados vazios, apesar de a infraestrutura de monitoramento estar funcionando.

### Causa Raiz

Os widgets afetados estavam configurados para exibir informações exclusivamente do switch recém-cadastrado.

Como o equipamento não apresentava problemas ativos, as listas de alarmes permaneciam vazias.

### Solução

Os filtros dos dashboards foram ajustados para considerar o ambiente completo do NOC.

### Resultado

Os widgets passaram a exibir as informações de monitoramento e os alertas operacionais relevantes.

## Lições Técnicas

- Conectividade IP não garante que o monitoramento esteja funcionando corretamente.
- Comunidades SNMP e macros de monitoramento precisam estar consistentes.
- Os itens de monitoramento devem ser compatíveis com as métricas disponibilizadas pelo equipamento.
- Filtros incorretos podem prejudicar a visualização de informações operacionais.
- Alterações no monitoramento precisam ser acompanhadas de testes de validação.

## Considerações de Segurança

A implementação original do laboratório utilizou SNMPv2c.

Para ambientes de produção, deve-se considerar o SNMPv3 com autenticação e criptografia.

Endereços IP internos, comunidades SNMP e outras informações sensíveis foram omitidos desta documentação pública.

## Status da Documentação

**Status:** Documentado com base no relatório técnico de implementação de 4 de novembro de 2026.

Evidências adicionais poderão ser incorporadas após verificação.
