from abc import ABC, abstractmethod

clas vendingMachine(ABC):
    def __init(self, price, machine_type):
        self.price = price
        self.machine_type = machine_type

    def serve(self, amount: int):
        self.insert_money(amount)
        if self.check_amount(amount)
           self.prepare_product()
           self.take_out()
           self.return_charge(amount)

    @abstractmethod
    def prepare_product(self):
        pass
