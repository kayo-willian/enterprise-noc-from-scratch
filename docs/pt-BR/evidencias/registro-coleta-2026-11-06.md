# Registro de evidências — 6 de novembro de 2026

[English](../../evidence/evidence-collection-2026-11-06.md) | **Português (BR)**

> **Projeto:** Enterprise NOC — From Scratch  
> **Tipo de registro:** inventário preliminar da coleta  
> **Situação:** análise e seleção de evidências para publicação

## Visão geral

Em 6 de novembro de 2026, foi realizada uma coleta de evidências da infraestrutura física e lógica do laboratório. O material reúne fotografias dos equipamentos, capturas de estações de trabalho e ferramentas de monitoramento, registros de hardware e documentos técnicos.

Os arquivos originais são preservados em armazenamento privado de trabalho. As imagens e configurações somente serão incorporadas ao repositório após revisão de conteúdo e ocultação de identificadores ou informações sensíveis.

## Componentes documentados

| Área | Evidências coletadas |
|---|---|
| Infraestrutura física | Rack, roteador Cisco C8200L, switch Catalyst 9200L, patch panel, cabeamento e estações de trabalho. |
| Estações | Registros de oito computadores Windows e duas estações Linux com funções distintas no laboratório. |
| Redes | Capturas de configuração IP por setor e cópia histórica da configuração do switch, anterior à ativação do SNMP. |
| Telefonia e autenticação | Dois telefones Grandstream e documentação do servidor Asterisk/FreeRADIUS. |
| Containers | Registros do Docker/Portainer, com dez containers em execução no instante da coleta. |
| Observabilidade | Capturas de Zabbix, Grafana e Uptime Kuma, incluindo painéis de infraestrutura e serviços. |
| Serviços adicionais | Evidências de Pi-hole, proxy reverso e serviço web em container. |

## Limitações e pontos em revisão

- Alguns endereços IP exibidos nas estações divergem dos cadastrados no Zabbix na data da coleta.
- Há hosts indisponíveis, itens não suportados e painéis sem dados no material capturado; esses estados serão descritos como observações do período, sem afirmar disponibilidade contínua.
- As imagens precisam passar por revisão para ocultar informações institucionais, credenciais, identificadores de equipamentos e outros dados internos.
- A configuração histórica do switch não substitui uma exportação atualizada do equipamento.
- Modelos e características não legíveis nas evidências permanecerão como **não confirmados** no inventário.

## Próximas etapas

1. Selecionar as fotografias e capturas mais representativas de cada área.
2. Preparar cópias para publicação, preservando os originais privados.
3. Consolidar o inventário de computadores, equipamentos e serviços.
4. Relacionar cada evidência à página técnica correspondente.
5. Atualizar a apresentação do projeto no README e o acompanhamento das pendências nas Issues.

---

**Nota:** este documento registra a existência e o conteúdo geral das evidências coletadas; não constitui certificação de funcionamento contínuo, testes completos de segurança ou validação de todas as configurações.
