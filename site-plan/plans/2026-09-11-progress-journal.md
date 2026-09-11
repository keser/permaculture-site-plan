# Progress Journal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new "Journal" page to the live microsite — a curated, narrative, reverse-chronological
record of real on-site work, backfilled from the current content of `site-plan/progress-log.md`, wired
into the site's nav and Home page, with the ongoing authoring workflow documented for future sessions.

**Architecture:** One new static page (`docs/journal.html`) following the site's existing `.viz-root`
hand-authored pattern (same as `index.html`, `zones-design.html`, `microclimates.html`). No hub/sub-page
split — a single scrolling page is sufficient at current content volume. Two dated `.entry` blocks for
this initial build, newest first. Standard nav/footer partial stamping via the existing `build_nav.py`.

**Tech Stack:** Plain static HTML/CSS, no JS, no build tool beyond the repo's existing
`scripts/build_nav.py` / `scripts/port_report.py`.

**Spec:** `site-plan/specs/2026-09-11-progress-journal-design.md`

## Global Constraints

- No root-absolute links: `grep -rn 'href="/' docs/` and `grep -rn 'src="/' docs/` must both return
  nothing after every task.
- `body { margin: 0; }` required in every hand-authored page's `<style>` block.
- Nav/footer content lives only in `docs/_partials/nav.html` / `footer.html`; every page's
  `<!-- NAV:START/END -->` and `<!-- FOOTER:START/END -->` regions are stamped via
  `python3 scripts/build_nav.py`, never hand-edited directly.
- Voice stays first-person throughout the journal entries ("I cut...", "I learned...").
- No neighbor / private-third-party names anywhere (none needed for this content, but the rule
  applies to all future entries too).
- **Presence-date rule (new, this phase):** never publish a forward-looking date range that signals
  when the property will be occupied or empty. Past work-dates ("the weekend of September 5") are
  fine. A dateless "what's next" beat is fine. A dated future window is not.
- Title/H1 convention for hand-authored pages: `<title>{Name} — Lot #86</title>`, `<h1>{Name}</h1>`
  (matches `water.html`, `zones-design.html`, `microclimates.html`, etc. — established by the
  2026-09-11 title-consistency fix).
- Exact address/coordinates are permitted per the site's existing public-location policy — unaffected
  by the presence-date rule above.

---

## File Structure

- **Create:** `docs/journal.html` — the new page. Full `.viz-root` CSS block, empty
  `<!-- NAV:START/END -->` and `<!-- FOOTER:START/END -->` marker regions (stamped by Task 2), two
  `.entry` blocks with curated prose.
- **Modify:** `docs/_partials/nav.html` — add the Journal link.
- **Modify:** `docs/index.html` — add one new `.nav-card` to the "Available now" grid.
- **Modify:** `CLAUDE.md` (project root, `permaculture-site-plan`) — document the ongoing
  journal-authoring workflow so it survives a fresh session.

No changes to `scripts/build_nav.py`, `scripts/port_report.py`, or their tests — this plan only
consumes the existing stamping tool, it doesn't change it.

---

### Task 1: Author `docs/journal.html`

**Files:**
- Create: `docs/journal.html`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: a complete, valid HTML page with empty NAV/FOOTER marker regions, ready for Task 2 to
  stamp. The page must render correctly (light + dark) even before stamping — the marker regions
  being empty just means no nav bar / footer show up yet, which Task 2 fixes.

- [ ] **Step 1: Write the file**

Create `docs/journal.html` with exactly this content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Journal — Lot #86</title>
<style>
  .viz-root {
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7; --text-primary: #0b0b0b;
    --text-secondary: #52514e; --text-muted: #898781; --border: rgba(11,11,11,0.10);
    --grid: #e1e0d9;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) .viz-root {
      color-scheme: dark;
      --surface-1: #1a1a19; --page: #0d0d0d; --text-primary: #ffffff;
      --text-secondary: #c3c2b7; --text-muted: #898781; --border: rgba(255,255,255,0.10);
      --grid: #2c2c2a;
    }
  }
  :root[data-theme="dark"] .viz-root {
    color-scheme: dark;
    --surface-1: #1a1a19; --page: #0d0d0d; --text-primary: #ffffff;
    --text-secondary: #c3c2b7; --text-muted: #898781; --border: rgba(255,255,255,0.10);
    --grid: #2c2c2a;
  }
  * { box-sizing: border-box; }
  body { margin: 0; }
  .viz-root {
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: var(--page); color: var(--text-primary);
    padding: 32px 20px 60px;
  }
  .wrap { max-width: 760px; margin: 0 auto; }
  h1 { font-size: 24px; font-weight: 600; margin: 0 0 6px; }
  .subhead { color: var(--text-secondary); font-size: 14px; line-height: 1.5; margin: 0 0 28px; }
  h2.section-head { font-size: 13px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: var(--text-muted); margin: 0 0 12px; }
  .entry { background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px; padding: 20px 22px 22px; margin-bottom: 20px; }
  .entry p { font-size: 14px; color: var(--text-secondary); line-height: 1.65; margin: 0 0 14px; }
  .entry p:last-child { margin-bottom: 0; }
</style>
</head>
<body>
<!-- NAV:START -->
<!-- NAV:END -->
<div class="viz-root"><div class="wrap">
  <h1>Journal</h1>
  <p class="subhead">A running account of real work at the site — what's been cleared, treated, planted, and learned, written up after each visit. Newest entries first.</p>

  <h2 class="section-head">Weekend of September 5, 2026</h2>
  <div class="entry">
    <p>I got the wood chipper up and running this weekend and put it through its first real chipping pass. First lesson: the wood needs to be as dry as possible — any green leaf material bogs the shredder down. So instead of feeding branches in fresh, I've started piling everything I cut to dry out before it goes through.</p>
    <p>Most of the cutting was in Zone 5: I cleared the dead branches off the mulberry, took down four of the maples growing under it, and cut some — though not all — of the low branches on the Norway spruces. There's still an afternoon's worth of spruce trimming left to finish.</p>
    <p>I also ran a second round of poison ivy treatment: triclopyr on a patch on the north side of the mulberry, plus a deep spray along the Zone 3 fence line and the corner west of the chicken coop. Most of that foliage should be dying back by my next visit, opening that ground up for more clearing.</p>
    <p>While I was out there I finally figured out what the Zone 5 compost system actually is — there's already a large brush pile sitting there from past clearing. The plan now: finish spraying it for poison ivy (done), shred the dried-out top layer, compact the rest down into one starter pile, and enclose the whole thing in a 3-bin staked-fence structure to keep it organized.</p>
    <p>I'd planned to air-layer the white cedar and the Rose of Sharon this visit, to propagate them before either one comes out, but that didn't happen. Instead I pruned the cedar — the cuttings are set aside to chip once they're dry — and pruned all but one of the lilac bushes, getting them ready to air-layer next. Propagating the lilacs will give me stock for the back-fence perennial garden ("grandma's lilacs") instead of buying new plants.</p>
    <p>I didn't get to moving the two grape vines yet, but I got a good look at them — they're likely Catawba, and notably they regrew from being cut back to nothing, so they're vigorous stock once I relocate them. I also picked up and assembled four round metal raised beds (2×2×1 ft), meant for grapes, hops, and other vines — probably where the grapes end up, though I haven't committed to that yet. I'm also thinking about rooting some cuttings from the existing blueberry to expand that planting, and there's a passion fruit vine growing on my balcony that might be worth putting in the ground here — I need to check whether it's the same species as the purple passionflower already on my wishlist.</p>
    <p>Next visit: trim the staged maple and spruce branches and logs down to shredder-ready size — no Y-branching, no thick stumps — then shred them. Spread the resulting mulch in the Zone 3 vegetable garden, starting at the chicken coop and working outward, over a base layer of flattened cardboard. One fencing note for that area: the fenced garden doubles as the dogs' free-roam space, so whenever that fence comes down, the chicken coop will need its own standalone fenced perimeter — it doesn't need to reuse the old dog kennel as the back side of it. And I'll keep working on clearing Zones 4 and 5.</p>
    <p>Honest note on pace: clearing Zones 4 and 5 is taking longer than I expected. This visit's time mostly went to cutting the maples, the second poison-ivy round, and staging debris for the shredder rather than to clearing itself. Zone 5 stays the priority, since that's where the compost system is going, but I'm adjusting my expectations — it'll keep competing with tree work and shredder prep for a while yet.</p>
  </div>

  <h2 class="section-head">Early September 2026</h2>
  <div class="entry">
    <p>Phase 1 — clearing and reset — is underway. I treated the majority of the property's poison ivy over the summer, and Zone 5 clearing starts this week: dead branches, brush, and a few small trees coming out.</p>
    <p>I'm picking up a new wood chipper/mulcher, and I'll start chipping dry brush in Zones 4 and 5 as soon as it arrives, cutting and chipping the low-hanging branches in the same pass. The overgrown fence line is also getting cleared and mulched.</p>
    <p>For the weekend ahead, my plan is to clear a spot in the NW corner and build out a hot compost system there — any woody debris that can't go through the chipper will get composted there or buried in the raised beds. I'm also planning to dig up and relocate the two existing grape vines (location still to be determined), and to start air-layering the white cedar and the Rose of Sharon so I have propagated stock before either one comes out — the layers need a full growing season to root before I can sever them.</p>
  </div>
</div></div>
<!-- FOOTER:START -->
<!-- FOOTER:END -->
</body>
</html>
```

- [ ] **Step 2: Verify the file is well-formed**

Run: `python3 -c "import xml.dom.minidom, re, pathlib; s = pathlib.Path('docs/journal.html').read_text(); print('OK - has NAV and FOOTER markers:', '<!-- NAV:START -->' in s and '<!-- FOOTER:START -->' in s)"`

Expected: `OK - has NAV and FOOTER markers: True`

- [ ] **Step 3: Commit**

```bash
git add docs/journal.html
git commit -m "Add Journal page with backfilled entries from progress-log.md"
```

---

### Task 2: Site integration — nav link, Home card, stamp partials

**Files:**
- Modify: `docs/_partials/nav.html`
- Modify: `docs/index.html`
- Run (no file created): `scripts/build_nav.py`

**Interfaces:**
- Consumes: `docs/journal.html` from Task 1 (must exist with empty NAV/FOOTER markers before running
  `build_nav.py`, or the stamp has nothing to fill in — Task 1 must be complete first).
- Produces: every page in `docs/*.html`, including `journal.html`, with the updated nav bar (new
  Journal link) stamped into its `<!-- NAV:START/END -->` region, and `journal.html` additionally
  getting the footer stamped into its `<!-- FOOTER:START/END -->` region.

- [ ] **Step 1: Add the nav link**

In `docs/_partials/nav.html`, change:

```html
    <a href="zones-design.html">Zones &amp; Design</a>
  </div>
```

to:

```html
    <a href="zones-design.html">Zones &amp; Design</a>
    <a href="journal.html">Journal</a>
  </div>
```

- [ ] **Step 2: Add the Home page card**

In `docs/index.html`, change:

```html
      <a class="nav-card" href="zones-design.html">
        <h3>Zones &amp; Design</h3>
        <p>Current permaculture zones, microclimates, and the design brainstorm for their future.</p>
      </a>
    </div>
```

to:

```html
      <a class="nav-card" href="zones-design.html">
        <h3>Zones &amp; Design</h3>
        <p>Current permaculture zones, microclimates, and the design brainstorm for their future.</p>
      </a>
      <a class="nav-card" href="journal.html">
        <h3>Journal</h3>
        <p>A running account of real work at the site, written up after each visit.</p>
      </a>
    </div>
```

- [ ] **Step 3: Stamp nav/footer across every page**

Run: `python3 scripts/build_nav.py`

Expected: output lists every `docs/*.html` file as updated (nav changed on all of them because
`nav.html` changed), including `docs/journal.html` gaining both its nav bar and its footer for the
first time.

- [ ] **Step 4: Verify no root-absolute links were introduced**

Run: `grep -rn 'href="/' docs/ ; grep -rn 'src="/' docs/`

Expected: no output (empty) from both.

- [ ] **Step 5: Verify journal.html now has a real nav and footer**

Run: `grep -c 'site-nav\|site-footer' docs/journal.html`

Expected: a number greater than 0 (both the nav and footer partial content, including their inline
`<style>` blocks and markup, are now present).

- [ ] **Step 6: Run the existing script test suite (regression check)**

Run: `python3 -m pytest scripts/tests/ -q`

Expected: `16 passed` (same count as before this plan — this task doesn't touch the scripts, this just
confirms nothing broke).

- [ ] **Step 7: Commit**

```bash
git add docs/_partials/nav.html docs/index.html docs/journal.html
git commit -m "Wire Journal into site nav and Home page"
```

---

### Task 3: Document the ongoing journal-authoring workflow

**Files:**
- Modify: `CLAUDE.md` (project root: `permaculture-site-plan/CLAUDE.md`)

**Interfaces:**
- Consumes: nothing from other tasks (can technically run independently, but ordered last since it's
  documentation of the feature the first two tasks just built).
- Produces: a durable, session-surviving record of the workflow change, in the file this project
  already uses for exactly this purpose (see its existing "Generated Reports" section).

- [ ] **Step 1: Locate the insertion point**

Read `CLAUDE.md` and find its "Generated Reports" section (documents the `.viz-root` HTML report
pattern, lists each existing report and what it's built from). Add a new subsection immediately after
the existing bullet list in that section, before the next top-level heading.

- [ ] **Step 2: Add the documentation**

Insert this content (adjust the exact heading level to match whatever level the existing bullets in
that section sit under — match the surrounding document's heading structure rather than assuming
a specific `###`/`##`):

```markdown
### Progress Journal

`docs/journal.html` is a different kind of page from the reports above: a curated, first-person,
reverse-chronological narrative of real on-site work, rather than a topic-based data report. It's
sourced from `site-plan/progress-log.md`, but it's a deliberate rewrite, not a port — task codes
(R1, S2, D4, etc.), phase-file cross-references, and internal plan-revision bookkeeping never appear
in it; the source's own corrections-to-itself aren't narrated, their corrected facts are just folded
in silently.

**Ongoing workflow:** whenever Andrew gives a real progress update, update `progress-log.md` /
phase files as usual, *and* draft the corresponding curated journal entry in the same pass, appended
to `docs/journal.html`. Apply the curation rules above every time — this isn't a one-time backfill.

**Privacy rule specific to this page:** never publish a forward-looking date range that signals when
the property will be occupied or empty (e.g. "on-site Sept 12–18"). Past work-dates are fine. A
dateless "what's next" beat is fine. This is separate from — and doesn't relax — the site's existing
address/location policy above.

Drafting a new entry into the working tree doesn't skip this repo's normal confirm-before-push
convention — committing and pushing the update still gets confirmed with Andrew first, same as any
other change.
```

- [ ] **Step 3: Verify the section reads correctly in context**

Run: `grep -n "Progress Journal" CLAUDE.md`

Expected: one match, at the heading you just inserted.

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "Document the progress-journal authoring workflow in CLAUDE.md"
```

---

## Final Verification (after all 3 tasks)

- [ ] `grep -rn 'href="/' docs/` → empty
- [ ] `grep -rn 'src="/' docs/` → empty
- [ ] `python3 -m pytest scripts/tests/ -q` → `16 passed`
- [ ] `python3 scripts/build_nav.py` → `0 file(s) updated` (idempotent — Task 2 already stamped
  everything, so a second run should be a no-op)
- [ ] Manually confirm in a browser (or via `curl` after push) that `journal.html` renders with a
  nav bar, footer, and both entries in both light and dark mode, and that Home's new card and the
  nav's new "Journal" link both work.
