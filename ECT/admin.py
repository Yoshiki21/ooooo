from django.contrib import admin

# Register your models here.
from .models import Meeting, Topic, Expression, Member

admin.site.register(Meeting)
admin.site.register(Topic)
admin.site.register(Expression)
admin.site.register(Member)
