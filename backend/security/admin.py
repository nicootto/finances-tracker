from django.contrib import admin
from django.contrib.admin import register

from security.models import Token


@register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass
