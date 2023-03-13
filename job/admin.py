from django.contrib import admin

# Register your models here.

from .models import JOb ,Category


admin.site.register(JOb)
admin.site.register(Category)