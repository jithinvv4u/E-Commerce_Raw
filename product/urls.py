from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('cart/',add_cart,name='cart'),
    path('cartplus/',cart_plus,name='cartplus'),
    path('cartminus/',cart_minus,name='cartminus'),
    path('cartdata/',showCart,name='cartdata'),
    path('delete/<int:id>',remove_cart,name='delete'),
    
    path('inventory/',inventoryHome,name='inventory'),
    path('additem/',createItemView,name='create'),
    path('updateItem/<int:id>',inventoryUpdate,name='inventoryUpdate'),
    path('deleteItem/<int:id>',inventoryDelete,name='inventoryDelete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
