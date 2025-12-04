from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class FilterProductSerialer(serializers.Serializer):
    min_price = serializers.FloatField(required=False)
    max_price = serializers.FloatField(required=False)
    stock = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)