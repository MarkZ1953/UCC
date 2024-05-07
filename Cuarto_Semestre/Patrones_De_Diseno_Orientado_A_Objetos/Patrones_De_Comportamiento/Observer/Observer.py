class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

class Observer:
    def update(self, event):
        pass

class ConcreteObserverA(Observer):
    def update(self, event):
        print("ConcreteObserverA received event:", event)

class ConcreteObserverB(Observer):
    def update(self, event):
        print("ConcreteObserverB received event:", event)

subject = Subject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.notify("Event 1")
subject.detach(observer_a)

subject.notify("Event 2")
