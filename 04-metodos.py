
class Movie:
   def __init__(self, name, yearLaunch, includedPlan = False, note = 0 , durationMinutes = 'Padrão'):
      self.name = name
      self.yearLaunch = yearLaunch
      self.includedPlan = includedPlan
      self.note = note
      self.durationMinutes = durationMinutes

   def __str__(self):
      return f"filme: {self.name}"

   def technical_sheet(self):
      print("## Dados do filme ##")
      print(f'Nome do filme = {self.name}')
      print(f'Ano de lançamento = {self.yearLaunch} ')
      print(f'Incluso no plano = {self.includedPlan}')
      print(f'Nota = {self.note}')
      print(f'Duração em minutos = {self.durationMinutes}\n')


mario = Movie('Mario Gross', 2020 ,False, 8.5, 200)
top_gun = Movie('Top Gun Marverik', 2020 ,False, 8.5)

mario.technical_sheet()
top_gun.technical_sheet()


