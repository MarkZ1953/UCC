import copy


class Prototype:
    def clone(self):
        pass


class Document(Prototype):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content

    def clone(self):
        return copy.deepcopy(self)


# Uso del Prototype
original_document = Document("Contenido del documento original")
cloned_document = original_document.clone()

print(original_document)  # Salida: Contenido del documento original
print(cloned_document)  # Salida: Contenido del documento original
print(original_document is cloned_document)  # Salida: False
