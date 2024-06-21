from django.contrib import admin
from app.models import Product, Image,AttributeKey,AttributeValue,ProductAttribute, Customers
# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
admin.site.register(Customers)
