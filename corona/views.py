from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def status(request):
    return render(request,"status.json")