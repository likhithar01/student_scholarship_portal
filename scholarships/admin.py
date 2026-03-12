from django.contrib import admin
from .models import Scholarship, Application


class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('user','scholarship','status','applied_at')

    list_filter = ('status',)

    search_fields = ('user__username','scholarship__title')


admin.site.register(Scholarship)
admin.site.register(Application,ApplicationAdmin)