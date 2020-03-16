from django.contrib import admin
from . models import Usage


class UsageAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')
    list_filter = ('date',)


admin.site.register(Usage)
