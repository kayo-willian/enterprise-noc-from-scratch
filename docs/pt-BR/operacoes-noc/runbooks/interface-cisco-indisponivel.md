# Runbook — Interface Cisco Indisponível ou Degradada

[English](../../../noc-operations/runbooks/cisco-interface-unavailable.md) | **Português (Brasil)**

**Projeto:** Enterprise NOC — From Scratch · Tapajós Inovações  
**Categoria:** NET / PHY / MON · **Tipo de documento:** Runbook de diagnóstico operacional  
**Equipamentos:** Switch Cisco Catalyst C9200L e roteador C8200L

## 1. Objetivo e evidências

Este runbook orienta a investigação de interface indisponível, contadores de erros incomuns, perda de conectividade de uma VLAN ou estado SNMP inconsistente. A captura de 04/11 registra `Gi1/0/1` como trunk do roteador; `Gi1/0/2–3` na VLAN 10; `Gi1/0/4–6` na VLAN 20; `Gi1/0/7–8` na VLAN 30; `Gi1/0/9–10` na VLAN 40; `Gi1/0/11–13` associadas à VLAN 50; `Gi1/0/14` na VLAN 70 e `Gi1/0/15` na VLAN 60. É uma **configuração histórica**, não um mapa de estados em tempo real.

Os painéis Grafana mostram interfaces `UP` e `DOWN` e alguns rótulos repetidos. O nome mostrado não identifica necessariamente cada porta física. Uma porta reserva desligada não é automaticamente um incidente.

## 2. Segurança e autorização

- Utilizar CLI Cisco em modo de leitura, dashboards autorizados e topologia física atual.
- Não retirar cabos, trocar patch cords, aplicar `shutdown`, alterar modo access/trunk, spanning tree ou ACLs como atalho de diagnóstico.
- Antes de qualquer correção, preservar a configuração pertinente em local seguro, avaliar impacto, obter autorização e definir reversão.
- Não publicar senhas, comunidades SNMP, segredos de gerenciamento ou configurações integrais não sanitizadas.

## 3. Definir o estado esperado

| Interface | Uso registrado | Atenção no diagnóstico |
|---|---|---|
| `Gi1/0/1` | Trunk para o C8200L | Estado do trunk, VLANs e alcance da interrupção |
| `Gi1/0/2–10` | Acesso dos departamentos | Confirmar estação e VLAN correspondente |
| `Gi1/0/11` | Servidor Asterisk/FreeRADIUS, VLAN 50 | Modo operacional **não estabelecido** na captura |
| `Gi1/0/12–13` | Telefones Grandstream | Conferir endpoints e alimentação conforme equipamento atual |
| `Gi1/0/14` | Archer AX53 IoT | VLAN 70 no registro datado |
| `Gi1/0/15` | Archer AX53 corporativo | VLAN 60 no registro datado |

A interface física do lado do roteador e as subinterfaces exatas não estão demonstradas em uma exportação completa. Não atribuir nomes presumidos.

## 4. Sequência de diagnóstico

### A. Correlacionar alertas

Registrar horário, hostname, índice e descrição SNMP, tráfego histórico e impacto. Conferir se aquela porta **deveria** estar conectada atualmente. Comparar descoberta de interfaces no Zabbix com a consulta do painel Grafana antes de confiar em seu rótulo.

### B. Inspeção Cisco não disruptiva

Executar em modo EXEC autorizado, substituindo a interface pelo destino confirmado:

~~~text
show interfaces status
show interfaces GigabitEthernet1/0/1
show interfaces trunk
show vlan brief
show interfaces counters errors
show spanning-tree interface GigabitEthernet1/0/1 detail
show mac address-table interface GigabitEthernet1/0/1
show logging
~~~

Preferir comandos por interface a exportar publicamente toda a configuração. Alguns comandos variam conforme plataforma, versão e privilégios.

### C. Interpretar os estados

| Observação | Interpretação ou verificação necessária |
|---|---|
| `administratively down` | Porta desabilitada; confirmar responsável e estado esperado |
| `notconnect` ou ausência de link | Verificar alimentação, cabo, transceptor ou caminho físico |
| Link up sem tráfego da VLAN | Conferir VLAN access, tags trunk, MAC e roteamento |
| Erros CRC/input aumentando | Investigar meio físico, conectores e qualidade de interface |
| Spanning Tree impedindo encaminhamento | Confirmar função STP e topologia antes de afirmar falha |
| SNMP `DOWN` e CLI indicando up | Conferir índice SNMP, horário de coleta e rótulo do Grafana |

Contadores de erro precisam de contexto temporal: valor histórico diferente de zero não comprova uma falha atual.

### D. Exceção na porta do servidor da VLAN 50

A configuração de `Gi1/0/11` em 04/11 registra `switchport access vlan 50` e `spanning-tree portfast trunk` sem `switchport mode access` explícito. Inspecionar modo operacional e configuração **atuais** antes de classificá-la como access ou trunk. Preservar essa particularidade histórica.

### E. Validar camada 3 separadamente

Se link e VLAN aparentam estar corretos, testar por **estações autorizadas** usando endereços atuais, gateways e serviços esperados. Os gateways `192.168.10.1`, `192.168.20.1`, `192.168.30.1` e `192.168.40.1` são observações datadas, não prova das interfaces atuais do roteador. Link ativo não comprova comunicação inter-VLAN nem aplicação de ACLs.

## 5. Decisão de correção e escalonamento

Não alterar roteador/switch antes de delimitar impacto e provável domínio da falha. Escalonar quando o trunk afeta vários departamentos, quando for cogitada alteração de roteamento/ACLs, diante de suspeita de defeito físico ou ausência de acesso à configuração atual. Falha de coleta SNMP deve ser tratada inicialmente como falha de monitoramento se o encaminhamento da rede ainda funciona.

## 6. Validação da recuperação

1. Confirmar função **atual** e estado físico esperado da interface.
2. Verificar VLAN/trunk com comandos de leitura.
3. Comprovar funcionamento do endpoint/serviço afetado por teste funcional apropriado.
4. Confirmar novas métricas válidas e mapeamento correto de interface SNMP para painel.
5. Registrar mudança (se houver), horários de teste, erros remanescentes e reversão.

## 7. Evidências e classificação

Registrar ID da porta, equipamento, VLAN, fuso/horário, estados antes/depois, resultados não disruptivos, usuários/serviços afetados, causa confirmada versus hipóteses, ação autorizada e validação. Não transformar porta ociosa `DOWN` em interrupção inventada.

## 8. Referências

- [Gerenciamento de incidentes](../gerenciamento-de-incidentes.md)
- [Mapa de portas](../../redes/mapa-de-portas-switch.md)
- [Captura da configuração Cisco](../../redes/registro-switch-vlans-2026-11-04.md)
- [Evidências do roteador](../../redes/roteador-c8200l.md)
- [Diagnóstico SNMP: três casos registrados](../../monitoramento/diagnostico-snmp.md)
- [Topologia consolidada](../../redes/topologia-logica-consolidada.md)

**Limite das evidências:** Os comandos são recomendações; não se afirma nova inspeção ou correção executada.