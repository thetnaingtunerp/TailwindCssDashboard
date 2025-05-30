from django.shortcuts import render

# Create your views here.

def blank_view(request):
    return render(request, 'blank.html')

def card_example(request):
    return render(request, 'cardexample.html')

def dashboard(request):
    return render(request, 'dashboard.html')