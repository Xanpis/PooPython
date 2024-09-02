from Trip import Trip

destino1= Trip("fortaleza")
destino2= Trip("Gramados")
destino3= Trip("São paulo")

print("\nOlá viajante Temos algumas ofertas para você")
traveler = input("\nDigite seu nome viajante : ")
print(f"Olá {traveler.title()} Temos 3 destino que combina com você "
      '''
      
      [0] Fortaleza
      [1] Gramados
      [2] São paulo 
      '''
      )  
chose = int(input(" Selecione o destino: "))
lista_trip = [destino1,destino2,destino3]

for option in lista_trip:
    if chose >= 3:
        print('falha: Opção invalida ')
        break
    else:
        print(f"{traveler.title()} Sua viagem para {lista_trip[chose].destiny} foi Marcada obrigado")
        break   
    
