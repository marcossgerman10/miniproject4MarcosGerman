from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency', 'streak', 'last_completed', 'user')
    list_filter = ('frequency', 'user')
    search_fields = ('name',)

