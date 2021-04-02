from django.urls import path
from product.views import product_list, product_add, dashboard

app_name = "awesome"

urlpatterns = [
    path("product-list/", product_list, name="product_list"),
    path("product-add/", product_add, name="product_add"),
    path("dashboard/", dashboard, name="dashboard"),
]

"""
    localhost:8000/product/product-list
"""