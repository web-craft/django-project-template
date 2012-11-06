# {{ project_name|title }} Project #

## About ##

Describe your project here.

## Prerequisites ##

- Python >= 2.5

## Installation ##
- go to project directory
- install system-wide dependencies from requirements-system.txt
- $ python bootstrap.py
- $ cp {{ project_name }}/settings/local.py.template {{project_name }}/settings/local.py
- adjust your local settings, such as database adapter in settings/local.py
- $ python manage.py syncdb
- $ python manage.py runserver

Fill out with installation instructions specific for your project.
