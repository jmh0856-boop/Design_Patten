from pizza import(
    PizzaStore,
    NyPizza,
    ChiPizza,
)

class NyPizzaStore(PizzaStore): # Concrete Creator 1
    def create_pizza(self): # 부모의 팩토리 메소드를 구현
        return NyPizza()


class ChiPizzaStore(PizzaStore): # Concrete Creator 2
    def create_pizza(self): # 부모의 팩토리 메소드를 구현
        return ChiPizza()
