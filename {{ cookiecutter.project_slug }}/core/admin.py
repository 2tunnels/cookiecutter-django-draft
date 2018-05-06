from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.site_title = admin.site.site_header = '{{ cookiecutter.project_name }}'

admin.site.register(User, UserAdmin)
