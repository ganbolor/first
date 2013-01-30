find . -name "*.pyc" -exec rm -rf {} \;

django-admin.py runserver --adminmedia=/tmp/new-admin-style/

django-admin.py runserver --noreload

python manage.py dumpdata --format=json devices > apps/devices/fixtures/initial_data.json
python manage.py dumpdata --format=json basics > apps/basics/fixtures/initial_data.json
python manage.py dumpdata --format=json owners > initial_owner_data.json

python manage.py dumpdata --format=json customers > apps/customers/fixtures/initial_data.json









