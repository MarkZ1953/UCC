class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitorA(Visitor):
    def visit(self, element):
        print("ConcreteVisitorA is visiting", element)

class ConcreteVisitorB(Visitor):
    def visit(self, element):
        print("ConcreteVisitorB is visiting", element)

class Element:
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit(self)

visitor_a = ConcreteVisitorA()
visitor_b = ConcreteVisitorB()

element_a = ConcreteElementA()
element_b = ConcreteElementB()

element_a.accept(visitor_a)
element_a.accept(visitor_b)

element_b.accept(visitor_a)
element_b.accept(visitor_b)
