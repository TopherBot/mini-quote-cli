# mini‑quote‑cli

A **tiny** command‑line tool that prints a random motivational quote.

## Features
- No external dependencies – pure Python 3.8+.
- Instant startup (< 10 ms) – ideal for shell aliases.
- Minimal footprint (≈ 2 KB source).
- Included GitHub Actions workflow that lints, tests, and sends a notification on failure.

## Install
```bash
# clone and install locally (editable for development)
git clone https://github.com/your‑username/mini-quote-cli.git
cd mini-quote-cli
pip install -e .
```

Or just drop the `mini_quote.py` file somewhere on your `$PATH` and run `python -m mini_quote`.

## Usage
```bash
$ mini-quote-cli
"Believe you can and you're halfway there." – Theodore Roosevelt
```

## Development
```bash
# run tests
pytest
# run the linter
ruff check .
```

## CI / Notifications
The repo contains a GitHub Actions workflow that:
1. Runs `ruff` for linting.
2. Executes unit tests with `pytest`.
3. Sends a Slack webhook notification on failure (configure `SLACK_WEBHOOK_URL` secret).

## License
MIT – see LICENSE file.
