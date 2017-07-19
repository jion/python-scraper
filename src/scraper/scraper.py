from dombuilder import DomBuilder
from dom import SimpleDOM

from urllib2 import urlopen, URLError, HTTPError

# Scraper responsability:
# orquestate the steps of the scraping process:
# Construction phase:
# 1. create the proper reader (input)
# 2. construct the HTML parser
# 3. customize the HTML parser adding operations
# 4. construct the Printer
#
# Running phase:
# 1. obtain an html input
# 2. pass the input to de HTML parser
# 3. Run the purser.
# 4. Print the results

def simpleUrlReader(url, consumer):
    """
    This function handle the process of reading from an url
    and passing data to a consumer (via a feed method on the
    consumer).
    I would wish to do this asynchronic, but for now it takes
    the whole HTML at once and just then pass it to the consumer.
    The function is decoupled for the Scraper class in order to be able
    to support another types of feeding (maybe html file, etc)
    """
    try:
        handler = urlopen(url)
        html = handler.read()
    except HTTPError, e:
        raise Exception("There was a problem getting the specified url - HTTP code %s" % e.code)
    except URLError, e:
        raise Exception("There was a problem getting the specified url:  %s" % str(e))
    else:
        #####################
        consumer.feed(html) #
        #####################


def defaultUrlScraper(url):
    reader = simpleUrlReader

    dom = SimpleDOM()
    domBuilder = DomBuilder(dom)

    scraper = Scraper(reader, domBuilder)
    scraper.setUrl(url)

    return scraper

class Scraper(object):
    """
    This class orchestrates the whole proccess of Scrapping the specified HTML.
    You can customize the proccess adding Operations that will be executed on
    the fly while the DOM object is created from parsing the HTML page.
    When results are ready this will output the results in a decoupled fashion
    passing the desired implementation of a printer to the printResults function.

    The initializer receives an object that accepts file protocol.
    """

    url = None

    def __init__(self, reader, domBuilder):
        self.operations = []
        self.domBuilder = domBuilder
        self.reader = reader

    def setUrl(self, url):
        self.url = url

    def addOperation(self, operation):
        operation.attachTo(self.domBuilder.dom)
        self.operations.append(operation)
        return self

    def _feed_parser(self):
        """
        This is the core method of all the scraper application.
        It feeds the builder with the HTML data, who will build
        a dom representation and doing analysis on the fly.
        """
        self.reader(self.url, self.domBuilder)
        
    def run(self):
        if self.url == None:
            raise Exception("Scraper Error - URL missing")

        self._feed_parser()

    def printResults(self, printer):
        for operation in self.operations:
            printer.printResults( operation )

