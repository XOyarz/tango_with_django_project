from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hey partener! <br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Hey, this is the about page. <br/> <a href='/rango/'>Back to Index</a>")