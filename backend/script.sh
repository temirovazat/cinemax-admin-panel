#!/bin/bash
postgres_ready() {
    $(which curl) http://${POSTGRES_HOST:-localhost}:${POSTGRES_PORT:-5432}/ 2>&1 | grep '52'
}

until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available.'

python manage.py migrate --fake movies 0001_initial
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput
gunicorn core.wsgi:application --bind 0:8000