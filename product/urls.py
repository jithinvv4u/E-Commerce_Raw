from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    #urls for cart operations
    path('cart/',add_cart,name='cart'),
    #cart add and remove are done with jquery and ajax
    path('cartplus/',cart_plus,name='cartplus'),
    path('cartminus/',cart_minus,name='cartminus'),
    path('cartdata/',showCart,name='cartdata'),
    path('delete/<int:id>',remove_cart,name='delete'),
    
    #urls for inventory operations
    path('inventory/',inventoryHome,name='inventory'),
    path('additem/',createItemView,name='create'),
    path('updateItem/<int:id>',inventoryUpdate,name='inventoryUpdate'),
    path('deleteItem/<int:id>',inventoryDelete,name='inventoryDelete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
