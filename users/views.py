from django.shortcuts import render, redirect
from django.views import View
from . forms import UserRegistrationForm

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')