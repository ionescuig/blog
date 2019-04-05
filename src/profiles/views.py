from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse, reverse_lazy


from.forms import SignupForm
from .models import Profile


def activate(request, code):
    try:
        profile = Profile.objects.get(activation_key=code)
    except:
        profile = None
    if profile is not None:
        profile.user.is_active = True
        profile.activation_key = None
        profile.activated = True
        profile.user.save()
        return redirect('profiles:account_success')
    else:
        return redirect('profiles:account_invalid')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save user
            user = form.save()
            user.is_active = False
            user.save()
            user.refresh_from_db() # load the profile instance created by the signal

            # send activation mail
            base_url = "{0}://{1}".format(request.scheme, request.get_host())
            user.profile.send_activation_mail(base_url)

            return redirect('profiles:email_sent')
    else:
        form = SignupForm()
    return render(request, 'profiles/signup.html', {'form': form})


class EmailSentView(TemplateView):
    template_name = 'profiles/email_sent.html'


class AccountActivationInvalidView(TemplateView):
    template_name = 'profiles/account_activation_invalid.html'


class AccountActivationSuccessView(TemplateView):
    template_name = 'profiles/account_activation_success.html'
