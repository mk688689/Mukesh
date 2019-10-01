from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
	path('', home_view, name="home"),
	path('about/', about_view, name="about"),
	path('branding-company-in-delhi/', brand_management_view, name="brand"),
	path('contact/', contact_view, name="contact"),
	path('success/', successView, name="success"),
	path('content-writing-service-in-delhi/', content_writing_view, name="content"),
	path('software-development-company-in-delhi/', custom_software_view, name="software"),
	path('digital-marketing-company-in-delhi/', digital_marketing_view, name="digital"),
	path('error/', error_view, name="error"),
	path('ppc-company-in-delhi/', ppc_view, name="ppc"),
	path('logo-designing-company-in-delhi', logo_design_view, name="logo"),
	path('get-a-quote/', quote_view, name="quote"),
	path('seo-company-in-delhi/', seo_view, name="seo"),
	path('smo-company-in-delhi/', smo_view, name="smo"),
	path('video-editing-services-delhi/', video_editing_view, name="video"),
	path('website-design-and-development/', web_development_view, name="web"),
	path('partner/', partner_view, name="partner"),
	path('policy/', policy_view, name="policy"),
	path('terms-condition/', terms_condition_view, name="terms"),
]