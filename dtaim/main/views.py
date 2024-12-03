from django.shortcuts import render
import datetime


# def index(request):
#     current_datetime = datetime.datetime.now()
#     html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
#     return HttpResponse(html)

def index(request):
    return render(request,'main/index.html')

def publication(request):
    return render(request,'main/publication.html')

def base(request):
    return render (request,'main/base.html')
    