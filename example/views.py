from django.shortcuts import render

def index(request):
    return render(request, 'example/home.html')

def contact(request):
    return render(request, 'example/contact.html', {'values': ['Свяжитесь с нами!', '8-800-555-35-35']})