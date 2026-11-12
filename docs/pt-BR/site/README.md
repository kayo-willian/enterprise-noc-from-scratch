# Enterprise NOC — Site Público: Arquitetura, Identidade Visual e Manutenção

[English](../../site/README.md) | **Português (Brasil)**

**Índice técnico:** [Português (Brasil)](../README.md) · [English](../../README.md)  
**Site:** [English](https://kayo-willian.github.io/enterprise-noc-from-scratch/) · [Português (Brasil)](https://kayo-willian.github.io/enterprise-noc-from-scratch/pt-BR/)  
**Organização:** Tapajós Inovações — empresa fictícia utilizada no cenário corporativo do laboratório  
**Base técnica:** Repositório `main`, commit `4ef6531513e07bba5eea1b76d48b558abfab7f9d` (11 de novembro de 2026); consolidação do portal na fase 8  
**Tipo de documento:** Registro de implementação e referência de manutenção

---

## 1. Objetivo e escopo

O site público apresenta o laboratório físico do Enterprise NOC como um estudo de caso técnico, acessível em dois idiomas. Ele relaciona o cenário corporativo fictício às fotografias, evidências históricas de configuração, segmentação de redes, serviços Linux e containers, capturas de monitoramento e referências à documentação detalhada do repositório.

Trata-se de uma **apresentação pública estática**, diferente da aplicação corporativa executada no ambiente Docker do laboratório. As páginas públicas não se conectam à rede privada nem consultam métricas ao vivo do Zabbix, Grafana, roteador, switch ou servidores. As capturas e os indicadores numéricos exibidos são **registros históricos**, não leituras operacionais em tempo real.

A implementação utiliza uma estrutura direta: HTML semântico, uma folha de estilos CSS compartilhada, um arquivo JavaScript e imagens locais versionadas. As páginas em inglês e português brasileiro compartilham a mesma estrutura, estilos, scripts e identidade visual; os textos e elementos de interface são apresentados no respectivo idioma.

Este documento registra os componentes existentes no repositório na referência técnica indicada acima. Ele não constitui certificação independente de acessibilidade, teste de carga, teste de intrusão ou auditoria da infraestrutura privada.

## 2. Organização do repositório e responsabilidades

```text
docs/
├── .nojekyll
├── index.html                         # Página pública em inglês
├── pt-BR/
│   ├── .nojekyll
│   ├── index.html                     # Página pública em português
│   └── site/
│       └── README.md                  # Documentação do site em português (este arquivo)
├── site/
│   └── README.md                      # Documentação do site em inglês (nova)
└── assets/
    ├── brand/
    │   ├── tapajos-jaguar-logo.png    # Logo atual do cabeçalho e rodapé
    │   ├── tapajos-jaguar-favicon.png # Ícone atual da aba do navegador
    │   ├── tapajos-emblem.svg         # Logo anterior, preservada no repositório
    │   └── tapajos-favicon.svg        # Ícone anterior, preservado no repositório
    ├── css/
    │   └── site.css                   # Identidade visual, layout e responsividade
    ├── js/
    │   └── site.js                    # Interações compartilhadas no navegador
    └── images/
        ├── physical/                  # Rack, equipamentos Cisco e cabeamento
        ├── endpoints/                 # Evidências disponíveis de estações
        ├── docker/                    # Containers e capturas do Portainer
        ├── monitoring/
        │   ├── zabbix/
        │   └── grafana/
        ├── services/                  # Capturas do Pi-hole e Uptime Kuma
        └── voip/                      # Fotografias da telefonia IP
```

Os dois HTMLs referenciam os **mesmos** arquivos `assets/css/site.css` e `assets/js/site.js`, as duas imagens atuais da onça em PNG e as mesmas fotografias e capturas técnicas. Isso evita a manutenção de duas implementações diferentes para o front-end.

| Componente | Página em inglês | Página em português |
| --- | --- | --- |
| HTML | [`docs/index.html`](../../index.html) | [`docs/pt-BR/index.html`](../index.html) |
| CSS | [`site.css`](../../assets/css/site.css) | Mesma folha de estilos |
| JavaScript | [`site.js`](../../assets/js/site.js) | Mesmo script |
| Logo principal | [`tapajos-jaguar-logo.png`](../../assets/brand/tapajos-jaguar-logo.png) | Mesma imagem |
| Favicon | [`tapajos-jaguar-favicon.png`](../../assets/brand/tapajos-jaguar-favicon.png) | Mesma imagem |
| Evidências | `docs/assets/images/` | Mesmo acervo de imagens |

O arquivo `docs/.nojekyll` está presente na raiz dos documentos publicados. O repositório também contém `docs/pt-BR/.nojekyll`.

## 3. Arquitetura do front-end e execução

```text
Navegador do visitante
       │
       ├── /index.html                 (inglês)
       └── /pt-BR/index.html           (português)
                     │
                     ├── /assets/css/site.css
                     ├── /assets/js/site.js
                     ├── /assets/brand/*.png
                     └── /assets/images/*
                                   │
                                   └── Links para documentação técnica no GitHub
```

- **HTML5:** regiões semânticas, hierarquia de conteúdo, metadados, cartões de evidências, navegação, perguntas expansíveis nativas e diálogo para imagens.
- **CSS3:** tipografia, paleta escura, componentes, grades, pontos de adaptação responsiva, estados de interação e suporte à redução de movimento.
- **JavaScript puro:** eventos e atualizações do DOM para navegação, seletor de VLAN, filtros da galeria, barra de progresso, animação de entrada e ampliação de imagens.
- **Hospedagem estática:** os arquivos públicos são disponibilizados pelo GitHub Pages. O site público não exige aplicação de servidor, autenticação, API de telemetria ao vivo nem banco de dados.
- **Recursos externos:** o CSS importa Google Fonts; os links de documentação técnica direcionam para este repositório no GitHub. Caso as fontes externas não carreguem, há famílias de fontes de sistema como alternativa.

Os arquivos estáticos podem ser mantidos diretamente. Não é necessário um framework de front-end nem um processo de compilação JavaScript para compreender as páginas atuais.

## 4. Mapa das 12 seções HTML

As duas versões possuem **12 elementos `<section>`**: abertura, outras dez seções com âncoras e uma chamada final sem `id`. Os identificadores HTML permanecem iguais nos dois idiomas para que o mesmo JavaScript funcione corretamente.

| Ordem | Seção / âncora | Conteúdo e funcionamento |
| --- | --- | --- |
| 1 | `#home` — Abertura | Identidade visual, apresentação, contexto do projeto, fotografia de fundo, botões e indicadores resumidos. |
| 2 | `#about` — Projeto | Contexto da empresa fictícia, escopo do laboratório real, desafios da infraestrutura e justificativa dos trabalhos documentados. |
| 3 | `#architecture` — Redes | Contexto Cisco C8200L/C9200L, representação lógica, sete cartões de VLAN e painel sincronizado de descrição técnica. |
| 4 | `#services` — Serviços | Nove cartões com referências: redes Cisco, Debian/Docker, Zabbix, Grafana, Asterisk, FreeRADIUS, Pi-hole, Uptime Kuma e Portainer. |
| 5 | `#evidence` — Evidências | Galeria de imagens com filtros, identificação das capturas e ampliação em diálogo. |
| 6 | `#cabling` — Cabeamento | Representação dos pinos RJ45/T568A, explicação de cabeamento físico e link para evidências. |
| 7 | `#monitoring` — Monitoramento | Descrição da arquitetura de observabilidade e valores datados; link para documentação técnica do Zabbix. |
| 8 | `#timeline` — Linha do tempo | Marcos históricos do registro do switch, da coleta de evidências e da consolidação documental. |
| 9 | `#budget` — Análise de custos | Três cenários em BRL, identificação do câmbio BRL/USD e acesso aos relatórios e às planilhas em português e inglês. |
| 10 | `#documentation` — Documentação | Links selecionados para arquitetura, VLANs, Docker, monitoramento, serviços e infraestrutura física. |
| 11 | `#faq` — Perguntas frequentes | Quatro perguntas expansíveis e link para o FAQ técnico completo. |
| 12 | Chamada final (sem `id`) | Links para o repositório e as evidências; o rodapé aparece após essa seção. |

O menu principal contém links para `#about`, `#architecture`, `#services`, `#evidence`, `#cabling`, `#monitoring` e `#documentation` e `#budget`. A marca retorna a `#top`. O rodapé possui navegação complementar e um link para voltar ao início.

### 4.1 Seletor de VLANs

A seção de redes apresenta **VLANs 10, 20, 30, 40, 50, 60 e 70**. Cada botão possui `data-vlan` e informações complementares em `data-title`, `data-description`, `data-url` e `data-link`. O JavaScript atualiza um único painel `[data-vlan-detail]`, sem criar novos blocos de conteúdo ou consultar equipamentos da rede.

O atributo `aria-pressed` identifica o cartão selecionado; a primeira VLAN é ativada na inicialização. As descrições representam o cenário documentado e não constituem comprovação de que todas as regras de isolamento e roteamento foram operacionalmente testadas.

### 4.2 Cartões de serviços

Os nove cartões reúnem nome, descrição, imagem ou elemento visual e link para um registro técnico correspondente. Na página inglesa, os links usam os documentos em inglês; na portuguesa, os caminhos em `docs/pt-BR/`. São **links de documentação**, não conexões autenticadas aos serviços internos do laboratório.

### 4.3 Galeria de evidências

A galeria contém **25 imagens selecionáveis**, divididas assim:

| Filtro | Itens | Conteúdo |
| --- | ---: | --- |
| `physical` | 3 | Equipamentos físicos e rack |
| `docker` | 3 | Containers e Portainer |
| `monitoring` | 10 | Zabbix e Grafana |
| `services` | 5 | DNS, disponibilidade e telefonia IP |
| `endpoints` | 4 | Registros de estações |
| `all` | 25 | Todas as categorias |

Seis botões possuem `data-filter`. Cada cartão de imagem apresenta `data-category`, metadados e uma fotografia ou captura. O script altera a propriedade `hidden` de cada item, marca o filtro ativo com `aria-pressed` e atualiza a contagem visível (`[data-count]`), anunciada pela região de status da galeria (`role="status"`).

Ao selecionar uma imagem, abre-se o `<dialog id="gallery-dialog">` nativo, exibindo a imagem, título, observação, navegação anterior/próxima e botão de fechamento. As setas esquerda/direita do teclado mudam de imagem enquanto o diálogo está ativo; clicar no fundo do diálogo também o fecha. A navegação percorre os itens **visíveis no filtro atual**, e não todo o acervo. Quando existe uma única imagem na seleção, os botões anterior/próxima são desabilitados.

As fotografias e capturas pertencem à documentação histórica do laboratório. Sua publicação não representa acesso em tempo real aos dashboards.

### 4.4 Diagrama de cabeamento

O componente RJ45 representa visualmente a sequência **T568A** com elementos `.wire` e classes CSS de cores (`.wg`, `.g`, `.wo`, `.b`, `.wb`, `.o`, `.wbr`, `.br`). As cores funcionais dos fios foram preservadas, mesmo após a mudança da identidade visual do restante do site para azul e grafite.

### 4.5 Monitoramento e FAQ

A seção de monitoramento descreve os papéis de Zabbix, Grafana, SNMP e Uptime Kuma e contextualiza os registros históricos. Ela não executa consultas de monitoramento. O FAQ utiliza os elementos nativos `<details>` e `<summary>`: as perguntas abordam a empresa fictícia, se o site é um dashboard ao vivo, os limites da comprovação de ACLs/autenticação Wi-Fi e a disponibilidade dos hosts nas capturas históricas.

### 4.6 Análise financeira

A seção `#budget` apresenta os valores consolidados da planilha em reais (A: R$ 86.683,14; B: R$ 7.448,85; C: R$ 1.084,09/mês) e os links para os relatórios e planilhas em português/BRL e inglês/USD. A versão em BRL é a referência dos preços; a versão em USD utiliza a taxa documentada de US$ 1 = R$ 5,5600, com data-base de 11/11/2026. Os valores são **estimativas**, não despesas pagas, contratos ou cotações independentes nos EUA. Os links apontam para os arquivos publicados em `docs/pt-BR/custos/` e `docs/costs/`.

## 5. Funcionamento do JavaScript (`site.js`)

O script utiliza uma função imediatamente invocada (IIFE) e APIs comuns dos navegadores. Não cria uma aplicação com estado global compartilhado além dos eventos registrados.

| Recurso | Seletores / APIs principais | Comportamento implementado |
| --- | --- | --- |
| Menu móvel | `[data-menu]`, `.nav-links`, `aria-expanded` | Alterna `.is-open`; clicar em um link fecha o menu. |
| Progresso de leitura | `.reading-line`, `scroll`, `scrollY` | Atualiza a barra conforme a posição de rolagem. |
| Animação de entrada | `.reveal`, `IntersectionObserver` | Adiciona `.is-visible` quando o elemento aparece; usa alternativa quando a API não existe. |
| Seleção de VLAN | `[data-vlan]`, `[data-vlan-detail]` | Atualiza título, descrição, link e `aria-pressed`. |
| Filtros das evidências | `[data-filter]`, `.photo[data-category]`, `[data-count]` | Mostra os itens correspondentes, atualiza o total e o filtro selecionado. |
| Diálogo de imagens | `#gallery-dialog`, `showModal()`, `close()` | Mostra imagem e metadados, com anterior/próxima, Escape pelo comportamento nativo, fundo e setas do teclado. |

O script **não** acessa métricas ao vivo, autentica usuários, envia formulários, grava informações em banco de dados nem modifica as evidências originais.

## 6. Sistema visual do site

### 6.1 Tipografia e espaçamento

O CSS importa **DM Sans** para textos gerais e **Manrope** para títulos e números em destaque. Existem fontes alternativas do sistema. Títulos grandes utilizam espaçamento entre letras ajustado, separações consistentes e dimensionamento responsivo com `clamp(...)`.

O layout emprega uma largura central padronizada (`--w`), cartões com bordas e raios consistentes, grades de colunas, divisões entre seções, pequenas etiquetas informativas e barra fixa de progresso. O CSS único preserva o mesmo comportamento responsivo nos dois idiomas.

### 6.2 Paleta de cores atual

O site separa intencionalmente a **cor da interface** da **cor própria da marca animal**.

| Variável | Valor | Utilização |
| --- | --- | --- |
| `--bg` | `#0b1220` | Fundo principal azul-noturno |
| `--bg-deep` | `#080e19` | Fundo ainda mais escuro |
| `--paper` | `#162236` | Cartões e superfícies |
| `--paper-soft` | `#1d2b40` | Superfícies secundárias |
| `--paper-hover` | `#243650` | Superfícies em destaque/interação |
| `--text` | `#f0f6ff` | Texto principal |
| `--muted` | `#b8c7dd` | Texto de apoio |
| `--soft` | `#91a6c0` | Legendas mais discretas |
| `--accent` | `#69c4ff` | Destaque azul elétrico |
| `--accent2` | `#369de2` | Azul secundário |
| `--gold` | `#edbc82` | Destaque quente secundário da interface (não é a cor-base do PNG) |
| `--line` | `rgba(137,172,222,.15)` | Divisórias discretas |
| `--line-strong` | `rgba(137,172,222,.31)` | Bordas mais evidentes |

O conjunto visual utiliza azul escuro, grafite, textos azulados discretos e ações em azul mais intenso. A onça dourada aprovada permanece como imagem independente e colorida; **suas cores não são alteradas pelo CSS**. Dessa maneira, os detalhes amarelo/dourado, preto e claro da marca são preservados.

### 6.3 Arquivos de identidade visual

A marca atual utiliza a **cabeça de uma onça estilizada, de perfil**, associando a identidade amazônica do Tapajós a um símbolo visual próprio do projeto técnico. O desenho aprovado possui áreas douradas/amarelas, espaços negativos escuros e detalhes claros. A imagem escolhida foi adaptada para o tamanho reduzido do cabeçalho e do favicon; os arquivos publicados são PNG com transparência.

- [Logo principal da onça](../../assets/brand/tapajos-jaguar-logo.png) — exibida no cabeçalho e no rodapé das duas páginas.
- [Favicon da onça](../../assets/brand/tapajos-jaguar-favicon.png) — declarado no `<head>` com tipo `image/png`.

Os dois SVGs anteriores continuam em `docs/assets/brand/` como referência histórica: `tapajos-emblem.svg` e `tapajos-favicon.svg`. **Não são os arquivos utilizados atualmente** pelo HTML publicado.

## 7. Responsividade e movimento

O CSS compartilhado inclui pontos de adaptação em **1050 px**, **760 px** e **480 px**, além de regras complementares para evidências e FAQ:

- **Desktop:** navegação completa; serviços, galeria, topologia, métricas e rodapé em múltiplas colunas.
- **Telas intermediárias:** redução dos espaçamentos de navegação e adaptação do número de colunas.
- **Celulares (≤760 px):** menu recolhível; grades simplificadas; ajustes de altura da abertura, espaçamento, tipografia e diálogo de imagens.
- **Telas pequenas (≤480 px):** cartões predominantemente em uma coluna, margens reduzidas e botões principais com largura total.
- **Movimento reduzido:** `@media (prefers-reduced-motion: reduce)` desabilita animações e transições e mantém o conteúdo de entrada visível.

A abertura mantém a mesma fotografia real do laboratório e ajusta apenas a sobreposição de gradientes e o posicionamento da imagem em telas estreitas. Os cartões e a galeria utilizam `object-fit: cover`, enquanto a imagem ampliada usa `object-fit: contain`.

## 8. Internacionalização e equivalência de conteúdo

O site não utiliza plugin de tradução nem um mecanismo dinâmico de idiomas. Ele possui **dois documentos HTML explícitos**:

- Inglês: `docs/index.html`, `<html lang="en">`.
- Português brasileiro: `docs/pt-BR/index.html`, `<html lang="pt-BR">`.

As páginas compartilham CSS, JavaScript, marca, imagens, ordem das 11 seções e os mesmos `id` de âncoras em inglês. Títulos, parágrafos, menu, descrições de imagens, textos de acessibilidade e links para documentos são localizados em cada idioma.

A mudança de idioma ocorre por hyperlinks comuns: o inglês aponta para `pt-BR/index.html` e o português para `../index.html`. As referências para mecanismos de busca são declaradas com `rel="alternate"` e `hreflang="en"` / `hreflang="pt-BR"`.

Ao atualizar o HTML de um idioma, é necessário refletir o **mesmo conteúdo relevante e comportamento** no outro. Não se devem traduzir nomes de classes CSS, IDs de elementos ou atributos `data-*` utilizados pelo JavaScript compartilhado.

## 9. Metadados, acessibilidade e carregamento

### 9.1 Metadados HTML

Os dois arquivos HTML contêm declaração de viewport, descrição, `theme-color` (`#0b1220`), metadados Open Graph, URL canônica, referências aos idiomas, favicon PNG e instrução de pré-carregamento da fotografia de destaque. Títulos e descrições são específicos de cada idioma. A imagem Open Graph é a fotografia de visão geral da infraestrutura física; atualmente não utiliza a onça dourada como imagem de compartilhamento.

### 9.2 Recursos de acessibilidade presentes no código

O código implementa estes cuidados:

- Atributos de idioma no elemento `<html>`.
- Link para pular ao conteúdo e região `<main id="main">` identificada.
- Navegação semântica, hierarquia de títulos e botões.
- Rótulos acessíveis no idioma da página para menu móvel, filtros, controles de galeria e diálogo ampliado; o rótulo do menu acompanha os estados aberto/fechado.
- Região de status que anuncia a quantidade de imagens exibidas após uma mudança de filtro.
- `aria-expanded` no menu móvel e `aria-pressed` nos controles selecionáveis.
- Contorno visual para `:focus-visible` no CSS.
- Elementos `<details>` nativos no FAQ e `<dialog>` para as fotografias ampliadas.
- Suporte à preferência de movimento reduzido e textos descritivos nas imagens em que foram fornecidos.

Essas medidas identificadas no código **não equivalem a uma certificação de conformidade WCAG**. Testes em navegadores e tecnologias assistivas constituem uma atividade separada.

### 9.3 Carregamento das páginas

O script é carregado com `defer`. Cada página possui **37 elementos `<img>`**, dos quais **34 utilizam `loading="lazy"`** no código examinado. A fotografia principal da infraestrutura possui pré-carregamento, e as imagens de evidência são fornecidas pelos arquivos do repositório. O desempenho visual depende do navegador, conexão e tamanho das fotografias originais; não se atribui aqui nenhum resultado de benchmark.

## 10. Publicação no GitHub Pages

**Endereços publicados:**

- Inglês: https://kayo-willian.github.io/enterprise-noc-from-scratch/
- Português: https://kayo-willian.github.io/enterprise-noc-from-scratch/pt-BR/

Os arquivos públicos estão sob `docs/`, e o repositório possui execuções bem-sucedidas de **pages build and deployment** associadas às alterações visuais examinadas. A atualização final da onça dourada foi publicada com sucesso para o commit `08d2aedafa8ce2a71277293816a287575782c9c0`.

O GitHub Pages entrega a apresentação estática; ele não disponibiliza a aplicação corporativa executada por Docker nem os serviços de monitoramento da rede local. A pasta pública, o histórico das execuções e as URLs são sustentados pelos arquivos e registros do repositório; configurações de publicação não visíveis nas fontes examinadas não são presumidas.

## 11. Visualização local e manutenção

Um servidor HTTP estático local é suficiente para visualizar o front-end, pois as funcionalidades atuais executam no navegador:

```bash
cd docs
python3 -m http.server 8000
```

Abra `http://localhost:8000/` para inglês e `http://localhost:8000/pt-BR/` para português. Encerre o servidor com `Ctrl+C`.

### Referência de edição

| Objetivo | Arquivo | O que preservar |
| --- | --- | --- |
| Alterar textos em inglês | `docs/index.html` | IDs das âncoras, atributos `data-*` e estrutura atual |
| Alterar textos em português | `docs/pt-BR/index.html` | Equivalência semântica e seletores compartilhados |
| Ajustar cores e espaçamento | `docs/assets/css/site.css` | Regras responsivas, contraste e cores funcionais T568A |
| Trocar a marca da onça | Dois PNGs atuais e, se os nomes mudarem, referências nos dois HTMLs | Proporção da logo, legibilidade do favicon e transparência |
| Atualizar a galeria | Itens dos dois HTMLs e arquivos em `docs/assets/images/` | Origem das evidências, descrições e categorias dos filtros |
| Alterar interações | `docs/assets/js/site.js` | Compatibilidade dos seletores nos dois idiomas |
| Alterar links técnicos | Seções de serviços e documentação nos dois HTMLs | Idioma de destino e caminhos reais do repositório |
| Alterar valores históricos | HTML pertinente e documento técnico de origem | Data da observação e identificação como dado não transmitido ao vivo |

Depois de uma edição local, é importante conferir os dois idiomas, a navegação, as interações e a renderização das páginas. Alterações no repositório ou na publicação seguem o processo de autorização estabelecido para o projeto.

### Lista objetiva de conferência visual e funcional

1. As duas URLs principais carregam e apresentam a mesma organização.
2. Cabeçalho e rodapé exibem a onça dourada; a aba do navegador utiliza o favicon PNG.
3. A mudança de idioma funciona nos dois sentidos.
4. A navegação para as seções funciona em desktop e dispositivos móveis.
5. A seleção das VLANs atualiza título, descrição e link técnico.
6. Os filtros da galeria mostram os itens esperados e a contagem correspondente.
7. O diálogo abre, permite navegar e fecha por controles e teclado.
8. Os links de documentação do GitHub direcionam ao idioma correto.
9. Indicadores históricos permanecem claramente distintos de métricas em tempo real.
10. As cores dos fios T568A, o layout móvel e a preferência por movimento reduzido permanecem íntegros.

Esta lista auxilia a manutenção; não afirma que todos os testes já foram executados em todos os navegadores.

## 12. Publicação e limites das evidências

O site público é um estudo de caso técnico estático e bilíngue, não uma interface de controle da infraestrutura ou dashboard em tempo real. Ele utiliza documentação sanitizada e capturas datadas; não publicar senhas, chaves privadas, comunidades SNMP reais ou credenciais wireless identificáveis. Capturas históricas não devem ser apresentadas como saúde atual dos equipamentos ou recuperação comprovada de incidentes.

## 13. Documentação técnica relacionada

- [Índice de documentação em português](../README.md)
- [Índice de documentação em inglês](../../README.md)
- [Análise financeira em português](../custos/enterprise-noc-orcamento-final-brl-2026.md)
- [Planilha em BRL](../custos/enterprise-noc-orcamento-final-brl-2026.xlsx)
- [Análise financeira em inglês](../../costs/enterprise-noc-final-budget-usd-2026.md)
- [Planilha em USD](../../costs/enterprise-noc-final-budget-usd-2026.xlsx)
- [Visão Geral da Infraestrutura](../arquitetura/visao-geral-da-infraestrutura.md)
- [Topologia Lógica Consolidada](../redes/topologia-logica-consolidada.md)
- [Registro de Configuração do Switch](../redes/registro-switch-vlans-2026-11-04.md)
- [Infraestrutura Docker](../containers/servicos-docker.md)
- [Monitoramento Zabbix](../monitoramento/zabbix.md)
- [Monitoramento Grafana](../monitoramento/grafana.md)
- [Infraestrutura Física](../evidencias/infraestrutura-fisica.md)
- [Perguntas Frequentes](../faq/perguntas-frequentes.md)
- [Gerenciamento de Incidentes NOC](../operacoes-noc/gerenciamento-de-incidentes.md)

---

**Enterprise NOC — From Scratch**  
*Da infraestrutura física às operações de rede.*  
**Referência da documentação do site:** 12 de novembro de 2026.
