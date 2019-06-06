import unittest
from .. import models
from django.contrib.auth.models import User


class UsersModelsTestCases(unittest.TestCase):
    def test_first_user_profile(self):
        # Setup
        name = 'UsersTestUser'
        mail = name + '@mail.com'
        password = '1234'
        image_url = 'profile_pics/default.jpg'
        image_url_prefix = '/media/'
        # Run
        test_user = User.objects.create_user(name, mail, password)
        response = User.objects.filter(username=name).first()
        # Check
        self.assertEqual(response, test_user)
        # Run
        # Lines below are done automatically by signals.py and this is why
        # are commented out here.
        #test_profile = models.Profile(user=test_user, image=image_url)
        #test_profile.save()
        # Check
        #self.assertEqual(test_profile, test_user.profile)
        self.assertEqual(image_url_prefix + image_url, test_user.profile.image.url)
