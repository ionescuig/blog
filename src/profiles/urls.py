"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from .views import AccountActivationInvalidView, activate,\
    EmailSentView, DeleteConfirmationView, DeleteUserView,\
    signup_view, UpdateUserView


urlpatterns = [
    path('activate/<str:code>', activate, name='activate'),
    path('email-sent', EmailSentView.as_view(), name='email_sent'),
    path('account-invalid', AccountActivationInvalidView.as_view(), name='account_invalid'),
    path('<int:pk>/delete', DeleteUserView.as_view(), name='delete'),
    path('account-deleted', DeleteConfirmationView.as_view(), name='delete_confirmation'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', signup_view, name='signup'),
    path('<int:pk>/update', UpdateUserView.as_view(), name='update'),
    # path('', include('django.contrib.auth.urls')),
]
