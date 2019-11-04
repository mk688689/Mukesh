from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path ('', home_view, name="home"),
    path ('about/', about_view, name="about"),
    path ('branding-services/', brand_management_view, name="brand"),
    path ('contact/', contact_view, name="contact"),
    path ('success/', successView, name="success"),
    path ('content-writing-service/', content_writing_view, name="content"),
    path ('software-development-services/', custom_software_view, name="software"),
    path ('digital-marketing-services/', digital_marketing_view, name="digital"),
    path ('error/', error_view, name="error"),
    path ('ppc-services/', ppc_view, name="ppc"),
    path ('logo-designing-services', logo_design_view, name="logo"),
    path ('get-a-quote/', quote_view, name="quote"),
    path ('seo-services/', seo_view, name="seo"),
    path ('smo-services/', smo_view, name="smo"),
    path ('video-editing-services/', video_editing_view, name="video"),
    path ('website-design-and-development-services/', web_development_view, name="web"),
    path ('partner/', partner_view, name="partner"),
    path ('local-partner/', local_partner_view, name="local-partner"),
    path ('policy/', policy_view, name="policy"),
    path ('terms-condition/', terms_condition_view, name="terms"),
    path ('help/', help_view, name="help"),
    path ('help-seo/', help_seo_view, name="help-seo"),
    path ('design-website/', design_view, name="design-website"),
    path ('social-media/', social_media_view, name="social-media"),
    path ('book-call/', book_call_view, name="book-call"),
    path ('blog/', blog_view, name="blog"),
    path ('blog-detail/<int:id>', blog_detail_view, name="blog-detail"),
]
