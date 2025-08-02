from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'activo', 'categoria')
    list_filter = ('activo', 'categoria')
    search_fields = ('nombre',)

admin.site.register(Categoria)
