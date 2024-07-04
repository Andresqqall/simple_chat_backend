from django.contrib import admin

from apps.chat.models import Thread, Message


# Register your models here.


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_on', 'created_by', 'updated_on', 'updated_by']
    search_fields = ['participants__first_name', 'participants__last_name']
    list_per_page = 15


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'is_read', 'created_on', 'created_by', 'updated_on', 'updated_by']
    list_per_page = 15
