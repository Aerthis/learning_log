from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entry

# Use admin.site.register() to tell Django to manage our model thru the admin site
admin.site.register(Topic)
admin.site.register(Entry)
