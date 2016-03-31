from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'What you search for is: ' +request.GET['q'].encode('utf-8')
    else:
        message = 'you submit the form'

    return HttpResponse(message)
