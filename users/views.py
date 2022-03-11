from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def collection(request):
    return render(request, 'users/collection.html')

def contact(request):
    return render(request, 'users/contact.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully ')
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
