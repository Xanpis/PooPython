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
h.size = 'small'
h.color = 'Black'
h.race = 'Equina'
print(vars(h))
h.scape()
h.eat()
