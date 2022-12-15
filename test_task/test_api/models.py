import os
from datetime import datetime
import requests
import json

from django.db import models
from .validators import PhoneNumberValidator


class Distribution(models.Model):
    """Модель рассылки."""
    id = models.IntegerField(verbose_name='ID_рассылки',
                             primary_key=True, )
    data_time_start = models.DateTimeField(
        verbose_name='Дата_и_время_старта')
    text = models.TextField(
        verbose_name='Текст рассылки', max_length=4096, )
    filter = models.CharField(
        verbose_name='Фильтр свойств клиентов',
        max_length=256)
    data_time_finish = models.DateTimeField(
        verbose_name='Дата_и_время_окончания'
    )

    def get_not_sending_messages(self):
        """Получение не отправленных сообщений."""
        return self.message.filter(status=False)

    def time(self):
        start = self.data_time_start
        finish = self.data_time_finish
        if start.timestamp() < datetime.now().timestamp() < finish.timestamp():
            return True

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('-id',)


class Client(models.Model):
    """Модель клиента."""
    id = models.IntegerField(verbose_name='ID_клиента',
                             primary_key=True)
    phone_number = models.CharField(verbose_name='Номер клиента',
                                    max_length=11,
                                    validators=(PhoneNumberValidator(),))
    operator_code = models.CharField(verbose_name='Код оператора',
                                     max_length=11)
    tag = models.CharField(verbose_name='Тег_(произвольная_метка)',
                           max_length=25)
    time_zone = models.CharField(verbose_name='Часвой_пояс_клиента',
                                 max_length=25)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('-id',)


class Message(models.Model):
    """Модель сообщения."""
    id = models.IntegerField(verbose_name='ID_сообщения',
                             primary_key=True)
    data_created = models.DateTimeField(verbose_name='Дата создания')
    status = models.BooleanField(verbose_name='Статус_отправки',
                                 default=False, )
    distribution = models.ForeignKey(Distribution,
                                     on_delete=models.CASCADE,
                                     related_name='message')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='message')

    def is_status(self):
        """Смена статуса на отправленный."""
        self.status = True
        self.save()

    def create_now(self):
        """Отправить."""
        self.data_created = datetime.now()
        self.save()

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('id',)


def get_distributions():
    return [dist for dist in Distribution.objects.all()
            if (dist.time() and dist.get_not_sending_messages().exists())]


def sending_message(message, phone_number, text):
    url = f'https://probe.fbrq.cloud.v1/send/{message}'
    test_token = os.getenv('test_token')
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {test_token}',
        'Content-Type': 'application/json',
    }
    values = {
        'id': message,
        'phone_number': phone_number,
        'text': text,
    }
    return requests.post(url=url,
                         data=json.dumps(values),
                         headers=headers).status_code
