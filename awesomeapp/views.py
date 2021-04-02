from django.shortcuts import render
from django.http import HttpResponse
from awesomeapp.models import Product


# Create your views here.

# def home(request):
#     context = {
#                 "namelist": [
#                 { "name": "Prasum",
#                     "Contact": "9813675753",
#                     "Address": "Baneshwor",
#                 },
#                 {
#                   "name": "Suman",
#                     "Contact": "981445753",
#                     "Address": "ktm",  
#                 },
#                 {
#                     "name": "Sunny",
#                     "Contact": "9811123753",
#                     "Address": "bhk", 
#                 },
#                 ]
#             }

#     return render(request, "grand.html", context)


def home(request):
    products = Product.objects.all()
    context = {"product_list": products}
    return render(request, "product.html", context)
