from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("HELLO WORLD IT'S AMAN HERE")

