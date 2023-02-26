from django.urls import path
from .views import *
urlpatterns = [
    path('', StatistikaView.as_view(), name='login'),
    path('statdel/<int:id>/', StatDelView.as_view()),
]