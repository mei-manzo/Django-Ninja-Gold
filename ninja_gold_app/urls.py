from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    # path('counting_test', views.counting_test),
]