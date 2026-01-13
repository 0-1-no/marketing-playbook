# Contributing to Marketing Playbook

Takk for at du vil bidra! Her er retningslinjene for hvordan du kan bidra til prosjektet.

## Release Workflow

### Automatisering

Repoet har to GitHub Actions som kjører automatisk:

1. **sync-marketplace.yml** - Synkroniserer versjon fra `plugin.json` til `marketplace.json`
2. **release.yml** - Oppretter git tags og GitHub Releases automatisk

### Manuell Release Checklist

Når du skal release en ny versjon:

1. **Oppdater CHANGELOG.md**
   ```markdown
   ## [X.Y.Z] - YYYY-MM-DD

   ### Added
   - Ny funksjonalitet

   ### Changed
   - Endringer i eksisterende funksjonalitet

   ### Fixed
   - Bugfixes
   ```

2. **Bump versjon i plugin.json**
   ```bash
   # Rediger .claude-plugin/plugin.json
   # Endre "version": "X.Y.Z"
   ```

3. **Marketplace.json oppdateres automatisk**
   - GitHub Action synkroniserer versjonen
   - Eller kjør manuelt:
   ```bash
   jq '.plugins[0].version = "X.Y.Z"' .claude-plugin/marketplace.json > tmp.json
   mv tmp.json .claude-plugin/marketplace.json
   ```

4. **Commit og push**
   ```bash
   git add -A
   git commit -m "release: vX.Y.Z - Kort beskrivelse"
   git push origin main
   ```

5. **Verifiser release**
   - Sjekk at GitHub Action opprettet tag og release
   - Test oppdatering: `claude plugin marketplace update 0-1-plugins`

## Pre-commit Hook

For lokal versjonskonsistens-validering:

```bash
# Aktiver pre-commit hook
git config core.hooksPath .githooks

# Test manuelt
./scripts/pre-commit-check.sh
```

## Semantic Versioning

Vi følger [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes i plugin API
- **MINOR** (0.X.0): Ny funksjonalitet, bakoverkompatibel
- **PATCH** (0.0.X): Bugfixes, dokumentasjonsendringer

## Mappestruktur

```
commands/       # Slash-kommandoer (/marketing-playbook:init, etc.)
skills/         # Auto-aktiverte kontekstuelle skills
scripts/        # Utility scripts
examples/       # Eksempel-outputs
```

## Retningslinjer

### Skills skal inneholde metodikk, ikke verdier

**Riktig:** "Consider fonts like Clash Display for headlines"
**Feil:** "Use font: Clash Display"

### Norsk for brukerinnhold, Engelsk for kode

- Kommandoer, beskrivelser, eksempler: Norsk
- Kodekommentarer, variabelnavn: Engelsk

### Test endringene dine

```bash
# I et prosjekt som bruker pluginen
/marketing-playbook
/marketing-playbook:check
```

## Spørsmål?

Opprett en issue på GitHub eller kontakt kontakt@0-1.no.
