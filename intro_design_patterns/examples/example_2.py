# Primeiro, definimos um cafe base
class Coffee:
    def __init__(self):
        self._cost = 5
        self._description = "Plain Coffee"

    def cost(self):
        return self._cost

    def description(self):
        return self._description


# Agora definimos decorators para adicionar 'milk' e 'sugar' ao 'coffee'.
def milk(coffee_class):
    class MilkDecorator(coffee_class):
        def __init__(self):
            super().__init__()
            self._cost += 2
            self._description += ", with Milk"

    return MilkDecorator

def sugar(coffee_class):
    class SugarDecorator(coffee_class):
        def __init__(self):
            super().__init__()
            self._cost += 1
            self._description += ", with Sugar"

    return SugarDecorator

# TODO
def vanilla(coffee_class):
    pass


# Usando os decorators para criar objetos com funcionalidades adicionais
@milk
class CoffeeWithMilk(Coffee):
    pass

@sugar
@milk
class CoffeeWithMilkAndSugar(Coffee):
    pass

## Teste
plain_coffee = Coffee()
print(f"{plain_coffee.description()}: ${plain_coffee.cost()}")

coffee_with_milk = CoffeeWithMilk()
print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = CoffeeWithMilkAndSugar()
print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")
