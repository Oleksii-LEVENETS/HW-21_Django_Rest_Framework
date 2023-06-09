"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from blog.views import UserLogIn

from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication
    path("api-auth/", include("rest_framework.urls")),
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api-user-login/", UserLogIn.as_view()),
    # My app "blog":
    path("", include("blog.urls")),
]
