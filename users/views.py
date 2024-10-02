from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        form  = UserRegisterForm(request.POST)

        if form.is_valid(): # check the validation of form
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('register')
    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        username = u_form.cleaned_data.get('username')
        messages.success(request, f'User info for {username} Updated')
        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'u_form':u_form, 'p_form': p_form})






