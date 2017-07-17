#!/usr/bin/env python2.7

import sys
sys.path.append('./lib')

from scrapper.operations import CountNumberOfElements, ListOcurrences
from scrapper.resultprinters import ConsolePrinter
from scrapper.scrapper import Scrapper

from urllib2 import urlopen as URLReader


url = "http://ordergroove.com/company"

def main():
    """
    This runs an example petition to the scrapper
    asking for the number of elements in the page (the one that is
    stored in global variable "url"), and the top 5 tags ocurrences.
    Scrapper was made in a way to be extendable by
    Operations, and also the output was decoupled using an abstract
    printer (only consoleOutput was implemented by now)
    """

    # Setting up & Running the Scrapper
    scrapper = Scrapper(URLReader(url))

    scrapper.addOperation(CountNumberOfElements())
    scrapper.addOperation(ListOcurrences(sortOrder="DESC", limit=5 ))

    scrapper.run()

    # Printing results
    consolePrinter = ConsolePrinter()
    scrapper.printResults(consolePrinter)


if __name__ == '__main__':
    main()
