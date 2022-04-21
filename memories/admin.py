from django.contrib import admin
from .models import Memory


class MemoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'photo')


admin.site.register(Memory)
