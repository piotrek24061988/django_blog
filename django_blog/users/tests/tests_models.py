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

    def test_str(self):
        # Setup
        name = 'UsersTestUser2'
        mail = name + '@mail.com'
        password = '1234'
        image_url = 'profile_pics/default.jpg'
        profile_str = 'Profile'
        # Run
        test_user = User.objects.create_user(name, mail, password)
        response = User.objects.filter(username=name).first()
        # Check
        self.assertEqual(response, test_user)
        # Run
        test_profile = models.Profile(user=test_user, image=image_url)
        # Check
        self.assertEqual(test_profile.__str__(), name + profile_str)
