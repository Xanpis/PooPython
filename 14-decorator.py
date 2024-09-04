from decorator import antes_depois, letra_maiuscula 


@antes_depois
def my_function():
    print("Dentro da funcao")
    

my_function()

@letra_maiuscula
def transformando_em_maiuscula():
    return "Transformando letras em maiusculas"  

var = transformando_em_maiuscula()
print(var)