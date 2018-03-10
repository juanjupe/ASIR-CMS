# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.contrib import messages
from django.dispatch import receiver
from django.dispatch import Signal
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from aldryn_newsblog.cms_appconfig import NewsBlogConfig, NewsBlogConfigTranslation
import cms.api
from cms.models.pagemodel import Page
from django.utils import translation


import cms.api
import aldryn_newsblog
from django.conf import settings
from django_auth_ldap.backend import LDAPBackend


@receiver([user_logged_in,user_logged_out],sender=User)

def log_user_activity (sender,**kwargs):
	signal=kwargs.get('signal',None)
	user = kwargs.get ('prueba', None)
	request = kwargs.get ('request', None)
	session_key = request.session.session_key
	if signal==user_logged_in:
		action = "login"
		messages.info(request,"¡Bienvenido!")
		create_page( 'prueba' )
	elif signal==user_logged_out:
		action = "logout"
		messages.info (request,'¡Adios!')
		
		
def create_page(prueba):
#creacion de a pagina para el suaurio
		ldap = LDAPBackend()
		user = ldap.populate_user( 'prueba' )
		user.first_name
		#Creamos la configuración para su blog
		user_conf = NewsBlogConfig(app_title=user.first_name,namespace=user.first_name)
		user_conf.save_base()
		user_conf.save()
		#buscar la ubicacion de donde va a colgar su pagina de blog
		parent_page = Page.objects.filter(title_set__title='BLOG_ALUMNOS')[1]
		#creamos la pagina del blog del usuario
		page = cms.api.create_page(user.first_name,'content.html',
						'en',apphook="NewsBlogApp",apphook_namespace=user_conf.namespace,
						parent=parent_page,published=True,in_navigation=True)
		#placeholder de su página
		placeholder = page.placeholders.get_or_create(slot='feature')
		placeholder = page.placeholders.get(slot='feature')
		#ahora añadimos los plugins de estilo
		plugin1 = cms.api.add_plugin(placeholder, 'StylePlugin','en')
		plugin2 = cms.api.add_plugin(placeholder, 'StylePlugin','en')
		plugin2.class_name="feature-content"
		plugin2.save()
		plugin1.save()
		#le damos todo los permisos al usuario
		user_assigned = cms.api.assign_user_to_page (page,user,grant_all=True)
		page.publish ( language = 'en' )
		page_user = cms.api.create_page_user(user, user, can_add_page=True, 
							can_change_page=True, can_delete_page=True, can_recover_page=False, 
							can_add_pageuser=False, can_change_pageuser=False, can_delete_pageuser=False, 
							can_add_pagepermission=False, can_change_pagepermission=False, 
							can_delete_pagepermission=False, grant_all=False)
