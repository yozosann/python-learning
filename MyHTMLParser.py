from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    count = 0

    def handle_starttag(self, tag, attrs):
        self.count += 1
        print('<%s> %d' % (tag, self.count))

    def handle_endtag(self, tag):
        self.count += 1
        print('</%s> %d' % (tag, self.count))

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        self.count += 1
        print('%s - %d' % (data, self.count))

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')