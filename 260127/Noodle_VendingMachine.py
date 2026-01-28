from VendingMachine import VendingMachine

class Noodle_VendingMachine(VendingMachine):
    def __init__(self):
        super().__init__(price = 1500, machine_type = "라면자판기")
    
    def prepare_product(self):
        print(f"[{self.machine_type}] 컵면 배출")
        print(f"[{self.machine_type}] 뜨거운 물 주입 중...")