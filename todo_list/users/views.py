from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-home')
