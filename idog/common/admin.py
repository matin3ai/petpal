from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'target_type', 'target_id', 'rating', 'created_at']
    list_filter = ['target_type', 'rating']
    search_fields = ['user__username', 'comment']