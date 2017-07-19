from collections import Counter
from helpers.observerpattern import Observer

class AbstractOperation(Observer):
    """
    Operations are plugins that are attached to the DomBuilder in order to
    procces different kind of analysis over DOM at the time is building and
    when it finished.
    This is the base to construct the different analysis that the Scraper
    do on the DOM, and the good thing is that they could do his job on the
    fly (at the same time that dom is being parsed).

    The initializer receives the specific configuration for the action,
    and is the client who need to construct the object with this configuration
    and pass it to the builder.

    Then, the scraper will call operation attachTo method passing the domBuilder
    in order to let the operation to attach to the needed events on the
    build proccess.

    Finally, a resultPrinter could call the getResults function in order to get
    the result of the operation and output in a useful way.
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
        self.result = None

    def attachTo(self, dom):
        self.dom = dom
        dom.subscribe("NodeAdded", self)

    def notify(self, eventData):
        if eventData['action'] == 'NodeAdded':
            self._incrementOcurrenceCounter(eventData['data']['node'][0])

    def _incrementOcurrenceCounter(self, tag):
        self.tagsList.append(tag)

    def _prepareResult(self):
        self.result = Counter(self.tagsList).most_common(self.limit)

    def getResults(self):
        if self.result == None:
            self._prepareResult()

        return self.result
