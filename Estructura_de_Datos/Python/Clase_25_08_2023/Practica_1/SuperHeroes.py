class SuperHeroes:
    def __init__(self, identidadPublica, identidadSecreta, fechaCreacion, creador, poderes, habilidades, nivelFuerza):
        self.__identidadPublica = identidadPublica
        self.__identidadSecreta = identidadSecreta
        self.__habilidades = habilidades
        self.__fechaCreacion = fechaCreacion
        self.__creador = creador
        self.__poderes = poderes
        self.__nivelFuerza = nivelFuerza

    @property
    def getHabilidades(self):
        return self.__habilidades

    @property
    def getIdentidadPublica(self):
        return self.__identidadPublica

    @property
    def getIdentidadSecreta(self):
        return self.__identidadSecreta

    @property
    def getCreador(self):
        return self.__creador

    @property
    def getPoderes(self):
        return self.__poderes

    @property
    def getNivelFuerza(self):
        return self.__nivelFuerza

    @property
    def getFechaCreacion(self):
        return self.__fechaCreacion


class SuperheroDatabase:
    def __init__(self):
        self.superHeroes = []

    def agregarSuperHeroe(self, superHeroe):
        for heroe in self.superHeroes:
            if heroe.public_identity == superHeroe.getIdentidadPublica:
                print("Error: Ya existe un superhéroe con esta identidad pública.")
                return
        self.superHeroes.append(superHeroe)
        self.superHeroes.sort(key=lambda x: x.getFechaCreacion)

    def buscarPorIdentidadSecreta(self, identidadSecreta):
        for heroe in self.superHeroes:
            if heroe.secret_identity == identidadSecreta:
                return heroe
        return None

    def buscarPorIdentidadPublica(self, identidadPublica):
        izquierda = 0
        derecha = len(self.superHeroes) - 1
        while izquierda <= derecha:
            mid = (izquierda + derecha) // 2
            if self.superHeroes[mid].public_identity == identidadPublica:
                return self.superHeroes[mid]
            elif self.superHeroes[mid].public_identity < identidadPublica:
                izquierda = mid + 1
            else:
                derecha = mid - 1
        return None

    def superHeroeMasAntiguo(self):
        return min(self.superHeroes, key=lambda x: x.fechaCreacion)

    def superHeroeMasFuerte(self):
        return max(self.superHeroes, key=lambda x: x.nivelFuerza)

    def sort_by_year_created(self):
        self.superHeroes.sort(key=lambda x: x.fechaCreacion)

    def sort_by_creator(self):
        self.superHeroes.sort(key=lambda x: x.__creador)

    def organizarPorFuerza(self):
        self.superHeroes.sort(key=lambda x: x.nivelFuerza)


# Crear instancia de la base de datos de superhéroes
database = SuperheroDatabase()

# Ejemplo de uso
superhero1 = SuperHeroes("Spider-Man", "Peter Parker", 1962, "Stan Lee", ["Agilidad", "Sentido arácnido"],
                         ["Lucha cuerpo a cuerpo"], 8)
superhero2 = SuperHeroes("Iron Man", "Tony Stark", 1963, "Stan Lee", ["Tecnología avanzada"],
                         ["Genio nivel intelectual"], 9)
superhero3 = SuperHeroes("Superman", "Clark Kent", 1938, "Jerry Siegel", ["Vuelo", "Fuerza sobrehumana"],
                         ["Visión de calor"], 10)

database.agregarSuperHeroe(superhero1)
database.agregarSuperHeroe(superhero2)
database.agregarSuperHeroe(superhero3)

print("Superhéroe más antiguo:", database.superHeroeMasAntiguo().public_identity)
print("Superhéroe más fuerte:", database.superHeroeMasFuerte().public_identity)

database.sort_by_year_created()
print("Superhéroes ordenados por año de creación:")
for hero in database.superHeroes:
    print(hero.public_identity, hero.year_created)

database.sort_by_creator()
print("Superhéroes ordenados por __creador:")
for hero in database.superHeroes:
    print(hero.public_identity, hero.__creador)

database.organizarPorFuerza()
print("Superhéroes ordenados por nivel de fuerza:")
for hero in database.superHeroes:
    print(hero.public_identity, hero.__nivelFuerza)
