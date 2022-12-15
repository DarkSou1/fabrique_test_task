import datetime

from django.test import TestCase

from .models import Distribution, Client, Message

FIRST_OBJECT = 1


class TestDistributionModel(TestCase):
    offset = datetime.timedelta(hours=0)
    DATA_START = datetime.datetime(
        2022, 12, 15, 0, 0,
        tzinfo=datetime.timezone(offset, name='UTC'))
    TEST_TEXT = 'test_text'
    TEST_FILTER = 'FILTER'
    DATA_FINISH = datetime.datetime(
        2022, 12, 19, 0, 0,
        tzinfo=datetime.timezone(offset, name='UTC'))

    @classmethod
    def setUpTestData(cls):
        Distribution.objects.create(
            data_time_start=cls.DATA_START,
            text=cls.TEST_TEXT,
            filter=cls.TEST_FILTER,
            data_time_finish=cls.DATA_FINISH,
        )

    def get_distribution(self):
        """Получение тестовой рассылки."""
        return Distribution.objects.get(id=FIRST_OBJECT)

    def test_text_content(self):
        """Проверка текста рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.TEST_TEXT,
                         distribution.text)

    def test_filter_content(self):
        """Проверка фильтра рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.TEST_FILTER,
                         distribution.filter)

    def test_data_time_start_content(self):
        """Проверка правильности начала рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.DATA_START,
                         distribution.data_time_start)

    def test_data_time_finish_content(self):
        """Проверка правильности конца рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.DATA_FINISH,
                         distribution.data_time_finish)


class TestClientModel(TestCase):
    TEST_PHONE_NUMBER = '71234567899'
    TEST_OPERATOR_CODE = '123'
    TEST_TAG = 'test_tag'
    TEST_TIMEZONE = 'UTC'

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            phone_number=cls.TEST_PHONE_NUMBER,
            operator_code=cls.TEST_OPERATOR_CODE,
            tag=cls.TEST_TAG,
            time_zone=cls.TEST_TIMEZONE,
        )

    def get_client(self):
        """Получение клиента."""
        return Client.objects.get(id=FIRST_OBJECT)

    def test_phone_number_content(self):
        """Проверка телефона клиента."""
        client = self.get_client()
        self.assertEqual(self.TEST_PHONE_NUMBER,
                         client.phone_number)

    def test_operator_code(self):
        """Проверка кода оператора."""
        client = self.get_client()
        self.assertEqual(self.TEST_OPERATOR_CODE,
                         client.operator_code)

    def test_tag_content(self):
        """Проверка тега клиента."""
        client = self.get_client()
        self.assertEqual(self.TEST_TAG, client.tag)

    def test_time_zone_content(self):
        """Проверка временной зоны клиента."""
        client = self.get_client()
        self.assertEqual(self.TEST_TIMEZONE, client.time_zone)


# class TestMessageModel(TestCase):
#     offset = datetime.timedelta(hours=0)
#     TEST_DATA_CREATED = datetime.datetime(
#         2022, 12, 15, 0, 0,
#         tzinfo=datetime.timezone(offset, name='UTC'))
#     TEST_STATUS = True
#     dist = TestDistributionModel.get_distribution(TestDistributionModel())
#     TEST_DISTRIBUTION = dist
#     client = TestClientModel()
#     TEST_CLIENT = TestClientModel.get_client(client)
#
#     @classmethod
#     def setUpTestData(cls):
#         Message.objects.create(
#             data_created=cls.TEST_DATA_CREATED,
#             status=cls.TEST_STATUS,
#             distribution=cls.TEST_DISTRIBUTION,
#             client=cls.TEST_CLIENT,
#         )
#
#     def get_message(self):
#         return Message.objects.get(id=FIRST_OBJECT)
#
#     # def test_data_created_content(self):
#     #     message = self.get_message()
#     #     self.assertEqual(self.TEST_DATA_CREATED, message.data_created)
