from django.contrib import admin
from .models import Users, Posts, Comment

# Register your models here.
admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Comment)