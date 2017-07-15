#!/usr/bin/env python2.7
from Scrapper import Scrapper
from Operations import CountNumberOfElements, ListOcurrences
from ResultPrinters import ConsolePrinter
from urlib2 import urlopen as URLReader


url = "http://ordergroove.com/company"

def main():
    """
    This function runs an example petition to the scrapper
    asking for the number of elements in the page (the one that is
    stored in global variable "url"), and the top 5 tags ocurrences.
    Scrapper was made in a way to be extendable via
    Operations, and also the output was decoupled using an abstract
    printer (only consoleOutput was implemented by now)
    """

    # Setting up & Running the Scrapper
    scrapper = Scrapper( URLReader( url ) )

    scrapper.addOperation( CountNumberOfElements() )
    scrapper.addOperation( ListOcurrences( order="DESC", limit=5 ) )

    scrapper.run();

    # Printing results
    consolePrinter = ConsolePrinter();
    scrapper.printResults ( consolePrinter )


if __name__ == '__main__':
    main()
