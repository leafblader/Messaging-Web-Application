"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.rootToLogin, name='login'),
    path('registeruser.html', views.newuser, name='registeruser'),
    path('login.html', views.login, name='login'),
    path('resetpassword.html', views.resetpassword, name='pReset'),
    path('appInterface.html',views.appInterface,name='main'),
    path('settings.html', views.settings, name="userSettings"),
    path('convo.html', views.displayChat, name="conversations"),
    path('msgbox.html', views.msgbox, name="msgbox"),
]
