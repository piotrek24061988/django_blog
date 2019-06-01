import unittest
from .. import views


class HomeTestCase(unittest.TestCase):
    def test_home(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'News Title'
        # Run
        response = views.home(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'About Page'
        # Run
        response = views.about(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)
