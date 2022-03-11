from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index1, name='index'),
    path('shoe', views.shoe, name='shoe'),
    path('mainAdmin', views.index, name='index1'),
    path('mainAdmin/orders', views.orders, name='orders'),
    path('mainAdmin/products', views.products, name='products'),
    path('mainAdmin/brands', views.brands, name='brands'),
    path('mainAdmin/category', views.category, name='category'),
    path('mainAdmin/customers', views.customers, name='customers'),
    path('mainAdmin/create', views.create, name='create'),
    path('mainAdmin/edit/<str:pk>', views.edit, name='edit'),
    path('single/<str:pk>', views.singleProduct, name='item'),
    path('cart', views.cartItems, name='cart'),
    path('delete/<str:pk>', views.deleteFromCart, name='delete'),
    path('delete1/<str:pk>', views.deleteFromOrder, name='delete1'),
    path('single/errorQuantity/<str:pk>', views.errorQuantity, name='errorQuantity'),
    path('updateCart/', views.updateCart, name='updateCart'),
    path('placeOrder/', views.placeOrderPage, name='placeOrderPage'),
    path('addToOrderedItems/', views.placeOrder, name='placeOrder'),
    path('end', views.end, name='end'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
