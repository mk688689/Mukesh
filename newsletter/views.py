from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from newsletter.forms import EmailSignUpForm
from .models import Signup, ContactPage
import json
import requests
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.core.mail import send_mail

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

    r = requests.post (
        members_endoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps (data)
    )

    return r.status_code, r.json ()


def email_list_signup(request):
    form = EmailSignUpForm (request.POST or None)
    if request.method == 'POST':
        if form.is_valid ():
            email_signup_qs = Signup.objects.filter (email=form.instance.email)
            if email_signup_qs.exists ():
                messages.info (request, "You are already subscribed")
            else:
                subscribe (form.instance.email)
                form.save ()
        return HttpResponseRedirect (request.META.get ("HTTP_REFERER"))


def contact(request):
    if request.method == 'POST':
        if 'message' in request.POST:
            bb = ContactPage()
            bb.name = request.POST['name']
            bb.email = request.POST['email']
            bb.subject = request.POST['subject']
            bb.message = request.POST['message']
            bb.save ()
            subject = "viralgroww Subject " + request.POST['subject']
            message = "  Name:  " + request.POST['name'] + "\n Email-ID:  " + request.POST[
                'email'] + "\n Message:  " + request.POST['message']
            user = "mk688689@gmail.com"
            res = send_mail (subject, message, user, ['mk688689@gmail.com'], fail_silently=True)
            return redirect ('contact')

    return render (request, 'contact.html')

#
# def index(request):
#     if request.method == 'POST':
#         if 'name' in request.POST:
#             db1 = Admission_form ()
#             db1.name = request.POST['name']
#             db1.email = request.POST['email']
#             db1.phone = request.POST['phone']
#             db1.course = request.POST['course']
#             db1.address = request.POST['address']
#             db1.save ()
#             subject = "Admission form for course  " + request.POST['course']
#             message = " Student's Name:  " + request.POST['name'] + "\n Email-ID:  " + request.POST[
#                 'email'] + "\n Phone Number:  " + request.POST['phone'] + "\n For Course:  " + request.POST[
#                           'course'] + "\n Address:  " + request.POST['address']
#             user = "mk688689@gmail.com"
#             res = send_mail (subject, message, user, ['mk688689@gmail.com'], fail_silently=True)
#             return redirect ('index')
#         elif 'email1' in request.POST:
#             nl = gettouch ()
#             nl.name1 = request.POST['name1']
#             nl.email1 = request.POST['email1']
#             nl.save ()
#             return redirect ('index')
#         else:
#             print ('Errors')
#             return render (request, '')
#         return render (request, 'index.html')
