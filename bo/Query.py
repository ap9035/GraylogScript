from typing import List

from Field import Field
from QueryResult import QueryResult
from GraylogAPIClient import GraylogAPIClient


class Query:
    def __init__(self, name: str, description: str, inputs: List[Field], outputs: List[Field]):
        self.name: str = name
        self.description: str = description
        self.inputs: List[Field] = inputs
        self.outputs: List[Field] = outputs
        self.graylog_api_client = GraylogAPIClient('../resources/mock_data.txt')

    def generate_search_string(self) -> str:
        search_string = ''
        for field in self.inputs:
            search_string += f'\"{field.value}\" '
        return search_string

    def run(self) -> List[dict]:
        search_string = self.generate_search_string()
        search_result = self.graylog_api_client.query(search_string)
        return search_result

    def extract(self, data: List[str]) -> List[QueryResult]:
        pass
