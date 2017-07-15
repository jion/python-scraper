#!/usr/bin/env python2.7

import urllib2
from HTMLParser import HTMLParser

def getHTML(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

class MyHTMLParser(HTMLParser, object):
    tags = {}
    def __init__(self):
        super(MyHTMLParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        print "<", tag,">"
        if tag in self.tags:
            self.tags[tag] += 1
        else:
            self.tags[tag]  = 1

    def handle_endtag(self, tag):
        print "</", tag, ">"

    def handle_data(self, data):
        pass

    def printTags(self):
        print "# of tags: %d" % len(self.tags) 
        print self.tags
        print "Top 5 tags: "
        topFive =  [v[0] for v in sorted(self.tags.iteritems(), key=lambda(k, v): (-v, k))]
        for tag in topFive[:5]:
            print "%s: %d ocurrences" % (tag, self.tags[tag])
    

def main():
    #sys.argv = [sys.argv[0]]+["--open_browser", "default_browser"]+sys.argv[1:]
    html = getHTML("http://ordergroove.com/company")
    myParser = MyHTMLParser()
    myParser.feed(html)
    myParser.printTags()


if __name__ == '__main__':
    main()
