import unittest, json
from .. import models


class NewsModelTestCases(unittest.TestCase):
    def test_json__source_news(self):
        # Setup
        with open('news/tests/source.json') as f:
            sources_json = json.load(f)
        for source_json in sources_json:
            # Run
            test_source = models.Source(title=source_json['source'], link=source_json['website'], country=source_json['land'])
            test_source.save()
            # Check
            self.assertEqual(source_json['source'], models.Source.objects.last().title)
            self.assertEqual(source_json['website'], models.Source.objects.last().link)
            self.assertEqual(source_json['land'], models.Source.objects.last().country)
        # Setup
        with open('news/tests/news.json') as f:
            newses_json = json.load(f)
        for news_json in newses_json:
            # Run
            test_news = models.News(title=news_json['title'], link=news_json['link'], source_id=news_json['source_id'])
            test_news.save()
            # Check
            self.assertEqual(news_json['title'], models.News.objects.last().title)
            self.assertEqual(news_json['link'], models.News.objects.last().link)
