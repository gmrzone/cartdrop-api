#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE cartdrop_dev;
    ALTER ROLE afzal SET client_encoding TO 'utf8';
    ALTER ROLE afzal SET default_transaction_isolation TO 'read committed';
    ALTER ROLE afzal SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE cartdrop_dev TO afzal;
EOSQL