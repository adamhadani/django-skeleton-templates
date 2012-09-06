from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, RedirectView
#from django.contrib.auth.views import login, logout


from django.contrib import admin
# To Use GeoDjango's derived admin module, enable instead:
#from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    # To enable admin app access
    url(r'^admin/', include(admin.site.urls)),
    
    # i18n / l10n
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    # Example to include app-specific urls
    #url(r'^myapp/', include('myapp.urls')),
    
)
