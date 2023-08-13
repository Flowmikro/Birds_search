from django.contrib import admin

from .models import BirdModel, AddBirdModel

admin.site.register(BirdModel)
admin.site.register(AddBirdModel)