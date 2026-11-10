# Análise de custos — Enterprise NOC From Scratch

**Idioma:** Português (Brasil) · **Moeda:** real (BRL) · **Base de preços:** 6 de novembro de 2026 · **Tipo de documento:** simulação financeira com subtotais parciais

> **Aviso:** este documento descreve uma **simulação financeira** baseada em preços de referência e premissas de implantação. **Não representa o valor efetivamente gasto**, uma proposta comercial, nem o custo final da infraestrutura. Totais são **parciais** enquanto existirem itens sem preço ou quantidade confirmada. Valores não confirmados **não devem ser interpretados como R$ 0,00**.

**Planilha de cálculo:** [Análise de custos da infraestrutura NOC — Excel](./analise-de-custos-infraestrutura-noc-pt-BR.xlsx). O `.xlsx` é a fonte editável dos cálculos; este `.md` é uma versão de leitura da mesma revisão.

> **Escopo financeiro:** Os valores abaixo são os subtotais de um cenário comparativo, não o orçamento integral do laboratório nem custos efetivamente pagos. O modelo financeiro mantém a premissa original de 9 computadores, enquanto o inventário físico identifica 10. Os valores de Wi-Fi foram calculados com referência comercial Intelbras W5 1200 GS; os equipamentos documentados da VLAN 60 e 70 são dois TP-Link Archer AX53. Portanto, os preços de Wi-Fi e os custos de computadores **não representam uma cotação completa da infraestrutura identificada**. A planilha XLSX permanece como fonte dos valores do cenário e precisa ser reconciliada antes de apresentar um custo total de implantação.

## 1. Objetivo e abrangência

O projeto reproduz uma infraestrutura corporativa fictícia, incluindo **estações de trabalho, rack, cabeamento estruturado, roteador e switch Cisco, Wi-Fi corporativo, IoT, telefonia IP, servidores Linux, containers Docker e monitoramento NOC**. A análise estima o investimento para adquirir e implantar o ambiente, o custo de implantação quando os ativos já existem e despesas recorrentes de operação.

A análise separa **equipamentos e consumíveis**, **ferramentas reutilizáveis**, **serviços técnicos**, **licenças** e **despesas mensais**. Preços de itens comparáveis não provam o modelo que está instalado. As quantidades ainda pendentes permanecem explicitamente identificadas.

## 2. Visão executiva dos três cenários

| Cenário | Situação | Valor parcial em 06/11/2026 | Inclui |
| --- | --- | --- | --- |
| **A — Implantação do zero** | Compra de equipamentos e materiais + instalação e configuração | R$ 46.606,36 | Equipamentos precificados, consumíveis selecionados e mão de obra simulada |
| **B — Equipamentos existentes** | Ativos principais fornecidos pela contratante | R$ 7.271,37 | Materiais adicionais selecionados e mão de obra simulada |
| **C — Operação mensal** | Infraestrutura já em funcionamento | R$ 355,00/mês | Horas mínimas simuladas de manutenção; despesas pendentes ficam de fora |

**Projeções parciais, sem inflação nem reajustes:**

| Indicador | Valor |
| --- | --- |
| C — 12 meses | R$ 4.260,00 |
| C — 36 meses | R$ 12.780,00 |
| A + 12 meses do C | R$ 50.866,36 |
| B + 12 meses do C | R$ 11.531,37 |

As projeções **não** incluem energia, internet, possíveis contratos de suporte, licenças Cisco ou custo dos computadores ainda não precificados. Também não representam suporte NOC 24×7.

## 3. Cenário A — Aquisição e implantação completa

Uma empresa começa sem a infraestrutura de referência e precisa comprar os equipamentos/materiais necessários e contratar a implantação. **Itens opcionais com quantidade zero não estão somados**; equipamentos pendentes não entraram no subtotal por falta de dados.

| Componente | Subtotal parcial | Critério |
| --- | --- | --- |
| Equipamentos e materiais | R$ 39.856,86 | Somente linhas ativas e precificadas do inventário |
| Mão de obra | R$ 6.749,50 | 32 atividades simuladas, detalhadas na seção de serviços |
| Licenças iniciais conhecidas | R$ 0,00 | Edições livres identificadas; contratos e outras licenças pendentes |
| Reserva e frete conhecidos | R$ 0,00 | Reserva definida como zero por padrão; frete não informado |
| **TOTAL A — PARCIAL** | **R$ 46.606,36** | Não inclui despesas ainda não precificadas |

### Composição por categoria

| Categoria | Subtotal A |
| --- | --- |
| Cisco | R$ 36.587,82 |
| Estações | R$ 0,00 |
| Wi-Fi / IoT | R$ 1.115,30 |
| Rack e energia | R$ 999,85 |
| Cabeamento | R$ 497,25 |
| Telefonia | R$ 499,98 |
| Ferramentas | R$ 156,66 |
| Mobiliário | R$ 0,00 |

### Inventário detalhado — equipamentos, materiais e ferramentas

**Leitura das tabelas:** `—` indica custo não computado no subtotal, seja por quantidade zero, compra desativada ou dado pendente. Os preços unitários são **referências de mercado registradas na planilha**, frequentemente de modelos similares; não são notas fiscais do ambiente. Os códigos **RF-xx** apontam para a seção de fontes.

#### Rede Cisco

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-001 | Roteador Cisco Catalyst C8200L — C8200L-1N-4T, SKU a confirmar | 1 un. | R$ 17.787,82 | R$ 17.787,82 | — | SKU exato pendente | RF-01 |
| EQ-002 | Switch Cisco Catalyst 9200L — C9200L-24P-4G-A, SKU/PoE/licença a confirmar | 1 un. | R$ 18.800,00 | R$ 18.800,00 | — | SKU exato pendente | RF-02 |
| EQ-033 | Módulos SFP/transceptores | 0 un. | Pendente | — | — | Opcional / validar | — |
| EQ-034 | Cabos/console/serial de gerenciamento | 0 un. | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** Os preços de Cisco dependem **fortemente de SKU, PoE, licenças, condição fiscal e suporte**. Modelos sugeridos como referência não substituem conferência do equipamento real. Módulos SFP e cabos de console estão fora do subtotal até verificação.

#### Estações

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-003 | Computadores montados no laboratório — Configurações pendentes • custo da aba Computadores | 9 un. | Pendente | — | — | Preço pendente | — |
| EQ-004 | Monitor avulso (se não incluído no PC) — Monitor 21'' econômico (somente se PC não inclui) | 0 un. | R$ 299,99 | — | — | Opcional / validar | RF-26 |
| EQ-005 | Teclado e mouse (se não incluídos no PC) — Kit teclado+mouse (somente se PC não inclui) | 0 un. | R$ 95,99 | — | — | Opcional / validar | RF-25 |
| EQ-006 | Servidor Linux / host Docker dedicado | 0 un. | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** A quantidade inicial usada é de **9 PCs**, mas ainda não há CPU/RAM/armazenamento nem preço unitário confirmados. Monitor e teclado/mouse só devem ser somados à parte se não estiverem incluídos no valor de cada PC. Servidor Docker adicional depende de verificar se é uma estação já contada.

#### Wi-Fi e IoT

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-007 | Dois TP-Link Archer AX53 (VLAN 60 + VLAN 70) — preço de referência comparativo: Intelbras W5 1200 GS, não corresponde ao modelo instalado | 2 un. | R$ 232,76 | R$ 465,52 | — | Modelo a confirmar | RF-03 |
| EQ-008 | Dispositivo Alexa com tela — Echo Show 5 — equipamento real não confirmado | 1 un. | R$ 599,00 | R$ 599,00 | — | Modelo a confirmar | RF-04 |
| EQ-009 | Lâmpada inteligente — Lâmpada Wi-Fi E27 compatível Alexa, ilustrativa | 1 un. | R$ 42,66 | R$ 42,66 | — | Modelo a confirmar | RF-05 |
| EQ-010 | Bocal / adaptador da lâmpada inteligente — Bocal E27, verificar se separado da lâmpada | 1 un. | R$ 8,12 | R$ 8,12 | — | Modelo a confirmar | RF-06 |

**Observação da categoria:** A rede documentada utiliza **dois TP-Link Archer AX53** em equipamentos separados, um na VLAN 60 e outro na VLAN 70. O preço unitário exibido nesta simulação corresponde ao Intelbras W5 1200 GS usado como comparativo de mercado, e não ao Archer AX53. W5 1200 GS, Echo Show 5 e lâmpada E27 são **comparativos**, ainda não identificações reais. Conferir se o bocal é item separado.

#### Rack e energia

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-011 | Rack 19 polegadas — Rack 12U — só comparativo; verificar tipo e U | 1 un. | R$ 650,56 | R$ 650,56 | — | Qtd. e modelo estimados | RF-07 |
| EQ-012 | Patch panel 24 portas — Patch panel 24p CAT6 referência econômica | 1 un. | R$ 202,35 | R$ 202,35 | — | Qtd. e modelo estimados | RF-08 |
| EQ-013 | Régua de energia para rack (PDU) — Régua rack 19'' 8 tomadas | 1 un. | R$ 99,00 | R$ 99,00 | — | Modelo a confirmar | RF-09 |
| EQ-014 | Organizador horizontal de cabos para rack — Organizador horizontal 1U | 1 un. | R$ 23,32 | R$ 23,32 | — | Modelo a confirmar | RF-10 |
| EQ-015 | Bandeja/suporte de rack (se utilizada) — Bandeja 300mm, se houver | 0 un. | R$ 53,20 | — | — | Opcional / validar | RF-11 |
| EQ-016 | Kit fixação rack (20 porcas/parafusos) — Kit 20 fixadores, preço do pacote | 1 un. | R$ 24,62 | R$ 24,62 | R$ 24,62 | Modelo a confirmar | RF-12 |
| EQ-017 | Nobreak / UPS | 0 un. | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** O rack 12U é apenas **referência de preço**; dimensões e componentes reais não foram medidos. O kit de fixadores é um **pacote de 20**, não o preço de cada parafuso. Bandejas e UPS só entram se existirem.

#### Cabeamento

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-018 | Caixa de cabo de rede CAT6 (305 m, ilustrativa) — 1 caixa 305m 100% cobre; categoria a confirmar | 1 un. | R$ 430,80 | R$ 430,80 | R$ 430,80 | Qtd. e modelo estimados | RF-13 |
| EQ-019 | Conectores RJ45 CAT6 (pacote de 100) — Pacote com 100 conectores | 1 un. | R$ 40,22 | R$ 40,22 | R$ 40,22 | Qtd. e modelo estimados | RF-14 |
| EQ-020 | Keystone RJ45 CAT6 (unidade) — Keystone CAT6 simples, se houver | 0 un. | R$ 7,60 | — | — | Opcional / validar | RF-15 |
| EQ-021 | Caixa/espelho de sobrepor para keystone — Caixa 2 pontos, sem keystones | 0 un. | R$ 7,15 | — | — | Opcional / validar | RF-16 |
| EQ-022 | Protetores de conector (boots) | 0 un. | Pendente | — | — | Opcional / validar | — |
| EQ-023 | Velcro para organização de cabos (rolo) — Rolo velcro 3 metros | 1 un. | R$ 13,97 | R$ 13,97 | R$ 13,97 | Modelo a confirmar | RF-17 |
| EQ-024 | Canaletas, conduítes e acessórios — Canaleta adesiva 2m, se houver | 0 un. | R$ 9,90 | — | — | Opcional / validar | RF-18 |
| EQ-025 | Patch cords comerciais adicionais | 0 un. | Pendente | — | — | Opcional / validar | — |
| EQ-036 | Abraçadeiras nylon (pacote de 100) — 3,5×200mm, pacote 100 | 1 pacote | R$ 12,26 | R$ 12,26 | R$ 12,26 | Qtd. estimada | RF-24 |
| EQ-037 | Protetores para plug RJ45 (boots) — Categoria a conferir | 0 pacote | Pendente | — | — | Opcional / validar | — |
| EQ-038 | Patch cord CAT6 pronto para uso — Comprimento a confirmar | 0 un. | Pendente | — | — | Opcional / validar | — |
| EQ-039 | Etiquetas de identificação / rotulagem — Marca/modelo a conferir | 0 pacote | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** Foi usada uma hipótese de **uma caixa de 305 m de cabo CAT6** e **um pacote de 100 conectores RJ45**, não uma medição da metragem instalada. Keystones, espelhos, canaletas e patch cords prontos não entram até confirmar uso. Evitar contar cabos montados manualmente duas vezes.

#### Telefonia

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-026 | Telefones IP Grandstream — GRP2601 utilizado como referência comercial; o modelo físico não consta das evidências de inventário | 2 un. | R$ 249,99 | R$ 499,98 | — | Qtd. e modelo estimados | RF-19 |
| EQ-027 | Headsets / acessórios de telefonia | 0 un. | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** Os dois Grandstream GRP2601 são **hipótese de quantidade e modelo**, sujeita a conferência. Fontes, PoE e demais acessórios devem ser checados.

#### Ferramentas

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-028 | Alicate de crimpagem RJ45 — Alicate de crimpagem reutilizável | 1 un. | R$ 74,01 | R$ 74,01 | — | Ferramenta reutilizável | RF-20 |
| EQ-029 | Testador de cabos de rede — Testador básico, NÃO certificador | 1 un. | R$ 39,99 | R$ 39,99 | — | Ferramenta reutilizável | RF-21 |
| EQ-030 | Ferramenta punch-down — Punch-down reutilizável | 1 un. | R$ 27,46 | R$ 27,46 | — | Ferramenta reutilizável | RF-22 |
| EQ-035 | Alicate decapador de cabos — Alicate decapador 3038 | 1 un. | R$ 15,20 | R$ 15,20 | — | Ferramenta reutilizável | RF-23 |

**Observação da categoria:** Alicate, testador básico, punch-down e decapador são **reutilizáveis**. O teste básico de continuidade **não equivale à certificação de cabeamento CAT6**. Ferramentas já existentes não são recompradas no cenário B.

#### Mobiliário

| ID | Item / referência | Qtd. | Preço unit. | A — subtotal | B — subtotal | Situação | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQ-031 | Bancadas e suportes para estações | 0 un. | Pendente | — | — | Opcional / validar | — |
| EQ-032 | Cadeiras e suportes de monitor | 0 un. | Pendente | — | — | Opcional / validar | — |

**Observação da categoria:** Bancadas, cadeiras e suportes estão **fora do orçamento-base** até decidir se mobiliário compõe o escopo de aquisição.

## 4. Cenário B — Contratação com equipamentos existentes

Neste cenário, a contratante já possui os roteadores, switches, computadores, rack e demais ativos principais. O preço considera **implantação/configuração** e somente os **consumíveis adicionais marcados como compra no cenário B**. Caso esses materiais também já estejam disponíveis, devem ser desmarcados na planilha para não criar custos artificiais.

- **Materiais adicionais:** R$ 521,87.
- **Mão de obra de implantação:** R$ 6.749,50.
- **Licenças iniciais (se aplicável):** R$ 0,00.
- **Frete / deslocamento adicional:** pendente, sem valor presumido.
- **TOTAL PARCIAL B:** **R$ 7.271,37**.

**Materiais adicionais atualmente incluídos no cenário B:**

| Material | Quantidade orçada | Subtotal B |
| --- | --- | --- |
| Kit fixação rack (20 porcas/parafusos) | 1 un. | R$ 24,62 |
| Caixa de cabo de rede CAT6 (305 m, ilustrativa) | 1 un. | R$ 430,80 |
| Conectores RJ45 CAT6 (pacote de 100) | 1 un. | R$ 40,22 |
| Velcro para organização de cabos (rolo) | 1 un. | R$ 13,97 |
| Abraçadeiras nylon (pacote de 100) | 1 pacote | R$ 12,26 |

O subtotal de mão de obra é **o mesmo no A e no B** nesta revisão, porque a planilha supõe o mesmo escopo de instalação; isso precisa ser reduzido se parte da montagem ou do cabeamento já estiver pronta. O B não é um contrato real nem uma tabela de preços obrigatória.

## 5. Serviços de implantação — composição da mão de obra

Os valores abaixo são **hipóteses comerciais editáveis**, calculadas a partir de quantidade × horas por unidade × tarifa horária. **Não representam salário, horas efetivamente medidas ou cotações comprovadas de prestadores.** A coluna de observações indica o alcance previsto e o que precisa ser validado.

| Código | Atividade técnica | Qtd. | Horas totais | R$/h | Subtotal | Observação |
| --- | --- | --- | --- | --- | --- | --- |
| MO-001 | Planejamento e levantamento dos pontos | 1 | 2 | R$ 55,00 | R$ 110,00 | Definir pontos, rotas e distâncias. |
| MO-002 | Passagem e organização do cabeamento | 1 | 6 | R$ 55,00 | R$ 330,00 | Horas estimadas para todo o laboratório. |
| MO-003 | Confecção manual de cabos RJ45 | 20 | 4 | R$ 55,00 | R$ 220,00 | 20 terminações/cabos apenas como cenário editável; conferir total. |
| MO-004 | Terminação e identificação do patch panel | 1 | 2 | R$ 55,00 | R$ 110,00 | Depende da quantidade de portas usadas. |
| MO-005 | Certificação e teste dos pontos de rede | 12 | 2.4000000000000004 | R$ 55,00 | R$ 132,00 | Teste simples com testador de continuidade; NÃO chamar de certificação de enlace CAT6. |
| MO-006 | Montagem, fixação e organização do rack | 1 | 3 | R$ 55,00 | R$ 165,00 | Inclui régua, patch panel e acomodação dos equipamentos. |
| MO-007 | Montagem e revisão dos computadores | 9 | 6.75 | R$ 50,00 | R$ 337,50 | Quantidade vinculada à premissa de PCs. |
| MO-008 | Instalação de sistema operacional e drivers | 9 | 6.75 | R$ 50,00 | R$ 337,50 | Quantidade vinculada à premissa financeira de nove PCs; não equivale ao inventário físico. |
| MO-009 | Endereçamento e testes de conectividade | 9 | 2.25 | R$ 50,00 | R$ 112,50 | Por PC; inclui validação DHCP/rede conforme cenário. |
| MO-010 | Planejamento IPv4, VLANs e segmentação | 1 | 3 | R$ 90,00 | R$ 270,00 | VLANs 10,20,30,40,50,60,70; projeto técnico. |
| MO-011 | Configuração do Catalyst 9200L | 1 | 4 | R$ 90,00 | R$ 360,00 | VLANs, access/trunk, segurança e validação; papéis a conferir. |
| MO-012 | Configuração do Catalyst C8200L | 1 | 4 | R$ 90,00 | R$ 360,00 | Roteamento, subinterfaces/ACLs conforme configuração real. |
| MO-013 | Implementação e testes de ACLs | 1 | 2 | R$ 90,00 | R$ 180,00 | Somente ACLs adicionais não incluídas na configuração básica do roteador. |
| MO-014 | Configuração dos dois roteadores wireless | 2 | 2 | R$ 90,00 | R$ 180,00 | Rede 60 e rede 70; modo roteador/AP ainda a confirmar. |
| MO-015 | Integração dos dispositivos de IoT | 1 | 1 | R$ 50,00 | R$ 50,00 | Configuração de Alexa/lâmpada por participantes; não atribuir autoria. |
| MO-016 | Implantação do FreeRADIUS e testes | 1 | 3 | R$ 70,00 | R$ 210,00 | Autenticação e integração na rede corporativa. |
| MO-017 | Implantação de Asterisk / VoIP | 1 | 4 | R$ 70,00 | R$ 280,00 | Instalação e configuração conforme evidências disponíveis. |
| MO-018 | Instalação e hardening básico do host Linux | 1 | 3 | R$ 70,00 | R$ 210,00 | Serviço hipotético de implantação de host Linux na simulação financeira. |
| MO-019 | Instalação Docker Engine e Compose | 1 | 2 | R$ 70,00 | R$ 140,00 | Rede, diretórios, políticas de reinício e testes. |
| MO-020 | Implantação MariaDB + Zabbix | 1 | 6 | R$ 70,00 | R$ 420,00 | Zabbix Server e interface Web, volumes e conexões. |
| MO-021 | Implantação do Grafana e datasources | 1 | 3 | R$ 70,00 | R$ 210,00 | Integração com Zabbix, usuários e painéis. |
| MO-022 | Desenvolvimento de dashboards NOC | 1 | 5 | R$ 70,00 | R$ 350,00 | Painéis de Zabbix e Grafana; horas de simulação comercial. |
| MO-023 | Monitoramento SNMP dos Cisco | 2 | 3 | R$ 90,00 | R$ 270,00 | Incluir monitoramento do switch incorporado em novembro. |
| MO-024 | Implantação do Uptime Kuma | 1 | 1.5 | R$ 70,00 | R$ 105,00 | Checagens, alertas e disponibilidade. |
| MO-025 | Implantação do Pi-hole / DNS interno | 1 | 2 | R$ 70,00 | R$ 140,00 | Resolução de nomes, integração DNS local. |
| MO-026 | Implantação do Nginx reverse proxy e TLS | 1 | 3 | R$ 70,00 | R$ 210,00 | Hospedagem local; certificados e segurança. |
| MO-027 | Publicação do portal HTML e testes | 1 | 2 | R$ 70,00 | R$ 140,00 | Portal estático; terminal animado possui dados simulados. |
| MO-028 | Configuração de Portainer (se instalado) | 1 | 1 | R$ 70,00 | R$ 70,00 | Validar que Portainer integra o escopo. |
| MO-029 | Definição de backups e persistência | 1 | 2 | R$ 70,00 | R$ 140,00 | Planejar persistência/backup; teste de recuperação somente se executado. |
| MO-030 | Testes ponta a ponta de acesso e monitoração | 1 | 4 | R$ 60,00 | R$ 240,00 | Conectividade, segregação, serviços, evidências. |
| MO-031 | Diagramas técnicos e inventário | 1 | 3 | R$ 60,00 | R$ 180,00 | Documentação profissional de arquitetura e infraestrutura. |
| MO-032 | Relatórios de configuração e entrega | 1 | 3 | R$ 60,00 | R$ 180,00 | Incluir análise de custos, credenciais excluídas. |

**Horas técnicas estimadas:** 101.65 h. **Custo de mão de obra:** **R$ 6.749,50**.

**Critério de cobrança:** serviços simples receberam estimativas menores; tarefas complexas, como configuração de rede Cisco, utilizam taxas diferentes. Entretanto, as tarifas **não foram verificadas com empresas locais** e precisam ser ajustadas antes de qualquer proposta comercial. Também é necessário evitar dupla cobrança por tarefas já abrangidas por instalação, configuração ou testes.

## 6. Cenário C — Operação e manutenção

Representa um ambiente já instalado. O subtotal atual cobre **manutenção preventiva limitada**, não uma equipe dedicada, monitoramento humano 24 horas por dia, atendimento com SLA ou operação empresarial integral. Itens pendentes e opcionais não são tratados como gratuitos.

| ID | Despesa / atividade | Quantidade | Valor unitário | Subtotal mensal | Ativo? | Observação |
| --- | --- | --- | --- | --- | --- | --- |
| OP-001 | Energia elétrica (rack + estações) | 1 mês | Pendente | — | Sim | Potência, tarifa e regime de uso pendentes; fórmula ligada às Premissas. |
| OP-002 | Link de internet / WAN | 1 mês | Pendente | — | Sim | Informe apenas quando plano e preço mensal forem conhecidos. |
| OP-003 | Suporte Linux e containers (preventivo) | 2 h/mês | R$ 70,00 | R$ 140,00 | Sim | 2h mensais hipotéticas; não equivale a suporte 24×7. |
| OP-004 | Administração de equipamentos Cisco e Wi-Fi | 1 h/mês | R$ 90,00 | R$ 90,00 | Sim | 1h/mês de manutenção; incidentes fora do pacote podem ser adicionais. |
| OP-005 | Revisão de painéis e alarmes NOC | 1 h/mês | R$ 70,00 | R$ 70,00 | Sim | Atividade distinta do suporte Linux; evitar duplicidade de horas. |
| OP-006 | Verificação de backups | 1 h/mês | R$ 55,00 | R$ 55,00 | Sim | Validação operacional mínima; armazenamento não incluso. |
| OP-007 | Fundo de reposição / peças | 1 mês | Pendente | — | Não | Não pressupor reserva sem política definida. |
| OP-008 | Armazenamento externo de backup | 1 mês | Pendente | — | Não | Só se for contratado; não confundir com volume local Docker. |
| OP-009 | Suporte/licenças recorrentes Cisco | 1 mês | Pendente | — | Não | Licenças e contratos dependem de SKU e contratação real. |
| OP-010 | Certificado TLS público comercial | 1 mês | Pendente | — | Não | Certificado privado/local não implica assinatura. |
| OP-011 | Suporte profissional de software | 1 mês | Pendente | — | Não | OSS gratuito não implica suporte contratado. |
| OP-012 | Domínio público / DNS externo | 1 mês | Pendente | — | Não | Domínios .local são internos; só incluir se adquirir domínio público. |

**Total parcial mensal:** **R$ 355,00**. **12 meses:** R$ 4.260,00. **36 meses:** R$ 12.780,00 (sem reajustes).

**Despesas ainda ausentes:** energia elétrica, internet, eventuais contratos e licenças pagos, armazenamento externo, peças e reservas. A simulação usa **2 h/mês** de suporte Linux/containers, **1 h/mês** de administração de redes, **1 h/mês** de revisão de dashboards e **1 h/mês** de verificação de backup. Esses serviços não equivalem à disponibilidade permanente de um operador NOC.

### Energia e internet: por que não há valor ainda?

A planilha exige potência média do rack/servidores e das estações, horas mensais de uso e tarifa elétrica (R$/kWh). Sem esses dados, estimar energia com um número arbitrário seria enganoso. A referência de funcionamento é **720 h/mês para o rack** e **176 h/mês por PC**, mas esses horários são somente hipóteses ajustáveis. O link de internet também depende do plano efetivamente contratado.

## 7. Software e licenciamento

A licença de uso de diversas soluções livres pode custar **R$ 0,00**, mas **implantação, manutenção, infraestrutura e suporte não são gratuitos**. O valor zero só foi aplicado às edições comunitárias/livres identificadas; edições comerciais, contratos e sistemas operacionais das estações não foram presumidos gratuitos.

| ID | Software / serviço | Regime | Licença inicial considerada | Status / ressalva |
| --- | --- | --- | --- | --- |
| SW-001 | Ubuntu / Debian Linux | Software livre | R$ 0,00 | Confirmar distribuição/versão no servidor físico. |
| SW-002 | Docker Engine / Compose | Software livre | R$ 0,00 | Edição comunitária, sem subscrição paga prevista. |
| SW-003 | Portainer Community Edition | Edição comunitária | R$ 0,00 | Se Portainer CE realmente estiver implantado; BE tem licenças próprias. |
| SW-004 | Zabbix Server / Web / Agent | Software livre | R$ 0,00 | Zabbix OSS, sem custo de licença de uso. |
| SW-005 | Grafana OSS | Software livre | R$ 0,00 | Edição OSS; verificar se instalada. |
| SW-006 | Uptime Kuma | Software livre | R$ 0,00 | Software de código aberto. |
| SW-007 | Pi-hole | Software livre | R$ 0,00 | Software de código aberto. |
| SW-008 | MariaDB Community | Software livre | R$ 0,00 | Banco de dados comunitário. |
| SW-009 | Nginx Open Source | Software livre | R$ 0,00 | Não considerar Nginx Plus sem contrato. |
| SW-010 | Apache HTTP Server | Software livre | R$ 0,00 | Portal HTML estático. |
| SW-011 | Asterisk | Software livre | R$ 0,00 | Licença de software distinta de configuração e telefonia. |
| SW-012 | FreeRADIUS | Software livre | R$ 0,00 | Software de código aberto. |
| SW-013 | Cisco IOS XE / DNA / SmartNet | A confirmar | Pendente | Assinaturas, suporte e direito de uso dependem do SKU do hardware. |
| SW-014 | Sistema operacional das estações | A confirmar | Pendente | Se houver Windows, checar situação de licenciamento OEM/volume. |
| SW-015 | Certificados TLS / PKI privada | A confirmar | Pendente | Certificado autoassinado não implica pagamento, mas exige administração. |

**Licenças iniciais precificadas nesta revisão:** **R$ 0,00** (somente soluções livres identificadas). Cisco IOS XE, contratos de suporte/licenciamento, sistema operacional das estações e eventuais certificados comerciais **permanecem pendentes**.

## 8. Computadores e critérios para a próxima revisão

A planilha considera provisoriamente **9 computadores** dentro de uma faixa inicial aproximada de 8 a 10 unidades, mas a quantidade efetiva pode ser maior. Nenhum deles foi precificado: **0 de 9 estações têm valor completo registrado**. Isso afeta diretamente o cenário A e pode alterar energia e outros custos de operação no C.

O orçamento dos PCs será preenchido por perfil ou máquina, registrando **processador, placa-mãe, RAM, SSD/HD, vídeo, monitor/periféricos incluídos, quantidade e fonte do preço**. PCs com componentes diferentes não devem receber artificialmente um preço único sem justificar a média. O servidor Linux só deve ser adquirido/contabilizado à parte se não for um dos computadores já incluídos.

## 9. Premissas que influenciam os resultados

| Parâmetro | Valor atual | Critério |
| --- | --- | --- |
| PCs previstos (estimativa) | 9 un. | Faixa inicial informada: aproximadamente 8 a 10; confirmar o número final. |
| PCs — limite inferior | 8 un. | Referência de quantidade informada. |
| PCs — limite superior | 10 un. | A quantidade pode ser maior; atualizar após inventário. |
| Hora técnica — cabeamento | R$ 55,00/h | Hipótese comercial, sem cotação local; ajustar conforme orçamento de prestadores. |
| Hora técnica — montagem/suporte | R$ 50,00/h | Hipótese comercial, sem cotação local. |
| Hora técnica — Linux / containers | R$ 70,00/h | Hipótese comercial, sem cotação local. |
| Hora técnica — redes Cisco | R$ 90,00/h | Hipótese comercial, sem cotação local; pode mudar por complexidade. |
| Hora técnica — testes/documentação | R$ 60,00/h | Hipótese comercial, sem cotação local. |
| Potência média rack/servidores | Pendente | Medir ou estimar com modelos confirmados (uso contínuo). |
| Potência média por estação | Pendente | Valor médio durante expediente; depende da configuração de cada PC. |
| Tarifa elétrica completa | Pendente | Inserir valor da concessionária com tributos, quando conhecido. |
| Horas mensais rack/servidores | 720 h/mês | Simulação 24h × 30 dias; alterar se o ambiente não operar continuamente. |
| Horas mensais de cada PC | 176 h/mês | 22 dias × 8h; cenário de empresa em horário comercial. |
| Internet contratada por mês | Pendente | Preencher apenas quando plano e valor forem conhecidos. |
| Reserva de imprevistos inicial | R$ 0,00 | Opcional. Zero por padrão para não inflar; só alterar se desejado. |
| Frete / deslocamento inicial | Pendente | Não presumido; cotar para a localidade antes do fechamento. |
| Referência de preços | 06/11/2026 data | Data de compilação das referências da aba Fontes. |
| Unidade monetária | BRL real | Por enquanto somente reais. Versão bilíngue e conversão ficam para depois. |

**Regra de consistência:** quando a planilha estiver atualizada, este documento deve ser revisado **na mesma alteração**, pois Markdown não recalcula fórmulas. Não copiar valores antigos para uma versão nova do inventário.

## 10. Exclusões e Premissas do Modelo Financeiro

Os principais pontos a confirmar são:

1. **Computadores:** quantidade efetiva, especificações, preços de compra e periféricos incluídos.
2. **Cisco:** código completo dos modelos, PoE, módulos, licenciamento e condições comerciais.
3. **Wi-Fi:** os dois equipamentos são TP-Link Archer AX53; o preço de referência Intelbras não representa uma cotação do modelo documentado.
4. **Rack:** altura em U, profundidade, tipo, equipamentos instalados, suportes e sistema elétrico.
5. **Cabeamento:** CAT5e/CAT6, metragem, pontos de rede, conexões, patch panel, keystones e consumíveis realmente utilizados.
6. **Telefonia:** quantidade e modelo dos telefones Grandstream; fontes e acessórios.
7. **Servidores:** identificar se o host Docker é uma estação já contada ou um equipamento independente.
8. **Mão de obra:** validar horas e tarifas com referências locais; ajustar tarefas já realizadas e evitar sobreposição.
9. **Operação:** consumo elétrico, horas de funcionamento, tarifa local, internet e contratos necessários.
10. **Despesas externas:** frete, impostos conforme destino, eventual reserva e equipamentos opcionais efetivos.

Os campos **pendentes não foram zerados** para caber em uma estimativa mais baixa. Um orçamento realista deve refletir o custo verificável, mesmo quando isso aumentar ou diminuir o resultado inicial.

## 11. Fontes de preços registradas na planilha

As 28 referências abaixo foram **registradas na planilha Excel do projeto** e estavam datadas de **06/11/2026**. Os preços anunciados podem mudar; links de lojas podem apontar para páginas de busca, produtos similares, condições fiscais específicas ou anúncios indisponíveis. **Não houve nova verificação independente das ofertas para este relatório Markdown.**

| ID | Produto de referência | Fornecedor / referência | Preço anunciado | Consulta | Link e ressalva |
| --- | --- | --- | --- | --- | --- |
| RF-01 | Cisco Catalyst C8200L-1N-4T | Switches Express — C8200L-1N-4T | R$ 17.787,82 | 06/11/2026 | [Consultar anúncio](https://switches.express/produto/router-cisco-c8200l-1n-4t/). Preço de referência; apenas CNPJ contribuinte ICMS SP; confirme o SKU. |
| RF-02 | Cisco Catalyst C9200L-24P-4G-A | MultiNetwork — C9200L-24P-4G-A | R$ 18.800,00 | 06/11/2026 | [Consultar anúncio](https://www.multinetwork.com.br/produto/switch-cisco-c9200l-24p-4g-a/). Preço indicativo para empresa em SP; disponibilidade e faturamento sob análise. |
| RF-03 | Roteador Intelbras, modelo semelhante | Loja Intelbras — W5 1200 GS | R$ 232,76 | 06/11/2026 | [Consultar anúncio](https://loja.intelbras.com.br/w5-roteador-1200gs/p). Modelo comparativo, não é confirmação do modelo instalado. |
| RF-04 | Echo Show com tela, comparativo | Mercado Livre (busca) — Echo Show 5 3ª geração | R$ 599,00 | 06/11/2026 | [Consultar anúncio](https://lista.mercadolivre.com.br/amazon-echo-show-5-3rd-gen-preto). Preço histórico de listagem comercial, sem cotação formal ou frete incluído. |
| RF-05 | Lâmpada inteligente Wi-Fi E27 | KaBuM! — Intelbras ELW 1001 | R$ 42,66 | 06/11/2026 | [Consultar anúncio](https://www.kabum.com.br/produto/1043228/lampada-inteligente-led-wi-fi-elw-1001-intelbras). Modelo comparativo compatível com Alexa; modelo real desconhecido. |
| RF-06 | Bocal E27 com chave | Central Elétrica — PVC E27 | R$ 8,12 | 06/11/2026 | [Consultar anúncio](https://www.lojacentraleletrica.com.br/produto/soquete-porta-lampada-com-chave-pvc-latao-e27). Somente se adquirido à parte. |
| RF-07 | Mini rack de parede 19" 12U | Solução Cabos — 12U x 570 mm | R$ 650,56 | 06/11/2026 | [Consultar anúncio](https://www.solucaocabos.com.br/mini-rack-de-parede-19--12us-x-570mm-branco/p). REFERÊNCIA de rack; medir U, profundidade, carga e tipo real. |
| RF-08 | Patch panel CAT6 24 portas | Solução Cabos — SC 24 portas CAT6 | R$ 202,35 | 06/11/2026 | [Consultar anúncio](https://www.solucaocabos.com.br/patch-panel-24-portas-cat6-dc/p). Alternativa econômica; patch panel REAL pode ser outra categoria. |
| RF-09 | Régua rack 19" 8 tomadas | Rack Outdoor — 8 tomadas 10A | R$ 99,00 | 06/11/2026 | [Consultar anúncio](https://rackoutdoor.com.br/shop/acessorios/reguas-de-tomadas/regua-de-tomada-para-rack-19-com-8-tomadas-10a-com-protecao/). Valor de loja, verificar tipo de tomada. |
| RF-10 | Guia horizontal rack 1U | Unicaserv — Pier Telecom ACR0012 | R$ 23,32 | 06/11/2026 | [Consultar anúncio](https://www.unicaserv.com.br/linha-metalurgica/acessorios-para-rack/guia-de-cabos-horizontal-fechada-padrao-19-1u-preta). Preço à vista, peça individual. |
| RF-11 | Bandeja fixa rack 19" 1U | Raitek — Max Eletron 300 mm | R$ 53,20 | 06/11/2026 | [Consultar anúncio](https://www.raitekdistribuidora.com.br/racks-e-acessorios/bandejas). Dimensão ilustrativa; verificar se bandeja existe. |
| RF-12 | Kit 20 porcas gaiola e parafusos | HD Store — Kit GForce 20 pç | R$ 24,62 | 06/11/2026 | [Consultar anúncio](https://www.hdstore.com.br/kit-porca-gaiola-parafuso-m5-padrao-rack-servidor-pacote-20-pecas). Pacote inteiro; não multiplicar por unidade. |
| RF-13 | Cabo CAT6 cobre 305m | PrimeCabos — UTP 23AWG 100% cobre | R$ 430,80 | 06/11/2026 | [Consultar anúncio](https://www.primecabos.com/cabo-de-rede/cabo-cat6). Caixa 305m; CAT6 é hipótese, validar categoria real. |
| RF-14 | Conector RJ45 CAT6 pacote 100 | KaBuM! — Plus Cable LA-CAT6 100p | R$ 40,22 | 06/11/2026 | [Consultar anúncio](https://www.kabum.com.br/produto/1066948/conector-rj45-plus-cable-cat-6-la-cat6-c-100-pecas). Pacote de 100, não 100 pacotes. |
| RF-15 | Keystone CAT6 | Central Cabos — WT-2002-BK simples | R$ 7,60 | 06/11/2026 | [Consultar anúncio](https://www.centralcabos.com.br/redes/keystone/cat6). Peça econômica; validar se havia keystone nas bancadas. |
| RF-16 | Caixa de sobrepor 2 keystones | Rede Loja — Seccon WT2073 | R$ 7,15 | 06/11/2026 | [Consultar anúncio](https://redeloja.com/produto/1747314101615). Peça sem keystones; apenas se instalada. |
| RF-17 | Velcro organização de cabos | Unicaserv — Rolo 3m | R$ 13,97 | 06/11/2026 | [Consultar anúncio](https://www.unicaserv.com.br/racks-e-acessorios/acessorios-para-racks/organizadores-para-racks). Pode substituir ou complementar abraçadeiras. |
| RF-18 | Canaleta adesiva 20x10 2m | Sodimac — Steck Conduteck 2m | R$ 9,90 | 06/11/2026 | [Consultar anúncio](https://www.sodimac.com.br/sodimac-br/product/780771/canaleta-com-adesivo-20x10mm-2-metros/780771/). Somente se utilizada; metro linear exige outro cálculo. |
| RF-19 | Telefone IP Grandstream | KaBuM! — GRP2601 | R$ 249,99 | 06/11/2026 | [Consultar anúncio](https://www.kabum.com.br/produto/194967/telefone-ip-grandstream-2-linhas-visor-lcd-preto-grp2601). Modelo ilustrativo; validar Grandstream real. |
| RF-20 | Alicate crimpador RJ45 | LC Ferragens — Vonder RJ45 | R$ 74,01 | 06/11/2026 | [Consultar anúncio](https://www.lcferragens.com.br/produto/alicate-crimpar-vonder-rj-45/). Ferramenta reutilizável; comprar apenas se a empresa não possuir. |
| RF-21 | Testador básico de cabos | FGTEC — Plus Cable LT-100 | R$ 39,99 | 06/11/2026 | [Consultar anúncio](https://www.fgtec.com.br/perifericos/testador-de-cabo-de-rede-pluscable-rj11-rj45-lt-100). Verifica continuidade, não certifica enlaces CAT6. |
| RF-22 | Ferramenta punch-down | Central Cabos — Exbom FRM-APD314 | R$ 27,46 | 06/11/2026 | [Consultar anúncio](https://www.centralcabos.com.br/ferramenta/alicates). Inserção keystone/patch panel; validar ferramenta usada. |
| RF-23 | Alicate decapador | Central Cabos — Alicate decapador 3038 | R$ 15,20 | 06/11/2026 | [Consultar anúncio](https://www.centralcabos.com.br/ferramenta/alicates). Ferramenta opcional reutilizável. |
| RF-24 | Abraçadeira nylon 100 unidades | Unicaserv — 3,5 x 200 mm 100p | R$ 12,26 | 06/11/2026 | [Consultar anúncio](https://www.unicaserv.com.br/infra-estrutura/abracadeiras/abracadeira-de-nylon-3-5mm-x-200mm-branca-cento). Preço de pacote 100, não preço unitário. |
| RF-25 | Teclado e mouse com fio, kit | KaBuM! — Logitech MK120 | R$ 95,99 | 06/11/2026 | [Consultar anúncio](https://www.kabum.com.br/perifericos/teclado-mouse). Opcional se já estiver no custo de PC. |
| RF-26 | Monitor simples 21" | Terabyte — BRX 21 60Hz | R$ 299,99 | 06/11/2026 | [Consultar anúncio](https://www.terabyteshop.com.br/produto/42811/monitor-brx-21-pol-60hz-hdmivga-vesa-preto-mbrx21bk). Opcional se já estiver no custo de PC. |
| RF-27 | Preço alternativo Cisco 8200L | Xtech — C8200L-1N-4T | R$ 23.422,08 | 06/11/2026 | [Consultar anúncio](https://xtech.com.br/cisco-catalyst-8200l-with-1-nim-slot-and-4x1g-wan-ports/p/55138/). Referência anterior; não somar alternativa ao inventário. |
| RF-28 | Preço alternativo Cisco 9200L | Xtech — C9200L-24P-4G-A | R$ 35.917,41 | 06/11/2026 | [Consultar anúncio](https://xtech.com.br/Switch-Cisco-Catalyst-9200l-24-Port-Poe-4-X-1g-Network-Advanta-C9200l-24p-4g-A/p/52916/). Referência alternativa mais alta; não somar. |

## 12. Limitações e transparência

- **Estimativas, não despesas históricas:** nenhum subtotal deve ser apresentado como desembolso efetivo ou orçamento formal contratado.
- **Modelos comparativos:** muitos preços são de itens similares e dependem de confirmação física antes do fechamento.
- **Software livre não elimina operação:** R$ 0,00 de licença não substitui mão de obra, servidores ou suporte.
- **Sem duplicidade:** patch cords montados manualmente, componentes já incluídos em PCs e ferramentas existentes não devem ser cobrados novamente.
- **Escopo:** a infraestrutura empresarial é simulada para fins técnicos; custos variam conforme fornecimento existente, quantidades, localização, frete, impostos e exigências de suporte.
- **Documentos distintos:** Excel serve aos cálculos e à edição; Markdown serve à consulta rápida e deve acompanhar as revisões do Excel.

---

**Última revisão desta transcrição:** 06/11/2026 · **Idioma:** português brasileiro · **Situação:** valores parciais sujeitos à verificação.
