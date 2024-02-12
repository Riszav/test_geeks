from rest_framework import serializers
from rest_framework.response import Response
from .models import Task
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = Task
        fields = 'id title description completed created'.split()

