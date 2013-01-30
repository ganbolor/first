#!/bin/sh

python manage.py sqldiff customers
python manage.py sqldiff operators
python manage.py sqldiff engeeners
python manage.py sqldiff basics
python manage.py sqldiff owners
python manage.py sqldiff devices
python manage.py sqldiff errors
