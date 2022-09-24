from django.urls import path
from apps.products.api.views.general_views import CategoryListAPIView, CategoryRetrieveAPIView, SubCategoryListAPIView, SubCategoryRetrieveAPIView

urlpatterns = [
    # Métodos listar y buscar
    path('category/list/',CategoryListAPIView.as_view(),name='category-list'),
    path('category/retrieve/<int:pk>',CategoryRetrieveAPIView.as_view(),name='category-retrieve'),
    path('sub-category/list/', SubCategoryListAPIView.as_view(),name='sub-category-list'),
    path('sub-category/retrieve/<int:pk>',SubCategoryRetrieveAPIView.as_view(),name='sub-category-retrieve')
]
