#!/bin/sh

# Usage: cf push --no-route -c "bash ./init-db.sh"
# echo "------ Create database tables ------"
# cd python manage.py migrate --noinput
 
# echo "------ create default admin user ------"
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@forecast.local', 'Passw0rd')" | python manage.py shell
python manage.py migrate
python manage.py loaddata forecast/fixtures/prod_user.json
waitress-serve --port=$VCAP_APP_PORT forecast.wsgi:application