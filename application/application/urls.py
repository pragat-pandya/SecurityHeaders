from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sponsors/', sponsor, name='sponsor'),
    path('donate/', donate, name='donate'),
    path('FrequentlyAskedQuestions', faqs, name='faq'),
    path('WhoWhyHow/', www, name='www'),

    path('scanner/', include('evaluator.urls')),
    
]
