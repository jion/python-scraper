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
        print "Total number of elements:", operation.getResults()
        print ""

    def ListOcurrencesPrinter( self, operation ):
        if operation.limit != None:
            print "Top %d most frequently used tags:" % operation.limit
        else:
            print "Ocurrences by tag: "
        
        results = operation.getResults()
        for (tag, ocurrences) in results:
            print "{:>5}: {:d}".format(tag, ocurrences)
        print ""

