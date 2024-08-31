
class Animal():
    def __init__(self, name, categoria) -> None:
        self.name = name
        self.categoria = categoria
       
class Fish(Animal):
    color = " "
    
    
class Parrot (Animal):
    color = " "
    
    
class Zoo:
    def __init__(self) -> None:   
        self.animal_dict = {}
        
    def add_animal(self, animal):
        self.animal_dict[animal.name] = animal.categoria
        
        
    def total_of_category(self,category):
        result = 0 
        
        for animal in self.animal_dict.values():
            if animal == category:
                result +=1
                
        return f"No nosso zoológico temos: {result} quantidade de: {category} "
  

zoo = Zoo()

peixe = Fish("Nemo","peixe")
peixe.color  = 'verde'
print(vars(peixe))

papagaio = Parrot("Louro","aves")
papagaio.color = 'Listrado'
print(vars(papagaio))

zoo.add_animal(peixe)
zoo.add_animal(papagaio)

print(zoo.total_of_category("aves"))
print(zoo.total_of_category("peixe"))