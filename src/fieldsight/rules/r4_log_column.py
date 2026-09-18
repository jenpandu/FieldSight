# FILE: src/fieldsight/rules/r4_log_column.py
#
# PURPOSE
# R4 — Form 300 column G/H/I/J with day counting and the 180-day cap.
#
# REQUIREMENT REFS: §6 R4; CFR-1904 §1904.7(b)(3), §1904.29(b)(3); FORM-301 column definitions
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Inputs: date_of_injury, died, return_to_work_date (optional), days_restricted.
#   - Day zero is the injury date; counting starts the day after (1904.7(b)(3)).
#   - Cap the count at 180 calendar days.
#   - Most severe wins: G > H > I > J.
#   - Record days_away_counted in inputs so trace shows the arithmetic.
#
# MUST / MUST NOT
#   - TEAM DECISION: whether the return-to-work day is counted. Decide, write it here and
#     in the decisions table, then write the test first.
#   - P1 has no return-to-work date → Column J without inventing a date.
#
# TESTED BY
#   tests/unit/test_r4_log_column.py — 179/180/181 days, P4's 1-day case, no return date,
#   missing injury date.
