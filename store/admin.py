from django.contrib import admin

from .models import *
# from django.contrib.auth.models import User

# admin.site.register(User)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
