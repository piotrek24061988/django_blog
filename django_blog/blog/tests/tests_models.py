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
        user = None
        with open('blog/tests/posts.json') as f:
            posts_json = json.load(f)
        # Run
        if not User.objects.filter(email=username1 + '@gmail.com').exists():
            user = User.objects.create_user(username1, username1 + '@gmail.com', '1234')
        else:
            user = User.objects.get(username=username1)
        response = User.objects.filter(username=username1).first()
        # Check
        self.assertEqual(response, user)
        # Run
        if not User.objects.filter(email=username2 + '@gmail.com').exists():
            user = User.objects.create_user(username2, username2 + '@gmail.com', '1234')
        else:
            user = User.objects.get(username=username2)
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
