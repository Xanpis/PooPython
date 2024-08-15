class Movie:
   total= 0
   qt = 0
   def __init__(self,):
      self.nome = self.filNome()
      self.nota = self.notaLup()

   def filNome(self):
      nome = input('nome do filme = ')
      return nome
   
      
   def notaLup(self):
      op = False
      while not op:
         nota = int(input('Digite a Nota ou (0) para Sair = '))
         self.total += nota 
         
         if nota != 0:
            self.qt += 1

         if nota == 0 :
            op = True  
            return self.total
      


movie = Movie()
print(f'Nome do filme: {movie.nome} \nNota Do filme: {movie.nota/movie.qt} \nQuantidade de avaliação: {movie.qt}  ')