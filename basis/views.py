from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from basis.forms import CreativeUserForm, CreativeUserChangeForm, PasswordResetRequestForm
from basis.models import User, UserToken


def index(request):
    return render(request, 'index.html', {})


def logout_view(request):
    logout(request)
    return redirect('main:index')


def error_500(request):
    return render(request, '500.html', {})


class RegisterView(View):
    def get(self, request):
        return render(request, 'basis/templates/registration.html', {'form': CreativeUserForm()})

    def post(self, request):
        form = CreativeUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(True)
            form.save_m2m()
            return redirect(reverse('main:login'))

        return render(request, 'basis/templates/registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'basis/templates/login.html', {'form': AuthenticationForm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'basis/templates/login.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'basis/templates/login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('main:profile'))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'basis/profile.html', {})


class ProfileChangeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'basis/profile_edit.html', {'form': CreativeUserChangeForm(instance=request.user)})

    def post(self, request):
        form = CreativeUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('main:profile'))

        return render(request, 'basis/profile_edit.html', {'form': form})



class ResetPasswordRequestView(FormView):
    template_name = 'main/reset.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy('main:reset_redirect_message')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email"]
            user = User.objects.get(email=data)
            token_raw = default_token_generator.make_token(user)
            UserToken.objects.create(user=user, token=token_raw)
            reset_password_link = str('http://localhost:8000') + reverse('main:reset',
                                                                         kwargs={
                                                                             'username': user.username,
                                                                             'token': token_raw
                                                                         }
                                                                         )

            send_email_task.delay(
                subject='Reset password',
                to_email=user.email,
                from_email=settings.EMAIL_HOST_USER,
                template='main/reset_message.html',
                args={'url': reset_password_link}
            )
        return self.form_valid(form)


class UserResetPasswordAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        token = kwargs['token']
        try:
            UserToken.objects.get(user=user, token=token)
        except UserToken.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class ResetPasswordView(UserResetPasswordAccessMixin, FormView):
    form_class = PasswordResetForm
    template_name = 'basis/reset_conf.html'
    success_url = reverse_lazy('main:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["password"]
            username = kwargs['username']
            token = kwargs['token']
            user_token = UserToken.objects.get(user__username=username, token=token)

            user = user_token.user
            user.set_password(data)
            user.save()

            user_token.delete()

        return self.form_valid(form)


class MessageSentView(TemplateView):
    template_name = 'basis/message_sent.html'