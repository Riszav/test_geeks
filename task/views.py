from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error': 'Director not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = TaskSerializer(task).data
        return Response(data=data)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        task.title = serializer.validated_data.get('title')
        task.description = serializer.validated_data.get('title')
        task.completed = serializer.validated_data.get('completed')
        task.save()
        return Response(data={'task_id': task.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def task_list_api_view(request):
    if request.method == 'GET':
        # print(request.data.get('bool'))
        # Step 1: Collect data of products from DB
        task = Task.objects.all()

        # Step 2: Reformat(Serialize) of products
        data = TaskSerializer(task, many=True).data

        # Step 3: Return data as JSON
        return Response(data=data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data.get('name')

        task = Task.objects.create(**serializer.validated_data)

        return Response(data={'task_id': task.id}, status=status.HTTP_201_CREATED)

