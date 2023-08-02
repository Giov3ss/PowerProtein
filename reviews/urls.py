from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),  # noqa
]
