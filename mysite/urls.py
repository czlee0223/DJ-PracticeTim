"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py 
from django.contrib import admin
from django.urls import include, path
from register import views as v

urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path("register/", v.register, name="register"),
    path('admin/', admin.site.urls),
    # path('', include("django.contrib.auth.urls")),
]