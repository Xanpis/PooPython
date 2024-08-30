class Phone:
    def __init__(self,brand,model_name,price):
        self._brand = brand
        self._model_name = model_name
        self._price  = price
    
    def __str__(self):
        return f"{self._brand}{self._model_name}"  
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para: {phone_num}")
    
    # Aplicando o polimorfismo na pratica  
    def discant(self):
        return self._price * 0.10 
        
        
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        # Quando eu passo o super eu estou reaproveitando os atributos do Metodo pai 
        # Assim eu não preciso escrever todos os self novamente
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
    
    # Mesmo metodo mas com assinatura diferente  
    def discant(self):
        return self._price * 0.15
        

Moto = Phone('Moto','G7',100,)
print(Moto)
Moto.make_a_call(139910)
print(vars(Moto))
print(Moto.discant())


iphone = SmartPhone('Iphone','13',5000,'4G','128G','50mpx' )
print(iphone)
iphone.make_a_call(234240)
print(vars(iphone))
print(iphone.discant())
    