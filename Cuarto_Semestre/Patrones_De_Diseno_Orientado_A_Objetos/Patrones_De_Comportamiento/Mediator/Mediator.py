class Mediator:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def notify(self, sender, event):
        for component in self.components:
            if component != sender:
                component.receive(event)

class Component:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, event):
        self.mediator.notify(self, event)

    def receive(self, event):
        print("Received event:", event)

# Uso
mediator = Mediator()
component1 = Component(mediator)
component2 = Component(mediator)
mediator.add_component(component1)
mediator.add_component(component2)

component1.send("Hello from component 1")
component2.send("Hi from component 2")
