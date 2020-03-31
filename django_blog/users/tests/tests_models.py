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
        testProfile = None
        # Run
        if not User.objects.filter(email=mail).exists():
            test_user = User.objects.create_user(name, mail, password)
        else:
            test_user = User.objects.get(username=name)
        response = User.objects.filter(username=name).first()
        print(test_user.profile.image.url)
        # Check
        self.assertEqual(response, test_user)
        # Run
        if not models.Profile.objects.filter(user=test_user).exists():
            testProfile = models.Profile(user=test_user, image=image_url)
            testProfile.save()
        else:
            testProfile = models.Profile.objects.get(user=test_user)
        # Check
        self.assertEqual(testProfile, test_user.profile)
        self.assertEqual(image_url_prefix + image_url, test_user.profile.image.url)

    def test_str(self):
        # Setup
        name = 'UsersTestUser2'
        mail = name + '@mail.com'
        password = '1234'
        image_url = 'profile_pics/default.jpg'
        profile_str = 'Profile'
        testProfile = None
        # Run
        if not User.objects.filter(email=mail).exists():
            test_user = User.objects.create_user(name, mail, password)
        else:
            test_user = User.objects.get(username=name)
        response = User.objects.filter(username=name).first()
        # Check
        self.assertEqual(response, test_user)
        # Run
        if not models.Profile.objects.filter(user=test_user).exists():
            testProfile = models.Profile(user=test_user, image=image_url)
            testProfile.save()
        else:
            testProfile = models.Profile.objects.get(user=test_user)
        # Check
        self.assertEqual(testProfile.__str__(), name + profile_str)
