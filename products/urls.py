from django.urls import path
from .views import ProductDetailView,ProductCategoryView, ProductSearchView

urlpatterns = [

    path("<int:pk>/",ProductDetailView.as_view(),name="product-detail"),
    path("category/<str:category>/",ProductCategoryView.as_view(),name="product-category"),
    path("search/",ProductSearchView.as_view(),name="product-search"),
]