"""gammasolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dash import views as dash_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns as statics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dash_views.index),
    path('dash/', dash_views.main),
    path('dash/drivers/', dash_views.drivers),
    path('dash/customers/', dash_views.customers),
    path('dash/brokers/', dash_views.brokers),
    path('dash/shippers/', dash_views.shippers),
    path('dash/orders/', dash_views.orders),
    path('dash/orders/new/', dash_views.newOrder),
]


urlpatterns += statics()
