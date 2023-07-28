from django.contrib import admin
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """
    Admin class Reviews
    """
    list_display = (
        'name',
        'review_title',
        'created_on',
        'service_review',
        'service_rating',
        'approved',
        'carousel_review',
    )
