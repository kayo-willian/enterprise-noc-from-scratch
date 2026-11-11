# Análise de Custos da Infraestrutura — Enterprise NOC

**Enterprise NOC — From Scratch**  
**Tapajós Inovações — Ambiente Corporativo Fictício**

**Português (Brasil)** | [English (USD)](../../costs/enterprise-noc-final-budget-usd-2026.md)

**Planilhas:** [Excel — Português (BRL)](enterprise-noc-orcamento-final-brl-2026.xlsx) | [Excel — English (USD)](../../costs/enterprise-noc-final-budget-usd-2026.xlsx)

| Informação | Especificação |
|---|---|
| Projeto | Enterprise NOC — From Scratch |
| Ambiente | Infraestrutura corporativa de referência |
| Empresa fictícia | Tapajós Inovações |
| Documento | Análise financeira e orçamento de referência |
| Idioma | Português brasileiro |
| Moeda | Real brasileiro (BRL) |
| Data-base | 11 de novembro de 2026 |
| Modelo | Aquisição, implantação e operação |
| Fonte dos cálculos | Planilha Microsoft Excel / LibreOffice Calc |
| Cenários | A — Aquisição integral; B — Ativos existentes; C — Operação |
| Situação | Modelo financeiro consolidado |

> **Nota financeira:** os valores representam uma simulação de aquisição, implantação e operação de uma infraestrutura equivalente à documentada no projeto. Não correspondem a pagamentos realizados, notas fiscais, contratos firmados ou propostas comerciais vinculantes. Os preços anunciados e as premissas financeiras estão identificados separadamente.

---

# 1. Objetivo e Abrangência

Esta análise apresenta o custo estimado para reproduzir e operar a infraestrutura corporativa documentada no projeto **Enterprise NOC — From Scratch**.

O modelo financeiro contempla equipamentos de rede, computadores, servidores Linux, recursos de monitoramento, telefonia IP, equipamentos wireless, cabeamento estruturado, montagem, configuração, licenciamento e despesas recorrentes.

O orçamento foi organizado para responder a três questões:

1. Quanto custaria adquirir e implementar toda a infraestrutura?
2. Quanto custaria implementar a solução quando os equipamentos principais já estão disponíveis?
3. Qual seria a despesa mensal estimada para manter essa infraestrutura em operação?

Os resultados são apresentados por meio de três cenários financeiros independentes e relacionados:

| Cenário | Denominação | Finalidade |
|---|---|---|
| A | Aquisição e implantação completa | Estimar investimento inicial com compra integral dos ativos |
| B | Implantação com ativos existentes | Estimar materiais adicionais, serviços técnicos e deslocamento |
| C | Operação e manutenção | Estimar despesas mensais e projeções recorrentes |

A planilha utiliza fórmulas para relacionar equipamentos, quantidades, preços, horas técnicas, consumo energético, serviços e provisões financeiras.

## 1.1. Fundamentação Técnica

O orçamento foi elaborado a partir da infraestrutura registrada nos documentos técnicos do projeto.

As principais referências são:

- [Visão geral da infraestrutura](../arquitetura/visao-geral-da-infraestrutura.md)
- [Infraestrutura física](../evidencias/infraestrutura-fisica.md)
- [Inventário de computadores e servidores](../estacoes/inventario-de-computadores.md)
- [Redes e arquitetura](../redes/README.md)
- [Mapa de portas do Cisco Catalyst C9200L](../redes/mapa-de-portas-switch.md)
- [Docker e serviços](../containers/servicos-docker.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Dashboards Grafana](../monitoramento/grafana.md)
- [Asterisk e FreeRADIUS](../servicos/asterisk-freeradius.md)
- [Registro de coleta de evidências](../evidencias/registro-coleta-2026-11-06.md)

Os registros físicos e de monitoramento foram coletados principalmente em **4 e 6 de novembro de 2026**.

As referências financeiras foram consolidadas na planilha com data-base de **11 de novembro de 2026**, incluindo referências comerciais anteriores preservadas no levantamento.

## 1.2. Natureza dos Valores

A planilha diferencia quatro categorias de informação financeira.

| Natureza | Definição |
|---|---|
| Preço anunciado | Valor apresentado por fornecedor ou referência comercial |
| Preço comparável | Valor de equipamento semelhante ao utilizado na infraestrutura |
| Premissa financeira | Valor adotado para simular determinada despesa ou condição operacional |
| Valor calculado | Resultado produzido pelas fórmulas da planilha |

Um preço comparável não confirma que o equipamento físico possui exatamente o mesmo fabricante, configuração comercial ou SKU.

Da mesma forma, um serviço incluído no orçamento de implantação não significa que sua execução tenha sido comprovada nos registros técnicos.

---

# 2. Infraestrutura Considerada

O orçamento utiliza o inventário físico e lógico documentado no projeto.

## 2.1. Equipamentos Principais

| Componente | Quantidade | Características |
|---|---:|---|
| Roteador Cisco Catalyst C8200L | 1 | Infraestrutura de roteamento corporativo |
| Switch Cisco Catalyst C9200L-24T-4G | 1 | Comutação e segmentação por VLANs |
| Computadores Windows | 8 | Estações departamentais |
| Computadores Linux | 2 | Monitoramento e telefonia/autenticação |
| TP-Link Archer AX53 | 2 | Redes wireless corporativa e IoT |
| Telefones IP Grandstream | 2 | Terminais de telefonia SIP |
| Dispositivo Amazon Alexa | 1 | Equipamento associado à rede IoT |
| Rack 19 polegadas | 1 referência de aquisição | Organização da infraestrutura de rede |
| Patch panel | 1 referência de aquisição | Terminação e organização do cabeamento |
| Monitor | 10 unidades orçadas | Um monitor por computador no cenário de aquisição |
| Kit teclado e mouse | 10 unidades orçadas | Um conjunto por computador no cenário de aquisição |

Os dez computadores físicos incluem os dois servidores Linux.

O servidor principal de monitoramento não é contabilizado novamente como equipamento adicional.

## 2.2. Segmentação de Rede

A infraestrutura documentada utiliza sete VLANs.

| VLAN | Finalidade |
|---|---|
| 10 | TI e infraestrutura |
| 20 | Contabilidade |
| 30 | Financeiro |
| 40 | Vendas |
| 50 | Telefonia IP e autenticação |
| 60 | Wi-Fi corporativo |
| 70 | Internet das Coisas |

A segmentação está associada à infraestrutura Cisco e aos serviços Linux documentados.

Os dois TP-Link Archer AX53 representam equipamentos físicos diferentes, vinculados às VLANs 60 e 70.

As despesas de configuração dessas redes estão previstas na composição dos serviços de implantação.

---

# 3. Estrutura da Planilha Financeira

A planilha contém **11 abas**, organizadas conforme a função de cada conjunto de dados.

| Aba | Finalidade |
|---|---|
| Painel | Consolidação financeira e indicadores gerais |
| Cenário A | Aquisição integral e implantação |
| Cenário B | Implantação com equipamentos existentes |
| Cenário C | Custos de operação e projeções |
| Inventário | Equipamentos, quantidades, preços e subtotais |
| Computadores | Inventário individual dos dez computadores |
| Implantação | Atividades técnicas, horas e tarifas |
| Operação mensal | Despesas recorrentes |
| Software | Licenças e subscrições |
| Premissas | Parâmetros financeiros e operacionais |
| Fontes | Referências comerciais e critérios de preço |

## 3.1. Organização dos Cálculos

A estrutura utiliza a seguinte sequência de dependências:

```text
FONTES
   |
   v
PREMISSAS
   |
   +-------------------+
   |                   |
   v                   v
INVENTÁRIO         COMPUTADORES
   |                   |
   +---------+---------+
             |
             v
        CENÁRIO A
             |
IMPLANTAÇÃO--+
             |
SOFTWARE-----+
             |
             v
           PAINEL


PREMISSAS
   |
   v
OPERAÇÃO MENSAL
   |
   v
CENÁRIO C
   |
   v
PAINEL


INVENTÁRIO + IMPLANTAÇÃO + PREMISSAS
             |
             v
        CENÁRIO B
             |
             v
           PAINEL
```

Os valores calculados não são independentes: alterações nos parâmetros utilizados pelas fórmulas modificam automaticamente os subtotais correspondentes.

## 3.2. Elementos de Controle

A planilha emprega:

- Identificadores individuais para equipamentos, serviços, custos e premissas.
- Categorias para agrupamento financeiro.
- Quantidades e unidades comerciais.
- Preços unitários em BRL.
- Fórmulas para subtotais e totais.
- Indicadores de inclusão nos cenários.
- Referências às fontes de preços.
- Descrições do escopo de cada item.
- Parâmetros editáveis para simulações financeiras.

Os campos de inclusão permitem distinguir os equipamentos considerados no cenário-base daqueles mantidos apenas como referências opcionais.

---

# 4. Resumo Executivo

## 4.1. Resultados Consolidados

| Indicador | Valor |
|---|---:|
| **Cenário A — Aquisição e implantação completa** | **R$ 86.683,14** |
| **Cenário B — Implantação com ativos existentes** | **R$ 7.448,85** |
| **Cenário C — Operação mensal** | **R$ 1.084,09** |
| Operação durante 12 meses | R$ 13.009,08 |
| Operação durante 36 meses | R$ 39.027,24 |
| Cenário A + 12 meses de operação | R$ 99.692,22 |
| Cenário B + 12 meses de operação | R$ 20.457,93 |

Todos os resultados estão expressos em reais.

As projeções de 12 e 36 meses utilizam valores constantes, sem correção monetária, reajustes contratuais ou expansão de capacidade.

## 4.2. Indicadores de Cobertura

O painel também apresenta a abrangência do modelo:

| Indicador | Quantidade |
|---|---:|
| Computadores físicos | 10 |
| Estações Windows | 8 |
| Servidores Linux | 2 |
| Linhas do inventário de equipamentos e materiais | 37 |
| Referências financeiras e técnicas | 45 |
| Atividades técnicas de implantação | 32 |
| Premissas financeiras e operacionais | 35 |

Os totais representam os registros organizados na planilha, incluindo itens opcionais no inventário.

---

# 5. Cenário A — Aquisição e Implantação Completa

O Cenário A representa a reprodução da infraestrutura mediante aquisição dos equipamentos e contratação das atividades de implantação.

São considerados:

- Equipamentos Cisco.
- Computadores e periféricos.
- Redes wireless e equipamento IoT.
- Rack e acessórios.
- Cabeamento estruturado.
- Telefonia IP.
- Ferramentas de montagem.
- Serviços técnicos.
- Provisão de licenças.
- Frete.
- Reserva financeira para imprevistos.

## 5.1. Composição do Investimento Inicial

| Componente | Valor |
|---|---:|
| Equipamentos e materiais | R$ 58.729,88 |
| Serviços de implantação | R$ 6.837,00 |
| Licenças iniciais provisionadas | R$ 12.792,00 |
| Frete e distribuição | R$ 2.055,55 |
| Reserva de imprevistos | R$ 6.268,71 |
| **TOTAL — CENÁRIO A** | **R$ 86.683,14** |

O total corresponde à soma dos cinco componentes financeiros.

```text
Cenário A =
Equipamentos e materiais
+ Serviços de implantação
+ Licenças iniciais
+ Frete
+ Reserva de imprevistos
```

Substituindo pelos valores da planilha:

```text
R$ 58.729,88
+ R$  6.837,00
+ R$ 12.792,00
+ R$  2.055,55
+ R$  6.268,71
----------------
R$ 86.683,14
```

Na planilha, o cálculo está consolidado em:

`Cenário A!D24`

## 5.2. Equipamentos por Categoria

| Categoria | Subtotal |
|---|---:|
| Rede Cisco | R$ 42.514,68 |
| Estações | R$ 12.732,50 |
| Wi-Fi e IoT | R$ 1.298,98 |
| Rack e energia | R$ 999,85 |
| Cabeamento | R$ 527,23 |
| Telefonia | R$ 499,98 |
| Ferramentas | R$ 156,66 |
| Mobiliário | R$ 0,00 |
| **TOTAL DE EQUIPAMENTOS E MATERIAIS** | **R$ 58.729,88** |

O mobiliário possui referências de preço próprias, mas está excluído do cenário-base.

O valor zero nessa categoria corresponde à ausência de aquisição prevista no modelo, não à gratuidade dos produtos.

## 5.3. Frete e Distribuição

O orçamento considera uma provisão de **3,5%** sobre o valor dos equipamentos e materiais.

```text
Frete = Total de materiais × 3,5%
```

```text
R$ 58.729,88 × 0,035 = R$ 2.055,55
```

Essa provisão representa uma estimativa de transporte regional.

O valor não corresponde a cotação individual de transportadora ou cálculo específico por endereço de entrega.

## 5.4. Reserva de Imprevistos

A reserva financeira corresponde a **8%** do subtotal formado por equipamentos, implantação e licenças.

```text
Reserva =
(Equipamentos + Implantação + Licenças) × 8%
```

```text
(R$ 58.729,88 + R$ 6.837,00 + R$ 12.792,00) × 0,08

Reserva = R$ 6.268,71
```

A reserva é uma provisão orçamentária.

Ela não representa despesa realizada.

---

# 6. Inventário Financeiro de Equipamentos e Materiais

A aba **Inventário** contém 37 linhas de equipamentos e materiais.

Cada item possui identificador, categoria, descrição, modelo de referência, quantidade, unidade comercial, preço, indicação de inclusão e subtotal.

A planilha diferencia a aquisição integral do Cenário A e os materiais adicionais do Cenário B.

## 6.1. Equipamentos Cisco

| ID | Equipamento | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-001 | Cisco Catalyst C8200L | 1 | R$ 23.422,08 | R$ 23.422,08 |
| EQ-002 | Cisco Catalyst C9200L-24T-4G-E | 1 | R$ 19.068,00 | R$ 19.068,00 |
| EQ-033 | Transceptor SFP 1 Gbps — opcional | 0 | R$ 150,00 | R$ 0,00 |
| EQ-034 | Cabo console USB–RJ45 | 1 | R$ 24,60 | R$ 24,60 |
| **Total** | | | | **R$ 42.514,68** |

### Cisco Catalyst C8200L

O roteador físico documentado pertence à família Cisco Catalyst C8200L.

A referência financeira utiliza o modelo comercial `C8200L-1N-4T`.

O valor considera exclusivamente o equipamento na referência selecionada. Contratos de suporte, subscrições e demais condições comerciais não estão automaticamente incluídos.

### Cisco Catalyst C9200L

O switch documentado é um Cisco Catalyst C9200L-24T-4G.

A planilha utiliza como referência o `C9200L-24T-4G-E`, com 24 portas de dados e quatro uplinks de 1 Gbps.

A escolha dessa referência evita utilizar o preço de uma variante PoE como se ela correspondesse ao modelo de 24 portas de dados documentado.

A presença de interfaces SFP no equipamento não determina a aquisição de transceptores. Por esse motivo, os módulos permanecem fora do cenário-base.

### Cabo de Console

O inventário inclui um cabo comercial USB–RJ45 para administração serial.

O preço corresponde a uma referência de mercado e não identifica necessariamente o acessório específico utilizado na coleta histórica.

---

## 6.2. Computadores e Periféricos

| ID | Equipamento | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-003 | Computadores físicos | 10 | R$ 868,31 | R$ 8.683,10 |
| EQ-004 | Monitores de 21 polegadas | 10 | R$ 299,99 | R$ 2.999,90 |
| EQ-005 | Kits teclado e mouse | 10 | R$ 104,95 | R$ 1.049,50 |
| EQ-006 | Servidor Docker adicional — excluído | 0 | R$ 868,31 | R$ 0,00 |
| **Total** | | | | **R$ 12.732,50** |

O modelo adota um desktop corporativo recondicionado como referência comercial de aquisição.

Os dez computadores já contemplam:

- Oito estações Windows.
- Um computador Debian destinado ao NOC e à infraestrutura Docker.
- Um computador Debian destinado a Asterisk e FreeRADIUS.

A aquisição de um servidor Docker adicional não integra o orçamento, pois o computador responsável por essa função já está contabilizado.

No cenário de aquisição integral, foram provisionados dez monitores e dez kits de teclado e mouse.

Esses periféricos são contabilizados separadamente do preço dos desktops.

---

## 6.3. Wi-Fi e IoT

| ID | Equipamento | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-007 | TP-Link Archer AX53 | 2 | R$ 299,99 | R$ 599,98 |
| EQ-008 | Amazon Echo Show 5 — comparável | 1 | R$ 699,00 | R$ 699,00 |
| EQ-009 | Lâmpada inteligente E27 — opcional | 0 | R$ 42,66 | R$ 0,00 |
| EQ-010 | Bocal E27 — opcional | 0 | R$ 8,12 | R$ 0,00 |
| **Total** | | | | **R$ 1.298,98** |

A infraestrutura utiliza dois equipamentos TP-Link Archer AX53:

- Um associado à VLAN 60, destinada ao Wi-Fi corporativo.
- Outro associado à VLAN 70, destinada à rede IoT.

O orçamento considera o mesmo modelo comercial documentado.

Para o dispositivo Alexa com tela, foi utilizado o Echo Show 5 como referência de preço.

Essa referência não estabelece o modelo exato do equipamento físico.

A lâmpada inteligente e o respectivo bocal estão disponíveis no inventário como itens opcionais, sem participação no investimento-base.

---

## 6.4. Rack e Energia

| ID | Equipamento | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-011 | Rack 19 polegadas — referência 12U | 1 | R$ 650,56 | R$ 650,56 |
| EQ-012 | Patch panel CAT6 de 24 portas | 1 | R$ 202,35 | R$ 202,35 |
| EQ-013 | Régua de energia para rack | 1 | R$ 99,00 | R$ 99,00 |
| EQ-014 | Organizador horizontal de cabos | 1 | R$ 23,32 | R$ 23,32 |
| EQ-015 | Bandeja para rack — opcional | 0 | R$ 53,20 | R$ 0,00 |
| EQ-016 | Kit com 20 fixadores para rack | 1 | R$ 24,62 | R$ 24,62 |
| EQ-017 | Nobreak 1200 VA — opcional | 0 | R$ 799,00 | R$ 0,00 |
| **Total** | | | | **R$ 999,85** |

O rack de 12U representa uma referência comercial para reprodução da infraestrutura.

A documentação física apresenta rack, equipamentos Cisco, patch panel e componentes de organização. As dimensões comerciais do rack usado como referência financeira não constituem medição do rack fotografado.

O nobreak e a bandeja permanecem como alternativas de ampliação do orçamento.

---

## 6.5. Cabeamento Estruturado

| ID | Material | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-018 | Caixa de cabo CAT6 — 305 metros | 1 | R$ 430,80 | R$ 430,80 |
| EQ-019 | Conectores RJ45 CAT6 — pacote com 100 | 1 | R$ 40,22 | R$ 40,22 |
| EQ-020 | Keystone CAT6 — opcional | 0 | R$ 7,60 | R$ 0,00 |
| EQ-021 | Caixa de sobrepor — opcional | 0 | R$ 7,15 | R$ 0,00 |
| EQ-023 | Velcro para organização de cabos | 1 | R$ 13,97 | R$ 13,97 |
| EQ-024 | Canaleta adesiva — opcional | 0 | R$ 9,90 | R$ 0,00 |
| EQ-036 | Abraçadeiras — pacote com 100 | 1 | R$ 12,26 | R$ 12,26 |
| EQ-037 | Protetores RJ45 — opcionais | 0 | R$ 25,00 | R$ 0,00 |
| EQ-038 | Patch cord CAT6 de 2 metros — opcional | 0 | R$ 25,00 | R$ 0,00 |
| EQ-039 | Etiquetas para identificação de cabos | 1 | R$ 29,98 | R$ 29,98 |
| **Total** | | | | **R$ 527,23** |

A caixa de 305 metros corresponde a uma unidade comercial de aquisição.

Ela não representa uma medição precisa da extensão total do cabeamento instalado.

Os conectores são contabilizados por pacote, evitando a multiplicação incorreta do preço por 100 unidades.

O modelo financeiro também distingue a confecção manual de cabos da compra de patch cords prontos, evitando contabilizar simultaneamente duas alternativas para o mesmo material.

---

## 6.6. Telefonia IP

| ID | Equipamento | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-026 | Telefone IP Grandstream | 2 | R$ 249,99 | R$ 499,98 |
| EQ-027 | Headset de telefonia — opcional | 0 | R$ 120,00 | R$ 0,00 |
| **Total** | | | | **R$ 499,98** |

O projeto possui dois telefones IP Grandstream associados ao ambiente Asterisk.

A planilha utiliza o modelo GRP2601 como referência comercial.

A documentação dos serviços registra os ramais 1001 e 1002 e seus respectivos endereços IP.

O preço do telefone é separado dos custos de implantação e configuração do sistema de telefonia.

---

## 6.7. Ferramentas

| ID | Ferramenta | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-028 | Alicate de crimpagem RJ45 | 1 | R$ 74,01 | R$ 74,01 |
| EQ-029 | Testador básico de cabos | 1 | R$ 39,99 | R$ 39,99 |
| EQ-030 | Ferramenta punch-down | 1 | R$ 27,46 | R$ 27,46 |
| EQ-035 | Alicate decapador | 1 | R$ 15,20 | R$ 15,20 |
| **Total** | | | | **R$ 156,66** |

As ferramentas são consideradas reutilizáveis.

Seu custo integra a aquisição inicial, mas não é repetido mensalmente.

O testador básico de continuidade não substitui um certificador profissional de enlaces CAT6.

---

## 6.8. Mobiliário

| ID | Item | Qtd. | Preço unitário | Subtotal A |
|---|---|---:|---:|---:|
| EQ-031 | Bancada ou mesa de trabalho | 0 | R$ 350,00 | R$ 0,00 |
| EQ-032 | Cadeira operacional | 0 | R$ 200,00 | R$ 0,00 |

O mobiliário foi mantido como categoria financeira opcional.

O orçamento-base concentra-se na aquisição e reprodução da infraestrutura de TI.

---

# 7. Inventário dos Computadores

A aba **Computadores** detalha individualmente as dez máquinas incluídas no projeto.

O preço comercial adotado é de **R$ 868,31 por desktop**, com base em referência de equipamento corporativo recondicionado.

Esse preço não estabelece que todas as máquinas físicas possuam o mesmo fabricante ou modelo comercial.

## 7.1. Inventário Individual

| ID | Função | Sistema operacional | RAM | Armazenamento | Referência de preço |
|---|---|---|---|---|---:|
| PC-01 | TI / NOC principal | Debian 13 | ≈ 8 GB | Raiz ext4 de 210,27 GiB | R$ 868,31 |
| PC-02 | TI | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-03 | Contabilidade 1 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-04 | Contabilidade 2 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-05 | Contabilidade 3 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-06 | Financeiro 1 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-07 | Financeiro 2 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-08 | Vendas 1 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-09 | Vendas 2 | Windows 11 Pro 21H2 | 8 GB | 224 GB exibidos | R$ 868,31 |
| PC-10 | Telefonia / autenticação | Debian forky/sid | ≈ 8 GB | Raiz ext4 de 211,21 GiB | R$ 868,31 |
| **Total** | **10 computadores** | | | | **R$ 8.683,10** |

## 7.2. Processadores

O Intel Core i5-4590 consta das especificações documentadas dos dois computadores Dell OptiPlex 3020 utilizados como servidores e das estações Windows com identificação de hardware disponível.

Na estação Windows PC-02, o i5-4590 permanece como referência da configuração predominante, sem identificação individual do processador nas evidências de hardware utilizadas na composição original.

A referência financeira utiliza o mesmo valor comercial para os dez desktops.

## 7.3. Padronização das Estações Windows

As oito estações Windows seguem o padrão de inventário adotado:

- Windows 11 Pro 21H2.
- 8 GB de memória RAM.
- 224 GB de capacidade de armazenamento exibida.

Essas características foram consolidadas a partir das evidências disponíveis e da padronização informada para o laboratório.

O valor exibido de armazenamento não identifica, por si só, a tecnologia física utilizada pela unidade.

## 7.4. Servidor Principal do NOC

O computador principal é um Dell OptiPlex 3020 executando Debian 13.

Sua função inclui a hospedagem dos componentes Docker de monitoramento e infraestrutura.

Entre os serviços documentados estão Zabbix, Grafana, Portainer, Pi-hole e Uptime Kuma.

A partição raiz documentada possui aproximadamente **210,27 GiB**.

O orçamento considera essa máquina dentro do total de dez computadores.

## 7.5. Servidor Asterisk e FreeRADIUS

O segundo computador Linux executa Debian forky/sid e hospeda os serviços de telefonia IP e autenticação.

O sistema foi registrado em um Dell OptiPlex 3020 com processador Intel Core i5-4590 e aproximadamente 8 GB de RAM.

A partição raiz possui aproximadamente **211,21 GiB**.

Asterisk e FreeRADIUS são serviços instalados nesse computador físico, sem duplicação do respectivo custo de hardware.

## 7.6. Custo de Aquisição dos Computadores

```text
10 computadores × R$ 868,31

Total = R$ 8.683,10
```

Os monitores, teclados e mouses são somados separadamente:

```text
Desktops:            R$  8.683,10
Monitores:           R$  2.999,90
Teclados e mouses:   R$  1.049,50
--------------------------------
Total:               R$ 12.732,50
```

Os custos de instalação de sistemas operacionais e configuração das estações são apresentados na aba **Implantação**.

---

# 8. Cenário B — Implantação com Ativos Existentes

O Cenário B representa uma contratação em que os equipamentos principais já estão disponíveis.

O investimento considera materiais adicionais, serviços técnicos e deslocamento.

Nesse modelo, não há recompra dos computadores, equipamentos Cisco, roteadores wireless ou telefones IP.

## 8.1. Composição Financeira

| Componente | Valor |
|---|---:|
| Materiais adicionais | R$ 551,85 |
| Serviços de implantação | R$ 6.837,00 |
| Novas licenças de sistema operacional | R$ 0,00 |
| Deslocamento técnico | R$ 60,00 |
| **TOTAL — CENÁRIO B** | **R$ 7.448,85** |

```text
Cenário B =
Materiais adicionais
+ Serviços de implantação
+ Novas licenças previstas
+ Deslocamento
```

```text
R$   551,85
+ R$ 6.837,00
+ R$     0,00
+ R$    60,00
--------------
R$ 7.448,85
```

O resultado está consolidado em:

`Cenário B!D13`

## 8.2. Materiais Adicionais

Os seguintes materiais possuem inclusão ativa no Cenário B:

| Material | Subtotal |
|---|---:|
| Kit de fixação do rack | R$ 24,62 |
| Caixa de cabo CAT6 — 305 metros | R$ 430,80 |
| Conectores RJ45 CAT6 — pacote com 100 | R$ 40,22 |
| Velcro para organização dos cabos | R$ 13,97 |
| Abraçadeiras de nylon | R$ 12,26 |
| Etiquetas de identificação | R$ 29,98 |
| **Total** | **R$ 551,85** |

A inclusão desses materiais representa a possibilidade de aquisição de consumíveis adicionais durante a implantação.

O modelo não atribui novamente o custo dos ativos principais já fornecidos.

## 8.3. Mão de Obra

A planilha utiliza a mesma composição de serviços dos cenários A e B.

O valor de **R$ 6.837,00** corresponde ao escopo integral simulado de instalação e configuração.

Assim, o Cenário B representa uma implantação completa com fornecimento prévio dos equipamentos, e não apenas um serviço reduzido de configuração.

## 8.4. Licenciamento

O Cenário B considera os sistemas operacionais fornecidos juntamente com os computadores existentes.

Por esse motivo, a provisão para aquisição de novas licenças Windows é excluída desse cenário.

Esse tratamento é uma premissa financeira e não uma declaração sobre contratos ou direitos de licenciamento específicos.

## 8.5. Deslocamento

O orçamento considera uma provisão de **R$ 60,00** para deslocamento técnico.

O valor é fixo e não representa uma cotação individual de transporte ou diárias.

---

# 9. Serviços de Implantação

A aba **Implantação** contém 32 atividades técnicas.

As atividades foram distribuídas entre cabeamento, montagem, redes, Linux, containers, monitoramento, telefonia, autenticação, testes e documentação.

## 9.1. Modelo de Cálculo

O custo de cada atividade é obtido pela fórmula:

```text
Horas totais = Quantidade × Horas por unidade

Custo da atividade = Horas totais × Tarifa horária
```

As tarifas são parâmetros comerciais de referência.

Não constituem salários, contratos de prestação de serviços ou registros das horas efetivamente trabalhadas.

## 9.2. Tarifas Técnicas

| Área | Tarifa |
|---|---:|
| Cabeamento e montagem de rack | R$ 55,00/h |
| Montagem e configuração de estações | R$ 50,00/h |
| Linux, containers e serviços | R$ 70,00/h |
| Redes Cisco e infraestrutura wireless | R$ 90,00/h |
| Testes e documentação | R$ 60,00/h |

As tarifas são utilizadas pelas fórmulas da aba Implantação a partir das referências mantidas em **Premissas**.

## 9.3. Atividades e Custos

| ID | Serviço | Horas totais | Custo |
|---|---|---:|---:|
| MO-001 | Planejamento e levantamento dos pontos | 2,0 h | R$ 110,00 |
| MO-002 | Passagem e organização do cabeamento | 6,0 h | R$ 330,00 |
| MO-003 | Confecção manual de cabos RJ45 | 4,0 h | R$ 220,00 |
| MO-004 | Terminação e identificação do patch panel | 2,0 h | R$ 110,00 |
| MO-005 | Teste básico de continuidade dos pontos | 2,4 h | R$ 132,00 |
| MO-006 | Montagem e organização do rack | 3,0 h | R$ 165,00 |
| MO-007 | Montagem e revisão dos computadores | 7,5 h | R$ 375,00 |
| MO-008 | Instalação de sistemas operacionais e drivers | 7,5 h | R$ 375,00 |
| MO-009 | Endereçamento e testes de conectividade | 2,5 h | R$ 125,00 |
| MO-010 | Planejamento IPv4, VLANs e segmentação | 3,0 h | R$ 270,00 |
| MO-011 | Configuração do Cisco Catalyst C9200L | 4,0 h | R$ 360,00 |
| MO-012 | Configuração do Cisco Catalyst C8200L | 4,0 h | R$ 360,00 |
| MO-013 | Implementação e testes adicionais de ACLs | 2,0 h | R$ 180,00 |
| MO-014 | Configuração dos dois Archer AX53 | 2,0 h | R$ 180,00 |
| MO-015 | Integração do dispositivo Alexa | 1,0 h | R$ 50,00 |
| MO-016 | Implantação do FreeRADIUS | 3,0 h | R$ 210,00 |
| MO-017 | Implantação do Asterisk e serviços VoIP | 4,0 h | R$ 280,00 |
| MO-018 | Instalação e configuração básica do host Linux | 3,0 h | R$ 210,00 |
| MO-019 | Instalação do Docker Engine e Compose | 2,0 h | R$ 140,00 |
| MO-020 | Implantação do MariaDB e Zabbix | 6,0 h | R$ 420,00 |
| MO-021 | Implantação do Grafana e fontes de dados | 3,0 h | R$ 210,00 |
| MO-022 | Desenvolvimento dos dashboards NOC | 5,0 h | R$ 350,00 |
| MO-023 | Monitoramento SNMP dos equipamentos Cisco | 3,0 h | R$ 270,00 |
| MO-024 | Implantação do Uptime Kuma | 1,5 h | R$ 105,00 |
| MO-025 | Implantação do Pi-hole e DNS interno | 2,0 h | R$ 140,00 |
| MO-026 | Implantação do Nginx e TLS | 3,0 h | R$ 210,00 |
| MO-027 | Publicação do portal HTML e testes | 2,0 h | R$ 140,00 |
| MO-028 | Configuração do Portainer CE | 1,0 h | R$ 70,00 |
| MO-029 | Definição de backups e persistência | 2,0 h | R$ 140,00 |
| MO-030 | Testes ponta a ponta e monitoramento | 4,0 h | R$ 240,00 |
| MO-031 | Diagramas técnicos e inventário | 3,0 h | R$ 180,00 |
| MO-032 | Relatórios de configuração e entrega | 3,0 h | R$ 180,00 |
| **TOTAL** | **32 atividades** | **103,4 h** | **R$ 6.837,00** |

## 9.4. Distribuição por Área

| Área técnica | Horas | Subtotal |
|---|---:|---:|
| Cabeamento | 16,4 h | R$ 902,00 |
| Rack | 3,0 h | R$ 165,00 |
| Estações | 17,5 h | R$ 875,00 |
| Rede Cisco | 13,0 h | R$ 1.170,00 |
| Wi-Fi e IoT | 3,0 h | R$ 230,00 |
| Identidade | 3,0 h | R$ 210,00 |
| Telefonia | 4,0 h | R$ 280,00 |
| Linux / Docker | 11,0 h | R$ 770,00 |
| Observabilidade | 12,5 h | R$ 935,00 |
| Rede / DNS | 2,0 h | R$ 140,00 |
| Web e segurança | 5,0 h | R$ 350,00 |
| Operação | 3,0 h | R$ 210,00 |
| Testes | 4,0 h | R$ 240,00 |
| Documentação | 6,0 h | R$ 360,00 |
| **TOTAL** | **103,4 h** | **R$ 6.837,00** |

## 9.5. Escopo dos Serviços

A composição inclui tanto atividades diretamente relacionadas à infraestrutura documentada quanto serviços previstos para a reprodução completa do ambiente.

A provisão de implementação adicional de ACLs está separada da configuração básica do roteador.

Os testes ponta a ponta, verificações de autenticação e demais atividades previstas financeiramente não representam evidência de execução histórica desses procedimentos.

O teste básico de continuidade do cabeamento também não equivale à certificação profissional de desempenho dos enlaces CAT6.

---

# 10. Software, Licenças e Subscrições

A aba **Software** apresenta os custos de licenciamento e suas condições financeiras.

O ambiente utiliza principalmente aplicações de código aberto.

O custo de licença das edições comunitárias consideradas é de **R$ 0,00**, sem eliminar custos de instalação, manutenção, infraestrutura ou suporte.

## 10.1. Software Comunitário

| ID | Software | Licença inicial |
|---|---|---:|
| SW-001 | Debian GNU/Linux | R$ 0,00 |
| SW-002 | Docker Engine / Compose | R$ 0,00 |
| SW-003 | Portainer Community Edition | R$ 0,00 |
| SW-004 | Zabbix Server / Web / Agent | R$ 0,00 |
| SW-005 | Grafana OSS | R$ 0,00 |
| SW-006 | Uptime Kuma | R$ 0,00 |
| SW-007 | Pi-hole | R$ 0,00 |
| SW-008 | MariaDB Community | R$ 0,00 |
| SW-009 | Nginx Open Source | R$ 0,00 |
| SW-010 | Apache HTTP Server | R$ 0,00 |
| SW-011 | Asterisk | R$ 0,00 |
| SW-012 | FreeRADIUS | R$ 0,00 |

A instalação e administração dessas aplicações estão contempladas nas atividades técnicas da aba Implantação.

## 10.2. Cisco IOS XE e Serviços Adicionais

A planilha contempla o Cisco IOS XE e a referência comercial do C9200L com Network Essentials.

Subscrições adicionais, contratos de suporte e serviços proprietários não integram automaticamente o custo-base.

A linha de licenciamento complementar permanece excluída do cenário financeiro.

Essa separação evita atribuir um preço arbitrário a contratos que variam conforme SKU, modalidade de aquisição e condições comerciais.

## 10.3. Windows 11 Pro

O modelo provisiona oito licenças Windows 11 Pro.

| Indicador | Valor |
|---|---:|
| Quantidade de estações | 8 |
| Licença de referência | Windows 11 Pro |
| Preço unitário | R$ 1.599,00 |
| **Total provisionado** | **R$ 12.792,00** |

O valor utiliza referência de varejo da Microsoft.

A provisão representa uma aquisição hipotética de licenças no Cenário A.

A existência de sistemas Windows instalados no laboratório não estabelece, por si só, a modalidade de licenciamento utilizada.

### Compatibilidade do Hardware

O Intel Core i5-4590 pertence à 4ª geração de processadores Intel Core.

Esse processador não consta da lista oficial de CPUs suportadas para Windows 11.

Portanto, a provisão financeira para licenças não representa validação de compatibilidade técnica ou atendimento aos requisitos oficiais do sistema operacional.

A limitação está registrada na planilha e deve ser considerada ao avaliar a reprodução do ambiente.

## 10.4. Certificados TLS

A planilha contempla o uso de certificados e infraestrutura TLS sem aquisição obrigatória de certificado público comercial.

A linha de emissão comercial permanece excluída.

Os serviços de configuração de Nginx e TLS são contabilizados na implantação.

## 10.5. Total de Licenciamento Inicial

| Componente | Custo inicial |
|---|---:|
| Software comunitário | R$ 0,00 |
| Licenças Windows 11 Pro | R$ 12.792,00 |
| Subscrições Cisco adicionais | R$ 0,00 no cenário-base |
| Certificados TLS comerciais | R$ 0,00 no cenário-base |
| **TOTAL** | **R$ 12.792,00** |

---

# 11. Cenário C — Operação e Manutenção

O Cenário C estima as despesas recorrentes necessárias à operação da infraestrutura.

O cálculo contempla:

- Energia elétrica.
- Conectividade à internet.
- Administração preventiva dos sistemas Linux.
- Administração da infraestrutura Cisco e wireless.
- Revisão de monitoramento.
- Verificação de backups.
- Reserva para reposição de equipamentos.
- Provisão de armazenamento externo.

Não se trata de contratação de NOC 24×7.

## 11.1. Composição Mensal

| ID | Despesa | Valor mensal |
|---|---|---:|
| OP-001 | Energia elétrica estimada | R$ 460,25 |
| OP-002 | Internet / WAN | R$ 159,90 |
| OP-003 | Suporte Linux e containers | R$ 140,00 |
| OP-004 | Administração Cisco e Wi-Fi | R$ 90,00 |
| OP-005 | Revisão de dashboards e alarmes | R$ 70,00 |
| OP-006 | Verificação de backups | R$ 55,00 |
| OP-007 | Reserva mensal de reposição | R$ 48,94 |
| OP-008 | Armazenamento externo de backup | R$ 60,00 |
| OP-009 | Contrato Cisco adicional — fora do escopo | R$ 0,00 |
| OP-010 | Certificado TLS comercial — fora do escopo | R$ 0,00 |
| OP-011 | Suporte proprietário de software — fora do escopo | R$ 0,00 |
| OP-012 | Domínio público adicional — fora do escopo | R$ 0,00 |
| **TOTAL MENSAL** | | **R$ 1.084,09** |

Os itens marcados como fora do escopo possuem custo zero por decisão do modelo financeiro, não por representarem serviços necessariamente gratuitos.

## 11.2. Manutenção Preventiva

A manutenção preventiva possui quatro componentes:

| Serviço | Horas mensais | Tarifa | Subtotal |
|---|---:|---:|---:|
| Suporte Linux e containers | 2 h | R$ 70,00/h | R$ 140,00 |
| Administração Cisco e Wi-Fi | 1 h | R$ 90,00/h | R$ 90,00 |
| Revisão de dashboards | 1 h | R$ 70,00/h | R$ 70,00 |
| Verificação de backups | 1 h | R$ 55,00/h | R$ 55,00 |
| **TOTAL** | **5 h** | | **R$ 355,00** |

A composição representa suporte preventivo limitado.

Atendimento contínuo, plantões, substituição emergencial de hardware e contratos empresariais específicos exigem composição comercial independente.

## 11.3. Internet

A referência mensal utilizada é de:

**R$ 159,90**

Esse valor corresponde a um plano varejista identificado em referência comercial para Santarém, Pará.

Não representa uma proposta de circuito dedicado empresarial com SLA, redundância de operadoras ou suporte garantido.

## 11.4. Backup Externo

A planilha reserva:

**R$ 60,00 por mês**

O valor representa uma provisão financeira para armazenamento externo de backups.

A despesa é distinta dos volumes locais utilizados pelos serviços Docker.

A provisão não corresponde a contrato de armazenamento efetivamente adquirido.

## 11.5. Reserva de Reposição

O modelo considera uma provisão de **1% ao ano** sobre o investimento em equipamentos e materiais.

```text
Reserva mensal =
Total de equipamentos × 1% / 12
```

```text
R$ 58.729,88 × 0,01 / 12

Reserva mensal = R$ 48,94
```

O objetivo financeiro da provisão é distribuir uma pequena reserva anual de reposição ao longo dos meses.

Ela não representa a compra antecipada de peças de substituição.

---

# 12. Estimativa de Consumo de Energia

O consumo energético utiliza potências médias estimadas, quantidades de equipamentos, horas mensais de operação e tarifa de referência.

A modelagem não utiliza medições elétricas diretamente realizadas nos equipamentos.

## 12.1. Potência por Equipamento

| Equipamento | Quantidade considerada | Potência média por unidade |
|---|---:|---:|
| Cisco Catalyst C8200L | 1 | 55 W |
| Cisco Catalyst C9200L | 1 | 75 W |
| Servidores Linux | 2 | 70 W |
| Estações Windows | 8 | 55 W |
| Monitores | 10 | 18 W |
| TP-Link Archer AX53 | 2 | 12 W |
| Telefones Grandstream | 2 | 4 W |
| Dispositivo Alexa | 1 | 6 W |

Essas potências representam parâmetros de cálculo, sujeitos à carga real dos equipamentos.

## 12.2. Horários de Funcionamento

| Grupo | Horas mensais |
|---|---:|
| Equipamentos de infraestrutura contínua | 720 h |
| Estações e monitores | 176 h |

O funcionamento contínuo corresponde à hipótese:

```text
30 dias × 24 horas = 720 horas
```

As estações seguem a hipótese:

```text
22 dias × 8 horas = 176 horas
```

## 12.3. Potência da Infraestrutura Contínua

A composição inclui roteador, switch, servidores Linux, roteadores wireless, telefones IP e Alexa.

```text
Cisco C8200L:       55 W
Cisco C9200L:       75 W
2 servidores:      140 W
2 Archer AX53:      24 W
2 Grandstream:       8 W
1 Alexa:             6 W
------------------------
Total:             308 W
```

Consumo mensal:

```text
308 W × 720 h / 1.000

221,76 kWh/mês
```

## 12.4. Potência das Estações

```text
8 desktops × 55 W = 440 W

10 monitores × 18 W = 180 W

Total = 620 W
```

Consumo mensal:

```text
620 W × 176 h / 1.000

109,12 kWh/mês
```

## 12.5. Consumo Total

```text
Infraestrutura contínua: 221,76 kWh

Estações e monitores:     109,12 kWh
-----------------------------------
Total estimado:          330,88 kWh/mês
```

## 12.6. Tarifa de Energia

A planilha utiliza o valor de referência:

**R$ 1,391 por kWh**

O parâmetro foi construído a partir de referência tarifária da Equatorial Pará, com estimativa de tributos.

Trata-se de um parâmetro de simulação baseado em tarifa residencial B1, não de uma tarifa comercial B3 efetivamente faturada.

## 12.7. Custo Mensal de Energia

```text
330,88 kWh × R$ 1,391

Custo = R$ 460,25/mês
```

Esse resultado é utilizado no Cenário C.

---

# 13. Projeções Financeiras

A planilha apresenta projeções acumuladas de operação.

Os valores não incluem reajuste de tarifas, inflação, crescimento do parque tecnológico ou atualização monetária.

## 13.1. Operação em 12 Meses

```text
R$ 1.084,09 × 12

R$ 13.009,08
```

## 13.2. Operação em 36 Meses

```text
R$ 1.084,09 × 36

R$ 39.027,24
```

## 13.3. Aquisição Integral com Primeiro Ano de Operação

```text
Cenário A + Operação anual
```

```text
R$ 86.683,14 + R$ 13.009,08

R$ 99.692,22
```

## 13.4. Implantação com Ativos Existentes e Primeiro Ano

```text
Cenário B + Operação anual
```

```text
R$ 7.448,85 + R$ 13.009,08

R$ 20.457,93
```

## 13.5. Síntese Comparativa

| Indicador | Investimento inicial | Operação em 12 meses | Total |
|---|---:|---:|---:|
| Aquisição integral | R$ 86.683,14 | R$ 13.009,08 | R$ 99.692,22 |
| Ativos existentes | R$ 7.448,85 | R$ 13.009,08 | R$ 20.457,93 |

O custo mensal de operação é o mesmo nas duas projeções.

O modelo considera que, após a implantação, os dois cenários utilizam infraestrutura funcional equivalente e compartilham as mesmas premissas operacionais.

---

# 14. Premissas Financeiras e Operacionais

A aba **Premissas** centraliza os parâmetros utilizados nos cálculos.

Os códigos PR-01 a PR-35 identificam as referências de quantidade, custo, funcionamento e projeção.

## 14.1. Quantidades e Estrutura

| Código | Parâmetro | Valor |
|---|---|---:|
| PR-01 | Computadores físicos | 10 |
| PR-02 | Estações Windows | 8 |
| PR-03 | Servidores Linux | 2 |
| PR-04 | Monitores | 10 |
| PR-05 | Kits teclado e mouse | 10 |
| PR-28 | Licenças Windows provisionadas | 8 |
| PR-32 | Servidores em operação contínua | 2 |
| PR-33 | Roteadores Archer AX53 | 2 |
| PR-34 | Telefones IP | 2 |
| PR-35 | Dispositivos Alexa considerados | 1 |

## 14.2. Tarifas de Serviços

| Código | Parâmetro | Valor |
|---|---|---:|
| PR-06 | Hora técnica de cabeamento | R$ 55,00 |
| PR-07 | Hora técnica de montagem | R$ 50,00 |
| PR-08 | Hora técnica de Linux e serviços | R$ 70,00 |
| PR-09 | Hora técnica de redes Cisco | R$ 90,00 |
| PR-10 | Hora técnica de testes e documentação | R$ 60,00 |

## 14.3. Potências Médias

| Código | Parâmetro | Valor |
|---|---|---:|
| PR-11 | Roteador Cisco C8200L | 55 W |
| PR-12 | Switch Cisco C9200L | 75 W |
| PR-13 | Servidor Linux | 70 W |
| PR-14 | Estação Windows | 55 W |
| PR-15 | Monitor | 18 W |
| PR-16 | TP-Link Archer AX53 | 12 W |
| PR-17 | Telefone IP | 4 W |
| PR-18 | Alexa | 6 W |

## 14.4. Operação e Despesas

| Código | Parâmetro | Valor |
|---|---|---:|
| PR-19 | Funcionamento contínuo | 720 h/mês |
| PR-20 | Funcionamento das estações | 176 h/mês |
| PR-21 | Tarifa elétrica estimada | R$ 1,391/kWh |
| PR-22 | Internet mensal | R$ 159,90 |
| PR-23 | Provisão de frete | 3,5% |
| PR-24 | Reserva de imprevistos | 8% |
| PR-25 | Deslocamento técnico — Cenário B | R$ 60,00 |
| PR-26 | Backup externo mensal | R$ 60,00 |
| PR-27 | Reserva anual de reposição | 1% |
| PR-29 | Licença Windows Pro | R$ 1.599,00 |
| PR-30 | Horizonte anual | 12 meses |
| PR-31 | Horizonte estendido | 36 meses |

Os parâmetros de tarifa, potência, horas operacionais, frete e reservas são hipóteses financeiras explícitas.

As quantidades de computadores e equipamentos de rede utilizam o inventário técnico do projeto.

---

# 15. Fontes e Referências de Preços

A aba **Fontes** reúne 45 registros numerados de RF-01 a RF-45.

Cada registro possui identificação, descrição, fornecedor ou origem, referência comercial, valor, data-base e critério de utilização.

Os preços correspondem às referências armazenadas na planilha em novembro de 2026.

Anúncios comerciais podem apresentar alterações de disponibilidade, condições de pagamento, tributação, frete e preço.

## 15.1. Equipamentos e Materiais

| Código | Referência | Valor | Fonte |
|---|---|---:|---|
| RF-01 | Cisco C8200L-1N-4T | R$ 23.422,08 | [Xtech](https://xtech.com.br/cisco-catalyst-8200l-with-1-nim-slot-and-4x1g-wan-ports/p/55138/) |
| RF-02 | Cisco C9200L-24T-4G-E | R$ 19.068,00 | [FoxTI](https://www.foxti.com.br/products/cisco-catalyst-c9200l-24t-4g-e-24-port-data-switch-with-4x1g-uplinks-network-essentials) |
| RF-03 | TP-Link Archer AX53 AX3000 | R$ 299,99 | [Pichau](https://www.pichau.com.br/roteador-tp-link-archer-ax53-wi-fi-6-dual-band-ax3000-4-antenas-preto-archer-ax53) |
| RF-04 | Amazon Echo Show 5 | R$ 699,00 | [Loja Vivo](https://z9w115.store.vivo.com.br/marca/amazon/c/) |
| RF-05 | Lâmpada inteligente E27 | R$ 42,66 | [KaBuM!](https://www.kabum.com.br/produto/1043228/lampada-inteligente-led-wi-fi-elw-1001-intelbras) |
| RF-06 | Bocal E27 | R$ 8,12 | [Central Elétrica](https://www.lojacentraleletrica.com.br/produto/soquete-porta-lampada-com-chave-pvc-latao-e27) |
| RF-07 | Rack 19 polegadas 12U | R$ 650,56 | [Solução Cabos](https://www.solucaocabos.com.br/mini-rack-de-parede-19--12us-x-570mm-branco/p) |
| RF-08 | Patch panel CAT6 24 portas | R$ 202,35 | [Solução Cabos](https://www.solucaocabos.com.br/patch-panel-24-portas-cat6-dc/p) |
| RF-09 | Régua rack 19 polegadas | R$ 99,00 | [Rack Outdoor](https://rackoutdoor.com.br/shop/acessorios/reguas-de-tomadas/regua-de-tomada-para-rack-19-com-8-tomadas-10a-com-protecao/) |
| RF-10 | Organizador horizontal 1U | R$ 23,32 | [Unicaserv](https://www.unicaserv.com.br/linha-metalurgica/acessorios-para-rack/guia-de-cabos-horizontal-fechada-padrao-19-1u-preta) |
| RF-11 | Bandeja fixa de rack | R$ 53,20 | [Raitek](https://www.raitekdistribuidora.com.br/racks-e-acessorios/bandejas) |
| RF-12 | Kit com 20 fixadores | R$ 24,62 | [HD Store](https://www.hdstore.com.br/kit-porca-gaiola-parafuso-m5-padrao-rack-servidor-pacote-20-pecas) |
| RF-13 | Cabo CAT6 — 305 m | R$ 430,80 | [PrimeCabos](https://www.primecabos.com/cabo-de-rede/cabo-cat6) |
| RF-14 | Conectores RJ45 CAT6 — 100 unidades | R$ 40,22 | [KaBuM!](https://www.kabum.com.br/produto/1066948/conector-rj45-plus-cable-cat-6-la-cat6-c-100-pecas) |
| RF-15 | Keystone CAT6 | R$ 7,60 | [Central Cabos](https://www.centralcabos.com.br/redes/keystone/cat6) |
| RF-16 | Caixa de sobrepor | R$ 7,15 | [Rede Loja](https://redeloja.com/produto/1747314101615) |
| RF-17 | Velcro para cabos | R$ 13,97 | [Unicaserv](https://www.unicaserv.com.br/racks-e-acessorios/acessorios-para-racks/organizadores-para-racks) |
| RF-18 | Canaleta adesiva 2 m | R$ 9,90 | [Sodimac](https://www.sodimac.com.br/sodimac-br/product/780771/canaleta-com-adesivo-20x10mm-2-metros/780771/) |
| RF-19 | Telefone Grandstream GRP2601 | R$ 249,99 | [KaBuM!](https://www.kabum.com.br/produto/194967/telefone-ip-grandstream-2-linhas-visor-lcd-preto-grp2601) |
| RF-20 | Alicate de crimpagem RJ45 | R$ 74,01 | [LC Ferragens](https://www.lcferragens.com.br/produto/alicate-crimpar-vonder-rj-45/) |
| RF-21 | Testador básico de cabos | R$ 39,99 | [FGTEC](https://www.fgtec.com.br/perifericos/testador-de-cabo-de-rede-pluscable-rj11-rj45-lt-100) |
| RF-22 | Ferramenta punch-down | R$ 27,46 | [Central Cabos](https://www.centralcabos.com.br/ferramenta/alicates) |
| RF-23 | Alicate decapador | R$ 15,20 | [Central Cabos](https://www.centralcabos.com.br/ferramenta/alicates) |
| RF-24 | Abraçadeiras — pacote com 100 | R$ 12,26 | [Unicaserv](https://www.unicaserv.com.br/infra-estrutura/abracadeiras/abracadeira-de-nylon-3-5mm-x-200mm-branca-cento) |
| RF-25 | Teclado e mouse Logitech MK120 | R$ 104,95 | [KaBuM!](https://www.kabum.com.br/produto/254649/teclado-e-mouse-logitech-mk120-resistente-a-agua-1000dpi-preto-abnt2-920-004429) |
| RF-26 | Monitor BRX 21 polegadas | R$ 299,99 | [TerabyteShop](https://www.terabyteshop.com.br/produto/42811/monitor-brx-21-pol-60hz-hdmivga-vesa-preto-mbrx21bk) |

## 15.2. Referências Complementares e Custos Operacionais

| Código | Referência | Valor | Fonte |
|---|---|---:|---|
| RF-27 | Cisco C8200L — referência alternativa | R$ 23.422,08 | [Xtech](https://xtech.com.br/cisco-catalyst-8200l-with-1-nim-slot-and-4x1g-wan-ports/p/55138/) |
| RF-28 | Cisco C9200L PoE — referência alternativa | R$ 35.917,41 | [Xtech](https://xtech.com.br/Switch-Cisco-Catalyst-9200l-24-Port-Poe-4-X-1g-Network-Advanta-C9200l-24p-4g-A/p/52916/) |
| RF-29 | Dell OptiPlex 3020 recondicionado | R$ 868,31 | [Mercado Livre — listagem](https://lista.mercadolivre.com.br/dell-optiplex-3020) |
| RF-30 | Windows 11 Pro | R$ 1.599,00 | [Microsoft Store](https://www.microsoft.com/pt-br/d/windows-11-pro/dg7gmgf0d8h4) |
| RF-31 | Energia — Equatorial Pará | R$ 1,391/kWh | [Tarifa Aberta](https://tarifaaberta.com.br/distribuidoras/equatorial-pa/) |
| RF-32 | Internet em Santarém | R$ 159,90/mês | [Radar da Telecom](https://www.radardatelecom.com/municipio/pa/santarem) |
| RF-33 | Cabo console USB–RJ45 | R$ 24,60 | [Central Cabos](https://www.centralcabos.com.br/cabo-console-usb-para-rj45-180-metros/p) |
| RF-34 | Nobreak 1200 VA | R$ 799,00 | Premissa orçamentária |
| RF-35 | Patch cord CAT6 de 2 m | R$ 25,00 | Premissa orçamentária |
| RF-36 | Headset de telefonia | R$ 120,00 | Premissa orçamentária |
| RF-37 | Mesa operacional | R$ 350,00 | Premissa orçamentária |
| RF-38 | Cadeira operacional | R$ 200,00 | Premissa orçamentária |
| RF-39 | Transceptor SFP 1 Gbps | R$ 150,00 | Premissa orçamentária |
| RF-40 | Protetores RJ45 | R$ 25,00 | Premissa orçamentária |
| RF-41 | Etiquetas de identificação | R$ 29,98 | [Mercado Livre — listagem](https://lista.mercadolivre.com.br/etiquetas-para-cabos) |
| RF-42 | Armazenamento externo de backup | R$ 60,00/mês | Premissa operacional |
| RF-43 | Software comunitário | R$ 0,00 de licença | [Debian e projetos de código aberto](https://www.debian.org/) |
| RF-44 | Requisitos de processadores do Windows 11 | Referência técnica | [Microsoft Learn](https://learn.microsoft.com/pt-br/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors) |
| RF-45 | Reserva de reposição | 1% ao ano | Premissa financeira |

## 15.3. Aplicação das Referências

A presença de um item na aba Fontes não significa inclusão automática no investimento.

Os valores são aplicados conforme:

1. Quantidade estabelecida para o item.
2. Preço unitário de referência.
3. Indicador de compra ativo no cenário correspondente.
4. Categoria de despesa.
5. Fórmula financeira utilizada.

As referências alternativas de equipamentos Cisco não são somadas simultaneamente aos preços escolhidos para o inventário-base.

Os produtos opcionais com quantidade zero permanecem disponíveis como parâmetros comerciais, sem afetar os totais dos cenários.

## 15.4. Condições Comerciais

Os preços publicados por fornecedores podem depender de:

- Disponibilidade de estoque.
- Condição de pagamento.
- Tributos aplicáveis.
- Localidade de entrega.
- Frete.
- Modalidade de faturamento.
- Estado do equipamento.
- Licenças e serviços adicionais.
- Alterações posteriores à data-base.

O orçamento utiliza o valor de referência armazenado na planilha, e não uma garantia de manutenção do preço comercial.

---

# 16. Regras de Cálculo do Modelo

As fórmulas da planilha estabelecem as relações entre quantidades, preços e totais.

## 16.1. Subtotal de Equipamentos

```excel
=IF(H9="Sim",E9*G9,0)
```

A fórmula representa a estrutura utilizada no Cenário A para os itens do inventário.

Quando a inclusão está ativa:

```text
Subtotal = Quantidade × Preço unitário
```

Quando a inclusão está desativada, o subtotal da linha é zero.

O Cenário B utiliza estrutura equivalente com sua própria coluna de inclusão.

## 16.2. Total do Inventário

```excel
=SUM(J9:J45)
```

Resultado do Cenário A:

**R$ 58.729,88**

Para os materiais adicionais do Cenário B:

```excel
=SUM(K9:K45)
```

Resultado:

**R$ 551,85**

## 16.3. Total de Serviços

```excel
=SUM(H9:H40)
```

Resultado:

**R$ 6.837,00**

A quantidade total de horas é calculada separadamente:

```excel
=SUM(F9:F40)
```

Resultado:

**103,4 horas**

## 16.4. Licenciamento Inicial

```excel
=SUM(F9:F23)
```

Resultado:

**R$ 12.792,00**

## 16.5. Cenário A

```excel
=SUM(D19:D23)
```

Resultado:

**R$ 86.683,14**

## 16.6. Cenário B

```excel
=SUM(D9:D12)
```

Resultado:

**R$ 7.448,85**

## 16.7. Operação Mensal

```excel
=SUM(G9:G20)
```

Resultado:

**R$ 1.084,09**

## 16.8. Projeção Anual

```excel
=G23*Premissas!C38
```

Resultado:

**R$ 13.009,08**

## 16.9. Projeção de 36 Meses

```excel
=G23*Premissas!C39
```

Resultado:

**R$ 39.027,24**

## 16.10. Relação entre Abas

As fórmulas referenciam os dados diretamente pelas respectivas abas.

Por exemplo:

```excel
=Inventário!J47
```

Representa o subtotal de aquisição de equipamentos e materiais.

A notação com `!` corresponde ao separador de referência entre a aba e a célula.

O modelo utiliza esse mecanismo para evitar a manutenção manual de valores repetidos nas diferentes áreas financeiras.

---

# 17. Limites do Orçamento

## 17.1. Aquisição de Equipamentos

O Cenário A utiliza preços de mercado de equipamentos documentados ou produtos comercialmente comparáveis.

O preço de um computador recondicionado não representa necessariamente o valor de aquisição original dos computadores físicos.

As referências de rack, periféricos, telefonia e acessórios também podem diferir dos modelos exatos empregados no laboratório.

## 17.2. Serviços Técnicos

As 32 atividades representam o escopo de reprodução e implantação da infraestrutura.

Os valores financeiros não constituem medição de horas históricas ou comprovação da contratação de prestadores.

As atividades de configuração e testes são tratadas como componentes do orçamento de implantação.

## 17.3. Energia Elétrica

A despesa de energia utiliza potência média estimada e tarifa de referência.

O cálculo não substitui uma medição de consumo ou uma fatura comercial.

A operação real pode variar conforme carga dos computadores, eficiência das fontes, tempo de utilização e condições tarifárias.

## 17.4. Conectividade

O valor mensal de internet corresponde a uma referência comercial de banda larga.

O modelo não inclui contratação específica de:

- Link dedicado.
- SLA empresarial.
- Redundância entre operadoras.
- Endereçamento IP público fixo.
- Contratos corporativos diferenciados.

## 17.5. Licenciamento Proprietário

As licenças Windows foram provisionadas no Cenário A.

Contratos Cisco adicionais e outras subscrições proprietárias dependem de modalidades comerciais específicas e permanecem separados do orçamento-base.

O valor de R$ 0,00 atribuído às edições comunitárias refere-se ao custo de licença de uso considerado, não ao custo total de implantação ou operação.

## 17.6. Itens Opcionais

Os seguintes componentes possuem referências financeiras, mas não integram o investimento-base:

- Transceptores SFP.
- Nobreak.
- Bandejas adicionais de rack.
- Keystones opcionais.
- Caixas de sobrepor.
- Canaletas adicionais.
- Patch cords comerciais adicionais.
- Protetores de conectores RJ45.
- Headsets.
- Lâmpadas inteligentes adicionais.
- Bocal de iluminação.
- Mesas e cadeiras.
- Servidor Docker adicional.

A exclusão está implementada pelas quantidades e pelos indicadores de compra das respectivas linhas.

## 17.7. Escopo do Ambiente

O cenário financeiro representa a reprodução de uma infraestrutura corporativa de referência.

Não se trata da avaliação patrimonial dos equipamentos efetivamente utilizados, nem da apuração contábil de despesas históricas.

A estimativa também não equivale ao custo contratual de uma operação NOC com atendimento contínuo.

---

# 18. Consistência e Rastreabilidade Financeira

O modelo relaciona as quantidades do inventário aos custos de implantação e operação.

## 18.1. Equipamentos e Serviços

Os seguintes critérios estruturam os totais:

| Elemento | Tratamento financeiro |
|---|---|
| Dez computadores físicos | Uma única aquisição por equipamento |
| Dois servidores Linux | Incluídos no total de dez computadores |
| Monitores | Aquisição separada dos desktops |
| Teclados e mouses | Aquisição separada dos desktops |
| Dois Archer AX53 | Equipamentos distintos |
| Dois telefones Grandstream | Duas unidades no investimento |
| Servidor Docker adicional | Excluído para evitar duplicação |
| Ferramentas | Aquisição inicial reutilizável |
| Serviços técnicos | Calculados por horas e tarifas |
| Software comunitário | Licença de uso com custo zero |
| Licenças Windows | Provisão inicial no Cenário A |
| Energia | Consumo estimado |
| Internet | Referência comercial mensal |
| Reserva de reposição | Percentual anual mensalizado |

## 18.2. Identificação das Estimativas

As seguintes informações possuem natureza de planejamento, sem medição ou contratação individual que determine seu valor exato:

- Potências médias dos equipamentos.
- Horários de funcionamento financeiro.
- Tarifa elétrica final com tributos.
- Horas técnicas de implantação.
- Tarifas comerciais dos serviços.
- Frete regional.
- Deslocamento técnico.
- Reserva de imprevistos.
- Reserva de reposição.
- Armazenamento externo de backup.
- Valores de produtos opcionais classificados como premissa.
- Quantidade comercial de cabeamento e consumíveis.
- Preço comparável dos desktops.
- Modelo comercial utilizado como referência para o dispositivo Alexa.
- Modelo comercial utilizado como referência para os telefones Grandstream.

Esses dados permanecem identificados como premissas ou referências comerciais, preservando a distinção entre a infraestrutura documentada e o custo estimado de sua reprodução.

## 18.3. Correspondência entre Excel e Markdown

O arquivo Excel constitui a versão editável do modelo financeiro.

Este README apresenta a estrutura, os resultados e os critérios financeiros correspondentes à revisão consolidada.

Alterações posteriores em quantidades, preços, tarifas, inclusão de equipamentos ou parâmetros operacionais podem modificar os resultados calculados pela planilha.

Os valores descritos neste documento correspondem à data-base indicada.

---

# 19. Resultado Financeiro Consolidado

A análise estabelece três referências principais para a infraestrutura do Enterprise NOC.

### Aquisição e Implantação Integral

**R$ 86.683,14**

Inclui equipamentos, materiais, serviços, licenças provisionadas, frete e reserva de imprevistos.

### Implantação com Ativos Existentes

**R$ 7.448,85**

Inclui materiais adicionais, serviços técnicos e deslocamento, considerando os equipamentos principais já fornecidos.

### Operação Mensal

**R$ 1.084,09**

Inclui energia estimada, internet de referência, manutenção preventiva, armazenamento de backup e reserva de reposição.

A projeção do investimento inicial com 12 meses de operação é:

| Modelo | Total estimado |
|---|---:|
| Aquisição integral + 12 meses | **R$ 99.692,22** |
| Ativos existentes + 12 meses | **R$ 20.457,93** |

Esses valores permitem comparar financeiramente a implantação de uma infraestrutura completa com a contratação de serviços sobre equipamentos já disponíveis.

---

# 20. Arquivos e Versões

## 20.1. Português — BRL

**Documentação financeira**

[enterprise-noc-orcamento-final-brl-2026.md](enterprise-noc-orcamento-final-brl-2026.md)

**Planilha financeira**

[enterprise-noc-orcamento-final-brl-2026.xlsx](enterprise-noc-orcamento-final-brl-2026.xlsx)

Moeda: **BRL — Real brasileiro**

Data-base: **11/11/2026**

## 20.2. English — USD

**Financial documentation**

[enterprise-noc-final-budget-usd-2026.md](../../costs/enterprise-noc-final-budget-usd-2026.md)

**Financial spreadsheet**

[enterprise-noc-final-budget-usd-2026.xlsx](../../costs/enterprise-noc-final-budget-usd-2026.xlsx)

Currency: **USD — United States Dollar**

Status: **Versão internacional reservada para publicação posterior.**

A versão internacional utilizará documentação e planilha próprias, preservando a separação entre os cenários em BRL e USD.

---

**Enterprise NOC — From Scratch**  
**Análise de Custos da Infraestrutura**  
**Revisão financeira: 11 de novembro de 2026**  
**Idioma: Português (Brasil)**  
**Moeda: BRL**
