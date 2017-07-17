from helpers.observable import Observable

class AbstractDOM(Observable):
    #locked = True

    def __len__(self):
        raise NotImplementedError()
    def addNode(self, tag, attrs, parent=None):
        raise NotImplementedError()
    def getNode(self, index):
        raise NotImplementedError()
    def addContent(self, node, content):
        raise NotImplementedError()
    # def lock(self):
    #     if not self.locked:
    #         self.locked = True
    #         self._trigger( "DomLocked" )
    # def unlock(self):
    #     if self.locked:
    #         self.locked = False
    #         self._trigger( "DomUnlocked" )

class SimpleDOM(AbstractDOM):
    """
    This is a simple implementation of DOM made just for the
    purpose of the example.
    DOM is stored in a simple List of tuples. Each tuple is an 3-tuple
    that represents a node in this way:
    
    ( Tag Name, Attributes, Parent )

    We are not interested in node content in this example so content
    is ignored and not stored in this structure.
    More complex implementations could made some optimization while
    the nodes are being created.
    """
    nodes = []

    def __len__(self): # Reafactor: extend from list
        return len(self.nodes)

    def addNode(self, node):
        self.nodes.append( node )
        return len(self.nodes) - 1

    def getNode(self, index):
        return self.nodes[index]

