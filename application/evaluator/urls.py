from django.urls import path
from .views import queryProcessor,deep, dScan, showResult

urlpatterns = [
    path('', queryProcessor, name="calculator"),
    path('enableDeepScanning/', deep, name='deep'),
    path('DeepScannig/', dScan, name='dScan'),
    path('show/<str:site>/', showResult, name='show')
]
