from django.contrib import admin

# Register your models here.

from django.forms import CheckboxSelectMultiple

from .models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)



