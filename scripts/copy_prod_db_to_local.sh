#!/usr/bin/env bash

scripts=$(cd $(dirname $0);pwd)
root=$(cd $(dirname $0);cd ..;pwd)

server=localhost
dt=$(date '+%Y-%m-%d-%H_%M')
filename="bapug_prod_db_${dt}.sql"

shared_path=$(grep BACKUP_ROOT $root/.env | sed 's/^.*=//')
backup_path=$(eval echo ${shared_path})
echo "Backup Path: ${backup_path}"
full_filename=${backup_path}/${filename}
echo "${full_filename}"

#ls -al ${backup_path}
# Can can do this all in one command!
ssh bapug.root 'su - postgres -c "pg_dump django"' > ${full_filename}


