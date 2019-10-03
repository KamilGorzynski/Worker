from django.contrib import admin
from .models import UrlObject, RequestHistory


@admin.register(UrlObject)
class WalletAdmin (admin.ModelAdmin):
    pass


@admin.register(RequestHistory)
class WalletAdmin (admin.ModelAdmin):
    pass
