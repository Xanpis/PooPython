

class Movie:
   name = ""
   yearLaunch = 0
   includedPlan = False
   note = 0
   durationMinutes = 0
   
   # sobre escrevendo o a referencia de uma classe 
   def __str__(self):
      return f"filme: {self.name}"

# primeiro filme
movie = Movie()
movie.name = "Super Mario"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 150

print(movie)

print("##Dados do filme##")
print(f"Nome do filme = {movie.name} \nAno de lançamento = {movie.yearLaunch}")