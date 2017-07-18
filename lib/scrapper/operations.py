from collections import Counter

class AbstractOperation(object):
    """
    Operations are plugins that are attached to the DomBuilder in order to
    procces different kind of analysis over DOM at the time is building and
    when it finished.
    This is the base to construct the different analysis that the Scrapper
    do on the DOM, and the good thing is that they could do his job on the
    fly (at the same time that dom is being parsed).

    The initializer receives the specific configuration for the action,
    and is the client who need to construct the object with this configuration
    and pass it to the builder.

    Then, the scrapper will call operation attachTo method passing the domBuilder
    in order to let the operation to attach to the needed events on the
    build proccess.

    Finally, a resultPrinter could call the getResults function in order to get
    the result of the operation and output in a useful way.
    """
    def attachTo(self, domBuilder):
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
    def __init__(self):
        self.numberOfElements = None

    def attachTo(self, domBuilder):
        domBuilder.subscribe("ParsingFinished", self._handleParsingFinished)

    def _handleParsingFinished(self, eventData):
        dom = eventData['dom']
        self.numberOfElements = len( dom )

    def getResults(self):
        return self.numberOfElements
        

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

    def attachTo(self, domBuilder):
        domBuilder.subscribe("NodeAdded", self._handleNodeAdded)
        domBuilder.subscribe("ParsingFinished", self._handleParsingFinished)

    def _handleNodeAdded(self, eventData):
        tag = eventData['element'][0]
        self.tagsList.append(tag)

    def _handleParsingFinished(self, eventData):
        self.result = Counter(self.tagsList).most_common(self.limit)

    def getResults(self):
        return self.result
