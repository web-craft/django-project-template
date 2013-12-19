{% comment %}

# Django Project Template #

This template provides sane defaults for new Django projects based on established best practices. To use django-project-template run the following command:

    django-admin.py startproject --template=https://github.com/web-craft/django-project-template/archive/master.zip --extension=py,md PROJECT_NAME

Note: Django version 1.6 or greater is required.


## Features ##

By default, this template includes:

A set of basic templates built from HTML5 Boilerplate 4.0.1 and Twitter Bootstrap 3.0.

Compressing JS and CSS:

- [Django Compressor](https://github.com/jezdez/django_compressor/)

Migrations:

- [South](http://south.aeracode.org/)

## References ##

This template adopts some ideas from the following projects:

- [Django 1.4 Base Template](https://github.com/xenith/django-base-template/)
- [Django Project Template](https://bitbucket.org/carljm/django-project-template/)
- [Django Layout](https://github.com/lincolnloop/django-layout/)

The text following this comment block will become the README.md of the new project.

-----------------------------------------
{% endcomment %}

# {{ project_name|title }} Project #


## About ##

Describe your project here.


## Prerequisites ##

- Python >= 2.7


## Installation ##

To bootstrap the project:

    cd path/to/{{ project_name }}
    install system-wide dependencies from requirements-system.txt
    $ python bootstrap.py
    $ . env/bin/activate
    $ cp {{ project_name }}/settings/local.py.template {{project_name }}/settings/local.py
    adjust your local settings, such as database adapter in settings/local.py
    $ python manage.py syncdb
    $ python manage.py runserver
