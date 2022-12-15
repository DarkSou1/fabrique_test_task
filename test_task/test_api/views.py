from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (ClientSerializer, DistributionSerializer,
                          MessageSerializer, MessageCreateSerializer)
from .models import Distribution, Client, Message


class ClientViewList(APIView):
    """Отображение Клиента."""

    def get(self, request):
        """Получение клиентов."""
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Добавление клиента."""
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    """Отображение изменение параметров или удаление клиентаю."""

    def get_client(self, pk):
        return get_object_or_404(Client.objects.get(pk=pk))

    def get(self, request, pk):
        """Получение клиента."""
        client = self.get_client(pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        """Изменение параметров клиента."""
        client = self.get_client(pk=pk)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Удаление клиента."""
        client = self.get_client(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DistributionViewList(APIView):
    """Отображение списка рассылок."""

    def get(self, request):
        """Получение списка рассылок."""
        distribution = Distribution.objects.all()
        serializer = DistributionSerializer(distribution, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Добавление новой рассылки."""
        serializer = DistributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class DistributionDetail(APIView):
    """Отображение рассылки, изменение и обновление."""

    def get_distribution(self, pk):
        """Получение экзепляра рассылки."""
        return get_object_or_404(Distribution.objects.get(pk=pk))

    def get(self, request, pk):
        """Получение рассылки"""
        distribution = self.get_distribution(pk)
        serializer = DistributionSerializer(distribution)
        return Response(serializer.data)

    def put(self, request, pk):
        """Изменение существующей рассылки"""
        distribution = self.get_distribution(pk)
        serializer = DistributionSerializer(distribution,
                                            data=request.data,
                                            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Удаление рассылки."""
        distribution = self.get_distribution(pk)
        distribution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageViewList(APIView):
    """Отображение списка сообщении и создание сообщения."""

    def get(self, request):
        """Получение списка сообщении."""
        if 'distribution_id' in request.data:
            messages = Message.objects.filter(
                distribution_id=request.data['distribution_id']
            )
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Создание сообщения."""
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
