class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("AbstractClass: base_operation1")

    def base_operation2(self):
        print("AbstractClass: base_operation2")

    def base_operation3(self):
        print("AbstractClass: base_operation3")

    def required_operation1(self):
        raise NotImplementedError

    def required_operation2(self):
        raise NotImplementedError

    def hook1(self):
        pass

    def hook2(self):
        pass

class ConcreteClass(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass: required_operation1")

    def required_operation2(self):
        print("ConcreteClass: required_operation2")

    def hook2(self):
        print("ConcreteClass: hook2")

concrete = ConcreteClass()
concrete.template_method()
