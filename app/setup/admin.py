from django.contrib import admin
from .models import SiteSetup
from django.http import HttpRequest


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.all().exists()
