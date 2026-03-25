---
description: Opprett kun JOURNEY.md for dette prosjektet. Kartlegger kundereisen fra awareness til loyalty.
disable-model-invocation: true
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Journey Init

Opprett `JOURNEY.md` for dette prosjektet gjennom fokusert intervju om kundereisen.

> **Forutsetning:** BRAND.md bør finnes. Kundereisen bygger på målgruppe-forståelse.
> Hvis BRAND.md mangler, kjør `/marketing-playbook:brand-init` først.

---

## Steg 1: Sjekk eksisterende

Sjekk om `marketing/JOURNEY.md` finnes.

Hvis filen finnes:
```
Eksisterende JOURNEY.md funnet.

Vil du:
1. Overskrive (start på nytt)
2. Oppdatere basert på eksisterende
3. Avbryt
```

Sjekk også om BRAND.md finnes:
```
[Hvis BRAND.md mangler:]

⚠️ BRAND.md ikke funnet.

For best resultat, kjør /marketing-playbook:brand-init først.
Kundereisen bygger på målgruppe-forståelse fra BRAND.md.

Vil du fortsette uten BRAND.md? (ikke anbefalt)
```

---

## Steg 2: Introduksjon

```
═══════════════════════════════════════════════════════════════
                       JOURNEY INIT
═══════════════════════════════════════════════════════════════

Jeg skal hjelpe deg med å kartlegge kundereisen fra første
kontakt til lojal kunde.

🗺️ Stages vi dekker:
   1. Awareness (ToFU) - Oppdagelse
   2. Consideration (MoFU) - Vurdering
   3. Evaluation (BoFU) - Evaluering
   4. Purchase - Kjøp
   5. Post-purchase - Etter kjøp
   6. Loyalty - Lojalitet

Dette tar ca. 10-15 minutter. Du kan svare "vet ikke ennå"
på stages som ikke er relevante ennå.

═══════════════════════════════════════════════════════════════
```

---

## Steg 3: Intervju

### Awareness (Oppdagelse)

**Spørsmål 1:** Hvordan oppdager folk dere typisk?
- Eksempler: "Google-søk, sosiale medier, word-of-mouth, annonser"
- Hvilke kanaler er viktigst?

**Spørsmål 2:** Hva er det første inntrykket du vil gi?
- Hva skal de tenke/føle når de først ser dere?

**Spørsmål 3:** Hva er den største barrieren for å få oppmerksomhet?
- Eksempel: "Mange konkurrenter", "Ukjent kategori", "Lav awareness"

### Consideration (Vurdering)

**Spørsmål 4:** Hva vurderer kundene før de bestemmer seg?
- Eksempel: "Pris, funksjoner, reviews, tillit"

**Spørsmål 5:** Hvilke spørsmål stiller de seg?
- Eksempel: "Er dette verdt prisen?", "Passer det for meg?"

**Spørsmål 6:** Hvilke bekymringer har de?
- Eksempel: "For dyrt", "Komplisert å bruke", "Usikker på kvalitet"

**Spørsmål 7:** Hvordan bygger dere tillit?
- Eksempel: "Reviews, case studies, gratis prøve, garantier"

### Purchase (Kjøp)

**Spørsmål 8:** Hvordan kjøper kundene? (kjøpsprosessen)
- Eksempel: "Online checkout", "Kontakt salg", "Freemium → betalt"

**Spørsmål 9:** Hva er de største friksjonspunktene i kjøpet?
- Eksempel: "Komplisert checkout", "Manglende betalingsalternativer"

### Post-purchase (Etter kjøp)

**Spørsmål 10:** Hva skjer rett etter kjøp?
- Eksempel: "Velkomst-e-post, onboarding, levering"

**Spørsmål 11:** Hva kan skape kjøpsanger?
- Eksempel: "Lang leveringstid", "Vanskelig å komme i gang"

**Spørsmål 12:** Hvordan sikrer dere en god opplevelse?
- Eksempel: "Rask support, god dokumentasjon, overraskelser"

### Loyalty (Lojalitet)

**Spørsmål 13:** Hva får kunder til å komme tilbake?
- Eksempel: "Nytt innhold, nye features, lojalitetsprogram"

**Spørsmål 14:** Har dere eller planlegger dere lojalitetsprogram/referrals?
- Beskriv kort hvis ja

**Spørsmål 15:** Hvordan holder dere kontakten med eksisterende kunder?
- Eksempel: "Nyhetsbrev, sosiale medier, community"

### Touchpoints

**Spørsmål 16:** Hvilke markedsføringskanaler bruker dere aktivt?
- Eksempler: "Facebook Ads, Google Ads, Instagram, LinkedIn, E-post, SEO"

**Spørsmål 17:** Hvilke kanaler vil dere satse mer på fremover?
- Prioriter gjerne

---

## Steg 4: Opprett JOURNEY.md

1. Opprett `marketing/JOURNEY.md`
2. Se `examples/JOURNEY.md` for struktur
3. Inkluder alle stages med:
   - Kundens perspektiv (mål, spørsmål, bekymringer)
   - Touchpoints
   - Våre mål for denne stage
   - Relevante psykologi-prinsipper
4. Marker stages som "[Under utvikling]" hvis bruker svarte "vet ikke"

---

## Steg 5: Bekreft og Neste Steg

```
═══════════════════════════════════════════════════════════════
                     ✅ JOURNEY.md OPPRETTET
═══════════════════════════════════════════════════════════════

📁 marketing/JOURNEY.md

Inneholder:
• Kundereise-oversikt (6 stages)
• Kundens perspektiv per stage
• Touchpoints og kanaler
• Psykologi-prinsipper

───────────────────────────────────────────────────────────────
STATUS
───────────────────────────────────────────────────────────────

[✅/❌] BRAND.md      - Merkevare
✅ JOURNEY.md     - Nettopp opprettet
[✅/❌] DISTRIBUTION.md - Kanaler og stack
[✅/❌] LEARNINGS.md    - Tester og innsikter

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

[Hvis DISTRIBUTION.md mangler:]
💡 Kjør /marketing-playbook:distribution-init for kanaler og stack

[Hvis BRAND.md mangler:]
💡 Kjør /marketing-playbook:brand-init for merkevare-grunnlag

═══════════════════════════════════════════════════════════════
```
