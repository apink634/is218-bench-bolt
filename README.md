# Bench & Bolt · Repair Inquiry Queue

IS218-003 Group Customer Studio. A shop coordinator records bike-repair inquiries and moves them through
honest statuses. **Simulated customer — all people and data are fictional.**

- Project record / plan: [SPEC.md](SPEC.md)
- Customer agreements: [customer-kit/CUSTOMER-NOTES.md](customer-kit/CUSTOMER-NOTES.md)
- Customer kit: start your agent with *“Read customer-kit/AGENTS.md. Start customer mode…”*

## Setup

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Checks

```sh
ruff format --check . && ruff check .   # format + lint
mypy                                     # types
bandit -q -r src                         # security
pytest                                   # unit + integration
```

Current stage: **Review 1 · Plan** — core rules + unit tests only; web app and store come in the first slice.
