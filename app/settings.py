# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-bootstrap3',
    'aldryn-events',
    'aldryn-newsblog',
    'djangocms-file',
    'djangocms-googlemap',
    'djangocms-history',
    'djangocms-link',
    'djangocms-picture',
    'djangocms-snippet',
    'djangocms-style',
    'djangocms-text-ckeditor',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    # add your project specific apps here
    'django_extensions',
    'social_django',
    'asir',
    
])
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '265323253041-f0leuou5med7qcgovg7tvqjt5f29e52u.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '28Jr8fIlaiPvUP4O5UuuqFcQ'

CMS_TEMPLATES = (
	('content.html','content'),
	('feature.html','feature-content'),
	('fullwidth.html','fullwidth'),

)


import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType


AUTHENTICATION_BACKENDS = (
	'django_auth_ldap.backend.LDAPBackend',
	'django.contrib.auth.backends.ModelBackend',
	'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
)
AUTH_LDAP_SERVER_URI = 'ldap://172.17.0.1:389'

AUTH_LDAP_BIND_DN =  "cn=admin,dc=asir,dc=com"
AUTH_LDAP_BIND_PASSWORD = "admin"
AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s,ou=users,dc=asir,dc=com"

AUTH_LDAP_CONNECTION_OPTIONS = {
ldap.OPT_REFERRALS: 0
}
AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "email": "mail", "username": "sn"}
