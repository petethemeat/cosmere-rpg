# cosmere-rpg

Application to manage characters in the Cosmere RPG tabletop game system.

This repository provides a small Python package and CLI to get started managing Cosmere RPG characters.

## Quick start

Create a virtual environment and install dev dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Run the example CLI:

```bash
python -m cosmere_rpg.main hello --name "Vin"
```

Run tests:

```bash
pytest -q
```

Development tips
- Use Black and isort (configured via `requirements-dev.txt`) to format code.

CI
The repository includes a GitHub Actions workflow to run tests on push and pull requests.
# cosmere-rpg
Application to manage characters in the Cosmere RPG tabletop game system
