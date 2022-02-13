from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from account.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Post


class UserRegisterView(View):
    """register user view"""
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'login first!', 'warning')
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'Registered successfully ! ', 'success')
            return redirect('home:home')

        # Handle Invalid form
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    """login user view"""
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'login first!', 'warning')
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in', 'success')
                return redirect('home:home')
            # Handle invalid username or password
            messages.error(request, 'username or password is incorrect', 'warning')

        # Handle Invalid form
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    """user logout view"""

    def get(self, request):
        logout(request)
        messages.success(request, 'logged out', 'success')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        posts = Post.objects.filter(user=user)
        context = {
            'user':user,
            'posts':posts
        }
        return render(request, 'account/profile.html',context)
