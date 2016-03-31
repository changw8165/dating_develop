"""dating_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.views.generic import ListView, DetailView
#from blog.models import Post

from django.contrib import admin
from dating_project.view import hello
from dating_project.testdb import testdb
from dating_project import search

#from . import views
#from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^testdb/$',testdb),
    url(r'^search_form/$',search.search_form),
    url(r'^search/$',search.search),
]
