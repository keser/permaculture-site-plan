# Map Asset Design System — Keys & Legends

Status: approved 2026-09-28 — all four decision forks resolved below (Forks 2 and 3 adopted at
their recommended defaults, per Andrew's go-ahead). Ready for the implementation plan.

## Goal

Systematize the map assets used across the PDC Pro Vision Figma file (design file
`aF9SVeTLwFN8PCEiU2OSBQ`) — area/polygon fills, line styles (with/without arrows), and site
markers (with/without labels) — plus the legend "key" components that document them, so that:

- Colors come from one shared, high-contrast palette instead of raw hex per shape.
- No meaning relies on color alone to be distinguished from another.
- Legend keys are built from one shared component instead of copy-pasted frames.

The Keys page (`222:2275`) is the existing inventory of every legend item created so far, across
the Base Map and all practice/lesson maps built from it.

## Current-state findings (audited 2026-09-28)

- **A "Map Overlay" variable collection already exists** — 9 named semantic colors (sage,
  cobalt, coral, gold, magenta, charcoal, slate, teal, violet), each aliased to a "Ramps"
  primitive collection (81 values — a full hue × shade scale). Properly scoped to
  `ALL_FILLS, STROKE_COLOR`. This is good infrastructure that's barely used.
- Of the map feature types sampled on the Base Map page (site boundary, driveway, water
  connection, electrical wiring, garden bed), only **electrical wiring** binds its stroke to a
  Map Overlay variable — everything else uses raw hardcoded RGB.
- **No paint styles or effect styles exist anywhere in the file** (0 of either).
- **Dash patterns are set freehand per vector, not from any shared set.** Site boundary uses
  `[8,8]`, garden bed uses `[4,8]`, and water-connection and electrical-wire both use the
  identical `[2,2]` — two different meanings sharing one line style, differentiated only by
  color. This is the concrete case for the "color alone" requirement to fix.
- **The Keys page has 7 separate hand-built legend frames** (Sector Compass Key ×2 duplicate
  copies + 1 real componentized version in the `Components` section, Circulation Element Key
  ×2, Contour Practice Key ×3, Site Water Flow Key, a generic "Key"). Only the Sector Compass
  Key's rows are real component instances — every other key is a copy-pasted frame tree.
- **That copy-paste pattern already caused a live bug:** in two different Contour Practice Key
  copies, all five soil-sample legend rows read "soil sample 02 location" regardless of number —
  the marker's number badge was updated correctly each time (it's a separate text layer), but the
  adjacent freeform label text was copy-pasted from row 2 and never retyped for rows 1, 3, 4, 5.
  A bound component would have made this class of error much harder to make.

## Scope inventory — meanings that need representing

Compiled from every legend row currently on the Keys page, plus Lesson 6 content already
committed in `pdc-pro-2026` that will need map representation soon.

**Area / polygon fills** (~9 distinct meanings so far): site/design boundary interior, water
catchment area, erosion risk area, invasive treatment zone, retained lawn corridor, de-lawned &
deep-mulched footprint, vegetable garden, chicken paddock, garden bed. Lesson 6 will add: the
compost/wood-processing cluster, drying/staging area, building-material pile.

**Line styles** (~12+ meanings across 4 families):
- *Water:* water flow, water flow on contour, water drainage, underground water line, effective
  vs. theoretical catchment divide, swale, roof/gutter runoff.
- *Circulation/access:* CAR foot path, monthly foot path, seasonal truck path, paved driveway.
- *Boundaries:* design site boundary, invasive-treatment-zone boundary.
- *Utilities:* electrical wire.
- *Directional/flow arrows:* water "enters / crosses / exits," mulch/material-flow arrows
  (Lesson 6 Goals Map notes).

**Markers** (~10+ meanings): water meter / connection point, grey water access, water spigot,
planned downspout, soil-sample sites (numbered 1–5), interim waste pit, long-term compost
system, ChipDrop drop-off site, understory plantings, pawpaw/mushroom site.

That's roughly 9 area meanings, 12+ line meanings, and 10+ marker meanings already documented,
before whatever Lessons 7–10 add. One color per individual meaning would blow well past the
existing 9-hue palette — see Fork 1 below.

## Decision forks — resolved 2026-09-28

**Fork 1 — hue-to-meaning binding: global (e.g. "blue always means water"), or local to each
map's own legend?** **Resolved: local, not global.** Andrew's call: color doesn't need a fixed
site-wide meaning — the same hue can mean "water" on one map and something unrelated on another,
as long as its use is consistent *within that map's own legend* and the legend documents what it
means there. This drops the rigid family→hue table from the earlier draft of this fork. What it
means for the system:
- The palette (below) is a shared, accessible, pre-vetted set of options — not a fixed
  meaning-to-color dictionary.
- Every map's Legend Row instances are the source of truth for what a color means *on that map*.
- The non-color-alone requirement still applies per map: within a single map/key, two different
  meanings must not share both the same color AND the same line style/marker shape — that's
  still checked at build time (see Accessibility checkpoints below), just scoped per-map instead
  of globally.
- **Base map context:** the base map itself (aerial/hand-drawn) stays greyscale — color is used
  only for the overlay lines/shapes/markers drawn on top of it, never for recoloring terrain or
  structures. Contrast checks only need to account for overlay-color-on-greyscale, not arbitrary
  photo colors.

**Palette expansion — resolved: add one new hue.** Andrew wants a true orange/yellow option,
which the existing 9 hues don't actually cover — `gold/500` (`#907600`) reads as dark olive/
mustard, not a bright yellow or orange, and `coral/500` (`#d2383b`) reads as red, not
pink-orange. Add one new hue, **amber**, as a full matching 9-step ramp (`amber/50` through
`amber/800`, same step scale as the existing 9 hues) in the `Ramps` collection, plus a
corresponding `Map Overlay` semantic variable scoped the same way (`ALL_FILLS, STROKE_COLOR`).
This brings the shared palette to 10 options. (If a distinct second hue — true yellow separate
from orange — turns out to be wanted once maps are actually built, that's a cheap follow-up, not
bundled into v1.)

**Fork 2 — line-style vocabulary — resolved at the recommended default.** Figma has no native
"stroke style" variable type, so this is a small documented enum plus reusable Line components,
not bindable tokens the way color is: Weight (thin / standard / heavy) × Dash (solid / fine-dash
/ coarse-dash) × Arrow (none / single / double) — a bounded set, not a combination invented ad
hoc per line as today.

**Fork 3 — marker shape vocabulary — resolved at the recommended default.** Numbered circle
(existing pattern, keep) for anything site/sequence-based — soil samples, future dig sites;
icon-in-circle (the water meter marker already does this — extend the pattern) for fixed
infrastructure/feature types. Shape + color + optional number, not color + number alone.

**Fork 4 — retrofit scope — resolved.** Build the full system now (palette, line styles,
markers, legend row component). Applying/retrofitting it onto existing Base Map geometry
(driveway, garden beds, site boundary, etc. — currently almost all raw hex) is an explicit,
separate, opt-in follow-up pass, not part of this build — it's a mechanical pass across finished
work with real risk of visual regressions, and deserves its own review rather than riding along.

## Proposed build order

Legend rows are built **last**, deliberately — the component needs to know what swatch types
(area / line / marker) it's rendering, so it depends on Phases 1–3 being locked first rather than
being redesigned per key as those pieces land.

**Phase 1 — Foundations (tokens)**
1. Add the `amber` hue: a full 9-step ramp in `Ramps` matching the existing step scale, plus its
   `Map Overlay` semantic variable (scoped `ALL_FILLS, STROKE_COLOR`).
2. Contrast-check all 10 `Map Overlay` hues against light/dark backgrounds and against each
   other at small-swatch size (legend chips read differently than full fills).
3. Define the line-style vocabulary (Fork 2) as a small set of reusable Line components — dash
   pattern and arrowheads aren't bindable variables, so this is componentized, not tokenized.

**Phase 2 — Marker components**
1. Build a "Site Marker" component: variants for Numbered / Icon / Dot, with a text/number
   override property.
2. Migrate soil-sample markers to it.
3. Build icon variants for recurring infrastructure marker types, using the existing water-meter
   marker as the pattern to extend.

**Phase 3 — Line components**
1. Build the Line component set per the Fork 2 vocabulary.
2. Document which semantic meaning maps to which line style + family hue — this table becomes
   the map's own internal style guide, and is what a legend row will reference.

**Phase 4 — Legend row component**
1. Build one "Legend Row" component: swatch slot (variant: Area / Line / Marker) + heading +
   optional body text.
2. Rebuild each of the 7 existing key frames from instances of it. This is also where the
   "soil sample 02 location" bug actually gets fixed — each row becomes a bound instance instead
   of independently-typed text.

**Phase 5 — Apply / optional retrofit**
1. Use the finished system for all new Lesson 6+ map additions.
2. (Separate go-ahead required) retrofit existing Base Map geometry to the new variables/styles.

## Accessibility checkpoints (threaded through every phase, not a separate pass)

- Contrast-check every palette hue (all 10, after the amber addition) against both light and
  dark backgrounds, and against every other hue, at the size it's actually used (small legend
  swatches on a greyscale base, not full fills) — this is a one-time check against the shared
  palette, done once in Phase 1, not repeated per map.
- Every meaning gets a non-color differentiator by default: dash pattern for lines, shape/icon
  for markers, and consider a subtle fill pattern for areas whose adjacent zones might render
  close in hue.
- Within any single map, never reuse an identical line style for two different meanings even if
  their colors differ — the water/electrical `[2,2]` collision found in this audit is the
  concrete case to fix first. Since color meaning is now local to each map (Fork 1), this check
  has to be re-run per map, not just once globally.

## Out of scope (this spec)

- Retrofitting all existing Base Map geometry to the new system (Fork 4 — deferred, separate
  go-ahead).
- The Sector Compass / wind-direction / water-flow diagram component family already in the
  Keys page's `Components` section — already properly componentized, not part of this pass.
- The "Chart Categorical" variable collection — serves the HTML dataviz reports (Lesson 1/3
  charts in `pdc-pro-2026`), unrelated to map keys.

## Next step

All decision forks are resolved — see `site-plan/plans/2026-09-28-map-design-system.md` for the
task/step implementation breakdown, following this repo's normal spec → plan split. Construction
in Figma starts once that plan is reviewed.
