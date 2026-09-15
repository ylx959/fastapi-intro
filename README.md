# FastAPI Intro

Learning FastAPI by building a simple REST API with Python.

This project serves as a hands-on introduction to backend development with FastAPI, covering API routing, request and response handling, data validation, and basic RESTful API concepts.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Getting Started

```bash
git clone https://github.com/ylx959/fastapi-intro.git
cd fastapi-intro
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
./dev.sh                  # http://127.0.0.1:8000
```

The venv and the install only need to run once; re-run the install whenever
`requirements.txt` changes. `./dev.sh` uses `.venv/bin/uvicorn` directly, so
there is no need to `source .venv/bin/activate`.

Interactive docs: `/docs` (Swagger UI), `/redoc` (ReDoc).

## Notes

This repository is intended as a learning project rather than a production-ready application. It will evolve as I explore more FastAPI and backend development concepts.
