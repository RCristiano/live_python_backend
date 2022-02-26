class Pizza:

    def __init__(self, sabor, ingredientes, preço) -> None:
        self.sabor = sabor
        self.ingredientes = ingredientes 
        self.preço = preço
    
class Mussarela(Pizza):
    """Pizza de Mussarela"""
    
    def __init__(self) -> None:
        self.sabor = 'Mussarela'
        self.ingredientes = ['farinha', 'queijo'] 
        self.preço = 30.5

class Calabresa(Pizza):
    """Pizza de Calabresa"""
    
    def __init__(self) -> None:
        self.sabor = 'Calabresa'
        self.ingredientes = ['farinha', 'calabresa'] 
        self.preço = 25
        

class MeioMeio(Pizza):
    """Pizza meio a meio"""
    
    def __init__(self, sabor1: Pizza, sabor2: Pizza) -> None:
        self.sabor = f'{sabor1.sabor} + {sabor2.sabor}'
        self.ingredientes = list(set(sabor1.ingredientes + sabor2.ingredientes))
        self.preço = ((sabor1.preço/2) + (sabor2.preço/2))


p1 = Calabresa()
p2 = Mussarela()

p3 = MeioMeio(Calabresa(), Mussarela())

    
def lucro_pizzas(pizzas: list[Pizza]) -> float:
    return sum(pizza.preço for pizza in pizzas)
