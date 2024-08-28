class Employer:
   __salary2 = 400

   def __init__(self, nome, salary):
      self.nome = nome
      # encapsulamento privado
      self.__salary = salary

   # buscando um atributo privado 
   def getSalary(self):
      return(self.__salary)
   
   # Adicionando um atributo privado 
   def setSalary(self,salary):
      self.__salary = salary


   def show (self):
      print(f"Nome: {self.nome}")
      print(f"Nome: {self.__salary2}")
      print(f"Nome: {self.__salary} \n")


fulano = Employer('Maria', 4000)
ciclano = Employer('João',2000)

fulano.show()
# Eu tenho acesso ao atributo da classe mas não posso modificá-lo 
ciclano.__salary = 3000
ciclano.show()

# Agora eu posso modificá-lo
ciclano.setSalary(700)
print(ciclano.getSalary())

ciclano.show()