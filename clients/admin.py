from django.contrib import admin
from .models import ClientProduct

# Register your models here.
@admin.register(ClientProduct)
class ClientProductAdmin(admin.ModelAdmin):
    ...