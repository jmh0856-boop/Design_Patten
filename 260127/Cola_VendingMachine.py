from VendingMachine import VendingMachine

class Cola_VendingMachine(VendingMachine):
    def __init__(self):
        super().__init__(price = 800, machine_type = "콜라자판기")
    
    def prepare_product(self): # 추상메소드를 구체적으로 구현(오버라이딩)
        print(f"[{self.machine_type}] 냉장 상태 확인 중...")
        print(f"[{self.machine_type}] 배출구로 이동 중...")
