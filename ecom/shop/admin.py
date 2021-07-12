from django.contrib import admin
from .models import order, products,order

# Register your models here.

admin.site.register(products)
admin.site.register(order)