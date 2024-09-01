"""
1- O método estático não utiliza o parâmetro referente a classe  
2- Você pose acessar mas não pode modificar o estado de uma classe
3- Usamos o decorator @staticmethod para criar o método  estático 

"""

class Curse:
   def __init__(self,name,trail):
      self.name = name
      self.trail = trail

   @staticmethod
   def curso_trail(tra):
      if tra == 'Python Fundamentos':
         curse = ['Dominando python','Modulo de pip']
      elif tra == 'Automação python':
         curse = ['Automação de tarefas', 'Web scraping',]
      else:
         curse =['A definir'] 
      return (curse)

print(Curse.curso_trail('Python Fundamentos'))