from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           # Home o dashboard
    path('usuarios/', include('users.urls')), # Empleados, login, roles
    path('productos/', include('products.urls')), 
    path('clientes/', include('clients.urls')), 
    path('ventas/', include('sales.urls')),

]
