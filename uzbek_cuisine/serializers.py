from rest_framework import serializers

from .models import Food, Category


class FoodSerializers(serializers.ModelSerializer):
    food_detail = serializers.SerializerMethodField(read_only=True, source='get_food_detail')

    class Meta:
        model = Food
        fields = ['id', 'food_name', 'food_price', 'food_category', 'food_detail']
        depth = 1

    def get_food_detail(self, obj):
        return f"http://localhost:8000/api/v1/food/{obj.id}"


class FoodDetailSerializer(serializers.ModelSerializer):
    food_category_info = serializers.SerializerMethodField(read_only=True, source='get_food_category_info')

    class Meta:
        model = Food
        fields = '__all__'

    def get_food_category_info(self, obj):
        info = {
            'category_id': obj.food_category.id,
            'category_name': obj.food_category.category_name
        }
        return info
