from django.contrib import admin

# Register your models here.
from .models import Author,Books

admin.site.register(Books)
admin.site.register(Author)
