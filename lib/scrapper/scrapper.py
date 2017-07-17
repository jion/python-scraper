from dombuilder import DomBuilder
from dom import SimpleDOM

class Scrapper(object):
    """
    This class orchestrates the whole proccess of Scrapping the specified HTML.
    You can customize the proccess adding Operations that will be executed on
    the fly while the DOM object is created from parsing the HTML page.
    When results are ready this will output the results in a decoupled fashion
    passing the desired implementation of a printer to the printResults function.

    The initializer receives an object that accepts the Reader protocol.
    """
    # TODO: ^ Check the specific name of the "Reader Protocol" for documentation
    dom = None        # \
    domBuilder = None # / TODO: Coupled dependencies. Review
    operationsList = None
    reader = None

    def __init__(self, reader):
        self.reader = reader
        self.operationsList = []

        # Concrete dependencies
        self.dom = SimpleDOM()
        self.domBuilder = DomBuilder()


    def addOperation(self, operation):
        self.operationsList.append( operation )
        return self

    def run(self):
        domBuilder = self.domBuilder

        for operation in self.operationsList:
            operation.deploy_phase( domBuilder )

        domBuilder.setInput( self.reader )
        domBuilder.setOutput( self.dom )

        domBuilder.build()

        for operation in self.operationsList:
            operation.finish_phase( self.dom )

    def printResults(self, printer):
        for operation in self.operationsList:
            printer.printResults( operation )
