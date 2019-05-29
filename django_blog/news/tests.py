import unittest
from . import views


class HomeTestCase(unittest.TestCase):
    def test_home(self):
        # Setup.
        request = 'fake request'
        response_status = 200
        response_content = b'<h1>News Home</h1>'
        # Run.
        response = views.home(request)
        # Check.
        self.assertEqual(response.status_code, response_status)
        self.assertEqual(response.content, response_content)

    def test_about(self):
        # Setup.
        request = 'fake request'
        response_status = 200
        response_content = b'<h1>News About</h1>'
        # Run.
        response = views.about(request)
        # Check.
        self.assertEqual(response.status_code, response_status)
        self.assertEqual(response.content, response_content)