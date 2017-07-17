class AbstractPrinter(object):
    def printResults(self, operation):
        pass

class ConsolePrinter(AbstractPrinter):

    def printResults(self, operation):
        operationName = type(operation).__name__

        if operationName == 'CountNumberOfElements':
            self.CountNumberOfElementsPrinter( operation )
        elif operationName == 'ListOcurrences':
            self.ListOcurrencesPrinter( operation )
        else:
            raise Exception( "Console Printer can't print output for " + operationName )

    def CountNumberOfElementsPrinter( self, operation ):
        print "The total number of elements is:", operation.getResults()

    def ListOcurrencesPrinter( self, operation ):
        print "Ocurrences by tag: "
        
        (tags, ocurrences) = operation.getResults()
        for tag in tags:
            print tag, ':', ocurrences[tag]

