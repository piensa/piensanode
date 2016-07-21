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
from datetime import timedelta
#
# General Django development settings
#

SITENAME = 'piensanode'
BASE_URL = os.getenv('BASE_URL', '192.168.56.151')
BASE_PORT = os.getenv('PORT', '8500')

SITE_URL = 'http://%s:%s' % (BASE_URL, BASE_PORT)

ALLOWED_HOSTS = [BASE_URL, ]


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
    'hypermap',
    'hypermap.aggregator',
    'hypermap.search',
    'hypermap.dynasty',
    'hypermap.search_api',    
    'maploom_registry',
    'rest_framework',
) + INSTALLED_APPS

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672/'

CELERYBEAT_SCHEDULE = {
    'Check All Services': {
        'task': 'hypermap.aggregator.tasks.check_all_services',
        'schedule': timedelta(minutes=1500)
    },
}

# amqp settings
BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@127.0.0.1:5672/')
CELERY_ALWAYS_EAGER = False
CELERY_DEFAULT_EXCHANGE = 'piensanode'
NOTIFICATION_QUEUE_ALL = not CELERY_ALWAYS_EAGER
NOTIFICATION_LOCK_LOCATION = LOCAL_ROOT

SEARCH_TYPE = 'elasticsearch'
SEARCH_URL = 'http://127.0.0.1:9200/'
SEARCH_ENABLED = True
SKIP_CELERY_TASK = False

DEBUG_SERVICES = False
DEBUG_LAYERS_NUMBER = False

MAPPROXY_CONFIG = os.path.join(MEDIA_ROOT, 'mapproxy_config')

# pycsw settings
REGISTRY_PYCSW = {
    'server': {
        # 'home': '.',
        'url': '%s/search/csw' % SITE_URL.rstrip('/'),
        'encoding': 'UTF-8',
        'language': LANGUAGE_CODE,
        'maxrecords': '10',
        'pretty_print': 'true',
        # 'domainquerytype': 'range',
        'domaincounts': 'true',
        'profiles': 'apiso'
    },
    'manager': {
        # authentication/authorization is handled by Django
        'transactions': 'true',
        'allowed_ips': '*',
        # 'csw_harvest_pagesize': '10',
    },
    'repository': {
        'source': 'HHypermap',
        'mappings': os.path.join(os.path.dirname(__file__), '..', 'search', 'pycsw_local_mappings.py')
    },
}

REGISTRY_PYCSW['server']['url'] = SITE_URL.rstrip('/') + '/registry/search/csw'

REGISTRY_PYCSW['metadata:main'] = {
    'identification_title': 'Registry Catalogue',
    'identification_abstract': 'Registry, a Harvard Hypermap project, is an application that manages ' \
    'OWS, Esri REST, and other types of map service harvesting, and maintains uptime statistics for ' \
    'services and layers.',
    'identification_keywords': 'sdi,catalogue,discovery,metadata,registry,HHypermap',
    'identification_keywords_type': 'theme',
    'identification_fees': 'None',
    'identification_accessconstraints': 'None',
    'provider_name': 'Organization Name',
    'provider_url': SITE_URL,
    'contact_name': 'Lastname, Firstname',
    'contact_position': 'Position Title',
    'contact_address': 'Mailing Address',
    'contact_city': 'City',
    'contact_stateorprovince': 'Administrative Area',
    'contact_postalcode': 'Zip or Postal Code',
    'contact_country': 'Country',
    'contact_phone': '+xx-xxx-xxx-xxxx',
    'contact_fax': '+xx-xxx-xxx-xxxx',
    'contact_email': 'Email Address',
    'contact_url': 'Contact URL',
    'contact_hours': 'Hours of Service',
    'contact_instructions': 'During hours of service. Off on weekends.',
    'contact_role': 'Point of Contact'
}
TAGGIT_CASE_INSENSITIVE = True
