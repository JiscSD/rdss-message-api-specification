from tests.abstract_schema_validator_test import AbstractSchemaValidatorTest
from unittest import TestCase


class MessageTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'messages/message_schema.json'

    def runTest(self):
        self.validate_json('messages/message.json')
