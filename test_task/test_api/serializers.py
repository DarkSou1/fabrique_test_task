from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Distribution, Client, Message


class ClientSerializer(serializers.ModelSerializer):
    """Сериализатор Клиента."""
    phone_number = serializers.CharField(max_length=11,
                                         validators=[
                                             UniqueValidator(
                                                 queryset=Client.objects.all())
                                         ]
                                         )

    class Meta:
        fields = ('id',
                  'phone_number',
                  'operator_code',
                  'tag',
                  'time_zone',)
        model = Client


class DistributionSerializer(serializers.ModelSerializer):
    """Сериализатор Рассылки."""
    data_time_start = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M",
        input_formats=["%d.%m.%Y %H:%M"])
    data_time_finish = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M",
        input_formats=["%d.%m.%Y %H:%M"]
    )
    messages = serializers.SerializerMethodField()
    status_messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        """Получение количества сообщений."""
        return obj.message.count()

    def get_status_messages(self, obj):
        """Получение количества отправленных сообщении."""
        return obj.message.filter(status=True).count()

    class Meta:
        model = Distribution
        fields = ('id',
                  'data_time_start',
                  'text',
                  'filter',
                  'data_time_finish',
                  'messages',
                  'status_messages')


class MessageSerializer(serializers.ModelSerializer):
    """Сериализатор отображения сообщений."""
    data_created = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M",
        input_formats=["%d.%m.%Y %H:%M"])
    status = serializers.BooleanField()
    client = ClientSerializer()
    distribution = DistributionSerializer()

    class Meta:
        model = Message
        fields = ('id',
                  'data_created',
                  'status',
                  'client',
                  'distribution',)


class MessageCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания сообщения."""
    data_created = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M",
        input_formats=["%d.%m.%Y %H:%M"])
    status = serializers.BooleanField(read_only=True)

    class Meta:
        model = Message
        fields = ('data_created', 'client',
                  'distribution', 'status')
