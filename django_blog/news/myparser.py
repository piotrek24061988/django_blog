from requests_html import HTMLSession
import unittest
#pip3 install requests-html


class LinksFinder:
    def __init__(self, words, sources):
        self.words = set(words)
        self.sources = set(sources)

    def printSources(self):
        print(self.sources)

    def printWords(self):
        print(self.words)

    def addSource(self, source):
        if source not in self.sources:
            self.sources.add(source)

    def removeSource(self, source):
        if source in self.sources:
            self.sources.remove(source)

    def addWord(self, word):
        if word not in self.words:
            self.words.add(word)

    def removeWord(self, word):
        if word in self.words:
            self.words.remove(word)

    def findLinks(self):
        session = HTMLSession()
        returnLinks = {}
        for source in self.sources:
            print('#####' + source + '####')
            for link in session.get(source).html.absolute_links:
                if any(word.lower() in link.lower() for word in self.words):
                    returnLinks[link] = source
        session.close()
        return returnLinks


websites = [
            'https://www.magnapolonia.org',
            'https://www.magnapolonia.org',
            'https://wpolityce.pl',
            'https://www.tvn24.pl',
            'https://www.polsatnews.pl',
            'https://www.rt.com',
            'https://www.jpost.com',
            'https://www.washingtonpost.com',
            'https://www.aljazeera.com',
            'https://www.spiegel.de'
           ]

words = ['polska', 'polska', 'polski', 'polskie', 'poland', 'polish', 'polnish', 'polen']


class NewsModelTestCases(unittest.TestCase):
    def test_find_some_links_containing_words(self):
        # Setup
        linksFinder = LinksFinder(words, websites)
        # Run
        linksFinder.printSources()
        linksFinder.printWords()
        print(linksFinder.findLinks())
        # Check
        self.assertNotEqual({}, linksFinder.findLinks())

    def test_find_links_empty_words(self):
        # Setup
        linksFinder = LinksFinder([], websites)
        # Run
        linksFinder.printSources()
        linksFinder.printWords()
        print(linksFinder.findLinks())
        # Check
        self.assertEqual({}, linksFinder.findLinks())
        # Run
        linksFinder.addWord('pol')
        print(linksFinder.findLinks())
        # Check
        self.assertNotEqual({}, linksFinder.findLinks())
        # Run
        linksFinder.removeWord('pol')
        print(linksFinder.findLinks())
        # Check
        self.assertEqual({}, linksFinder.findLinks())

    def test_find_links_empty_source(self):
        # Setup
        linksFinder = LinksFinder(words, [])
        # Run
        linksFinder.printSources()
        linksFinder.printWords()
        print(linksFinder.findLinks())
        # Check
        self.assertEqual({}, linksFinder.findLinks())
        # Run
        linksFinder.addSource('https://wpolityce.pl')
        # Check
        self.assertNotEqual({}, linksFinder.findLinks())
        # Run
        linksFinder.removeSource('https://wpolityce.pl')
        # Check
        self.assertEqual({}, linksFinder.findLinks())

    def test_find_empty_words_empty_source(self):
        # Setup
        linksFinder = LinksFinder([], [])
        # Run
        linksFinder.printSources()
        linksFinder.printWords()
        print(linksFinder.findLinks())
        # Check
        self.assertEqual({}, linksFinder.findLinks())


if __name__ == "__main__":
    unittest.main()
