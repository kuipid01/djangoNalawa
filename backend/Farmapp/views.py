from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .models import Product
from .models import Category
from django.http import HttpResponse
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def post(self,request, *args, **kwargs):
        image= request.data['image']
        name= request.data['name']
        quantity= request.data['quantity']
        description = request.data['description']
        category= request.data['category']
        price = request.data['price']
        Product.objects.create(name=name, category=category, quantity=quantity, image=image, description=description, price=price)
        return HttpResponse({'message': 'Product Created'}, status=200)
    



class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self,request, *args, **kwargs):
        name= request.data['name']
        description = request.data['description']
        Category.objects.create(name=name,  description=description,)
        return HttpResponse({'message': 'Category Created'}, status=200)
# Create your views here.
