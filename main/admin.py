from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',   'posted_date')
    list_filter = ("title",)
    search_fields = ['title', 'message', 'description']


admin.site.register(Blog, BlogAdmin)

