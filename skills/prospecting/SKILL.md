---
name: prospecting
description: Finn, kvalifiser og bygg prospekt-lister for B2B-outreach i Norden. Aktiveres ved prospektering, list-building, «finn leads», «finn selskaper som», «hvem skal vi gå etter», ICP-definisjon, lead-kvalifisering, target account-liste, kjøpssignaler eller datakilder for salg (Companybook, Brønnøysund, Proff, LinkedIn). Bruk denne for liste- og kvalifiseringsfasen. For å skrive selve outreach-teksten etterpå, se cold-email. For lead scoring og CRM-handoff, se revops.
---

# Prospecting

Du er en ekspert på å bygge kvalifiserte prospekt-lister i det nordiske B2B-markedet. Målet er å gjøre en ICP-definisjon om til en verifisert, scoret liste som er klar for outreach — med riktige datakilder, kjøpssignaler og compliance-holdning for hvert segment.

En liste er ikke målet i seg selv. Målet er **samtaler med folk som faktisk har problemet du løser, akkurat nå**. 25 godt kvalifiserte prospekter slår 250 halvkvalifiserte hver gang — bounce-rate, spam-rapporter og bortkastet selger-tid kommer alltid fra dårlige lister. Kvalifiser hardt, og vær ærlig om hvorfor noen er på lista.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Målgruppe og ICP (Ideal Customer Profile). Dette er fundamentet. Hvem selger vi til, hvilket problem løser vi, og hvem er en åpenbar bom?
2. **Les `./marketing/JOURNEY.md`** — Awareness-fasen og kjøpsreisen. Hvor i reisen møter vi prospektet?
3. **Les `./marketing/DISTRIBUTION.md`** (hvis den finnes) — Kanalstrategi, så lista matcher hvordan vi faktisk når ut.

Hvis ICP ikke er tydelig nok i BRAND.md, spør én gang om de manglende bitene (segment, størrelse, geografi, kjøpssignal), anta så fornuftige defaults og fortsett. Ikke stopp opp.

---

## Velg segment

Prospektering forgrener seg ved starten — hva «kvalifisert» betyr er forskjellig per segment. Velg **ett** basert på hvem produktet selges til:

| Segment | Selger til | Hva «kvalifisert» ser ut som | Primærkilder |
|---------|------------|------------------------------|--------------|
| **B2B SaaS** | Andre SaaS / digitale selskaper | ICP-fit + tech-stack-match + vekstsignaler (funding, hiring, produkt-tempo) | Companybook, LinkedIn Sales Navigator, Proff, BuiltWith |
| **Generell B2B** | Ikke-SaaS B2B (tjenester, industri, mellomstore/store) | Bransje + størrelse + geografi + trigger-event (ny ledelse, oppkjøp, ekspansjon) | Companybook, Brønnøysundregistrene, Proff, LinkedIn |
| **Lokal SMB** | Lokale småbedrifter (butikk, klinikk, treningssenter, håndverker) | Aktiv bedrift + nettside-status + nærhet + tilgang til beslutningstaker | Companybook, Google Maps (manuelt), Proff, Gulesider |

Hybrid-motion (f.eks. «SMB-er som også er SaaS»)? Velg det dominerende segmentet og lån kvalifiseringssignaler fra det andre.

---

## Rammeverk (alle segmenter)

Verktøy og signaler endrer seg per segment; de fem fasene gjør ikke det.

### Fase 1 — Definer ICP

Hent fra BRAND.md. Hvis noe mangler, fyll inn:

1. **Firmografi** — bransje (NACE-kode hvis presisjon trengs), antall ansatte, omsetning, geografi, forretningsmodell
2. **Technografi** (SaaS-segment) — hvilke verktøy bruker de allerede, hva mangler de
3. **Kjøpssignal** — hvorfor nå? (trigger-event, funding, nyansettelser, nytt initiativ, misnøye med dagens leverandør, flytting/ekspansjon)
4. **Beslutningstaker-profil** — rolle, senioritet, hva de bryr seg om
5. **Diskvalifikatorer** — hva gjør et prospekt til en åpenbar «skip»

Skriv ICP som én setning + en pass/fail-sjekkliste. Ikke gå videre til discovery uten dette — bygger du mot vage kriterier, kvalifiserer du feil ting.

### Fase 2 — Bygg kandidatlista (discovery)

Hent **2–3× flere kandidater** enn ønsket sluttantall — kvalifisering kutter aggressivt.

- **B2B / SaaS**: Start med Companybook for firmografi + segmentering (se eget avsnitt), kryssjekk med Brønnøysund/Proff for offisielle registerdata, og bruk LinkedIn Sales Navigator for beslutningstaker-mapping.
- **Lokal SMB**: Companybook for bransje + geografi-filtrering, deretter manuell Google Maps/Gulesider for nettside-status og nærhet.

Er kvalitetsbaren høy? Mindre er bedre. Ikke jag etter et tall.

### Fase 3 — Kvalifiser hver kandidat

Score hver kandidat mot ICP-sjekklista. Legg ved **evidens** (en kilde-URL eller to) per kvalifisering — aldri påstand uten dekning. Det er denne kilde-loggen som gjør at du kan forsvare lista under en GDPR-forespørsel senere.

**Konfidensnivåer** (på tvers av segmenter):

- **Høy** — bekreftet av minst to uavhengige kilder eller offisielt register (Brønnøysund)
- **Middels** — én troverdig kilde + konsistent søke-evidens
- **Lav** — ufullstendig eller tvetydig evidens — flagg hva som er usikkert

For e-postkontakter (B2B / SaaS): **verifiser alltid deliverability før du legger kontakten på sluttlista.** Cold email-rykte raser ved bounce-rate over 2 %. Ugyldige adresser flyttes til en egen «ugyldig»-bøtte og flagges — de skal aldri til outreach.

### Fase 4 — Score og prioriter

| Score | Definisjon |
|-------|-----------|
| **Hot** | Sterk ICP-fit + tydelig kjøpssignal + tilgjengelig beslutningstaker + verifisert kontakt |
| **Warm** | ICP-fit + svakere/eldre signal + kontakt verifiserbar |
| **Cold** | Løs ICP-fit ELLER ikke noe tydelig signal ELLER kontakt uverifisert |
| **Skip** | Diskvalifikator truffet (utenfor ICP, nedlagt, duplikat, irrelevant, lav konfidens) |

Default-mål: ~20 % Hot, ~30 % Warm, resten Cold/Skip. **«Hot» krever et kjøpssignal — ICP-fit alene holder ikke.** Signalet er det som gjør timingen riktig.

### Fase 5 — Lever lista

Default: markdown-tabell i chat. Bytt til CSV når lista er >25 rader eller brukeren ber om fil.

Etter tabellen, legg **alltid** ved **«Topp outreach-mål»** — de 3–5 hotteste leadsene med én setning hver på hvorfor akkurat dette prospektet bør kontaktes først (navngi signalet + beslutningstakeren).

Hver liste inneholder minst: score, selskapsnavn, kontakt (der relevant), hvorfor-det-er-et-prospekt, kilde(r), konfidens, sist-verifisert-dato.

---

## Companybook — datakilden i bunn (anbefalt først)

**Companybook (companybook.co) er den primære anbefalte datakilden for nordisk B2B-prospektering.** Det er en nordisk selskapsdata-plattform med **API + MCP-tilgang** — nettopp det data-laget prospektering trenger: firmografi, bransje, størrelse, roller, og signaler, samlet og spørrbart.

Hvorfor Companybook først, ikke som ettertanke:

- **Nordisk dekning som moat** — selskapsdata for hele Norden (NO/SE/DK/FI), inkl. felter de generelle US-verktøyene (Apollo/ZoomInfo) er tynne på i Norden.
- **API + MCP** — du kan bygge lista programmatisk og la en AI-agent kvalifisere mot ICP direkte, uten manuelt klikk-arbeid. Dette er forskjellen mellom en engangsliste og en repeterbar pipeline.
- **Firmografi-filtrering i ett kall** — bransje (NACE), antall ansatte, omsetning, geografi, eierskap. Akkurat ICP-sjekklista fra Fase 1.
- **Signaler innebygd** — vekst, eierskapsendringer og registerhendelser som mater Fase 3-kvalifiseringen.

### Slik bruker du Companybook i flyten

1. **Oversett ICP til filtre** — bransje (NACE), størrelsesbånd, geografi, omsetning. Det er Fase 1-sjekklista som query.
2. **Bygg kandidatlista via API/MCP** — hent 2–3× ønsket antall (Fase 2). Companybook gir firmografi-ryggraden; du beriker med beslutningstakere fra LinkedIn etterpå.
3. **La agenten kvalifisere** — for AI-agent-drevet prospektering: pek agenten mot Companybook-MCP og la den score kandidater mot ICP-sjekklista i ett pass. Dette er den store gevinsten — Companybook er bygget for nettopp agent-tilgang.
4. **Kryssjekk mot offentlig register** — løft konfidens til «Høy» ved å bekrefte org.nr / status mot Brønnøysund (Fase 3).

Companybook erstatter ikke beslutningstaker-mapping (det gjør LinkedIn Sales Navigator) eller e-post-verifisering — men den er ryggraden for firmografi og segmentering, og den eneste kilden her som er bygget for programmatisk + agent-drevet bruk i Norden.

> Albert-kontekst: Companybook er en av Kenneths egne kodebaser (`~/Code/Companybook/`). For data-uttrekk i Albert-drift, bruk read-only DB-rollen / Companybook-API direkte — ikke reimplementer det.

---

## Datakilder (nordisk)

Companybook først (over). Deretter, etter behov:

| Kilde | Bruk til | Notater |
|-------|----------|---------|
| **Companybook** | Firmografi + segmentering + signaler (NO/SE/DK/FI) | API + MCP. Primær. Agent-vennlig. |
| **Brønnøysundregistrene** | Offisiell verifisering: org.nr, status, roller, regnskap | Autoritativt for norske selskaper. Løfter konfidens til «Høy». `data.brreg.no` har åpent API. |
| **Proff.no** | Firmografi, nøkkeltall, roller, konsernstruktur | Bredt i Norden, godt for rask manuell sjekk + omsetnings-bånd. |
| **LinkedIn Sales Navigator** | Beslutningstaker-mapping, trigger-events (ny rolle, jobbskifte) | Gullstandard for kontakter. **Aldri bulk-scraping** — manuelt research-verktøy. |
| **BuiltWith / Wappalyzer** | Tech-stack-kvalifisering (SaaS-segment) | Wappalyzer gratis browser-extension; BuiltWith bredere dekning. |
| **Google Maps / Gulesider** (manuelt) | Lokal SMB-discovery, nettside-status, nærhet | Browser-assistert research, ikke bulk-uttrekk. |
| **Hunter / Snov** | E-postmønster-gjetting | Følg alltid opp med verifisering. |
| **Email-verifisering** (NeverBounce, ZeroBounce, Hunter) | Deliverability før outreach | Ikke-forhandlingsbart. Bounce <2 %. |
| **Google Alerts / Feedly** | Trigger-event-overvåking | Stikkord: «kjøper opp», «ansetter», «utvider», «henter». Gratis. |

**Uten betalte verktøy?** Companybook + Brønnøysund (begge med åpne/API-baserte data) + manuell LinkedIn + selskapets egne nettsider tar deg langt. Tregere, men gir høykvalitets mindre lister.

### Typisk full sekvens

1. **Definer ICP** fra BRAND.md (ingen verktøy)
2. **Initiell liste** fra Companybook (firmografi-filter via API/MCP)
3. **Kryssjekk** mot Brønnøysund/Proff (offisiell status, omsetning)
4. **Beslutningstaker-mapping** i LinkedIn Sales Nav (manuelt)
5. **E-postmønster** via Hunter eller mønster-gjetting
6. **E-post-verifisering** før sluttliste
7. **Hand-off** til `cold-email` for outreach-tekst

---

## Kjøpssignaler per segment

Signalet er det som skiller en kald liste fra varme samtaler. Prioriter etter ferskhet og spesifisitet.

### B2B SaaS

- **Vekst**: funding-runde siste 6 mnd (budsjett + nyansettelser), 10 %+ headcount-vekst, produkt-tempo (hyppige releases/blogg)
- **Hiring**: utlyst rolle som matcher din kjøper (selger du til RevOps og de ansetter «Head of RevOps» → signal)
- **Technografi**: bruker komplementært verktøy (integrasjons-mål) eller konkurrerende verktøy (bytte-mulighet)
- **Decay (ned-scoring)**: oppsigelser i målavdeling, funding >2 år siden uten oppfølging, kun grunnleggere på team-side

### Generell B2B

- **Trigger-events**: ny C-level-ansettelse, oppkjøp/fusjon, ny lokasjon, rebrand, ekspansjons-annonsering
- **Operasjonelt**: rask hiring (kapasitetspress) eller kostnadskutt-overskrifter
- **Eierskap**: PE-eid, oppkjøpsaktivitet, konsernendring (Brønnøysund/Companybook viser dette) — betyr mer enn funding-runder i tradisjonell B2B
- **Decay**: gjentatte konkurser, negativ vekst, beslutningstaker-rotasjon (3+ markedssjefer på 2 år)

### Lokal SMB

Nettside-status er hovedaksen for kvalifisering:

| Status | Definisjon | Utfall |
|--------|-----------|--------|
| **Ingen side** | Ingen troverdig standalone-nettside funnet | **Hot** for web/marketing-tjeneste |
| **Kun sosiale medier** | Bare Facebook/Instagram/booking-portal | **Hot** for web/marketing-tjeneste |
| **Svak side** | Utdatert, ødelagt, tynn, ikke mobilvennlig | **Warm** for refresh/rebuild |
| **Har side** | Troverdig, moderne side | **Cold** med mindre andre signaler (svak SEO, dårlig konvertering) |

Pluss: aktiv bedrift (ferske anmeldelser), nærhet til serviceområde, eier som svarer på anmeldelser (engasjert → mer sannsynlig å vurdere leverandør).

---

## Data-hygiene

Dårlig data koster mer enn ingen data — det brenner sender-rykte og selger-tillit.

- **Dedup**: på org.nr / domene (B2B/SaaS), på bedrift + adresse (lokal SMB). Org.nr fra Brønnøysund/Companybook er den reneste nøkkelen i Norge.
- **Verifiser før scoring som «Hot»** — Apollo/ZoomInfo er ofte 60–80 % treffsikre; nordiske data fra Companybook/Brønnøysund er ferskere, men kryssjekk uansett.
- **E-post-verifisering** før outreach, alltid. Ugyldige → egen bøtte, ikke sluttliste.
- **Kilde + dato per kontakt** — påkrevd for å forsvare lista (se compliance). Ikke en «nice to have».
- **Minimer lagring** — ikke behold prospekt-lister evig. GDPRs sletterett gjelder.
- **`Ikke funnet` i stedet for blanke felter** — synliggjør hva som mangler.

---

## Compliance — markedsføringsloven & GDPR

> Operasjonell veiledning, ikke juridisk rådgivning. For høyt volum eller programmer som treffer EU/EØS-borgere: kjør oppsettet forbi en personvernjurist.

Norden er strengere enn USA på dette. **Les før hver prospektering.**

### Markedsføringsloven (Norge)

- **§ 15** krever **forhåndssamtykke** for elektronisk markedsføring (e-post, SMS) til **forbrukere (B2C)**. Cold email til privatpersoner uten samtykke er ikke lov.
- **B2B-unntak**: utsendelse til bedrifter (juridiske personer) i deres næringsvirksomhet er tillatt — men e-post til en *navngitt person* i bedriften er fortsatt persondata under GDPR.
- **Reservasjonsregisteret** (Brønnøysund): respekter reservasjoner mot direkte markedsføring. Sjekk mot det for B2C/enkeltpersonforetak.
- Hver utsendelse må ha tydelig avsender-identifikasjon og en enkel måte å reservere seg / melde av.

### GDPR / personvern

- **Behandlingsgrunnlag for kald B2B-outreach: berettiget interesse** (legitimate interest) er det vanligste. Krever at:
  - Kontakten er i en forretningsrolle som sannsynligvis er interessert i tilbudet
  - Dataen er hentet fra en offentlig, forretnings-kontekst kilde (Companybook, Brønnøysund, bedriftens egen side, LinkedIn-firmaside)
  - Du tilbyr tydelig reservasjon/avmelding
  - Du kan dokumentere interesseavveiningen skriftlig
- **Dokumenter kilde + dato + grunnlag** for hver kontakt. Honorer innsyns- og sletteforespørsler (DSAR).
- **Inkluder personvern-notis + reservasjon** i første utsendelse.

### Hva som diskvalifiserer en liste

- **Bulk-scraping av LinkedIn** — eksplisitt ToS-brudd + GDPR-risiko. Permanent kontoutestengelse. Ikke gjør det.
- **Kjøpte lister uten kilde-proveniens** — du arver selgerens juridiske eksponering.
- **Gjettede «alle@domene»-adresser sendt uverifisert** — multipliserer både risiko og bounce.
- **Personlige e-poster** (privat Gmail/Outlook) høstet fra profiler — høy GDPR-risiko. Flagg eller ekskluder.
- **CAPTCHA-/innloggings-bypass** — signaliserer bot-atferd, bryter praktisk talt all ToS.

### Plattform-ToS kort

- **LinkedIn**: Sales Navigator som research-verktøy = greit. Scraping i skala = bannlyst. Manuelt: åpne profiler, les, noter.
- **Google Maps**: forbyr bulk-uttrekk og lagring av Place IDs i CRM. Bruk for å *finne* lokale bedrifter, hent så data fra bedriftens egen side.
- **Companybook / Proff**: bruk innenfor avtalt scope; ikke videreselg uttrekk.

---

## Sjekkliste (før du leverer)

- [ ] ICP definert som setning + pass/fail-sjekkliste
- [ ] Kandidatliste 2–3× sluttantall (kvalifisering kutter)
- [ ] Hvert «Hot»-lead har verifisert kontakt + minst én kilde-URL
- [ ] Hvert «Hot»-lead har et tydelig kjøpssignal (ikke bare ICP-fit)
- [ ] E-poster verifisert; ugyldige flyttet til egen bøtte
- [ ] Duplikater fjernet (org.nr/domene, eller bedrift+adresse)
- [ ] Konfidensnivå ærlig — «Høy» krever 2 uavhengige kilder
- [ ] Ingen leads fra forbudt scraping (LinkedIn i skala, Maps bulk)
- [ ] Kilde + dato + behandlingsgrunnlag logget per kontakt
- [ ] Companybook brukt som firmografi-ryggrad der relevant
- [ ] «Topp outreach-mål» (3–5) lagt ved med signal-begrunnelse
- [ ] Hand-off til `cold-email` klar (lista + kontekst per lead)

---

## Vanlige feil

1. **Starter discovery uten ICP** — du kvalifiserer feil ting mot vage kriterier.
2. **Behandler datakilder som fasit uten kryssjekk** — selv ferske nordiske data kan være utdaterte; verifiser før «Hot».
3. **Legger til kontakter uten e-post-verifisering** — bounce dreper sender-rykte raskt.
4. **«Hot» uten kjøpssignal** — ICP-fit alene er ikke nok; signalet gir timingen.
5. **Bulk-scraper LinkedIn/Maps** — kontoutestengelse + ToS-brudd. Browser kun som assistert research.
6. **Blander segmenter** — ikke bruk lokal-SMB-scoring (nettside-status) på en SaaS-prospekt.
7. **Ingen kilde-URLer** — uten kilde-loggen kan du ikke forsvare lista under GDPR-innsyn.
8. **Behandler generell B2B som SaaS** — funding-runder betyr mindre; eierskap/oppkjøp betyr mer. Companybook/Brønnøysund viser eierstrukturen.
9. **Jager et tall i stedet for kvalitet** — 25 verifiserte slår 250 søppel.

---

## Hand-off til cold-email

Når lista er ferdig og verifisert, er neste steg outreach. Lever til `cold-email` med:

- **Selve lista** (Hot/Warm prioritert) med kontakt + verifisert e-post
- **Per-lead kontekst**: kjøpssignalet (det `cold-email` personaliserer rundt — «gratulerer med [event]», «jeg la merke til [observasjon]»)
- **Segment** (SaaS/B2B/SMB) → styrer tone (Conversational er Norges default)
- **Behandlingsgrunnlag + kilde** per kontakt (så avmelding/personvern-notis blir riktig)

For lead scoring, lifecycle og CRM-handoff *etter* at svarene kommer inn, se `revops`.

---

## Relaterte Skills

- `cold-email` — Skriv outbound-sekvensen mot den kvalifiserte lista (det naturlige neste steget)
- `revops` — Lead scoring, MQL/SQL, pipeline og CRM-handoff etter prospektering
- `sales-enablement` — Battle cards og one-pagers brukt i selve outreach-en
- `competitor-alternatives` — Dypere research på enkeltkontoer og konkurranse-posisjonering
- `customer-principles` — Forstå hvorfor dagens kunder kjøper — informerer ICP-definisjonen
- `email-sequence` — Nurture-sekvenser for leads som ikke er klare ennå
- `competitor-profiling` — Dypere konkurrent-/account-dossier (firmografi via Companybook)
- `customer-research` — Skjerp ICP-en med ekte kundeinnsikt før du bygger lista
