# Contributing to GEOMETRIA_SOLAR

## Scope

This repository documents mathematical formalization of Maya and Inca solar geometry.
Contributions should connect to one or more of:

- Archaeoastronomy (azimuth, altitude, precessional calculations)
- Sacred geometry (pyramid proportions, wall angles, calendar structures)
- RAFAELIA synthetic framework (symbolic-mathematical integrations)
- Electromagnetic resonance models of ancient sites

## Branch Naming

| Type | Pattern | Example |
|---|---|---|
| Research | `research/<topic>` | `research/venus-pentagram` |
| Documentation | `docs/<topic>` | `docs/teotihuacan-alignment` |
| Fix | `fix/<issue>` | `fix/azimuth-formula` |

## Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
research: add Stonehenge solstice azimuth comparison
docs: expand INCAS precessional correction section
fix: correct Venus synodic period calculation
```

## Adding a Document

1. Place Markdown documents in `docs/`
2. Use ASCII filename (no spaces, no special characters): `kebab-case.md`
3. Include a YAML front matter block:

```yaml
---
title: "Document Title"
domain: "archaeoastronomy | sacred-geometry | rafaelia"
date: YYYY-MM-DD
author: "Your Name"
---
```

## Mathematical Notation

- Use LaTeX in Markdown code blocks (`$$...$$` for display, `$...$` for inline)
- Define all variables at first use
- Cite sources for constants (e.g., Venus synodic period = 583.92 d)

## Pull Request Process

1. Create a branch from `main` with the naming convention above
2. Add/update documents in `docs/`
3. Update the document table in `README.md`
4. Submit PR using the PR template

## Code of Conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Academic integrity applies:
cite all prior work and astronomical data sources.
