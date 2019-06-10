import unittest, json
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

    def test_second_post(self):
        # Setup
        user = User.objects.create_user('PostUser2', 'PostUser2@gmail.com', '1234')
        topic = 'testTitle2'
        message = 'testContent2'
        # Run
        post = models.Post(title=topic, content=message, author_id=user.id)
        post.save()
        # Check
        self.assertEqual(topic, models.Post.objects.last().title)
        self.assertEqual(message, models.Post.objects.last().content)

    def test_json_post(self):
        # Setup
        with open('blog/tests/posts.json') as f:
            posts_json = json.load(f)
        # At least 2 users needed
        user1 = User.objects.create_user('PostUser3', 'PostUser3@gmail.com', '1234')
        user2 = User.objects.create_user('PostUser4', 'PostUser4@gmail.com', '1234')
        for post_json in posts_json:
            # Run
            post = models.Post(title=post_json['title'], content=post_json['content'], author_id=post_json['user_id'])
            post.save()
            # Check
            self.assertEqual(post_json['title'], models.Post.objects.last().title)
            self.assertEqual(post_json['content'], models.Post.objects.last().content)
