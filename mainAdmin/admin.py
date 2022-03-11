from django.contrib import admin
from .models import productItems
from .models import cart
from .models import orderItem,CheckOut
# Register your models here.

admin.site.register(productItems)
admin.site.register(cart)
admin.site.register(orderItem)
admin.site.register(CheckOut)
