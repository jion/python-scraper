class Observable(object):
    """
    This class implements the observer design pattern.
    You just need to inherit from this class to add
    the ability to the class of be observable.
    """
    observers= {}

    def subscribe(self, action, observer):
        if action not in self.observers:
            self.observers[action] = []

        self.observers[action].append( observer )

    def _trigger(self, action, eventData=None):
        if action not in self.observers:
            return # No suscribers for this event

        e = { 'action': action, 'data': eventData }

        for observer in self.observers[action]:
            observer.notify(e)

class Observer(object):
    def notify(self, eventData):
        pass
