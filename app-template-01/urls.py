from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('{{ app_name }}.views',
       # (r'^example_url/', 'example_view')
)




