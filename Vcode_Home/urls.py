"""Vcode_hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_home, name="Home Page"),
    path('IDE', views.display_ide, name="IDE Page"),
    path('FeHtml', views.display_feh, name="FeHtml Page"),
    path('FeCss', views.display_fec, name="FeCss Page"),
    path('FeJs', views.display_fej, name="FeJs Page"),
    path('BeDjango', views.display_bdj, name="BeDjango Page"),
    path('DbMysql', views.display_dms, name="DbMysql Page"),
    path('github', views.display_gh, name="github Page"),
    path('roadmap', views.display_rp, name="roadmap Page"),
    path('fequiz1', views.display_fq1, name="fequiz1 Page"),
    path('feassign1', views.display_fa1, name="feassign1 Page"),
    path('register', views.display_register, name="register Page"),
    path('login', views.display_login, name="login Page")
]
