# Evaluation (§14)

- `golden/` — one YAML per case, written by the teammate who did NOT tune retrieval,
  before seeing retrieval output.
- `runner.py` runs cases through the full harness; `judge.py` is the groundedness
  evaluator on the separate judge deployment; `attribution.py` and `refusal_metrics.py`
  are deterministic.
- CI runs the deterministic tier on every build. Judge evaluators run on demand, twice:
  the day the workflow first produces a cited answer, and at the end. Commit both runs
  in `results/` and analyse the delta in docs/evaluation-report.md.
