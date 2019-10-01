from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from newsletter.forms import EmailSignUpForm
from .models import Signup
import json
import requests
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
	data = {
		"email_address": email,
		"status": "subscribed"
	}
	r = requests.post(
		members_endoint,
		auth=("", MAILCHIMP_API_KEY),
		data = json.dumps(data)
	)
	return r.status_code, r.json()


def email_list_signup(request):
	
	form = EmailSignUpForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			email_signup_qs = Signup.objects.filter(email=form.instance.email)
			if email_signup_qs.exists():
				messages.info(request, "You are already subscribed")
			else:
				subscribe(form.instance.email)
				form.save()
		return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
