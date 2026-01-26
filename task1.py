from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass

class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("칼로 베는 행동을 구현")

class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("화살을 쏘는 행동을 구현")

class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("도끼로 찍는 행동을 구현")

class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("검을 휘두르는 행동을 구현")

class Character(ABC):
    def __init__(self):
        self.weapon: WeaponBehavior = None
    
    @abstractmethod
    def fight(self):
        pass

    def set_Weapon(self, w : WeaponBehavior):
        self.weapon = w

    def perform_fight(self):
        if self.weapon:
            self.weapon.use_weapon()
        else:
            print("무기가 없습니다")

class Queen(Character):
    def fight(self):
        print("여왕이 전투를 시작합니다.")

class King(Character):
    def fight(self):
        print("국왕이 전투를 시작합니다.")

class Troll(Character):
    def fight(self):
        print("트롤이 전투를 시작합니다.")

class Knight(Character):
    def fight(self):
        print("기사가 전투를 시작합니다.")
