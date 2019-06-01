import unittest
from .. import views
from .. import models
from django.contrib.auth.models import User


class PostTestCase(unittest.TestCase):
    def test_first(self):
        # Setup.
        request = 'dummy'
        # Run.
        response = 'dummy'
        # Check.
        self.assertEqual(response, request)