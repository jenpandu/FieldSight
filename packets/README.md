# Incident packets (see packet-preparation.md)

Build these FIRST. Everything downstream depends on them.

| Folder | Profile | Expected |
|---|---|---|
| inc-0411 | P1 happy path | Recordable, Column J; recordability worker only; zero triggers |
| inc-0412 | P2 in-patient admission, energized switchgear | Recordable Column H near 180 days; 24h clock; all three workers |
| inc-0413 | P3 handwritten, illegible date of injury | Below 0.60 → human determination; no workers |
| inc-0414 | P4 observation-only overnight | Recordable, NOT reportable; reviewer rejection + re-dispatch; malformed artifact; contradicting photo |

Rules: real OSHA Form 301 (page 7 of corpus/pdf/FORM-301.pdf); no people, plates,
addresses or identifiable premises in photos; record every photo source in SOURCES.md;
the injection fixture lives in tests/fixtures/injection/, never here.

Open question for the instructor: P1 "no image artifact" vs "every packet needs a photo".
