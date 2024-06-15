from django.contrib import admin
from django.urls import path

from app.views import index, product_detail, customer_detail

urlpatterns = [
    path('index/',index, name='index'),
    path('product-detail/<int:pk>/', product_detail, name='product_details'),
    path('customers/', customer_detail, name='customers'),
]
