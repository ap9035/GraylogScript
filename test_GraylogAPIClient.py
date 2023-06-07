from unittest import TestCase
from GraylogAPIClient import GraylogAPIClient


class TestGraylogAPIClient(TestCase):
    def test_query(self):
        search_string = 'A128356'
        graylog_api_client = GraylogAPIClient('resources/mock_data.txt')
        search_result = graylog_api_client.query(search_string)
        self.assertEqual(len(search_result), 1)