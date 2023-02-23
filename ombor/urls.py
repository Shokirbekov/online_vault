from django.contrib import admin
from django.urls import path
from django.urls import path, include
from vault.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view()),
    path('vault/', include('vault.urls')),
]