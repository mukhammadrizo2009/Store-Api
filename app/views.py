from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer , FilterProductSerialer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        
        if self.action == 'list':
            filter_serializer =  FilterProductSerialer(data=self.request.query_params)
            
            if filter_serializer.is_valid(raise_exception=True):
                min_price = filter_serializer.data.get('min_price')
                max_price = filter_serializer.data.get('max_price')
                stock = filter_serializer.data.get('stock')
                created_at = filter_serializer.data.get('created_at')
                
                if min_price is not None:
                    queryset = queryset.filter(min_price=min_price)
                if max_price is not None:
                    queryset = queryset.filter(max_price=max_price)
                if stock is not None:
                    queryset = queryset.filter(stock=stock)
                if created_at is not None:
                    queryset = queryset.filter(created_at=created_at)
                    
        return queryset