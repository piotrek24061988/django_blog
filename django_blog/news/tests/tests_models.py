import unittest
from .. import models


class NewsModelTestCases(unittest.TestCase):
    def test_first_source(self):
        # Setup
        source = 'wpolityce'
        website = 'https://wpolityce.pl/'
        land = 'Poland'
        # Run
        test_source = models.Source(title=source, link=website, country=land)
        test_source.save()
        # Check
        self.assertEqual(source, models.Source.objects.last().title)
        self.assertEqual(website, models.Source.objects.last().link)
        self.assertEqual(land, models.Source.objects.last().country)

    def test_second_source(self):
        # Setup
        source = 'tvn'
        website = 'https://www.tvn24.pl/'
        land = 'Poland'
        # Run
        test_source = models.Source(title=source, link=website, country=land)
        test_source.save()
        # Check
        self.assertEqual(source, models.Source.objects.last().title)
        self.assertEqual(website, models.Source.objects.last().link)
        self.assertEqual(land, models.Source.objects.last().country)

    def test_first_news(self):
        # Setup
        source = 'magnapolonia'
        website = 'https://www.magnapolonia.org'
        land = 'Poland'
        message_title = 'W Niemczech ukarano ksiedza za brak akceptacji homoseksualizmu'
        message_link = 'https://www.magnapolonia.org/w-niemczech-ukarano-ksiedza-za-brak-akceptacji-homoseksualizmu/'
        message_title2 = 'Wegierski rzad ma zamiar wspierac ekspansje wegierskiej kultury na zakarpaciu'
        message_link2 = 'https://www.magnapolonia.org/wegierski-rzad-ma-zamiar-wspierac-ekspansje-wegierskiej-kultury-na-zakarpaciu/'
        # Run
        test_source = models.Source(title=source, link=website, country=land)
        test_source.save()
        test_news = models.News(title=message_title, link=message_link, source=test_source)
        test_news.save()
        # Check
        self.assertEqual(message_title, models.News.objects.last().title)
        self.assertEqual(message_link, models.News.objects.last().link)
        # Run
        test_news2 = models.News(title=message_title2, link=message_link2, source=test_source)
        test_news2.save()
        # Check
        self.assertEqual(message_title2, models.News.objects.last().title)
        self.assertEqual(message_link2, models.News.objects.last().link)
