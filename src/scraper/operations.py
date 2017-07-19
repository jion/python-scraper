from collections import defaultdict
from helpers.observerpattern import Observer

class AbstractOperation(Observer):
    """
    Operations are plugins that are attached to dom events in order to
    procces different kind of analysis over at the time it is build.
    This is the base to construct the different analysis that the Scraper
    do on the DOM.

    The initializer receives the specific configuration for the action,
    and is the scraper client who need to construct the object with this
    configuration and pass it to the builder.
    """
    def attachTo(self, dom):
        pass

    def getResults(self):
        pass


###########################
# Concrete Operations

class CountNumberOfElements(AbstractOperation):
    """
    Count the number of elements present in DOM.
    Result of this operation is a number indicating the total number of
    elements present in DOM.
    """

    def attachTo(self, dom):
        self.dom = dom

    def getResults(self):
        return len(self.dom)
        

class ListOcurrences(AbstractOperation):
    """
    This operation count the number of ocurrences of each tag name present
    in DOM.
    It takes optional configuration argument:
     * limit: specifies the max number of results desired.

    Result of this operation is list of n tuples with the format (tag, ocurrences),
    ordered from most common to less common.
    """

    def __init__(self, limit=None):
        self.limit = limit
        self.tagsList = []
        self.elementsCounter= defaultdict(int)
        self.result = None

    def attachTo(self, dom):
        self.dom = dom
        dom.subscribe("NodeAdded", self)

    def notify(self, eventData):
        if eventData['action'] == 'NodeAdded':
            self._incrementOcurrenceCounter(eventData['data']['node'][0])

    def _incrementOcurrenceCounter(self, tag):
        self.elementsCounter[tag] += 1
        #self.tagsList.append(tag)


    def _prepareResult(self):
        sortedTuples = sorted(self.elementsCounter.items(), key=lambda (k, v): -v)
        
        # TODO: Refactor this to make it more pythonic
        if self.limit != None:
            newResult = []
            lastCount = -1
            count = 0
            for item in sortedTuples:
                if item[1] != lastCount:
                    if count == self.limit:
                        break
                    lastCount= item[1]
                    count += 1
                newResult.append(item)
            sortedTuples = newResult

        self.result = sortedTuples

    def getResults(self):
        if self.result == None:
            self._prepareResult()

        return self.result
