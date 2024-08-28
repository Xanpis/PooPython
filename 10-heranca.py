# classe generica 
class Animal:
    name = ''
    size = ''
    color = ''

    def eat(self):
        print("Animal comendo")

# classes especializadas 
class Horse(Animal):
    race = ''

    def scape(self):
        print("Cavalo fugindo")


class Leao(Animal):
    juba = True

    def hunt(self):
        print("Leão caçando")

h = Horse()
h.name = 'Carpido'
h.color = 'Black'
h.scape()
h.eat()
