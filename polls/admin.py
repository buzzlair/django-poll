from django.contrib import admin
from .models import Question

# Register your models here.

# Resistering the model to admin interface
admin.site.register(Question)