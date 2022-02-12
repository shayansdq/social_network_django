from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {
            'form':form
        }
        return render(request, 'account/register.html',context)

    def post(self):
        pass
