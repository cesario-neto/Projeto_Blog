from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link, LinkGroup, SiteSetup


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        has_object = SiteSetup.objects.all().exists()
        if has_object:
            return False
        return True


@admin.register(LinkGroup)
class LinkGroupAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        qtn_objects = LinkGroup.objects.all()
        if len(qtn_objects) >= 3:
            return False
        return True


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = 'name', 'url'
