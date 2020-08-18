from pdfApp.views import split_view, rotate_view, watermarker_view
from django.urls import path, include
from . import views

urlpatterns = [
    path('split/', views.split_view, name='split'),
    path('rotate/', views.rotate_view, name='rotate'),
    path('split/', views.watermarker_view, name='watermarker'),
]
