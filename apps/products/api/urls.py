from django.urls import path
from apps.products.api.views.general_views import CategoryListAPIView, CategoryRetrieveAPIView
from apps.products.api.views.product_views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    # Métodos listar y buscar
    path('category/list/',CategoryListAPIView.as_view(),name='category-list'),
    path('category/retrieve/<int:pk>',CategoryRetrieveAPIView.as_view(),name='category-retrieve'),
    path('product/list/',ProductListAPIView.as_view(),name='product-list'),
    path('product/retrieve/<int:pk>',ProductRetrieveAPIView.as_view(),name='product-retrieve')
]
