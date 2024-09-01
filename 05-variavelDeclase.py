class Movie:
   # variável de classe 
   platform = 'Obit code '

   def __init__(self, name, yearLaunch, includedPlan = False, durationMinutes = 'Padrão'):
      self.name = name
      self.yearLaunch = yearLaunch
      self.includedPlan = includedPlan
      self.totalValuation= 0
      self.durationMinutes = durationMinutes
      self.evaluates = 0

   def __str__(self):
      return f"filme: {self.name}"

   def technical_sheet(self):
      print("## Dados do filme ##")

      # chamando a variável da classe
      print(f'Plataforma = {Movie.platform}')

      print(f'Nome do filme = {self.name}')
      print(f'Ano de lançamento = {self.yearLaunch} ')
      print(f'Incluso no plano = {self.includedPlan}')
      print(f'Nota = {self.totalValuation}')
      print(f'Avaliação Total = {self.evaluates}')
      print(f'Duração em minutos = {self.durationMinutes}\n')

   def evaluate(self,nota):
      self.totalValuation += nota
      self.evaluates += 1 

   def avenge(self):
      print(f'Media do film : {self.name}: {self.totalValuation/self.evaluates:.2f} \n')


mario = Movie('Super Mario Bros', 2023, False, 190)
mario.evaluate(9.5)
mario.evaluate(10)
mario.evaluate(8)
mario.technical_sheet()
mario.avenge()

avatar = Movie('Avatar', 2024, False, 300)

# Editando a plataforma do filme da variável da classe 
Movie.platform = 'Obit code pro'
avatar.technical_sheet()