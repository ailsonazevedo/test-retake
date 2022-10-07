from django.contrib import admin

from .models import Process, Parts, JudicialClass

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('number','topic', 'judge', 'category', 'created', 'modified')
    list_filter = ('number', 'judicialClass', 'judge', 'category')
    search_fields = ('number', 'judicialClass', 'judge', 'category')

@admin.register(Parts)
class PartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    list_filter = ('name',)
    search_fields = ('name',)   

@admin.register(JudicialClass)
class JudicialClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    list_filter = ('name',)
    search_fields = ('name',)