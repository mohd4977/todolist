from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "authenticator/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    success_message = "User was loggedin successfully"

    def get_success_url(self):
        return reverse_lazy('tasks')

class UserRegister(SuccessMessageMixin,FormView):
    template_name = 'authenticator/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    success_message = "User was created successfully"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegister, self).get(*args, **kwargs)