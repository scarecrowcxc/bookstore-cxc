"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from .views import cart_add, cart_count, cart_show, cart_del


urlpatterns = [
    url(r'^cart_add/$', cart_add, name='cart_add'),
    url(r'^cart_count/$', cart_count, name='cart_count'),
    url(r'^cart_show/$', cart_show, name='cart_show'),
    url(r'^cart_del/$', cart_del, name='cart_del'),

]
