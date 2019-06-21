from requests_html import HTMLSession
#pip3 install requests-html

websites = {
            'https://www.magnapolonia.org',
            'https://wpolityce.pl',
            'https://www.tvn24.pl',
            'https://www.polsatnews.pl',
            'https://www.rt.com',
            'https://www.jpost.com',
            'https://www.washingtonpost.com',
            'https://www.aljazeera.com',
            'https://www.spiegel.de'
           }

words = {'trump', 'putin', 'merkel', 'macron', 'netanyahu', 'jinping', 'morawiecki'}
words = {'morawiecki'}

session = HTMLSession()

for website in websites:
  print('#####' + website + '####')
  r = session.get(website)
  for i in r.html.absolute_links:
    if any(word.lower() in i.lower() for word in words):
      print(i)
  print('#################')
