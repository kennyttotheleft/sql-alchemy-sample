#!/usr/bin/env bash

set -Eeo pipefail

while ! psql -h ${DB_PRIMARY_HOST} -p $((${DB_PRIMARY_PORT} + 0)) -U ${DB_REPLICATION_USER} -d ${POSTGRES_DB} -c "select 'primary database server is running';" 2>&1 ; do \
	sleep 1s ; \
done

# load backup from primary instance
pg_basebackup -h ${DB_PRIMARY_HOST} -p $((${DB_PRIMARY_PORT} + 0)) -D ${PGDATA} -S ${DB_REPLICATION_SLOT} --progress -X stream -U ${DB_REPLICATION_USER} -Fp -R || :

# start postgres
bash /usr/local/bin/docker-entrypoint.sh -c 'config_file=/etc/postgresql/postgresql.conf' -c 'hba_file=/etc/postgresql/pg_hba.conf'
