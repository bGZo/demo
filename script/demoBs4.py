# Don't name bs4 to your file, which will not found the lib file...
# see https://stackoverflow.com/questions/47958281/importerror-cannot-import-name-beautifulsoup
from bs4 import BeautifulSoup
# import bs4


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')


temp = soup.get_text()

# soup.find(id="link3").get('href')
# soup.p['class']
# soup.prettify()

print(temp)