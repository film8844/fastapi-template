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

3. Setup
   fix `.env.example`

```env
# app config
TITLE=
DESCRIPTION=
VERSION=
AUTH_SECRET=

# database config
DB_HOST=127.0.0.1
DB_PORT=5432
DB_TABLE=
DB_USER=
DB_PASSWORD=
```

and coppy it.

```bash
cp .env.example .env.dev
cp .env.example .env
```

4. Run

```bash
bash run_dev.sh
```

server will run on 127.0.0.1:8000
`127.0.0.1:8000/docs` for documents
