from rest_framework import serializers
from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ToDo