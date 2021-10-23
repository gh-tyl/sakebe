#!/bin/sh
source ./.env
echo "Start dropdb. Type password."
dropdb --if-exists $DB_NAME --host=$DB_HOST_LOCAL --port=$DB_PORT --username=$DB_USER --password
echo "Start dropuser. Type password."
dropuser --if-exists $DB_USER --password
echo "Start createuser. Type password."
createuser --createdb $DB_USER --password
echo "Start createdb. Type password."
createdb --encoding=$DB_ENCODING --lc-collate=$DB_LC_COLLATE --lc-ctype=$DB_LC_CTYPE --template=template0 $DB_NAME --host=$DB_HOST_LOCAL --port=$DB_PORT --username=$DB_USER --password