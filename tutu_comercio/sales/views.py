from django.shortcuts import render, redirect
from products.models import Producto
from .models import Venta, ItemVenta

def crear_venta(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        venta = Venta.objects.create()
        for producto in productos:
            cantidad = int(request.POST.get(f'cantidad_{producto.id}', 0))
            if cantidad > 0:
                ItemVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )
        return redirect('venta_realizada', venta_id=venta.id)

    return render(request, 'sales/crear_venta.html', {'productos': productos})


def venta_realizada(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    return render(request, 'sales/venta_realizada.html', {'venta': venta})
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Producto
from .models import Venta, ItemVenta

# Vista para crear una venta (tipo POS)
def crear_venta(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        venta = Venta.objects.create()

        for producto in productos:
            cantidad_str = request.POST.get(f'cantidad_{producto.id}', '0')
            try:
                cantidad = int(cantidad_str)
            except ValueError:
                cantidad = 0

            if cantidad > 0:
                ItemVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )

                # Opcional: actualizar stock (si querés manejarlo)
                producto.stock -= cantidad
                producto.save()

        return redirect('venta_realizada', venta_id=venta.id)

    return render(request, 'sales/crear_venta.html', {'productos': productos})


# Vista para mostrar el resumen de la venta
def venta_realizada(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    items = ItemVenta.objects.filter(venta=venta)

    total = sum(item.cantidad * item.precio_unitario for item in items)

    return render(request, 'sales/venta_realizada.html', {
        'venta': venta,
        'items': items,
        'total': total
    })
