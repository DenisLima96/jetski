from django.contrib import admin
from jets.models import jet


class JetAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year','model_year','value')
    search_fields = ('model',)


admin.site.register(jet, JetAdmin)