from django.contrib import admin

from .models import Distribution, Client, Message

@admin.register(Distribution)
class AdminDistribution(admin.ModelAdmin):
    list_display = ('id',
                    'data_time_start',
                    'text',
                    'filter',
                    'data_time_finish',)


@admin.register(Client)
class AdminCLient(admin.ModelAdmin):
    list_display = ('id',
                    'phone_number',
                    'tag',
                    'time_zone')


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ('id',
                    'data_created',
                    'status',
                    'distribution',
                    'client')
