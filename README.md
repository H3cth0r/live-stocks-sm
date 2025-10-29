# live-stocks-sm

## Features
- Async API
- Real Time upda
- Technical Indicators: RSI SMA
- Database Storage: PostgreSQL with SQLAlchemy to store stock information.
- Caching: Redis used to cache indicator results for daster response times.
- Reproducible environment: Using Nixos and python environments.
- Containerized services: Postgres and Redis.

## Requirements
- Nix
- Docker
- Git

## Run
### Turn Nixos On
```
nix-shell
```

### Turn Redis and Postgres Up
```
docker-compose up -d
```

### Run FastAPI app
```
uvicorn app.main:app --reload
```

## Test
```
python test_app.py
```

to test websockets:
```
websocat ws://127.0.0.1:8000/api/ws/AAPL
```


## Turn off
```
docker compose down -v
```


## Docs
```
http://127.0.0.1:8000/docs
```
