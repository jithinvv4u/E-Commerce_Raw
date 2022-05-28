from django.contrib import admin
from .models import Cart, Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_disaplay=('name','description','quantity','rate','category','image')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('user','item','quantity')