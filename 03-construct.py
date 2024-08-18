
class Movie:
   def __init__(self, name, yearLaunch, includedPlan = False, note = 0 , durationMinutes = 150):
      self.name = name
      self.yearLaunch = yearLaunch
      self.includedPlan = includedPlan
      self.note = note
      self.durationMinutes = durationMinutes

  
   def __str__(self):
      return f"filme: {self.name}"


movie = Movie('Fifa', 2023)
movie2 = Movie()
print("##Dados do filme##")
print(f"Nome do filme = {movie.name} \nAno de lançamento = {movie.yearLaunch} \nDuração: {movie.durationMinutes}")