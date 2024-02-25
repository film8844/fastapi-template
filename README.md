# Fast API template with database

## Installation

### Local run

1. Run database

```bash
docker compose --file docker-compose.database.yaml up -d
```

2. install lib.

```bash
pip install -r requirements/prod.txt
```

3. Run

```bash
bash run_dev.sh
```

server will run on 127.0.0.1:8000
`127.0.0.1:8000/docs` for documents
