from django.urls import path
from libreria.views import AutoresListAV

urlpatterns = [
    path('list/', AutoresListAV.as_view(), name='autores-list'),
]