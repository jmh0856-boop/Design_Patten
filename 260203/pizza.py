from abc import(
    ABC,
    abstractmethod,
)

class Pizza(ABC): # product (추상 클래스)
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    def cut(self):
        print(f"{self.__class__.__name__}를 자릅니다")

    def box(self):
        print(f"{self.__class__.__name__}를 박스에 포장합니다")


class NyPizza(Pizza): # ConcreteProduct - 뉴욕 피자
    def prepare(self):
        print("뉴욕 피자를 준비합니다")

    def bake(self):
        print("뉴욕 피자를 만듭니다")


class ChiPizza(Pizza): # ConcreteProduct - 시카고 피자
    def prepare(self):
        print("시카고 피자를 준비합니다")

    def bake(self):
        print("시카고 피자를 만듭니다")


class PizzaStore(ABC): # Creator (추상 클래스)
    @abstractmethod
    def create_pizza(self): # 팩토리 메소드
        pass

    def order_pizza(self):
        pizza = self.create_pizza()

        print(f"--- {pizza.__class__.__name__} 주문 시작 ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

