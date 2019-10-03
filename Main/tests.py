import json

from django.shortcuts import get_object_or_404
from django.test import TestCase

from rest_framework.test import APIClient

from .models import UrlObject, RequestHistory


from Main.serializers import UrlObjectSerializer, RequestHistorySerializer


class BaseTest(TestCase):
    client = APIClient()

    def setUp(self):
        if not self.get_all_from_table(UrlObject):
            urls_list = [
                {'id': 1, 'url': 'https://httpbin.org/range/50', 'interval': 5},
                {'id': 2, 'url': 'https://httpbin.org/range/25', 'interval': 45},
            ]
            self.model_create(UrlObject, urls_list)

        if not self.get_all_from_table(RequestHistory):
            url_object_1 = UrlObject.objects.get(id=1)
            requests_history_list = [
                {
                    'id': 1,
                    'response': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx',
                    'duration': 645738,
                    'created_at': '2019-10-01 21:03:01.579534',
                    'url_object': url_object_1,
                },
                {
                    'id': 2,
                    'response': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx',
                    'duration': 595376,
                    'created_at': '2019-10-01 21:03:06.579534',
                    'url_object': url_object_1,
                },
            ]
            self.model_create(RequestHistory, requests_history_list)

    @staticmethod
    def get_model_by_id(model, model_id):
        return model.objects.get(id=model_id)

    @staticmethod
    def model_create(model, params_list):
        for params in params_list:
            model.objects.create(**params)

    @staticmethod
    def get_all_from_table(model):
        return model.objects.all()


class UrlObjectTest(BaseTest):
    url = '/api/fetcher/'

    def test_1(self):
        """test_object_list"""
        response = self.client.get(self.url, format='json')
        url_list = UrlObject.objects.all()
        serializer = UrlObjectSerializer(url_list, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        """test_object_get"""
        response = self.client.get('{}1/'.format(self.url), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'url': 'https://httpbin.org/range/50', 'interval': 5})

    def test_3(self):
        """test_object_create"""
        request = {
            'id': 3,
            'url': 'https://httpbin.org/range/66',
            'interval': 11
        }
        response = self.client.post(self.url, request, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.get_model_by_id(UrlObject, 3).id, 3)

    def test_4(self):
        """test_object_update"""
        request = {
            'url': 'https://httpbin.org/range/25',
            'interval': 9
        }
        response = self.client.put('{}2/'.format(self.url), json.dumps(request), content_type='application/json', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_model_by_id(UrlObject, 2).interval, 9)

    def test_5(self):
        """test_object_delete"""
        with self.assertRaises(Exception) as exp:
            response = self.client.delete('{}1/'.format(self.url), format='json')
            self.assertEqual(response.status_code, 204)
            get_object_or_404(UrlObject, pk=1)
            self.assertTrue('No UrlObject matches the given query' in exp.exception)

    def test_6(self):
        """test_object_history"""
        response = self.client.get('{}1/history/'.format(self.url), format='json')
        requests_history_list = RequestHistory.objects.filter(url_object_id=1)
        serializer = RequestHistorySerializer(requests_history_list, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

