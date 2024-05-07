class Expression:
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number

class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

expression = Plus(Number(5), Number(3))
result = expression.interpret({})
print("Result:", result)
