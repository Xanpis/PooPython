from Trip import Trip

destino1= Trip("fortaleza")
destino2= Trip("Gramados")
destino3= Trip("São paulo")

print("Olá viajante Temos algumas ofertas para você")
traveler = input("Digite seu nome viajante \n")
print(f"Olá {traveler} Temos 3 destino que combina com você "
      '''
      [0] Fortaleza
      [1] Gramados
      [2] São paulo
      
      '''
      )  
chose = int(input(" Selecione o destino: \n"))
lista_trip = [destino1,destino2,destino3]

for option in lista_trip:
    if chose >= 3:
        print('falha: Opção invalida ')
        break
    else:
        print(f"{traveler} Sua viagem para {lista_trip[chose].destiny} foi Marcada obrigado")
        break   
    
