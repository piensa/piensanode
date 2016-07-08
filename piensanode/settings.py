# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import geonode
from geonode.settings import *
#
# General Django development settings
#

SITENAME = 'piensanode'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
GEONODE_ROOT = os.path.abspath(os.path.abspath(geonode.__file__))
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "piensanode.wsgi.application"


# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'piensanode.urls'

INSTALLED_APPS = (
    'haystack',
    'hypermap',
    'hypermap.aggregator',
    'hypermap.search',
    'hypermap.dynasty',
    'maploom_registry',
) + INSTALLED_APPS

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672/'

CELERYBEAT_SCHEDULE = {
    'Check All Services': {
        'task': 'hypermap.aggregator.tasks.check_all_services',
        'schedule': timedelta(minutes=15)
    },
}

# haystack settings
ES_ENGINE = 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine'
ES_URL = 'http://127.0.0.1:9200/'

SEARCH_URL = ES_URL
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': ES_ENGINE,
        'URL': ES_URL,
        'INDEX_NAME': 'hypermap',
    },
}

# amqp settings
BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@127.0.0.1:5672/')
CELERY_ALWAYS_EAGER = False
NOTIFICATION_QUEUE_ALL = not CELERY_ALWAYS_EAGER
NOTIFICATION_LOCK_LOCATION = LOCAL_ROOT

SEARCH_TYPE = 'elasticsearch'
SEARCH_URL = ES_URL
SEARCH_ENABLED = True
