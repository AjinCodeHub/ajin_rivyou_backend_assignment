from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category = self.kwargs["category"]
        return Product.objects.filter(category__iexact=category)
    
class ProductSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q", "").strip()
        limit = int(request.GET.get("limit", 20))
        category_filter = request.GET.get("category_filter")
        if not query:
            return Response(
            {
                "error": "Query parameter 'q' is required."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
            
        tier1 = Product.objects.filter(category__icontains=query)

        serializer = ProductSerializer(tier1,many=True,)

        results = []

        for product in serializer.data:
            product["relevance_score"] = 0.95
            product["rank_reason"] = "Category match"
            results.append(product)
        return Response(
            {
                "query": query,
                "total_results": len(results),
                "results": results[:limit],
            }
    )