from django.contrib import admin

# Register your models here.
from main.models import Book, Journal

admin.site.register(Book)
admin.site.register(Journal)