import unittest
from .. import views


class RequestStub:
    class USER:
        def is_authenticated(self):
            return True

    META = {'CSRF_COOKIE': []}
    user = USER
    method = 'POST'
    POST = {'POST': {}}


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

    def test_profile_post(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Profile Title'
        # Run
        response = views.profile(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_profile_get(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Profile Title'
        # Run
        request.method = 'GET'
        response = views.profile(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)
