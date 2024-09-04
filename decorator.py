
def antes_depois(fun):
    def wrapper():
        print("Antes de executar a funcao")
        fun()
        print("Depois de executar a funcao")
    return wrapper

def letra_maiuscula(funcao):
    def wrapper():
        fun = funcao()
        make = fun.upper()
        return make
    return wrapper