from django.contrib import admin
from .models import *

# Register your models here.
class LeadsManager (admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'date_time')

class ScansManager (admin.ModelAdmin):
  list_display = ('ip', 'url', 'date_time', 'is_private', 'client_details')


admin.site.register(Lead, LeadsManager)
admin.site.register(Scan, ScansManager)