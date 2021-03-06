import unittest
from .. import views


class VideosViewsTestCases(unittest.TestCase):
    def test_home(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'Videos Page'
        # Run
        response = views.home(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)
