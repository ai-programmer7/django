from django.contrib import admin
from .models import Company, Service, Advantage, Message

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['custom_column', 'name', 'description', 'title_bottom_left',
                    'info_bottom_left', 'info_bottom_right']
    list_editable = ['name', 'description', 'title_bottom_left',
                     'info_bottom_left', 'info_bottom_right']

    @admin.display(description='id')
    def custom_column(self, obj):
        return obj.id


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['custom_column', 'service_name', 'title', 'short_info', 'description']
    list_editable = ['service_name', 'title', 'short_info', 'description']
    ordering = ['service_name']

    @admin.display(description='id')
    def custom_column(self, obj):
        return obj.id


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['custom_column', 'advantage1', 'advantage2', 'advantage3']
    list_editable = ['advantage1', 'advantage2', 'advantage3']

    @admin.display(description='id')
    def custom_column(self, obj):
        return obj.id


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'phone', 'message', 'time']
    readonly_fields = ['name', 'mail', 'phone', 'message', 'time']
    list_per_page = 10


