import unittest
from .. import views


class RequestStub:
    META = {'CSRF_COOKIE': []}

    def method(self):
        pass


class UsersViewsTestCases(unittest.TestCase):
    def test_home(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Register Title'
        # Run
        response = views.register(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)