from abc import ABC, abstractmethod

# 추상 클래스
class VendingMachine(ABC):
    def __init__(self, price, machine_type):
        self.price = price
        self.machine_type = machine_type

    # 템플릿 메서드
    def serve(self, amount: int):
        self.insert_amount(amount)
        if self.check_amount(amount):
            self.prepare_product()
            self.take_out()
            self.return_change(amount)
        else:
            print(f"{self.machine_type} 금액이 부족합니다.")
            self.return_change(amount)
        print()
    # 돈 투입
    def insert_amount(self, amount):
        print(f"{self.machine_type} 돈 투입: {amount}원")

    # 금액 확인 반환값에 따라 if, else 실행 결정
    def check_amount(self, amount):
        print(f"{self.machine_type} 금액 확인 완료 (필요: {self.price}원)")
        return amount >= self.price

    # 제품 준비 (추상메소드: 서브클래스에서 구현)
    @abstractmethod
    def prepare_product(self):
        pass

    # 제품 배출
    def take_out(self):
        print(f"{self.machine_type} 제품 배출 완료")

    # 거스름돈 반환
    def return_change(self, amount):
        change = amount - self.price
        if change >= 0:
            print(f"{self.machine_type} {change}원 반환")