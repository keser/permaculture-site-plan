# Permaculture Master Site Plan

## Program

Long-term master site plan for a 0.43-acre residential property (Portland,
CT area). Independent of any course — full authority over scope, timeline,
and content rests with the owner and his father, the two long-term
stakeholders. Public during development, not just after completion, to
demonstrate the technical design approach as it's built.

## Privacy

**Location is public.** As of 2026-09-11, the exact street address, lot number, and
coordinates may appear in this repo. Rationale (Andrew): this information is publicly
discoverable regardless of what this repo does, and the goal is a reusable pattern for
generating this kind of detailed site-profile reporting for other project sites in the
future — which would need the same location data every time. (Prior to 2026-09-11, this
repo kept location generic; older commits/docs reflecting that are not being scrubbed.)

Exact parcel records (survey PDFs, parcel spreadsheets) still aren't stored in this repo
— they live in a private iCloud folder instead. This is a media-size/repo-hygiene
convention, not a privacy one.

**People are still private.** Neighbors and other private third parties are never named
— refer to them by role ("the adjacent neighbors"), not by name. (The two long-term
stakeholders, the owner and his father, are referred to by role throughout.)

## Workspace Structure

```
permaculture-site-plan/
├── CLAUDE.md
├── site-plan/              — narrative docs, zones, sector analysis, phase plans
│   ├── site-profile.md      — climate, solar, sector & passive-design reference
│   ├── progress-log.md      — dated log of on-site work & plan revisions
│   ├── specs/                — brainstorming-skill design docs (see below)
│   ├── maps/                — exported Figma base maps
│   └── sketches/             — iPad Pro scans, dated, raw
├── inspiration/             — public inbox: links, images, references
└── docs/                    — the published site-profile microsite (GitHub Pages root)
```

## Media Convention

Original/raw media (photos, scans, video) lives in a private iCloud folder,
never git-tracked here. When a doc needs to reference a specific original
file, link to it by absolute path. Only finished, ready-to-use assets
(Figma exports, cleaned-up sketches) get copied into `site-plan/maps/` or
`site-plan/sketches/` and tracked in git.

## Related Repo

Course deliverables for the concurrent Permaculture Design Certificate
program live in a separate private repo:
`~/Code/keser/pdc-pro-2026`. Course material stays
there; anything from the course genuinely useful long-term gets
deliberately rewritten into this repo in the owner's own words, rather
than living here natively.

## Task Tracking Convention (site-plan/ phase files)

Tasks are ID-prefixed by phase and can depend across phases freely (e.g. `D3` depends on
`R17`): `R`=Reset, `C`=Construction, `S`=Establish Systems, `D`=Diversity/Habitat, `DS`=Design
(ongoing, not sequential — runs alongside whatever phase is active).

`project-plan-overview.md` is a **denormalized rollup** of every task row in the five phase
files — it exists for at-a-glance viewing, not as a separate source of truth. When editing a
task's status/description/dependencies, update it in both the phase file *and* the overview
file, or they will drift out of sync.

## Progress Log

`site-plan/progress-log.md` is the dated narrative — what happened on the property and
why the plan changed, newest entry first. Phase files carry current task status; the log
carries history and the rationale behind dependency/scope revisions. Add an entry
whenever on-site work happens or a task's dependencies change.

## Issue Tracking

Plain GitHub Issues, no Projects board. Labels: `task`, `dad-request`,
`professor-feedback`.

## Deferred Decisions

- ~~Publishing engine for GitHub Pages (Jekyll vs. Docusaurus) — not yet chosen.~~
  Decided 2026-09-11: **plain static HTML, no generator.** Matches the `.viz-root`
  report pattern already in use (self-contained, no build step). GitHub Pages serves
  `docs/` on `main` as-is — note this means design-doc specs live at `site-plan/specs/`
  instead of the brainstorming skill's usual `docs/superpowers/specs/`, since `docs/`
  is now the public site root, not a docs folder.

## Site Microsite (`docs/`)

Published at GitHub Pages once enabled. Plain HTML/CSS, no build step, no JS framework —
matches the `.viz-root` visual pattern from `pdc-pro-2026`'s data-viz reports (light/dark
aware, inline SVG, self-contained). `docs/.nojekyll` disables GitHub's default Jekyll
processing so files are served exactly as committed.

**Shared nav/footer, without a generator:** `docs/_partials/nav.html` and
`.../footer.html` are the source of truth. Every page has
`<!-- NAV:START -->…<!-- NAV:END -->` / `<!-- FOOTER:START -->…<!-- FOOTER:END -->`
marker comments; a local script (`scripts/build-nav.py`) stamps the current partial
content between those markers. **Re-run it after editing nav/footer or adding a page,
before committing** — there's no build step at serve time, so a stale stamp stays stale
until someone runs the script again.

Content is ported from `pdc-pro-2026`'s report HTML (see that repo's own CLAUDE.md for
the source list) — copied and adapted here, not symlinked or generated, per the
Related Repo convention below. Built in phases; see `site-plan/specs/` for each phase's
design doc.
