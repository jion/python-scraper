class Observable(object):
    observers= {}

    def subscribe(self, action, handler):
        if action not in self.observers:
            self.observers[action] = []

        self.observers[action].append( handler )

    def _trigger(self, action, eventData=None):
        if action not in self.observers:
            return # No suscribers for this event

        for handler in self.observers[action]:
            handler(eventData)
