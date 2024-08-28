# classe generica 
class Animal:
    name = ''
    size = ''
    color = ''

    def eat(self):
        print("Animal comendo")

# clases espesializadas 
class Hose(Animal):
    race = ''

    def scape(self):
        print("Cavalo fugindo")


class Leao(Animal):
    juba = True

    def hunt(self):
        print("Leão caçando")