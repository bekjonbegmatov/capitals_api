from django.contrib import admin
from . import models


# Register your models here.
# class CountriesAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('country' , 'capital' , 'region' , 'geography')

admin.site.register(models.Countries)
# admin.site.register(CountriesAdmin)
