## UV install
```angular2html
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```angular2html
source $HOME/.local/bin/env
```

```
uv python install 3.14
```

```
uv python pin 3.14
```

```angular2html
uv --version
```

```angular2html
uv add <name_of_library>
```

```angular2html
uv sync
```

```angular2html
uv sync --no-dev
```

```angular2html
uv run python main.py
```



## Alembic
```initial command
alembic init alembic
```


## Flask
```run flask app
flask --app src.myapp.run run
```


## Docker

### Launch DataBase
```
docker compose up -d db
```

### Clear docker dependecies
```
docker compose down --volumes
```

### Migrations
```
docker compose run --rm --build migrations
```