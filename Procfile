web: cd forecast-admin/forecast && ./manage.py migrate && ./manage.py collectstatic --noinput && ./manage.py createcachetable && waitress-serve --port=$PORT forecast.wsgi:application
