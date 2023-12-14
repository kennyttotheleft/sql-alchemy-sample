#!/usr/bin/env bash

set -Eeo pipefail

create_user_sql="CREATE USER "${DB_REPLICATION_USER}" WITH REPLICATION ENCRYPTED PASSWORD '"${DB_REPLICATION_PASSWORD}"';"
create_slot_sql="SELECT * FROM pg_create_physical_replication_slot('"${DB_REPLICATION_SLOT}"');"
psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" -c "${create_user_sql}"
psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" -c "${create_slot_sql}"
