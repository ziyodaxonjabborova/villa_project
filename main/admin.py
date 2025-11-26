from django.contrib import admin
from .models import Property, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)     

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'area', 'floor')  
    list_filter = ('category',)  
    search_fields = ('title', 'address')  
