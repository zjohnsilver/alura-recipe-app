from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


# Create your views here.
def recipes(request):
    return render(request, "recipes.html")
