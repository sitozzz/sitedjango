from django.shortcuts import render
from django import forms
from .forms import PostForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def index(request):

    return render(request, 'example/home.html')


def contact(request):
    return render(request, 'example/contact.html', {'values': ['Свяжитесь с нами!', '8-800-555-35-35']})


class FeedBackForm(forms.Form):
    subject = forms.CharField(max_length=80)
    sender = forms.EmailField()
    message = forms.CharField()
    copy = forms.BooleanField(required=False)


def contactView(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        # Если данные введены корректно
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipe = ['sit7602@gmail.com']
            if copy:
                recipe.append(sender)
            try:
                send_mail(subject, message, 'sit7602@gmail.com')
            except BadHeaderError:
                return HttpResponse('Invalid header')
            return render(request, 'example/thnks.html')
    else:
        form = FeedBackForm()
        return render(request, 'example/feedback.html', {'form': form})


def thnks(request):
    thnks = 'thnks'
    return render(request, 'thnks.html', {'thnks': thnks})


def localForm(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'example/form.html', locals())
        # if form.is_valid():
        #     data = form.save(commit=False)
