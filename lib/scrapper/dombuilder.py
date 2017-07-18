from helpers.observable import Observable
from HTMLParser import HTMLParser

class DomBuilder(Observable, HTMLParser):
    """
    This class is on charge of parse the plainHTML provided via a Reader and construct
    a dom representation with it. For the sake of this example, we will use a simple list
    to represent the dom structure, but properly deacoupled in order to be able to create
    better data structures that allow to create more complex operations.
    """

    # Some elements don't have a closing tag ( https://www.w3.org/TR/html51/syntax.html#void-elements )
    voidTags = ["area", "base", "br", "col", "embed", "hr", "img", "input", "keygen",
                "link", "menuitem", "meta", "param", "source", "track", "wbr"] # const

    def __init__(self, dom):
        HTMLParser.__init__(self)

        self.dom = dom
        self.actualParent = [None,]

    def _finishParsing(self):
        self._trigger("ParsingFinished", { 'dom': self.dom })


    def handle_starttag(self, tag, attrs):
        element = (tag, attrs, self.actualParent[-1])
        nodeIndex = self.dom.addNode( element )
        self._trigger("NodeAdded", {'element': element })
        
        if tag not in self.voidTags:
            self.actualParent.append( nodeIndex )

    def handle_endtag(self, tag):
        if tag in self.voidTags:
            return # We already did the job

        actualParent =  self.actualParent.pop()
        if self.dom.getNode( actualParent )[0] != tag:
            raise HTMLParser.Error("Closing tag is missing") # TODO: Custom error object. (ParseEror ?)

        if self.actualParent[-1] == None:
            self._finishParsing()
