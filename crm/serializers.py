from rest_framework import serializers

from .models import Customer, Category, Event


class EventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "active"]


class CustomerSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    category = CategorySerializer(read_only=True)
    event_set = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
        depth = 1
