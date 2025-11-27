from django.contrib import admin
from django.urls import path
from .views import home_view,product_view,contact_view


urlpatterns = [
    path("",home_view,name="home"),
    path("/product",product_view,name="product"),
    path("/contact",contact_view,name="contact"),

]