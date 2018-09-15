from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')