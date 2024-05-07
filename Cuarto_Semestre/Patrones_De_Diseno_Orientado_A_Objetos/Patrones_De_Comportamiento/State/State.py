class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA is handling the request.")

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB is handling the request.")

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle()

context = Context(ConcreteStateA())
context.request()

context.state = ConcreteStateB()
context.request()
