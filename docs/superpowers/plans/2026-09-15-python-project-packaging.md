# Python Project Packaging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the FastAPI application installable from a standard `pyproject.toml` after cloning.

**Architecture:** Use PEP 621 project metadata with setuptools as the build backend. Install the existing `main.py` as a single module and document an editable pip installation workflow without changing application behavior.

**Tech Stack:** Python 3.10+, setuptools, pip, FastAPI, Uvicorn

## Global Constraints

- Require Python 3.10 or newer.
- Declare `fastapi` and `uvicorn[standard]` as runtime dependencies.
- Do not change the existing API application or endpoints.
- Do not introduce a lockfile, Docker, or a package-directory refactor.

---

### Task 1: Add installable project metadata and document setup

**Files:**
- Create: `pyproject.toml`
- Modify: `.gitignore`
- Modify: `README.md`

**Interfaces:**
- Consumes: the existing `main.py` module and `app` FastAPI object
- Produces: a pip-installable project and documented clone-to-run commands

- [x] **Step 1: Confirm the manifest does not exist**

Run: `test ! -e pyproject.toml`
Expected: exit code 0.

- [x] **Step 2: Add standard project metadata**

Create `pyproject.toml` with:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "fastapi-intro"
version = "0.1.0"
description = "A simple REST API for learning FastAPI."
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "fastapi",
    "uvicorn[standard]",
]

[tool.setuptools]
py-modules = ["main"]
```

- [x] **Step 3: Update the installation documentation**

Replace the manual dependency command in `README.md` with:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

Explain that dependencies come from `pyproject.toml`, and retain the existing `uvicorn main:app --reload` command and endpoint URLs.

Add `*.egg-info/` to `.gitignore` so editable-install metadata remains untracked.

- [x] **Step 4: Validate metadata and editable installation**

Run: `.venv/bin/python -c 'import tomllib; tomllib.load(open("pyproject.toml", "rb"))'`
Expected: exit code 0.

Run: `.venv/bin/python -m pip install -e . --no-deps`
Expected: exit code 0 and an editable `fastapi-intro` installation.

- [x] **Step 5: Verify application behavior**

Run: `.venv/bin/python -c 'from fastapi import FastAPI; from main import app; assert isinstance(app, FastAPI)'`
Expected: exit code 0.

Start `.venv/bin/uvicorn main:app --host 127.0.0.1 --port 8765`, request `http://127.0.0.1:8765/`, and stop the server.
Expected response: `{"x":3,"y":4}`.

- [x] **Step 6: Review the final changes**

Run: `git diff --check && git diff -- pyproject.toml README.md`
Expected: no whitespace errors, with only the planned manifest and README changes.
