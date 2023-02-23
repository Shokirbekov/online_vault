from django.urls import path
from .views import *

urlpatterns = [
    path('bolim/', BolimView.as_view()),
    path('products/', MahsulotView.as_view()),
    path('productdel/<int:id>/', MahsulotDelView.as_view()),
    path('update/<int:id>/', MahsulotUpdateView.as_view(), name="update"),
    path('clients/', ClientView.as_view(), name="client"),
    path('clientdel/<int:id>/', ClientDelView.as_view(), name="clientdel"),
    path('clientupdate/<int:id>/', ClientUpdateView.as_view(), name="clientupdate")
]