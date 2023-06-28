from django.contrib import admin
from .models import userregister
from .models import Products
from .models import Cart
# Register your models here.
admin.site.register(userregister)
admin.site.register(Products)
admin.site.register(Cart)
