from django.urls import path
from .views import queryProcessor

urlpatterns = [
    path('', queryProcessor, name="calculator")
]