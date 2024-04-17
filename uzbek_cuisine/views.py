from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Food, Category
from .serializers import FoodSerializers, FoodDetailSerializer


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class FoodDetailAPIView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer


class FoodCreateAPIView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer


class FoodUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    permission_classes = [IsAdminUser]


class FoodDeleteAPIView(DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    permission_classes = [IsAdminUser]
