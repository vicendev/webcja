from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, "core/index.html")

def works_view(request):
    return render(request, "core/works.html")