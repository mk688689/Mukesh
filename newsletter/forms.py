from django import forms
from .models import Signup, ContactPage, QuotePage, InquiryPage

class EmailSignUpForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={
		"type": "email",
		"name": "email",
		"placeholder": "Email Address...",
		"id": "email"
		}), label="")
	class Meta:
		model = Signup
		fields = ('email', )

class ContactForm(forms.ModelForm):
	name = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "username",
		"placeholder": "Name",
		"required": "True"
		}), label="")
	from_email = forms.EmailField(required=False, widget=forms.TextInput(attrs={
		"type": "email",
		"name": "email_contact",
		"placeholder": "Email",
		"required": "True"
		}), label="")
	subject = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "subject",
		"placeholder": "Subject",
		"required": "True"
		}), label="")	
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={
		"name": "message",
		"placeholder": "Your Message...",
		"required": "True"
		}), label="")

	class Meta:
		model = ContactPage
		fields = ('name', 'from_email', 'subject', 'message', )

class QuoteForm(forms.ModelForm):
	name = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "username",
		"placeholder": "Name",
		"required": "True"
		}), label="")
	quote_email = forms.EmailField(required=False, widget=forms.TextInput(attrs={
		"type": "email",
		"name": "email_contact",
		"placeholder": "Email",
		"required": "True"
		}), label="")
	website = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "website",
		"placeholder": "Website",
		"required": "True"
		}), label="")
	business = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "business",
		"placeholder": "Your Industry?",
		"required": "True"
		}), label="")
	SERVICE_CHOICES = [
		('Select', 'Please Select a Service.'),
		('SOCIAL MEDIA MARKETING', 'Social Media Marketing'),
		('WEBSITE DEVELOPMENT', 'Website Development'),
		('SEO AND WEBSITE DEVELOPMENT', 'SEO & Website Development'),
		('SEO, SMO AND WEBSITE DEVELOPMENT', 'SEO, SMO & Website Development'),
		('EXECUTIVE', 'I want to talk to your executive.')
	]
	service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select(attrs={
		"class": "custom-select-box",
		"required": "True"
		}), label="")
	message = forms.CharField(widget=forms.Textarea(attrs={
		"name": "message",
		"placeholder": "Your Message",
		"required": "False"
		}), label="")
	class Meta:
		model = QuotePage
		fields = ('name', 'quote_email', 'website', 'business', 'service', 'message', )


class InquiryForm(forms.ModelForm):
	name = forms.CharField(required=False, widget=forms.TextInput(attrs={
		"type": "text",
		"name": "username",
		"placeholder": "Name",
		"required": "True"
		}), label="")
	inquiry_email = forms.EmailField(required=False, widget=forms.TextInput(attrs={
		"type": "email",
		"name": "email",
		"placeholder": "Email",
		"required": "True"
		}), label="")
	SERVICE_CHOICES = [
		('Select', 'Please Select a Service.'),
		('SOCIAL MEDIA MARKETING', 'Social Media Marketing'),
		('WEBSITE DEVELOPMENT', 'Website Development'),
		('SEO AND WEBSITE DEVELOPMENT', 'SEO & Website Development'),
		('SEO, SMO AND WEBSITE DEVELOPMENT', 'SEO, SMO & Website Development'),
		('EXECUTIVE', 'I want to talk to your executive.')
	]
	service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select(attrs={
		"class": "custom-select-box",
		"required": "True"
		}), label="")
	requirements = forms.CharField(widget=forms.Textarea(attrs={
		"name": "message",
		"placeholder": "Other Requirements",
		"required": "False"
		}), label="")
	class Meta:
		model = InquiryPage
		fields = ('name', 'inquiry_email', 'service', 'requirements', )