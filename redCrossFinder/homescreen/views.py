from django.shortcuts import render
#from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.forms import CreateUserForm

def home (request):
    return render(request, 'home.html', {})

def login (request):
    return render(request, 'login.html', {})

def register (request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)
