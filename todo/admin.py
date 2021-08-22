from django.contrib import admin
from .models import ToDo


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'due', 'is_completed', 'author')
    search_fields = ('text',)
    list_filter = ('is_completed',)
    empty_value_display = '-пусто-'


admin.site.register(ToDo, PostAdmin)