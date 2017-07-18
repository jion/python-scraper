from dombuilder import DomBuilder
from dom import SimpleDOM

from urllib2 import urlopen

# Scrapper responsability:
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

def defaultUrlScrapper(url):
    reader = urlopen(url)

    dom = SimpleDOM()
    domBuilder = DomBuilder(dom)

    return Scraper(reader, domBuilder)

class Scraper(object):
    """
    This class orchestrates the whole proccess of Scrapping the specified HTML.
    You can customize the proccess adding Operations that will be executed on
    the fly while the DOM object is created from parsing the HTML page.
    When results are ready this will output the results in a decoupled fashion
    passing the desired implementation of a printer to the printResults function.

    The initializer receives an object that accepts file protocol.
    """
    def __init__(self, reader, domBuilder):
        self.operations = []
        self.domBuilder = domBuilder
        self.reader = reader

    def addOperation(self, operation):
        operation.attachTo(self.domBuilder)
        self.operations.append(operation)
        return self

    def _feed_parser(self):
        # TODO: The feed could be decoupled in order to implement
        # other ways to feed the parser (read chunks instead read
        # at all once on memory, etc). But this is enough for the
        # purpose of this example
        html = self.reader.read() 
        self.domBuilder.feed(html)
        
    def run(self):
        self._feed_parser()

    def printResults(self, printer):
        for operation in self.operations:
            printer.printResults( operation )

