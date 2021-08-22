from rest_framework import views
from todo.models import ToDo
from api.serializer import ToDoSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404



class ToDoList(views.APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        # todos = ToDo.objects.filter(author=request.user)
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response({'todo': serializer.data})

    def post(self, request):
        serializer = ToDoSerializer(
            data={**request.data, 'author': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response({'todo': serializer.data})
        return Response(serializer.errors, status=400)


class ToDoEdit(views.APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, todo_id):
        todo = get_object_or_404(ToDo.objects.all(), id=todo_id)

        if todo.author_id != request.user.id:
            return Response({'detail': 'unauthorized'}, status=403)

        serializer = ToDoSerializer(
            instance=todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'todo': serializer.data})

        return Response(serializer.errors, status=400)














