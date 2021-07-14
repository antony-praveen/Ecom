"""ecom URL Configuration

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
from shop import views
from django.views.generic import TemplateView

from django.views.static import serve
from django.conf.urls import url
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="adminw"),
    path("", views.index, name="index"),
    path("test/", TemplateView.as_view(template_name="shop/test.html"), name="test"),
    path("about/", TemplateView.as_view(template_name="shop/about.html"), name="about"),
    path('<int:obj_id>',views.detail, name="detail"),
    path("checkout/",views.checkout, name="checkout"),

    
    #url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

