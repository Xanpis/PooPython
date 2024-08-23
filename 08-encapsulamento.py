class Employer:
   def __init__(self, nome, salary):
      self.nome = nome
      # encapsulamento privado
      self.__salary = salary
   
   def show (self):
      print(f"Nome: {self.nome}")
      print(f"Nome: {self.__salary} \n")


fulano = Employer('Maria', 4000)
ciclano = Employer('João',2000)
fulano.show()
# Eu tenho acesso ao atributo da classe mas não posso modificá-lo 
ciclano.__salary = 3000
ciclano.show()