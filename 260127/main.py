from Coffee_VendingMachine import Coffee_VendingMachine
from Cola_VendingMachine import Cola_VendingMachine
from Noodle_VendingMachine import Noodle_VendingMachine

if __name__ == "__main__":
    coffee_vendingmachine = Coffee_VendingMachine()
    coffee_vendingmachine.serve(2000)

    cola_vendingmachine = Cola_VendingMachine()
    cola_vendingmachine.serve(2000)

    noodle_vendingmachine = Noodle_VendingMachine()
    noodle_vendingmachine.serve(2000)

    print("---금액 부족 테스트---")
    cola_vendingmachine.serve(500)
    coffee_vendingmachine.serve(500)
    noodle_vendingmachine.serve(500)