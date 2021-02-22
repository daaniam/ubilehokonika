"""ubilehokonika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views

app_name = 'main'

forms_urls = [
    path('add_announcement_form', views.add_announcement_form, name="add_announcement_form"),
    path('set_announcement_count_form', views.set_announcement_count_form, name="set_announcement_count_form")
]

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.handle_login, name="login"),
    path('logout', views.handle_logout, name="logout"),
    path('accomodation', views.accomodation, name="accomodation"),
    path('webmanage', views.webmanage, name="webmanage"),
] + forms_urls
