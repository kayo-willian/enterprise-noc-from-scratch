# Enterprise NOC — Public Website: Architecture, Design and Maintenance

**English** | [Português (Brasil)](../pt-BR/site/README.md)

**Project:** [Enterprise NOC — From Scratch](../../README.md)  
**Website:** [English](https://kayo-willian.github.io/enterprise-noc-from-scratch/) · [Português (Brasil)](https://kayo-willian.github.io/enterprise-noc-from-scratch/pt-BR/)  
**Organization:** Tapajós Inovações — fictional company used as the laboratory's business scenario  
**Technical basis:** Repository `main`, commit `08d2aedafa8ce2a71277293816a287575782c9c0` (November 10, 2026)  
**Document type:** Implementation record and maintenance reference

---

## 1. Purpose and scope

The public website presents the Enterprise NOC physical laboratory as an accessible, bilingual technical case study. It connects the project's fictional corporate scenario with photographs, historical configuration evidence, network segmentation, Linux and container services, monitoring screenshots, and links to the detailed repository documentation.

The website is a **public static presentation**, not the corporate application hosted within the laboratory's Docker environment. The public pages do not connect to the private network or retrieve live Zabbix, Grafana, router, switch, or server metrics. The screenshots and numeric indicators shown on the page are **historical illustrations**, not live operational readings.

The implementation deliberately uses a straightforward front end: semantic HTML, a single shared CSS stylesheet, a single JavaScript file, and versioned local image assets. The English and Brazilian Portuguese pages use the same structure, styles, scripting and branding; their interface and explanatory text are localized.

This document records what is present in the repository as of the technical basis above. It does not imply an independent accessibility certification, load test, application penetration test, or audit of the private laboratory.

## 2. Repository layout and responsibilities

```text
docs/
├── .nojekyll
├── index.html                         # English public page
├── pt-BR/
│   ├── .nojekyll
│   ├── index.html                     # Portuguese public page
│   └── site/
│       └── README.md                  # Portuguese website documentation (this addition)
├── site/
│   └── README.md                      # English website documentation (this addition)
└── assets/
    ├── brand/
    │   ├── tapajos-jaguar-logo.png    # Current header and footer brand
    │   ├── tapajos-jaguar-favicon.png # Current browser-tab icon
    │   ├── tapajos-emblem.svg         # Earlier logo, retained in repository
    │   └── tapajos-favicon.svg        # Earlier icon, retained in repository
    ├── css/
    │   └── site.css                   # Shared design system, layout, responsive rules
    ├── js/
    │   └── site.js                    # Shared client-side interactions
    └── images/
        ├── physical/                  # Rack, Cisco equipment, structured cabling
        ├── endpoints/                 # Available workstation evidence
        ├── docker/                    # Containers and Portainer screenshots
        ├── monitoring/
        │   ├── zabbix/
        │   └── grafana/
        ├── services/                  # Pi-hole and Uptime Kuma screenshots
        └── voip/                      # IP telephony photographs
```

The two HTML files reference the **same** `assets/css/site.css` and `assets/js/site.js`. They also reference the same two current jaguar PNGs and the same evidence images. This avoids maintaining two separate front-end implementations.

| Component | English page | Portuguese page |
| --- | --- | --- |
| HTML | [`docs/index.html`](../index.html) | [`docs/pt-BR/index.html`](../pt-BR/index.html) |
| CSS | [`site.css`](../assets/css/site.css) | Same shared stylesheet |
| JavaScript | [`site.js`](../assets/js/site.js) | Same shared script |
| Main logo | [`tapajos-jaguar-logo.png`](../assets/brand/tapajos-jaguar-logo.png) | Same image |
| Favicon | [`tapajos-jaguar-favicon.png`](../assets/brand/tapajos-jaguar-favicon.png) | Same image |
| Evidence | `docs/assets/images/` | Same image collection |

The `docs/.nojekyll` file is present in the published documentation root. The repository also contains `docs/pt-BR/.nojekyll`.

## 3. Front-end architecture and runtime

```text
Visitor's browser
      │
      ├── /index.html                 (English)
      └── /pt-BR/index.html           (Portuguese)
                    │
                    ├── /assets/css/site.css
                    ├── /assets/js/site.js
                    ├── /assets/brand/*.png
                    └── /assets/images/*
                                  │
                                  └── Links to GitHub technical records
```

- **HTML5:** page landmarks, content hierarchy, metadata, evidence cards, navigation, native FAQ disclosure elements and image dialog.
- **CSS3:** typography, dark palette, component styling, layouts, responsive breakpoints, hover/focus states and reduced-motion support.
- **Vanilla JavaScript:** event handlers and DOM updates for navigation, the VLAN selector, gallery filters, progress indicator, scroll reveals and image lightbox.
- **Static hosting:** the public files are delivered by GitHub Pages. There is no published server-side application, login system, live telemetry API or database dependency for the public presentation.
- **External resources:** Google Fonts is referenced through CSS `@import`; technical-documentation links lead to this repository on GitHub. The page itself does not need Google Fonts to remain readable because system-font fallbacks are declared.

The site is maintained directly as static source files. The repository does not require a front-end framework or a JavaScript package build to understand these pages.

## 4. Page map: all 11 HTML sections

Both language versions contain **11 `<section>` elements**: the hero, nine other sections with anchors, and a final call to action without a section ID. The English identifiers are also used by the Portuguese page, so common interaction code remains compatible.

| Order | Section / anchor | Implemented content and behavior |
| --- | --- | --- |
| 1 | `#home` — Hero | Branding, introductory statement, project context, background photograph, calls to action and compact project indicators. |
| 2 | `#about` — Project | Fictional business context, real laboratory scope, infrastructure challenges and the rationale behind the documented work. |
| 3 | `#architecture` — Network | Cisco C8200L/C9200L context, logical diagram, seven interactive VLAN cards and a synchronized technical-description panel. |
| 4 | `#services` — Services | Nine evidence-oriented service cards: Cisco networking, Debian/Docker, Zabbix, Grafana, Asterisk, FreeRADIUS, Pi-hole, Uptime Kuma and Portainer. |
| 5 | `#evidence` — Evidence | Filterable image gallery, evidence labels and image enlargement dialog. |
| 6 | `#cabling` — Cabling | Illustrated RJ45/T568A pin arrangement, physical cabling explanation and link to infrastructure evidence. |
| 7 | `#monitoring` — Monitoring | Monitoring architecture narrative and dated figures; link to technical Zabbix documentation. |
| 8 | `#timeline` — Timeline | Historical milestones for the switch snapshot, evidence collection and documentation consolidation. |
| 9 | `#documentation` — Technical documentation | Curated links to architecture, VLAN, Docker, monitoring, service and physical infrastructure records. |
| 10 | `#faq` — FAQ | Four native expandable questions and a link to the longer technical FAQ. |
| 11 | Final call to action (no ID) | Project/GitHub and evidence links; the footer follows this section. |

The global navigation links to `#about`, `#architecture`, `#services`, `#evidence`, `#cabling`, `#monitoring` and `#documentation`. The brand link returns to `#top`. The footer provides supplemental navigation and a return-to-top link.

### 4.1 Interactive VLAN panel

The network section presents **VLANs 10, 20, 30, 40, 50, 60 and 70**. Each selector uses `data-vlan` and accompanying `data-title`, `data-description`, `data-url` and `data-link` information. The JavaScript updates the single `[data-vlan-detail]` panel rather than inserting separate content blocks or making network requests.

`aria-pressed` reflects the selected card; the first VLAN is selected when the script initializes. Descriptions are based on the documented laboratory scenario and are not proof that every isolation or routing control has been operationally verified.

### 4.2 Service cards

The nine service cards combine a name, explanatory text, imagery or a visual marker, and a link to the appropriate technical record. Links in English point to the English documentation paths; Portuguese links point to the corresponding `docs/pt-BR/` records. These are **documentation links**, not authenticated access to laboratory services.

### 4.3 Evidence gallery

The gallery includes **25 selectable evidence items**, divided as follows:

| Filter key | Items | Subject |
| --- | ---: | --- |
| `physical` | 3 | Physical equipment and rack |
| `docker` | 3 | Containers and Portainer |
| `monitoring` | 10 | Zabbix and Grafana |
| `services` | 5 | DNS, availability and IP telephony |
| `endpoints` | 4 | Workstation records |
| `all` | 25 | All categories combined |

Six filter buttons use `data-filter`. Each photo has `data-category`, descriptive metadata and an image. The script sets each item's `hidden` property, updates the active filter's `aria-pressed`, and refreshes the displayed item counter (`[data-count]`).

Selecting an image opens the native `<dialog id="gallery-dialog">` lightbox, with the image, title, note, previous/next buttons and close control. Arrow Left/Right keys change the displayed image while the dialog is active; clicking the dialog backdrop also closes it. Navigation wraps within the **currently visible filter result**, not the entire gallery. The script disables previous/next controls when the selection contains one item.

The photographs and screenshots originate from the laboratory evidence collection. Their presence on the public site must not be interpreted as real-time dashboard access.

### 4.4 Cabling diagram

The RJ45 component renders the **T568A** pin sequence visually using `.wire` elements and color-specific CSS classes (`.wg`, `.g`, `.wo`, `.b`, `.wb`, `.o`, `.wbr`, `.br`). The functional cable colors are deliberately preserved even though the rest of the website changed to a blue/graphite visual identity.

### 4.5 Monitoring and FAQ

The monitoring section communicates the role of Zabbix, Grafana, SNMP and Uptime Kuma and provides dated evidence context. It does not run monitoring queries. The FAQ uses native `<details>` and `<summary>` elements: questions cover the fictional company, whether the page is a live dashboard, the limits of ACL/Wi-Fi verification and the state of hosts shown in historical screenshots.

## 5. JavaScript behavior (`site.js`)

The script is wrapped in an immediately invoked function expression (IIFE) and uses standard browser APIs. It does not introduce global application state beyond its event handlers.

| Feature | Main selectors / APIs | Actual behavior |
| --- | --- | --- |
| Mobile navigation | `[data-menu]`, `.nav-links`, `aria-expanded` | Toggles `.is-open`; clicking a navigation link closes the menu. |
| Reading progress | `.reading-line`, `scroll`, `scrollY` | Updates a bar according to the document's scroll position. |
| Scroll reveal | `.reveal`, `IntersectionObserver` | Adds `.is-visible` when content enters the viewport; uses a fallback if the API is missing. |
| VLAN selection | `[data-vlan]`, `[data-vlan-detail]` | Updates title, description, link and `aria-pressed`. |
| Evidence filters | `[data-filter]`, `.photo[data-category]`, `[data-count]` | Shows matching photos and updates the count and selected-filter state. |
| Image dialog | `#gallery-dialog`, `showModal()`, `close()` | Displays the selected image and metadata, with previous/next, Escape through native dialog behavior, backdrop and arrow-key controls. |

The script does **not** fetch live metrics, authenticate users, submit forms, write to a database or change the original evidence files.

## 6. Visual design system

### 6.1 Typography and spacing

The CSS imports **DM Sans** for general interface text and **Manrope** for headings and emphasized numeric content. System fallback fonts are specified. Large headings use tight letter spacing, consistent heading spacing and responsive `clamp(...)` sizing.

The layout has a centered content width (`--w`), shared card borders/radii, multi-column grids, visual section separators, small status labels and a fixed scrolling progress indicator. The CSS is shared by both languages, so responsive behavior remains consistent.

### 6.2 Current color tokens

The current site intentionally separates the **interface color** from the **animal brand color**.

| Variable | Value | Usage |
| --- | --- | --- |
| `--bg` | `#0b1220` | Primary midnight-blue background |
| `--bg-deep` | `#080e19` | Deep background tone |
| `--paper` | `#162236` | Cards and surfaces |
| `--paper-soft` | `#1d2b40` | Secondary surfaces |
| `--paper-hover` | `#243650` | Hover surfaces |
| `--text` | `#f0f6ff` | Main text |
| `--muted` | `#b8c7dd` | Supporting text |
| `--soft` | `#91a6c0` | Quieter captions |
| `--accent` | `#69c4ff` | Primary electric-blue highlight |
| `--accent2` | `#369de2` | Secondary blue accent |
| `--gold` | `#edbc82` | Warm secondary UI highlight (not the PNG's source color) |
| `--line` | `rgba(137,172,222,.15)` | Subtle dividers |
| `--line-strong` | `rgba(137,172,222,.31)` | Stronger borders |

The main design uses dark blue, graphite, muted blue text and brighter blue actions. The approved golden jaguar remains an independent full-color image; it is **not recolored through CSS**. This keeps its yellow/gold, black and light details recognizable.

### 6.3 Branding assets

The current identity uses a **stylized jaguar head in profile**, reflecting the Amazon/Tapajós geographic context while presenting a recognizable technical-project symbol. The approved design features bright golden/yellow surfaces, dark negative space and light details. The source design was adapted for small on-page image placements and a browser favicon; the published assets are PNG files with transparency.

- [Primary jaguar logo](../assets/brand/tapajos-jaguar-logo.png) — displayed in the header and footer of both pages.
- [Jaguar favicon](../assets/brand/tapajos-jaguar-favicon.png) — referenced in the HTML `<head>` as `image/png`.

Two earlier SVG files remain in `docs/assets/brand/` for historical reference: `tapajos-emblem.svg` and `tapajos-favicon.svg`. They are **not** the assets referenced by the current HTML pages.

### 6.4 Visual evolution and decisions

| Phase | Change | What was intentionally preserved |
| --- | --- | --- |
| Initial identity | Dark olive/green interface with an abstract river-and-network-node symbol. | Content structure and laboratory evidence. |
| November 10, 2026 — palette revision | Replaced green-oriented UI colors with midnight-blue, graphite and electric-blue styling across the shared stylesheet. Introduced a temporary blue jaguar identity. | Section layout, page copy, photographs, JavaScript behavior and T568A wire colors. |
| November 10, 2026 — approved final mark | Replaced the temporary jaguar with the selected **golden jaguar** PNG logo and matching favicon for English and Portuguese. | The blue theme, existing content, 11-section structure and client-side behavior. |

The palette and temporary jaguar revision are recorded in repository commit `ed8d10ae9ba38aaa9634dbbd8573bfe62b5530e0`. The approved golden-jaguar integration is recorded in commit `08d2aedafa8ce2a71277293816a287575782c9c0`. These identifiers are provenance, not deployment instructions.

## 7. Responsive behavior and motion

The shared CSS includes breakpoints at **1050 px**, **760 px** and **480 px**, with additional rules for the evidence/FAQ components:

- **Desktop:** full navigation; multi-column service, gallery, topology, metrics and footer layouts.
- **Medium screens:** reduced navigation spacing and adapted grid column counts.
- **Mobile (≤760 px):** collapsible navigation; simplified grids; adjusted hero sizing, spacing, typography and gallery/dialog layout.
- **Small screens (≤480 px):** primarily single-column cards, narrower padding and full-width primary buttons.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` disables animations and transitions and ensures reveal content remains visible.

The hero maintains the same underlying laboratory photograph while changing gradient overlays and background positioning for narrow screens. Images in cards and the gallery use `object-fit: cover`; enlarged lightbox images use `object-fit: contain`.

## 8. Internationalization and content parity

The site does not use a translation plugin or a dynamic language runtime. Instead, it maintains **two explicit HTML documents**:

- English: `docs/index.html`, `<html lang="en">`.
- Brazilian Portuguese: `docs/pt-BR/index.html`, `<html lang="pt-BR">`.

Both pages share CSS, JavaScript, brand assets, image files, the same 11-section order and the same English-language anchor IDs. Each page provides localized titles, paragraphs, navigation, image labels, accessibility text and links to the correct language's technical records.

The language switch is a regular hyperlink: English links to `pt-BR/index.html`, while Portuguese links to `../index.html`. Search-engine language references are provided through `rel="alternate"` and `hreflang="en"` / `hreflang="pt-BR"`.

When updating one HTML file, mirror the **substantive content and behavior** in the other. Do not translate CSS class names, element IDs or JavaScript `data-*` selectors; doing so would break the shared script.

## 9. Metadata, accessibility and performance provisions

### 9.1 Document metadata

Both HTML documents contain a viewport declaration, description, `theme-color` (`#0b1220`), Open Graph metadata, canonical URL, alternate-language URLs, a PNG favicon reference and a preload hint for the hero evidence photograph. Their titles and descriptions are language-specific. Open Graph uses the physical infrastructure overview photograph as its image; it does not currently use the golden jaguar logo as the social-preview image.

### 9.2 Implemented accessibility-related features

The source includes the following provisions:

- Language attributes on the `<html>` element.
- A skip-to-content link and a named `<main id="main">` landmark.
- Semantic navigation, section headings and buttons.
- Accessible labels for the mobile menu, filters, gallery controls and enlarged-image dialog.
- `aria-expanded` on the mobile navigation control and `aria-pressed` on selectable controls.
- A visible `:focus-visible` outline in the stylesheet.
- Native `<details>` elements for the FAQ and a native `<dialog>` for enlarged photographs.
- Reduced-motion CSS support and descriptive image text where provided.

These source-level provisions are **not a claim of complete WCAG conformance**. Browser/assistive-technology testing would be a separate activity.

### 9.3 Page loading

The script is loaded with `defer`. The English and Portuguese pages each reference **37 `<img>` elements**, with **34 marked `loading="lazy"`** in the inspected source. The hero infrastructure photograph is preloaded, and the published evidence images are served from the repository assets. Display performance depends on browser, network connection and the relatively large original photographs; no benchmark is asserted here.

## 10. GitHub Pages publication

**Published URLs:**

- English: https://kayo-willian.github.io/enterprise-noc-from-scratch/
- Portuguese: https://kayo-willian.github.io/enterprise-noc-from-scratch/pt-BR/

The public website files reside under `docs/`, and the repository has successful GitHub Actions **pages build and deployment** runs associated with the reviewed branding changes. The final golden-logo change was successfully deployed for commit `08d2aedafa8ce2a71277293816a287575782c9c0`.

GitHub Pages hosts the static presentation; it does not deploy the Docker-based corporate portal or expose the local laboratory monitoring services. The publication directory, workflow results and URLs are supported by the repository; deployment settings not visible in the checked files are not assumed.

## 11. Local preview and change workflow

A local static server is sufficient to preview the front end, because the current page's interactive features are browser-side:

```bash
cd docs
python3 -m http.server 8000
```

Open `http://localhost:8000/` for English and `http://localhost:8000/pt-BR/` for Portuguese. Stop the temporary server with `Ctrl+C`.

### Editing guide

| Goal | Edit | Preserve |
| --- | --- | --- |
| Update English copy | `docs/index.html` | Anchor IDs, `data-*` attributes, existing element structure |
| Update Portuguese copy | `docs/pt-BR/index.html` | Semantic parity with English and shared DOM selectors |
| Change palette or spacing | `docs/assets/css/site.css` | Responsive rules, readable contrast and T568A functional colors |
| Change the jaguar mark | The two current PNGs and, if filenames change, both HTML references | Logo proportions, favicon legibility and transparent image background |
| Update gallery content | Both HTML evidence entries and `docs/assets/images/` | Image evidence provenance, descriptive labels and filter category consistency |
| Update interactions | `docs/assets/js/site.js` | Matching selectors and behavior in both languages |
| Update technical document links | Both HTML documentation/service sections | Correct target language and valid repository paths |
| Update historical values | Relevant HTML and linked source document | The original observation date and clear non-live status |

After a local change, inspect both languages, test navigation and interactive elements, and review the actual rendered pages. GitHub deployment or repository edits should happen only through the project's established authorization workflow.

### Practical smoke-check list

1. Both homepage URLs load and show the same layout.
2. Header and footer show the golden jaguar, and the browser tab uses the PNG favicon.
3. Language switching navigates correctly in both directions.
4. Desktop and mobile navigation anchors reach the intended sections.
5. Selecting each VLAN updates title, description and technical link.
6. Gallery category filters show the correct items and counts.
7. Lightbox opens, navigates and closes via its controls and keyboard.
8. Links to external GitHub technical records resolve to the correct language.
9. Historical data remains identified as observations rather than live results.
10. T568A wiring colors, mobile layout and reduced-motion behavior remain intact.

This is a maintenance checklist, not a statement that every test above has already been executed in every browser.

## 12. Evidence integrity, privacy and boundaries

The public site is a technical case study, not an infrastructure control plane. It deliberately links to sanitized repository documentation rather than embedding passwords, private certificates, database dumps or raw persistent volumes. Its screenshots are observational evidence; do not reinterpret them as current system health or use them to claim an incident was fixed.

Avoid exposing credentials, secret tokens, real SNMP community strings, personally identifying device information or unnecessary internal configuration details when adding new captures. Keep technical explanations aligned with the corresponding source documentation; unknown facts that cannot reasonably be recovered should be described once as documentation boundaries, not carried indefinitely as mandatory future tasks.

Tapajós Inovações is the fictional corporate scenario presented by the site; the equipment, photographs, configurations and monitoring captures document the project's physical laboratory implementation.

## 13. Historical scope and future changes

The **implemented** site already has its bilingual static architecture, navigation, cards, VLAN interactions, evidence gallery, image dialog, cabling illustration, monitoring narrative, FAQ, responsive stylesheet, current golden-jaguar assets and published GitHub Pages URLs.

This document describes those components and their maintenance. It does not add new website features, new monitoring data or alternative architectures. Further visual or functional changes can be recorded as new dated decisions without rewriting historical evidence.

## 14. Related project documentation

- [Main project README](../../README.md)
- [Portuguese project README](../../README.pt-BR.md)
- [Infrastructure Architecture](../architecture/infrastructure-overview.md)
- [Consolidated Logical Network Topology](../networking/consolidated-logical-topology.md)
- [Switch Configuration Snapshot](../networking/switch-vlan-snapshot-2026-11-04.md)
- [Docker Infrastructure](../containers/docker-services.md)
- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)
- [Physical Infrastructure](../evidence/physical-infrastructure.md)
- [Technical FAQ](../faq/technical-faq.md)
- [NOC Incident Management](../noc-operations/incident-management.md)

---

**Enterprise NOC — From Scratch**  
*From physical infrastructure to network operations.*  
**Website documentation reference:** November 10, 2026.
