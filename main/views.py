from email.message import EmailMessage

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from newsletter.models import Signup, ContactPage, QuotePage, InquiryPage
from newsletter.forms import EmailSignUpForm, ContactForm, QuoteForm, InquiryForm
from django.core.mail import send_mail, BadHeaderError
from .models import Blog


def home_view(request):
    form = EmailSignUpForm ()
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup ()
        new_signup.email = email
        new_signup.save ()

    context = {
        'form': form
    }
    return render (request, 'index.html', context)


def about_view(request):
    form = EmailSignUpForm ()
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup ()
        new_signup.email = email
        new_signup.save ()

    context = {
        'form': form
    }
    return render (request, 'about.html', context)


def brand_management_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'brand-management.html', context)


def contact_view(request):
    form = EmailSignUpForm ()
    contact_form = ContactForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'name' in request.POST:
            if contact_form.is_valid ():
                new_contact = ContactPage ()
                new_contact.name = contact_form.cleaned_data['name']
                new_contact.subject = contact_form.cleaned_data['subject']
                new_contact.from_email = contact_form.cleaned_data['from_email']
                new_contact.message = contact_form.cleaned_data['message']
                new_contact.save ()
                try:
                    send_mail (new_contact.subject, new_contact.from_email, new_contact.message,
                               ['tusharjain060@gmail.com'])
                except BadHeaderError:
                    return HttpResponse ('Invalid Header Found')
                return redirect ('success')
    context = {
        'form': form,
        'contact_form': contact_form
    }
    return render (request, "contact.html", context)


def successView(request):
    return HttpResponse ("<script>alert( 'success.thanks for contact us');</script>")


def partner_view(request):
    return render (request, 'international_partner.html')


def policy_view(request):
    return render (request, 'privacy_policy.html')


def terms_condition_view(request):
    return render (request, 'terms-condition.html')


def content_writing_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'content-writing.html', context)


def custom_software_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'customized-swd.html', context)


def digital_marketing_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'digital-marketing.html', context)


def error_view(request):
    return render (request, 'error-page.html')


def logo_design_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'logo-designing.html', context)


def ppc_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'ppc-click-management.html', context)


def quote_view(request):
    form = EmailSignUpForm ()
    quote_form = QuoteForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'website' in request.POST:
            if quote_form.is_valid ():
                new_quote = QuotePage ()
                new_quote.name = quote_form.cleaned_data['name']
                new_quote.website = quote_form.cleaned_data['website']
                new_quote.quote_email = quote_form.cleaned_data['quote_email']
                new_quote.business = quote_form.cleaned_data['business']
                new_quote.service = quote_form.cleaned_data['service']
                new_quote.message = quote_form.cleaned_data['message']
                new_quote.save ()
                try:
                    send_mail (new_quote.website, new_quote.service, new_quote.message, ['mk688689@gmail.com'])
                except BadHeaderError:
                    return HttpResponse ('Invalid Header Found')
                return redirect ('success')
    context = {
        'form': form,
        'quote_form': quote_form
    }
    return render (request, 'quote.html', context)


def seo_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'seo-services.html', context)


def smo_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'smo-services.html', context)


def video_editing_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['mk688689@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'video-editing.html', context)


def web_development_view(request):
    form = EmailSignUpForm ()
    inquiry_form = InquiryForm (request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            new_signup = Signup ()
            new_signup.email = email
            new_signup.save ()
        elif 'inquiry_email' in request.POST:
            if inquiry_form.is_valid ():
                new_inquiry = InquiryPage ()
                new_inquiry.name = inquiry_form.cleaned_data['name']
                new_inquiry.inquiry_email = inquiry_form.cleaned_data['inquiry_email']
                new_inquiry.service = inquiry_form.cleaned_data['service']
                new_inquiry.requirements = inquiry_form.cleaned_data['requirements']
                new_inquiry.save ()
            try:
                send_mail (new_inquiry.name, new_inquiry.inquiry_email, new_inquiry.requirements,
                           ['singlagarvit68@gmail.com'])
            except:
                return HttpResponse ('Invalid Header Found')
            return redirect ('success')
    context = {
        'form': form,
        'inquiry_form': inquiry_form
    }
    return render (request, 'web-development.html', context)


def help_view(request):
    return render (request, 'help.html')


def help_seo_view(request):
    return render (request, 'help-seo.html')


def design_view(request):
    return render (request, 'design-website.html')


def social_media_view(request):
    return render (request, 'social-media-marketing.html')


def book_call_view(request):
    return render (request, 'book-call.html')


def blog_view(request):
    post = Blog.objects.all()
    return render(request, 'blog.html', {'post':post})


def blog_detail_view(request, id):
    data = Blog.objects.get(id=id)
    return render(request, 'post-details.html', {'data':data})

