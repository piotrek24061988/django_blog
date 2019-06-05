import unittest
from .. import views


class RequestStub:
    class USER:
        def is_authenticated(self):
            return True

    META = {'CSRF_COOKIE': []}
    user = USER

    def method(self):
        pass


class UsersViewsTestCases(unittest.TestCase):
    def test_register(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Register Title'
        # Run
        response = views.register(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_profile_authenticated(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Profile Title'
        # Run
        request.USER.authenticated = True
        response = views.profile(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)
