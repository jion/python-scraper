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
    Then, the builder will call to deploy_phase with a reference of hisself
    so the operation need to attach to the proper action he want to be aware (if any).
    Finally, DomBuilder will call finish)phase method when parse be finished.
    """
    def attachTo(self, domBuilder):
        pass

    def getResults(self):
        pass


###########################
# Concrete Operations

class CountNumberOfElements(AbstractOperation):
    """
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
    """
    ocurrences = None
    tagsList = None
    resultsReady = False

    def __init__(self, sortOrder=None, limit=None):
        self.sortOrder = sortOrder
        self.limit = limit

        self.ocurrences = {}
        self.tagsList = []

    def attachTo(self, domBuilder):
        domBuilder.subscribe("NodeAdded", self._handleNodeAdded)
        domBuilder.subscribe("ParsingFinished", self._handleParsingFinished)

    def _handleNodeAdded(self, eventData):
        tag = eventData['element'][0]
        if tag in self.ocurrences:
            self.ocurrences[tag] += 1
        else:
            self.ocurrences[tag]  = 1

    def _handleParsingFinished(self, eventData):
        keys = self.ocurrences.keys()
        self.tagsList = keys
        if(self.sortOrder != None):
            self.tagsList = [v[0] for v in sorted(self.ocurrences.iteritems(), key=lambda(k, v): (v, k), reverse=(self.sortOrder == "DESC"))]

    def getResults(self):
        return (self.tagsList, self.ocurrences)
