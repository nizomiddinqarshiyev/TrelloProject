from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    Board, Card, Task
)
from .serializers import BoardSerializer, CardSerializer, TaskSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk):
        board = Board.objects.get(pk=pk)
        board.updated_at = datetime.now()
        board.save()
        board_serializer = self.get_serializer(board)
        return Response(board_serializer.data)

    def partial_update(self, request, pk):
        board = Board.objects.get(pk=pk)
        board.updated_at = datetime.now()
        board.save()
        board_serializer = self.get_serializer(board)
        return Response(board_serializer.data)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
