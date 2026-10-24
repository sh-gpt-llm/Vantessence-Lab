# Session 02 — Dictionaries

**Level:** L1 — Foundations  
**Status:** In progress

## Core idea

A dictionary maps unique, hashable keys to values. It is useful when a value
should be retrieved by a meaningful name or identifier rather than by its
position.

```python
service = {
    "id": "payments-api",
    "owner": "Commerce",
    "tier": 1,
}

service["status"] = "healthy"
owner = service["owner"]
review_date = service.get("last_review", "not recorded")
```

- `record[key]` raises `KeyError` when the key is missing; use it for required
  fields.
- `record.get(key, default)` returns the default when the key is absent; use it
  when absence is expected.
- Keys are unique. Assigning an existing key updates its value.
- A dictionary's insertion order is preserved in modern Python, but use keys
  for lookup rather than relying on positions.

## Enterprise application

Service inventory records, feature flags, configuration, and API payloads often
have named fields. Validate required fields at system boundaries; a fallback
value should not hide missing data that is actually required.

## Exercises

Complete the self-checking exercises in
[`../exercises/session-02-dictionaries.py`](../exercises/session-02-dictionaries.py).
Explain why each assertion passes, and identify which fields are required or
optional in the service example.

## Evidence

- [ ] Complete and pass all three exercise checks.
- [ ] Answer the five-question quiz in the session guide.
- [ ] Explain the difference between direct indexing and `.get()` without
  notes.
