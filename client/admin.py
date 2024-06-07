from django.contrib import admin

from .models import Client ,OCCUPATIONS ,HireNeed


# Register your models here.

admin.site.register(Client)
admin.site.register(OCCUPATIONS)
admin.site.register(HireNeed)