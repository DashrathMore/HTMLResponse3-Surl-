from django.shortcuts import render

# Create your views here.
def third(request):
    return render (request, 'third.html')

def forth(request):
    return render(request, 'forth.html')