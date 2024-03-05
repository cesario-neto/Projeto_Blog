from django.http import HttpRequest
from .models import SiteSetup


def site_setup(request: HttpRequest):
    try:
        site_setup = SiteSetup.objects.all().first
    except SiteSetup.DoesNotExist:
        site_setup = None

    return {
        'site_setup': site_setup
    }
