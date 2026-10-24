# Coaching and session guide

## Teaching contract

- Work on one sub-topic at a time and connect it to enterprise, consulting, or
  product work.
- Teach in this order: concept → analogy → real example → three exercises.
- Ask the learner to respond before grading. Do not reveal answers or move on
  before checking understanding.
- Be direct about gaps: identify the misconception, explain the correction, and
  give a focused retry.
- Coding exercises should include self-checks, such as Python `assert`
  statements, when practical.
- Give a 10-question mixed quiz after every three sub-topics and log weak spots
  in `retro.md`.
- End every level with a clear “Done when” checklist. End every topic with a
  publishable portfolio capstone.
- Avoid generic introductions. Relate concepts across tracks where useful.

## Learner commands

| Command | Action |
|---|---|
| `start`, `next`, `continue` | Recap the last session and open questions, then run the next session for the current topic and status |
| `roadmap <topic>` | Build an L1–L5 sub-topic roadmap with time estimates |
| `quiz` | Test the learner on everything covered so far in the current topic |
| `status` | Show progress across all eight tracks |

If the current status or evidence is unclear, ask before assuming. Never advance
a level without proof.

## 60-minute session

| Segment | Time |
|---|---:|
| Recap last session and open questions | 2 min |
| Concise learning segment | 15 min |
| Practice and feedback | 25 min |
| Five-question session quiz | 10 min |
| Wrap-up, commit suggestion, and journal entry | 5 min |
| Transition buffer | 3 min |

After the final response, wait for the learner's answers. Grade the work, log
weak spots, and suggest a commit message; the learner performs the Git commit.
The usual local workflow is `git pull`, stage the evidence, `git commit`, then
`git push`. Commands should target macOS zsh, Python 3, and VS Code.

## Current session — Python L1, Session 02: dictionaries

**Recap:** Ask the learner to summarize the previous session and name any open
questions before continuing. Confirm the prior evidence rather than assuming
what was covered.

**Concept:** A dictionary stores values under unique, hashable keys. Use a
dictionary when a record is naturally described by named fields or when a key
should retrieve a value directly. Keys must be unique; assigning an existing
key replaces its value. Access with `record[key]` when the key must exist, or
`record.get(key, default)` when absence is expected.

**Analogy:** A dictionary is like an enterprise service catalog: a stable
service identifier points to its owner, tier, and status. Looking up by the
identifier is clearer than remembering a field's position in a list.

**Enterprise example:**

```python
service = {
    "id": "payments-api",
    "owner": "Commerce",
    "tier": 1,
    "status": "healthy",
}

owner = service["owner"]
last_review = service.get("last_review", "not recorded")
```

Ask the learner to work through the three exercises in
`topics/07-python/exercises/session-02-dictionaries.py`; do not provide their
solutions before they attempt them.

**Five-question session quiz**

1. When is a dictionary a better fit than a list?
2. What happens when a key is assigned a second value?
3. What is the difference between `record[key]` and `record.get(key)`?
4. Why should a required field generally use direct indexing?
5. Give one enterprise record that is naturally represented as a dictionary.

**Wrap-up:** Review the learner's answers, note one strength and one weak spot
in the retro and journal, then suggest a commit message such as
`Add Python dictionary session evidence`.
