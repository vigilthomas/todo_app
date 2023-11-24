"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todo.views import *
from django.contrib import admin
from django.urls import path
from todo.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",IndexView.as_view(), name="home"),
    path("auth/register", RegisterView.as_view(), name="auth_register"),
    path("",LoginView.as_view(),name="auth_login"),
]
"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path("home", IndexView.as_view(), name="home"),
    path("", LoginView.as_view(), name="auth_login"),
    path("logout", LogoutView.as_view(), name="auth_logout"),
    path("register", RegisterView.as_view(), name="auth_register"),
    path("update/<int:pk>", UpdateView.as_view(), name="update"),
    path("check/<int:pk>", CheckView.as_view(), name="check"),
    path("uncheck/<int:pk>", UncheckView.as_view(), name="uncheck"),
    path("delete/<int:pk>", DeleteView.as_view(), name="delete"),
]
