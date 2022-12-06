from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SingUP.as_view(), name="signup")
]