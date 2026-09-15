# FastAPI Intro

Learning FastAPI by building a simple REST API with Python.

This project serves as a hands-on introduction to backend development with FastAPI, covering API routing, request and response handling, data validation, and basic RESTful API concepts.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ylx959/fastapi-intro.git
cd fastapi-intro
```

### 2. Create a virtual environment

Create a virtual environment for project dependencies:

```bash
python3 -m venv .venv
```

This only needs to be done once.

### 3. Activate the virtual environment

Every time you open a new terminal session for this project, activate the virtual environment:

```bash
source .venv/bin/activate
```

After activation, your terminal should look similar to:

```text
(.venv) user@machine fastapi-intro %
```

To leave the virtual environment:

```bash
deactivate
```
### 4. Install dependencies


If setting up the project from scratch:

```bash

python -m pip install fastapi "uvicorn[standard]"

```

## Running the Server

Start the FastAPI development server:

```bash

uvicorn main:app --reload
```

The API will be available locally at:

```text

http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation:

```text

Swagger UI: http://127.0.0.1:8000/docs

ReDoc:      http://127.0.0.1:8000/redoc
```


## Notes

This repository is intended as a learning project rather than a production-ready application. It will evolve as I explore more FastAPI and backend development concepts.