import unittest
from .. import models
from django.contrib.auth.models import User


class UsersModelsTestCases(unittest.TestCase):
    def test_first_user_profile(self):
        # Setup
        name = 'UsersTestUser'
        mail = name + '@mail.com'
        password = '1234'
        # Run
        test_user = User.objects.create_user(name, mail, password)
        response = User.objects.filter(username=name).first()
        # Check
        self.assertEqual(response, test_user)
        # Run
        #test_profile = models.Profile(user=test_user, image=None)
        #test_profile.save()
        # Check
        #self.assertEqual(test_profile, test_user.profile)
        #self.assertEqual(None, test_user.profile.image)