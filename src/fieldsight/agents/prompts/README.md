# Prompts

One markdown file per participant, loaded at runtime. Version them in git; a prompt
change is a PR like any code change and should be followed by a deterministic eval run.

Each prompt must state: the goal, the corpus scope (doc_types/section paths), the tools
available, that thresholds come only from `evaluate_rule`, the citation format
(sources by index), and that the output is descriptive — never a legal conclusion.
