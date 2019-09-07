from django.contrib import admin
from .models import Signup, ContactPage, QuotePage, InquiryPage

class SignupAdmin(admin.ModelAdmin):
	pass
admin.site.register(Signup, SignupAdmin)

class ContactPageAdmin(admin.ModelAdmin):
	pass
admin.site.register(ContactPage, ContactPageAdmin)

class QuotePageAdmin(admin.ModelAdmin):
	pass
admin.site.register(QuotePage, QuotePageAdmin)

class InquiryPageAdmin(admin.ModelAdmin):
	pass
admin.site.register(InquiryPage, InquiryPageAdmin)