from VendingMachine import VendingMachine

class Coffee_VendingMachine(VendingMachine):
    def __init__(self):
        super().__init__(price = 1200, machine_type = "커피자판기")
    
    def prepare_product(self): # 추상메소드를 구체적으로 구현(오버라이딩)
        print(f"[{self.machine_type}] 원두 분쇠 중...")
        print(f"[{self.machine_type}] 추출 중...")
        print(f"[{self.machine_type}] 컵에 담는 중...")
