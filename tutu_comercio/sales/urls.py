from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_venta, name='crear_venta'),
    path('realizada/<int:venta_id>/', views.venta_realizada, name='venta_realizada'),
]
