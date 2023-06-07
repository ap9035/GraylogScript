from unittest import TestCase
from bo.Query import Query
from bo.Field import Field


class TestQuery(TestCase):
    def test_generate_search_string(self):
        query_name = 'test_query'
        query_description = 'test query description'
        input_field1 = Field('message', 'A128356')
        input_field2 = Field('message', 'bbb')
        query_inputs = [input_field1, input_field2]
        query_outputs = []
        query = Query(query_name, query_description, query_inputs, query_outputs)
        search_string = query.generate_search_string()
        self.assertEqual(search_string, '"A128356" "bbb" ')

    def test_run(self):
        query_name = 'test_query'
        query_description = 'test query description'
        input_field1 = Field('message', 'A128356')
        input_field2 = Field('message', 'bbb')
        query_inputs = [input_field1, input_field2]
        query_outputs = []
        query = Query(query_name, query_description, query_inputs, query_outputs)
        query_result = query.run()
        self.assertEqual(len(query_result), 1)
