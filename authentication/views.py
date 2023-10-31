from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})







# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from . import forms
# from django.views.generic import View
# from django.conf import settings

# def signup_page(request):
#     form = forms.SignupForm()
#     if request.method == 'POST':
#         form = forms.SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     return render(request, 'authentication/signup.html', context= {'form': form})


# class LoginPage(View):
#     form_class = forms.LoginForm
#     template_name = 'authentication/login.html'
    
#     def get(self, request):
#       form = self.form_class()
#       message = '' 
#       return render (
#         request, self.template_name, context={'form': form, 'message': message}
#     )
#     def post(self, request):
#         form = self.form_class(request.POST)
#         message = ''
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'], 
#                 password=form.cleaned_data['password']
#                 )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#                 #message = f'Bonjour, {user.username} ! Vous etes connectes.' 
#             else:
#                 message = 'Identifiants invalides.'
#         return render (
#         request, self.template_name, context={'form': form, 'message': message})

# def logout_user(request):
#     logout(request)
#     return redirect ('login')

# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#                 #message = f'Bonjour, {user.username} ! Vous etes connectes.' 
#             else:
#                 message = 'Identifiants invalides.'
#     return render (
#         request, 'authentication/login.html', context={'form': form, 'message': message}
#     )
 

