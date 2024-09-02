from decorator import antes_depois, letra_maiuscula 


@antes_depois
def my_function():
    print("Dentro da funcao")
    

my_function()

@letra_maiuscula
def transformando_em_maiuscula(dd):
    return dd

transformando_em_maiuscula('nomes')