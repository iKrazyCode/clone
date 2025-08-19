from django.contrib import admin

from .models import TemplateCopy, Account
# Register your models here.



class AccountTabularInline(admin.TabularInline):
    model = Account
    extra = 0



@admin.register(TemplateCopy)
class TemplateCopy(admin.ModelAdmin):
    inlines = [AccountTabularInline,]


@admin.register(Account)
class Account(admin.ModelAdmin):
    ...