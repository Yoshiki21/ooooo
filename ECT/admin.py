from django.contrib import admin

# Register your models here.
from .models import Meeting, Topic

admin.site.register(Meeting)
admin.site.register(Topic)