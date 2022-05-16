"""django_project URL Configuration

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
from Inventory.views import Home_view, Edit_view, Create_view, item_view, Warehouse_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_view, name= 'home'),
    path('edit/<int:pk>/', Edit_view, name = 'edit' ),
    path('create', Create_view, name = 'create'),
    path('item/<int:pk>/', item_view, name='item' ),
    path('ware/', Warehouse_view, name='ware'),
]

