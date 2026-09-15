# Python Project Packaging Design

## Goal

Make the FastAPI project installable after cloning through a standard Python
project manifest, equivalent in purpose to a Node.js `package.json`.

## Scope

- Add a root-level `pyproject.toml`.
- Declare project metadata, the supported Python version, and runtime
  dependencies for FastAPI and Uvicorn.
- Update `README.md` so setup uses `python -m pip install -e .`.
- Keep the existing application code and server command unchanged.

## Packaging approach

Use the standard PEP 621 `[project]` table in `pyproject.toml`. Use setuptools
as the build backend because it is broadly supported by pip and requires no
additional package manager. Since this repository currently contains a single
`main.py` module rather than a distributable package directory, explicitly
configure setuptools to install that module and avoid accidental package
discovery.

The runtime dependencies are:

- `fastapi`
- `uvicorn[standard]`

The manifest will require Python 3.10 or newer, which is compatible with the
application's current syntax and supported FastAPI releases without imposing a
needlessly new interpreter requirement.

## User workflow

After cloning, a user will run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
uvicorn main:app --reload
```

The existing `/`, `/docs`, and `/redoc` endpoints remain unchanged.

## Error handling

Dependency installation failures remain visible through pip's normal error
output. No wrapper script or custom installer is introduced.

## Verification

- Validate that `pyproject.toml` parses successfully with Python's `tomllib`.
- Build project metadata through pip using the existing virtual environment.
- Import `main.app` and confirm it is a FastAPI application.
- Start Uvicorn briefly and request the root endpoint, confirming the existing
  JSON response.

## Out of scope

- Lockfiles and exact dependency pinning.
- Docker configuration.
- Refactoring `main.py` into a package directory.
- Production server configuration.
