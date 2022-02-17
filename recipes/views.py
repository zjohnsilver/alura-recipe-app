from django.shortcuts import render


# Create your views here.
def index(request):
    data = {"recipes_name": {1: "Lasanha", 2: "Yakisoba"}}
    return render(request, "index.html", data)


# Create your views here.
def recipes(request):
    return render(request, "recipes.html")
