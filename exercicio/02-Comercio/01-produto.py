class Produto:
   def __init__(self,nome,preco):
      self.nome = nome
      self.preco = preco
   
   def desconto(self,porcent ):
      self.dec = porcent
      self.descontoTotal = self.preco - (self.preco * porcent / 100)

   def __str__(self):
      return f"Nome: {self.nome}"
   
   def empimeProdoto(self):
      print(f'Nome do Produto: {self.nome}')
      print(f'Preço: {self.preco}')
      print(f'Desconto: {self.dec}%')
      print(f'Total: {self.descontoTotal}\n')
         

arroz = Produto('Arroz',5)
arroz.desconto(50)
arroz.empimeProdoto()

feijao = Produto('Feijao',8.00)
feijao.desconto(10)
feijao.empimeProdoto()

lagosta = Produto('lagosta', 250)
lagosta.desconto(15)
lagosta.empimeProdoto()