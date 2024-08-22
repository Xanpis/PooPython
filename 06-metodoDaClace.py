"""
1- O método de classe usa parâmetro referente a classe  
2- O método de classe pode acessar ou mudar o estado da classe
3- Usamos o decorator @classmethod para criar o método da classe

"""
class Console:
   def __init__(self,name,price):
      self.name = name
      self.price = price
   
   @classmethod
   def from_text(cls,string):
      import re
      item = re.findall("é \w*",string)
      na = item[0][2:]
      pri = item[1][2:]
      return cls( na, int(pri))

wiiu = Console.from_text('Meu video game é Wiiu e o preço é 1000 reais')
print(wiiu.__dict__)
xboxOne = Console.from_text('Meu video game é xboxOne e o preço é 1000 reais')
print(xboxOne.__dict__)
