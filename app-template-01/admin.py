from django.contrib import admin
# When using GeoDjango, use this instead of django.contrib.admin
#from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#from tastypie.admin import ApiKeyInline
#from tastypie.models import ApiAccess, ApiKey

from .models import *

# When using tastypie for RESTful API enable the following
"""
admin.site.register(ApiAccess)
class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]
admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
"""

# Register all models with geographical data (GeoDjango)
# to support displaying map widgets for geometry-based fields
# Example:
#admin.site.register(Group, admin.GeoModelAdmin)
