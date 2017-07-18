#!/usr/bin/env python2.7

import sys
sys.path.append('./lib')

from scraper.operations import CountNumberOfElements, ListOcurrences
from scraper.resultprinters import ConsolePrinter
from scraper.scraper import defaultUrlScraper as Scraper


url = "http://ordergroove.com/company"

def main():
    """
    This runs an example petition to the scraper
    asking for the number of html elements and the
    5 most used tags on the page that is stored in
    global variable "url").
    Scraper was made in a way to be extendable by
    Operations, and also the output was decoupled using an abstract
    printer (only consoleOutput was implemented by now)
    """

    # Setting up & Running the Scraper
    scraper = Scraper(url)

    scraper.addOperation(CountNumberOfElements())
    scraper.addOperation(ListOcurrences(limit=5))

    scraper.run()

    # Printing results
    consolePrinter = ConsolePrinter()
    scraper.printResults(consolePrinter)


if __name__ == '__main__':
    main()
