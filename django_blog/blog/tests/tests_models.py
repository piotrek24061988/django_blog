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

    def test_json_post(self):
        # Setup
        username1 = 'PostUser1'
        username2 = 'PostUser2'
        with open('blog/tests/posts.json') as f:
            posts_json = json.load(f)
        # Run
        user = User.objects.create_user(username1, username1 + '@gmail.com', '1234')
        response = User.objects.filter(username=username1).first()
        # Check
        self.assertEqual(response, user)
        # Run
        user = User.objects.create_user(username2, username2 + '@gmail.com', '1234')
        response = User.objects.filter(username=username2).first()
        # Check
        self.assertEqual(response, user)
        # ---------------------------------------------------------------------------
        for post_json in posts_json:
            # Run
            post = models.Post(title=post_json['title'], content=post_json['content'], author_id=post_json['user_id'])
            post.save()
            # Check
            self.assertEqual(post_json['title'], models.Post.objects.last().title)
            self.assertEqual(post_json['content'], models.Post.objects.last().content)
