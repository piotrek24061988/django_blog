import unittest
from .. import views
from .. import models
from django.contrib.auth.models import User


class PostTestCase(unittest.TestCase):
    def test_user_empty(self):
        # Setup.
        user = None
        # Run.
        response = User.objects.filter(username=user).first()
        # Check.
        self.assertEqual(response, user)

    def test_first_user(self):
        # Setup.
        name = 'TestUSer'
        mail = name + '@mail.com'
        password = '1234'
        # Run
        user = User.objects.create_user(name, mail, password)
        response = User.objects.filter(username=name).first()
        self.assertEqual(response, user)
