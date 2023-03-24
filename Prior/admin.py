from django.contrib import admin
from .models import *

# Register your models here.
for model in [Category, Course, Section, Video]:
    admin.site.register(model)
