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
from market import views as market_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns as statics
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dash_views.index),
    path('dash/', dash_views.main, name='dash-main'),

    path('dash/drivers/', dash_views.drivers, name='dash-drivers'),
    path('dash/drivers/new/', dash_views.new_driver, name='dash-new-driver'), # create
    path('dash/drivers/<int:pk>/', dash_views.read_driver, name='dash-read-driver'), # read
    path('dash/drivers/<int:pk>/edit/', dash_views.edit_driver), # update
    path('dash/drivers/<int:pk>/delete/', dash_views.delete_driver), # delete

    path('dash/customers/', dash_views.customers, name='dash-customers'),
    path('dash/customers/new/', dash_views.new_customer, name='dash-new-customer'), # create
    path('dash/customers/<int:pk>/', dash_views.read_customer, name='dash-read-customer'), # read
    path('dash/customers/<int:pk>/edit/', dash_views.edit_customer), # update
    path('dash/customers/<int:pk>/delete/', dash_views.delete_customer), # delete

    path('dash/orders/', dash_views.orders, name='dash-orders'),
    path('dash/orders/new/', dash_views.new_order, name='dash-new-order'), # create
    path('dash/orders/<int:pk>/', dash_views.read_order, name='dash-read-order'), # read
    path('dash/orders/<int:pk>/edit/', dash_views.edit_order), # update
    path('dash/orders/<int:pk>/delete/', dash_views.delete_order), # delete

    path('dash/equipment/', dash_views.equipment, name='dash-equipment'),
    path('dash/equipment/new/', dash_views.new_equipment, name='dash-new-equipment'), # create
    path('dash/equipment/<int:pk>/edit/', dash_views.edit_equipment, name='dash-edit-equipment'), # update
    path('dash/equipment/<int:pk>/delete/', dash_views.delete_equipment, name='dash-delete-equipment'), # delete

    path('dash/documents/', dash_views.documents, name='dash-documents'),
    path('dash/documents/new/', dash_views.new_document, name='dash-new-document'), # create
    path('dash/documents/<int:pk>/edit/', dash_views.edit_document), # update
    path('dash/documents/<int:pk>/delete/', dash_views.delete_document), # delete

    path('market/locations/', market_views.locations, name='market-locations'),
    path('market/cities/new/', market_views.new_city, name='market-new-city'), # create
    path('market/cities/<int:pk>/', market_views.read_city, name='market-read-city'), # read
    path('market/cities/<int:pk>/edit/', market_views.edit_city), # update
    path('market/cities/<int:pk>/delete/', market_views.delete_city), # delete

]


urlpatterns += statics()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
