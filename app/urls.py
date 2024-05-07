from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('signup',views.signup,name="signup"),
    path('login_view',views.login_view,name="login_view"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('Addbloom/',views.Addbloom,name="Addbloom"),
    path('viewbloom/<str:name>',views.viewbloom,name="viewbloom"),
    path('orderbloom/<int:id>',views.orderbloom,name="orderbloom")
]


