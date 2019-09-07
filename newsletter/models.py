from django.db import models

class Signup(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.email

class ContactPage(models.Model):
	name = models.CharField(max_length=100)
	from_email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class QuotePage(models.Model):
	name = models.CharField(max_length=100)
	quote_email = models.EmailField()
	website = models.CharField(max_length=100)
	business = models.CharField(max_length=100)
	SERVICE_CHOICES = [
		('SOCIAL MEDIA MARKETING', 'Social Media Marketing'),
		('WEBSITE DEVELOPMENT', 'Website Development'),
		('SEO AND WEBSITE DEVELOPMENT', 'SEO & Website Development'),
		('SEO, SMO AND WEBSITE DEVELOPMENT', 'SEO, SMO & Website Development'),
		('EXECUTIVE', 'I want to talk to your executive.')
	]
	service = models.CharField(
		max_length=100,
		choices = SERVICE_CHOICES,
		default = 'SOCIAL MEDIA MARKETING',
	)

	message = models.CharField(max_length=500)

	def __str__(self):
		return self.website

class InquiryPage(models.Model):
	name = models.CharField(max_length=100)
	inquiry_email = models.EmailField()
	SERVICE_CHOICES = [
		('SOCIAL MEDIA MARKETING', 'Social Media Marketing'),
		('WEBSITE DEVELOPMENT', 'Website Development'),
		('SEO AND WEBSITE DEVELOPMENT', 'SEO & Website Development'),
		('SEO, SMO AND WEBSITE DEVELOPMENT', 'SEO, SMO & Website Development'),
		('EXECUTIVE', 'I want to talk to your executive.')
	]
	service = models.CharField(
		max_length=100,
		choices = SERVICE_CHOICES,
		default = 'SOCIAL MEDIA MARKETING',
	)
	requirements = models.CharField(max_length=500)

	def __str__(self):
		return self.inquiry_email