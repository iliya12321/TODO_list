from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreationForm


class SignUp(CreateView):
    """Регистрация"""
    form_class = CreationForm
    success_url = reverse_lazy('tasks:task_list')
    template_name = 'users/signup.html'
