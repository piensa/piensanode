{{ project_name|title }}
========================

You should write some docs, it's good for the soul.

Installation
------------

Install the native dependencies for your platform.

Create a local virtual environment for your project and install Django into it.::

    $ mkvirtualenv my_geonode
    $ pip install Django

Create a new template based on the geonode example project.::
    
    $ django-admin.py startproject my_geonode --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst,yml -n Vagrantfile

.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.

Install the dependencies for your geonode project::

    $ pip install -e my_geonode

Install and Configure GeoServer

.. note:: At this point, you should put your project under version control using Git or similar.

If you are using Vagrant, setup your vagrant environment::

    $ cd my_geonode
    $ vagrant up

Usage
-----

Setup the database::

    $ python manage.py syncdb

.. note:: You will be asked to provide credentials for the superuser account.

Start the development server::

    $ python manage.py runserver
