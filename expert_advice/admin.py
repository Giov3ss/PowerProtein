from django.contrib import admin
from .models import ExpertAdvice

@admin.register(ExpertAdvice)
class ExpertAdviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_field = ['name', 'email', 'message']
