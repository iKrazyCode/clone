from django.contrib import admin

from .models import TemplateCopy, Account
# Register your models here.

@admin.register(TemplateCopy)
class TemplateCopy(admin.ModelAdmin):
    ...


@admin.register(Account)
class Account(admin.ModelAdmin):
    ...