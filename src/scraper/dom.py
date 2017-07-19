from helpers.observerpattern import Observable

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

class SimpleDOM(AbstractDOM):
    """
    Simple implementation of DOM made just for the purpose of the example.
    DOM is stored in a simple List of nodes. Each node is a 2-tuple
    that represents a node as follow:
    
    ( Tag Name, Parent )


    Tag Name is a String with the tag name, and parent is the list index
    where the parent of element is stored.
    So, the stored data structure of p node of the follow example:

    <div>
      <p class="example">Hello</p>
    </p>

    will be a tuple like this:

    ( 'p', 0 )

    assuming that div tag has the list index 0.
    We are not interested in node content nor attributes for the purpose
    of this example so this data is ignored and not stored in this structure.

    More complex implementations could made some optimization while
    the nodes are being created.
    """
    nodes = []

    def __len__(self): # Reafactor: extend from list
        return len(self.nodes)

    def addNode(self, node):
        self.nodes.append( node )
        self._trigger("NodeAdded", {'node': node })
        return len(self.nodes) - 1

    def getNode(self, index):
        return self.nodes[index]

