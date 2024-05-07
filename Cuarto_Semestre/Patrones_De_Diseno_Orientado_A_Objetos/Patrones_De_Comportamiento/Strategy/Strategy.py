class Strategy:
    def execute_strategy(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute_strategy(self):
        print("Executing ConcreteStrategyA.")

class ConcreteStrategyB(Strategy):
    def execute_strategy(self):
        print("Executing ConcreteStrategyB.")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute_strategy()

context = Context(ConcreteStrategyA())
context.execute_strategy()

context2 = Context(ConcreteStrategyB())
context2.execute_strategy()
