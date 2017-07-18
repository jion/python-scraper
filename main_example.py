#!/usr/bin/env python2.7

import sys
sys.path.append('./lib')

from scrapper.operations import CountNumberOfElements, ListOcurrences
from scrapper.resultprinters import ConsolePrinter
from scrapper.scrapper import defaultUrlScrapper as Scrapper


url = "http://ordergroove.com/company"

def main():
    """
    This runs an example petition to the scrapper
    asking for the number of html elements and the
    5 most used tags on the page that is stored in
    global variable "url").
    Scrapper was made in a way to be extendable by
    Operations, and also the output was decoupled using an abstract
    printer (only consoleOutput was implemented by now)
    """

    # Setting up & Running the Scrapper
    scrapper = Scrapper(url)

    scrapper.addOperation(CountNumberOfElements())
    scrapper.addOperation(ListOcurrences(limit=5))

    scrapper.run()

    # Printing results
    consolePrinter = ConsolePrinter()
    scrapper.printResults(consolePrinter)


if __name__ == '__main__':
    main()
