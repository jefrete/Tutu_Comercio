from django.http import HttpResponse

def users_home(request):
    return HttpResponse("Vista base de USERS")
