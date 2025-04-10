from django.urls import path
from libreria.views import AutoresListAV, LibrosListAV, ResenaListAV

urlpatterns = [
    path('autores/', AutoresListAV.as_view(), name='autores-list'),
    path('libros/', LibrosListAV.as_view(), name='libros-list'),
    path('resena/', ResenaListAV.as_view(), name='resena-list')
]