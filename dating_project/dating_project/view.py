#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context             = {}
    context['hello']    = 'we are the world!'
    return render(request, 'hello.html', context)

    #return HttpResponse("Hello World!")



