class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("Light is on.")

    def turn_off(self):
        print("Light is off.")

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

light = Light()
turn_on_command = TurnOnCommand(light)
turn_off_command = TurnOffCommand(light)

turn_on_command.execute()
turn_off_command.execute()
