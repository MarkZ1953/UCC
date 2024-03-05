class Pizza:
    def __init__(self, dough="", sauce="", toppings=[]):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def __str__(self):
        return f"Pizza con {self.dough} de masa, salsa de {self.sauce} y los siguientes ingredientes: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza


# Uso del Builder
builder = PizzaBuilder()
pizza = builder.set_dough("delgada").set_sauce("tomate").add_topping("queso").add_topping("jamón").build()

print(pizza)  # Salida: Pizza con delgada de masa, salsa de tomate y los siguientes ingredientes: queso, jamón
