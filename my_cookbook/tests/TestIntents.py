import unittest

from my_cookbook.util import schema
from my_cookbook.tests import utils
from my_cookbook.util import requester
from my_cookbook.util import responder
from my_cookbook.skill import main

CONTEXT = {"debug": True}


class IntentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.delete_table('http://localhost:8000')

    def test_single_launch(self):
        r = requester.Request()
        event = r.with_type(requester.Types.LAUNCH).new().build()
        skill = main.Skill()
        response_dict = skill.handle_event(event, CONTEXT)

        self.assertTrue(responder.is_valid(response_dict))

    def test_multiple_launch(self):
        request = requester.Request().with_type(requester.Types.LAUNCH).new()

        for i in range(10):
            event = request.build()
            skill = main.Skill()
            response_dict = skill.handle_event(event, CONTEXT)
            self.assertTrue(responder.is_valid(response_dict))

    def test_single_end(self):
        r = requester.Request()
        event = r.with_type(requester.Types.END).new().build()
        skill = main.Skill()
        response_dict = skill.handle_event(event, CONTEXT)

        self.assertTrue(responder.is_valid(response_dict))

    def test_multiple_end(self):
        request = requester.Request().with_type(requester.Types.END).new()
        skill = main.Skill()

        for i in range(10):
            event = request.build()
            response_dict = skill.handle_event(event, CONTEXT)
            self.assertTrue(responder.is_valid(response_dict))

    def test_copy_attributes(self):
        request = requester.Request()
        response = responder.tell("test")
        request.copy_attributes(response)
        self.assertEqual(request.request['session']['attributes'],
                         response['sessionAttributes'])

    def test_all_new_intents(self):
        skill = main.Skill()
        for intent_name in schema.intents():
            intent = requester.Intent(intent_name).build()
            request = requester.Request().with_type(
                requester.Types.INTENT).new().with_intent(intent)
            event = request.build()
            response_dict = skill.handle_event(event, CONTEXT)
            self.assertTrue(responder.is_valid(response_dict))
