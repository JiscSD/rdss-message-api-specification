from tests.abstract_schema_validator_test import AbstractSchemaValidatorTest
from unittest import TestCase


class MessageHeaderTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'messages/header/header_schema.json'

    def runTest(self):
        self.validate_json('messages/header/header.json')
