from rest_framework import serializers
from .models import Task, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    is_overdue = serializers.ReadOnlyField()
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'created_at', 'updated_at',
            'due_date', 'status', 'priority', 'completed_at',
            'category', 'category_name', 'owner_username', 'is_overdue'
        ]
        read_only_fields = ['created_at', 'updated_at', 'completed_at', 'owner']