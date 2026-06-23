# Kvalitetsmodus for Copy (Multi-Agent Debatt)

En delt metodikk for å heve kvaliteten på **høyverdi tekst** — overskrifter, betalt annonsetekst, kjernebudskap, hero-copy og emnelinjer. Dette er tekst som blir lest tusenvis av ganger, der noen få prosent løft i konvertering er verdt ekstra innsats. For alt annet skriver du i én gjennomkjøring.

---

## Default vs. Kvalitetsmodus

| | Default | Kvalitetsmodus |
|---|---------|----------------|
| **Hva** | Ett utkast, én gjennomkjøring | En debatt-loop med flere roller |
| **Hastighet** | Rask | Treg |
| **Kostnad** | Billig | Dyr (mange tokens) |
| **Resultat** | Godt nok | Målbart bedre |
| **Bruk for** | Det meste | Kun den teksten som virkelig teller |

Default er riktig 95% av tiden. Skriv, sjekk mot `BRAND.md`, lever. Kvalitetsmodus er et bevisst valg du tar når teksten har nok rekkevidde eller innflytelse til å forsvare kostnaden — for da slår en liten kvalitetsforskjell tilbake mange ganger.

---

## 5-Rolle-Loopen

Tanken er enkel: én skribent som også er sin egen dommer blir blind for egne svakheter. Ved å splitte arbeidet i distinkte roller — der hver rolle har én jobb — tvinger du frem reell motstand, og motstand er det som hever kvalitet.

1. **Writer** — skriver første utkast ut fra brief og `BRAND.md`.
2. **Critic** — finner KUN problemer. Ingen forslag til fiks, ingen ros. Jobben er å rive utkastet fra hverandre: hva er vagt, klisjé, off-brand, svakt løfte, feil awareness-nivå?
3. **Rewriter** — skriver om utkastet basert på kritikken. Ser kritikken, ikke Writerens begrunnelser.
4. **Merger** — tar det beste fra original og omskriving og smelter sammen til én sterk versjon.
5. **Judge-panel** — velger vinneren mellom kandidatene og begrunner kort hvorfor.

Deretter looper du: ny runde med Critic på vinneren, ny Rewriter, ny Merger, ny Judge — helt til ingenting slår den nåværende versjonen. Da stopper du. Et naturlig stoppunkt er to runder uten at Judge bytter vinner.

```
Writer → Critic → Rewriter → Merger → Judge ─┐
   ▲                                          │
   └──── loop til ingenting slår vinneren ────┘
```

**Eksempel — én runde på en hero-overskrift:**

- **Writer:** «Den smarteste måten å håndtere bedriftsdata på.»
- **Critic:** «Smarteste» er en udokumentert påstand. «Håndtere bedriftsdata» er vagt — hvilket utfall? Ingen spesifisitet, ingenting som skiller fra konkurrenten. Off-brand: BRAND.md sier «konkret over kreativt».
- **Rewriter:** «Finn enhver norsk bedrift på sekunder — med data du kan stole på.»
- **Merger:** kombinerer Rewriterens konkrete løfte med et tall fra briefen: «Søk i 1,2 mill. norske selskaper på sekunder.»
- **Judge:** velger Merger-versjonen — «konkret, etterprøvbart tall, klart utfall, on-brand. Slår baseline.»

Legg merke til at Critic-en aldri foreslo en fiks; den bare pekte på svakhetene, slik at Rewriter-en løste dem fritt. Det er den arbeidsdelingen som gir løft.

---

## Fresh Context er den egentlige verdien

Selve gullet her er ikke at det er «flere roller» — det er at hver rolle får **isolert kontekst**. Hvis alle rollene deler én samtalehistorikk, ser Critic-en hva Writer-en tenkte, Rewriter-en husker forrige kritikk, og hele panelet drifter mot enighet. Da lærer agentene å «game» dommeren i stedet for å gjøre teksten bedre, og du ender med **convergent mediocrity**: alt konvergerer mot en trygg, kjedelig midte.

Sikre frisk kontekst slik:

- Kjør hver rolle som en **separat agent-instans** (egen samtale), eller
- Gi hver rolle **eksplisitt kontekst som input** (briefen, kandidat-tekstene, kriteriene) — ikke en delt, akkumulert tråd.

Poenget: Critic-en skal vurdere *teksten*, ikke *forsvare* Writer-en. Judge-en skal vurdere *kandidatene*, ikke huske hvem som «vant sist». Isolasjon er det som gjør at hver rolle bidrar med uavhengig signal.

---

## Unngå Kjedelig Konsensus

Den største fellen i en debatt-loop er at den glatter ut til enighet og produserer noe trygt og intetsigende. Det er det motsatte av målet. Motgift:

- **Distinkte rolle-instrukser.** Critic-en skal RIVE, ikke glatte. Hvis Critic-en begynner å skrive «dette er ganske bra, men kanskje...», har du tapt — instruer den eksplisitt til å finne det som er galt, selv om utkastet virker greit.
- **Injiser diversitet.** Be Rewriter/Merger om vinkler som er *ulike* hverandre (ulik awareness-vinkel, ulik følelse, ulik struktur), ikke varianter av samme setning. Ulike kandidater gir Judge-en noe reelt å velge mellom.
- **Riktig spørsmål til Judge.** La Judge spørre «er dette bedre enn baseline?», ikke «er dette trygt nok?». «Trygt nok» belønner det blasse; «bedre enn baseline» tvinger frem et reelt løft eller en ærlig erkjennelse av at runden ikke ga noe.
- **Husk input-kvalitet.** Loopen forsterker det den får inn. Svak brief, vag målgruppe eller manglende `BRAND.md`-kontekst gir over-konsensus rundt et tomt sentrum — low-signal inn, low-signal ut. Bruk tid på briefen før du bruker tokens på debatten.

---

## Token-Caveat — Når Bruke, Når Ikke

Dette er dyrt. En full loop kan koste 5–10x en vanlig skriveoppgave i tokens. Det er verdt det når teksten har høy innflytelse, og bortkastet ellers. Vær disiplinert:

| Bruk kvalitetsmodus på | IKKE bruk kvalitetsmodus på |
|------------------------|------------------------------|
| Hero-overskrift på hovedlandingsside | Bilder / visuell generering |
| Betalt annonsetekst som skal kjøre med budsjett | Bulk-varianter (50 annonse-permutasjoner) |
| Kjernebudskap / posisjoneringssetning | Raske CRO-iterasjoner og småjusteringer |
| Emnelinjer for store utsendelser | Intern tekst, utkast, brainstorm |
| Tagline / signaturløfte | Lavtrafikk-sider og throwaway-copy |

Tommelfingerregel: jo flere øyne teksten får og jo mer som henger på den, jo lettere forsvares loopen. Skal noe leses tusenvis av ganger eller bære en kampanje, kjør den. Lager du mange varianter for å teste, eller itererer raskt på en CRO-detalj, hold deg til default — der er volum og fart viktigere enn å polere én streng.

---

## Praktisk Oppsett

- **Skala loopen til verdien.** Én Critic → Rewriter-runde gir mesteparten av løftet billig. Legg til Merger og flere runder kun når teksten forsvarer det.
- **Hold `BRAND.md` som input til hver rolle.** Tone, Words We Use/Avoid og posisjonering skal styre alle kandidater — ellers vinner kanskje den mest fengende, men off-brand, teksten.
- **Logg vinneren og hvorfor.** Begrunnelsen fra Judge er gjenbrukbar læring til neste høyverdi-tekst.

For copy-rammeverkene (AIDA, ATIDCOA, PAS) og awareness-vinkler som rollene jobber innenfor, se `storytelling-copywriting`.
