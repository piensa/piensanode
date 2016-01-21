{{ project_name|title }}
========================

You should write some docs, it's good for the soul.

Installation
------------

Create a new template based on the geonode example project.::
    
    $ django-admin.py startproject my_geonode --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst,yml
    $ sudo pip install -e my_geonode

.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.

Usage
-----

