

class Move :
   def __init__(self, name = str ):
      self.name = name

   def __str__(self):
      return f"Nome = {self.name}"
   

guio = Move()
guio.name = 'The cool dream of canada'
print(guio)