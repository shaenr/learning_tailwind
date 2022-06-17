import imp
from django.conf import settings as conf
from .views import PageView

def get_site_title(request):
    sep = PageView.title_sep
    return {
        'site_title':  conf.SITE_TITLE + sep if conf.SITE_TITLE else '',
    }