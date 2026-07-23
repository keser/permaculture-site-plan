# Permaculture Master Site Plan

## Program

Long-term master site plan for a 0.43-acre residential property (Portland,
OR area). Independent of any course — full authority over scope, timeline,
and content rests with the owner and his father, the two long-term
stakeholders. Public during development, not just after completion, to
demonstrate the technical design approach as it's built.

## Privacy

Public docs in this repo never state the exact street address or parcel
number. Refer to the property generically (e.g. "a 0.43-acre residential
lot in the Portland area"). Exact parcel records (survey PDFs, parcel
spreadsheets) are never stored in this repo — they live in a private
iCloud folder instead.

## Workspace Structure

```
permaculture-site-plan/
├── CLAUDE.md
├── site-plan/              — narrative docs, zones, sector analysis, phase plans
│   ├── maps/                — exported Figma base maps
│   └── sketches/             — iPad Pro scans, dated, raw
└── inspiration/             — public inbox: links, images, references
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
`~/Code/keser/permaculture-certification-summer-26`. Course material stays
there; anything from the course genuinely useful long-term gets
deliberately rewritten into this repo in the owner's own words, rather
than living here natively.

## Task Tracking

Plain GitHub Issues, no Projects board. Labels: `task`, `dad-request`,
`professor-feedback`.

## Deferred Decisions

- Publishing engine for GitHub Pages (Jekyll vs. Docusaurus) — not yet
  chosen. The folder structure above is generator-agnostic.
