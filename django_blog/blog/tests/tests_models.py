import unittest
from .. import models
from django.contrib.auth.models import User


class BlogModelsTestCases(unittest.TestCase):
    def test_user_empty(self):
        # Setup
        user = None
        # Run
        response = User.objects.filter(username=user).first()
        # Check
        self.assertEqual(response, user)

    def test_first_user(self):
        # Setup
        name = 'TestUser'
        mail = name + '@mail.com'
        password = '1234'
        # Run
        user = User.objects.create_user(name, mail, password)
        response = User.objects.filter(username=name).first()
        # Check
        self.assertEqual(response, user)

    def test_first_post(self):
        # Setup
        user = User.objects.create_user('PostUser', 'PostUser@gmail.com', '1234')
        topic = 'testTitle'
        message = 'testContent'
        # Run
        post = models.Post(title=topic, content=message, author_id=user.id)
        post.save()
        # Check
        self.assertEqual(topic, models.Post.objects.last().title)
        self.assertEqual(message, models.Post.objects.last().content)
