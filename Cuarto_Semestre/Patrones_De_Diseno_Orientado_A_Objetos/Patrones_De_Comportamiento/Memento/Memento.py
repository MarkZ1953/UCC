class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = ""

    def set_state(self, state):
        self.state = state

    def save_to_memento(self):
        return Memento(self.state)

    def restore_from_memento(self, memento):
        self.state = memento.state

# Uso
originator = Originator()
originator.set_state("State 1")
print("Current state:", originator.state)

memento = originator.save_to_memento()

originator.set_state("State 2")
print("Current state:", originator.state)

originator.restore_from_memento(memento)
print("Restored state:", originator.state)
