from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def handle_not_found(request, exception):
    return render (request, 'not-found.html')

def about(request):
     return render(request, 'about.html')