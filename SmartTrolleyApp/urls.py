"""
URL configuration for SmartTrolley project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from SmartTrolleyApp.views import *

urlpatterns = [
    # ////////////////////////////////// ADMIN ///////////////////////////////////////////////
    path('', LoginPage.as_view(),name="login"),
    path('add_product',AddProductPage.as_view(),name="add product"),
    path('view_staff',ViewStaffPage.as_view(),name="view staff"),
    path('add_staff',AddStaffPage.as_view(),name="add staff"),
    path('adminboard',AdminBoardPage.as_view(),name="adminboard"),
    path('edit_product/<int:p_id>',EditProductPage.as_view(),name="edit product"),
    path('delete_product/<int:p_id>',DeleteProductPage.as_view(),name="delete product"),
    path('edit_staff/<int:s_id>',EditStaffPage.as_view(),name="edit staff"),
    path('view_product',ViewProductPage.as_view(),name="view product"),
    path('registration',RegistrationPage.as_view(),name="registration"),
    path('delete_staff/<int:s_id>',DeleteStaffPage.as_view(),name="delete_staff"),


    # ////////////////////////////////// STAFF //////////////////////////////////////////////////

    path('crosscheck/<int:c_id>',CrossCheckPage.as_view(),name="crosscheck"),
    path('viewuser',ViewUserPage.as_view(),name="viewuser"),
    path('staffhome',StaffhomePage.as_view(),name="staffhome"),
    path('productdetails',ProductDetailsPage.as_view(),name="productdetails"),





    


    
]
