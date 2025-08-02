from django.http import HttpResponse

def products_home(request):
    return HttpResponse("Vista base de PRODUCTS")
