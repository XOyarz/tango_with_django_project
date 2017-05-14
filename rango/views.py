from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy etc cupcake"}
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Hey, this is the about page. <br/> <a href='/rango/'>Back to Index</a>")