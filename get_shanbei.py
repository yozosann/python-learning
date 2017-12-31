from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from urllib.parse import urljoin
import re

class BranchHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹单词的表格
        if tag == 'table':
            for attr in attrs:
                if re.match(r'table', attr[1]):
                    self.flag = 1
                    break
        
        # 处理包裹单词名的strong元素
        if tag == 'strong' and self.flag == 1:
            self.is_get_data = 1

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'table':
            self.flag = 0
    
    def handle_data(self, data):
        if self.is_get_data and self.flag:
            self.res.append(data + '\n')
            print(data + '\n')
            self.is_get_data = None

class MasterHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹链接的div
        if tag == 'div':
            for attr in attrs:
                if re.match(r'wordlist', attr[1]):
                    self.flag = 1
                    break
        
        # 处理包裹单词名的strong元素
        if tag == 'a' and self.flag == 1:
            for attr in attrs:
                if attr[0] == 'href':
                    self.res.append(attr[1])

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'div':
            self.flag = 0

parserBranch = BranchHTMLParser()
parserMaster = MasterHTMLParser()

def getTXT(data):
    with open('./txt/cc.txt','w') as f:
        f.writelines(data)

with request.urlopen('https://www.shanbay.com/wordbook/104791/') as f:
    data = f.read().decode('utf-8')
    parserMaster.feed(data)
    urlList = parserMaster.res
    for url in urlList:
        for n in range(1, 11):       
            open_url = urljoin("https://www.shanbay.com/", url) + '?page=' + str(n)
            with request.urlopen(open_url) as f:
                data = f.read().decode('utf-8')
                parserBranch.feed(data)
        getTXT(parserBranch.res)

        

