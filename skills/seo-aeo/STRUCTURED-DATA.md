# Strukturert Data for AEO (Schema.org)

> **Metodikk-fil i `seo-aeo`.** Denne filen dekker *hvorfor* og *hvilke* schema-typer som betyr mest for AEO (AI-synlighet).
> **For full implementering** — alle schema-typer med kode, CMS-patterns (Next.js / Nuxt / SvelteKit), `@graph`-kombinering og validering — se **`schema-markup`**-skillen. Den er kanonisk kilde for JSON-LD. Ikke dupliser kode-eksemplene her.

---

## Hvorfor strukturert data er AEO-kritisk

Schema.org-markup gjør innhold maskinlesbart. Søkemotorer bruker det til rich snippets; AI-systemer (ChatGPT, Perplexity, Gemini, Google AI Overviews) parser det for å forstå entiteter, fakta og relasjoner — og siterer strukturert innhold oftere enn rå HTML.

| Fordel | Beskrivelse |
|--------|-------------|
| Rich snippets | FAQ, reviews, produktinfo direkte i SERP |
| AI-forståelse | LLM-er trekker ut entiteter og fakta mer presist |
| Knowledge Graph | Bidrar til Googles (og AI-modellers) kunnskapsbase |
| Entitets-klarhet | Kobler navn → organisasjon → forfatter → kompetanse |

---

## Schema-typer rangert etter AEO-verdi

Implementer disse via `schema-markup`-skillen — her er hvilke som flytter nålen mest for AI-sitering:

| Schema | AEO-verdi | Hvorfor |
|--------|-----------|---------|
| **FAQPage** | Høy | Spørsmål-svar er formatet AI henter mest direkte |
| **HowTo** | Høy | Strukturerte steg gjenbrukes i AI-svar |
| **Article + author** | Høy | E-E-A-T-signaler (hvem, kompetanse, dato) |
| **Organization / WebSite** | Medium | Entitets-klarhet, knowledge panel |
| **Product + review** | Medium | Konkrete, siterbare data |
| **BreadcrumbList** | Lav–medium | Kontekst om sidehierarki |

---

## AEO best practices for schema

1. **FAQPage på alt Q&A-innhold** — den enkleste veien til AI-sitering.
2. **Article med `author` + credentials** — knytt forfatter til en `Person` med `url`/`sameAs` (E-E-A-T).
3. **Hold `dateModified` ekte og fersk** — AI vekter ferskhet.
4. **Vær spesifikk og fakta-tett** — jo flere konkrete felt (tall, datoer, navn), desto mer siterbart.
5. **Match synlig innhold** — schema som ikke speiler det brukeren ser, kan ignoreres eller straffes.

> For citability-rubrikk og plattform-spesifikk AI-optimalisering, se `ai-seo`. For innholdsarkitektur og E-E-A-T, se `AEO.md` i denne skillen.

---

## Implementering og validering

Alt det praktiske — JSON-LD-templates per type, `@graph`-kombinering, CMS-patterns og valideringspipeline (Rich Results Test, Schema Validator, Search Console) — ligger i **`schema-markup`**-skillen. Start der.
