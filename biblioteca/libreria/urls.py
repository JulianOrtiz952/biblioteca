from django.urls import path
from libreria.views import AutoresListAV, LibrosListAV, ResenaListAV, LibroYResenaListAV

urlpatterns = [
    path('autores/', AutoresListAV.as_view(), name='autores-list'),
    path('libros/', LibrosListAV.as_view(), name='libros-list'),
    path('resena/', ResenaListAV.as_view(), name='resena-list'),
    path('libros/detallados', LibroYResenaListAV.as_view(), name='libros-detallados-list'),
]