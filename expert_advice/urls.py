from django.urls import path
from . import views

app_name = 'expert_advice'

urlpatterns = [
    path('expert-advice/', views.ExpertAdviceView.as_view(), name='expert_advice'),  # noqa
    path('success/', views.success, name='success'),
]
