import datetime

from django.test import TestCase

from .models import Distribution, Client

FIRST_OBJECT = 1


class TestDistributionModel(TestCase):
    offset = datetime.timedelta(hours=0)
    data_time_start = datetime.datetime(
        2022, 12, 15, 0, 0,
        tzinfo=datetime.timezone(offset, name='UTC'))
    text = 'test_text'
    test_filter = 'FILTER'
    data_time_finish = datetime.datetime(
        2022, 12, 19, 0, 0,
        tzinfo=datetime.timezone(offset, name='UTC'))

    @classmethod
    def setUpTestData(cls):
        Distribution.objects.create(
            data_time_start=cls.data_time_start,
            text=cls.text,
            filter=cls.test_filter,
            data_time_finish=cls.data_time_finish,
        )

    def get_distribution(self):
        """Получение тестовой рассылки."""
        return Distribution.objects.get(id=FIRST_OBJECT)

    def test_text_content(self):
        """Проверка текста рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.text, distribution.text)

    def test_filter_content(self):
        """Проверка фильтра рассылки."""
        distribution = self.get_distribution()
        self.assertEqual(TestDistributionModel.test_filter, distribution.filter)

    # def test_data_time_start_content(self):
    #     """Проверка правильности начала рассылки."""
    #     distribution = self.get_distribution()
    #     self.assertEqual(TestDistributionModel.data_time_start, distribution.data_time_start)
    #
    # def test_data_time_finish_content(self):
    #     """Проверка правильности конца рассылки."""
    #     distribution = self.get_distribution()
    #     self.assertEqual(TestDistributionModel.data_time_finish, distribution.data_time_finish)


# class TestClientModel(TestCase):
#     TEST_PHONE_NUMBER = '71234567899'
#     TEST_OPERATOR_CODE = '123'
#     TEST_TAG = 'test_tag'
#     TEST_TIMEZONE = 'UTC'
#
#     @classmethod
#     def setUpTestData(cls):
#         Client.objects.create(
#             phone_number=cls.TEST_PHONE_NUMBER,
#             operartor_code=cls.TEST_OPERATOR_CODE,
#             tag=cls.TEST_TAG,
#             timezone=cls.TEST_TIMEZONE,
#         )
#
#     def get_client(self):
#         return Client.objects.get(id=FIRST_OBJECT)
#
#     def test_phone_number_content(self):
#         client = self.get_client()
#         self.assertEqual(self.TEST_PHONE_NUMBER, client.phone_number)


