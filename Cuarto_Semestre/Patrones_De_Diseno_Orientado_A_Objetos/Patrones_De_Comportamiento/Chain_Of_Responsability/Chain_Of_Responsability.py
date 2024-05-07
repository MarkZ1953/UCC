class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandlerA handles the request.")
        else:
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandlerB handles the request.")
        else:
            super().handle_request(request)

handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB(handler_a)

handler_b.handle_request('A')
handler_b.handle_request('B')
handler_b.handle_request('C')
