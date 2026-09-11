# Site Profile Microsite — Progress Journal Design

Status: approved, pending implementation.

## Goal

Add a "Journal" section to the live microsite: a curated, public-facing narrative of
real on-the-ground work at the site, sourced from `site-plan/progress-log.md`. This is a
new content type for the site — every existing page is a topic-based data report or
reference (climate, water, species, zones); the journal is the first chronological,
narrative page. It's also the first page whose content will keep growing after this
initial build, via an ongoing authoring workflow (see below).

## Why this and not a mechanical port

Every prior phase (V1–V3b) either ported an existing HTML report or transcribed a
markdown deliverable close to verbatim. `progress-log.md` cannot be ported that way: it's
written as Andrew's own internal project-management notes — dense, referencing task
codes (R1, S2, D4, C1–C5...) that only resolve against the phase files, full of
plan-revision bookkeeping and self-corrections a public reader never needs. This phase is
new content *authoring*, with the source material as raw input rather than a document to
transcribe.

## Privacy: presence-date handling (new category, not the existing address policy)

`progress-log.md` includes forward-looking on-site date windows (e.g. "Looking ahead:
on-site 2026-09-12 through 2026-09-18"). Publishing exact future presence/absence windows
for a real, named address is a physical-security signal distinct from the address/location
policy already in this repo's CLAUDE.md (that policy concerns discoverability of the
location, not occupancy timing).

**Rule:** forward-looking date ranges that indicate when the property will be occupied or
empty are never published. Past work-dates ("the weekend of September 5") are fine — they
describe what already happened, not a future window. A "what's next" beat may appear in an
entry, but only as dateless task description ("Next visit: trim and shred the staged
branches..."), never tied to a specific date range.

## Curation rules (source → journal entry)

Applies to both the initial backfill and every future entry:

1. **Strip task codes and phase-file cross-references** (R1, S2, D4, C1–C5, etc.) — internal
   tracking, meaningless to a public reader.
2. **Drop forward-dated plans**, per the privacy rule above. A dateless "what's next" is
   fine; a dated window is not.
3. **Drop internal-only bookkeeping**: plan-revision notes ("R4 dependency trimmed from..."),
   open questions to self, and self-corrections about earlier *internal* notes (e.g. "R3's
   description said Norway pines, actual species is Norway spruce" — a reader never saw the
   wrong version, so there's nothing to correct for them). If a correction changes a fact
   the reader would otherwise be told, fold the corrected fact in silently; don't narrate
   the correction.
4. **Prose rewrite is permitted and expected** — unlike the verbatim policy for ported
   course content, this is curated authoring: reorganize by topic, smooth into readable
   paragraphs, cut redundancy across the source's own drafts-and-corrections structure.
   This is the one page on the site where paraphrasing is the intended mode, not a
   violation.
5. **Voice stays first-person** ("I cut...", "I learned...") — matches every other
   first-person page on the site (Zones & Design). This does not change.
6. **Same site-wide privacy rules apply**: no neighbor/private-third-party names. (None
   currently appear in `progress-log.md`, but future entries might.)
7. Exact address/coordinates continue to be fine per the existing site-wide policy — this
   spec only adds the presence-date rule above, it doesn't relax or restate the rest.

## Page structure

- New file: `docs/journal.html`. Single scrolling page, `.viz-root` pattern (same
  light/dark CSS system, `body { margin: 0; }`, no framework) — matching every
  hand-authored page.
- **Reverse-chronological** — newest entry first, matching the source log's own
  convention.
- Each dated entry is a real `<h2 class="section-head">` (the semantic-heading pattern
  V3b introduced), labeled by date (e.g. "Weekend of September 5, 2026"), not by the
  source's internal date-grouping mechanics.
- Text-only for this phase — no charts, no images. (Andrew confirmed no photos are ready
  yet; a future entry can add a `.thumb`/image block using the same pattern as the Water
  hub's optional thumbnails, if photos become available. Not built now — YAGNI.)
- No category tags/badges for v1 (e.g. "Clearing", "Propagation") — plain prose is enough
  at this content volume. Revisit if the page grows long enough that scanning becomes
  hard.

## Initial backfill scope

Curate the full current content of `progress-log.md` (both the 2026-09-03 and 2026-09-11
source entries) into journal entries now, rather than launching empty. Two entries in the
initial build:

- **September 2026, early month** (from the 2026-09-03 source entry): Phase 1 clearing
  starting, poison ivy treatment over summer, chipper acquisition, hot compost system
  plan, grape relocation and cedar/Rose-of-Sharon propagation plans.
- **Weekend of September 5** (from the 2026-09-11 source entry, which itself documents
  that weekend plus a same-day follow-up): chipper operational, the dry-wood lesson,
  tree/branch clearing, the second poison-ivy round, the Zone 5 compost-pile
  identification, the cedar/lilac pruning (correcting the plan that said air-layering
  would happen), the raised beds, and the passionflower/blueberry propagation ideas.

Both entries get written out in full during planning (per this project's no-placeholder
plan convention) — the plan will contain the actual curated prose, not a description of
what to write.

## Site integration

- **Nav**: add "Journal" to `docs/_partials/nav.html`, appended last (same convention as
  every prior addition — Species Inventory, then Zones & Design, each landed at the end).
- **Home**: add one new card to `docs/index.html`'s "Available now" grid — a
  direct-content card (no sub-hub), same visual weight as Climate/Wind/Flood & Hazard.
- **Footer/boilerplate**: standard `.viz-root` CSS, `body { margin: 0; }`,
  `<!-- NAV:START/END -->` / `<!-- FOOTER:START/END -->` marker regions stamped via
  `python3 scripts/build_nav.py` like every other page.

## Relative links

Same bar as every prior phase: `grep -rn 'href="/' docs/` and `grep -rn 'src="/' docs/`
must both return nothing after this change.

## Ongoing authoring workflow (behavior change, not a one-time build step)

Once this ships: whenever Andrew gives a real progress update (as narrated prose, the way
he has been), the assistant updates `progress-log.md`/phase files as it already does, *and*
drafts the corresponding curated journal entry in the same pass, applying the curation
rules above — appended to `docs/journal.html` in the working tree. This is a standing
behavior change, and the implementation plan's final task documents it in this repo's
CLAUDE.md (alongside the existing "Generated Reports" / hand-authored-page conventions),
so it isn't lost the next time this project picks back up in a fresh session.

Publishing still goes through the repo's existing confirm-before-push convention — drafting
the entry is automatic, but committing/pushing to `main` is not silently included.

## Out of scope (explicitly deferred)

- Photos/images in journal entries (no photos ready yet).
- Category tags/badges.
- Any hub/sub-page structure (single page is sufficient at current volume).
- The three previously-deferred site-consistency findings (hub-design unification, Home
  depth-signaling, semantic headings on the *ported* pages) — unrelated to this phase.
