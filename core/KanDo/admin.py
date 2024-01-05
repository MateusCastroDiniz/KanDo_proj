from django.contrib import admin

from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'status', 'priority')
    list_filter = ('status',)
    search_fields = ['status', 'priority', 'title']
    prepopulated_fields = {'title': ('description',)}


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('column_name', 'board', 'created_on')
    list_filter = ('board',)
    search_fields = ['column_name', 'created_on',]


class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_name', 'owner', 'created_on')
    list_filter = ('owner',)
    search_fields = ['board_name', 'owner',]


admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)

# Register your models here.
