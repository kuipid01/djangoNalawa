from rest_framework import serializers
from .models import Product
from .models import Category
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # read_only_fields = ('category',)

        fields = ['id', 'name', 'price', 'image','updated_at','quantity','category']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description',]