from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, EditProfile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  return render(request, 'home/home.html')

def about(request):
  return render(request, 'accounts/about.html')

@login_required
def pass2(request):
  return render(request, 'accounts/change_password2.html')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return render(request, 'accounts/about.html')
    return render(request, 'accounts/reg_form.html', {'form': form})
  else:
    form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})

@login_required
def view_profile(request):
  args = {'user': request.user}
  return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
  if request.method == 'POST':
    form = EditProfile(request.POST, instance=request.user)
    
    if form.is_valid():
      form.save()
      return redirect('accounts/profile')
  else:
    form = EditProfile(instance=request.user)
    args = {'form': form}
    return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(data=request.POST, user=request.user)

    if form.is_valid():
      update_session_auth_hash(request, form.user)
      return redirect('accounts/profile')
    else:
      return redirect('accounts/change_password')
  else:
    form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/change_password.html', args)