from texttable import Texttable

table = Texttable()


class CalculadoraNotasUCC:
    pass


table.add_rows([
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
])

print(table.draw())
