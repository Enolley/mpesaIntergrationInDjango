from django.urls import path
from . import views

urlpatterns = [
    path('pay', views.pay, name="Pay"),
    path('stk', views.stk, name="Stk")
]
