from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, HrefEditForm

from .models import Href
from .models import Profile

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])

            # Сохраняем пользователя в базе данных.
            new_user.save()

            # Создание профиля пользователя.
            Profile.objects.create(user=new_user)

            return render(request, 'hrefs/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'hrefs/register.html', {'user_form': user_form})

@login_required
def index(request):
    all_hrefs_list = Href.objects.all()
    return render(request, 'hrefs/index.html', {'all_hrefs_list': all_hrefs_list})

@login_required
def add(request):
    if request.method == 'POST':
        add_href_form = HrefEditForm(request.POST)
        if add_href_form.is_valid():
            new_href = add_href_form.save()
            
            return render(request, 'hrefs/add.html')
    
    return render(request, 'hrefs/add.html', {'add_href_form': HrefEditForm()})

#def edit(request, href_id):
#    response = "EDIT %s."
#    return HttpResponse(response % href_id)

def delete(request, href_id):
    response = "DELETE %s."
    return HttpResponse(response % href_id)

def view(request, href_id):
    response = "VIEW %s."
    return HttpResponse(response % href_id)

@login_required
def dashboard(request):
    return render(request, 'hrefs/dashboard.html', {'section': 'dashboard'})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'hrefs/edit.html', {'user_form': user_form,'profile_form': profile_form})