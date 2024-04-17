from django.urls import path
from .views import FoodListAPIView, FoodDetailAPIView, FoodCreateAPIView

# Swagger

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django REST_API  HomeWork",
        default_version='v1',
        description="Learn Django REST Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', FoodListAPIView.as_view(), name='list'),
    path('<int:pk>/', FoodDetailAPIView.as_view(), name="detail"),
    path('create/', FoodCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', FoodCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', FoodCreateAPIView.as_view(), name='create'),
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema_json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
