from django.contrib import admin
from .models import product,brands,gender,product_type


# Register your models here.
admin.site.register(brands)
admin.site.register(gender)
admin.site.register(product_type)
admin.site.register(product)