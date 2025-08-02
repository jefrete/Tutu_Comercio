from django.http import HttpResponse

def clients_home(request):
    return HttpResponse("Vista base de CLIENTS")
