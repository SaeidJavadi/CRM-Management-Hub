# PostgreSQL Docker Commands

This guide shows basic commands to access, backup, and restore your PostgreSQL database running in Docker.

## Access PostgreSQL

```bash
# Enter the PostgreSQL container
docker exec -it docker_db bash

# Access PostgreSQL with user and database
psql -U $POSTGRES_USER -d $POSTGRES_DB
```

## Backup Database

```bash
# Backup the database from inside the container
docker exec -it docker_db backup
```

## Restore Database

```bash
# Restore the database from a backup file
docker exec -it docker_db restore <fileName>
```

> Replace `<fileName>` with the name of your backup file.
