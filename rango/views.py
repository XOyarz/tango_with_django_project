from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hey partenere")