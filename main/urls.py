from django.contrib import admin
from django.urls import path
from .views import home_view,property_view,contact_view,property_details_view


urlpatterns = [
    path("",home_view,name="home"),
    path("property/",property_view,name="property"),
    path("contact/",contact_view,name="contact"),
    path("property-details/<int:pk>/",property_details_view,name="detail"),

]