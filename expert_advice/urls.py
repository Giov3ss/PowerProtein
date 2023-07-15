from django.urls import path
from . import views

app_name = 'expert_advice'

urlpatterns = [
    path('expert-advice/', views.expert_advice, name='expert_advice'),
    path('success/', views.success, name='success'),
]