class Warrior:
  def __init__(self,name,attack,defense):
    self.name = name
    self.a = attack
    self.d = defense
    
  def status(self):
    print("이름 : {}, 공격력 : {}, 방어력 : {} ".format(self.name,self.a,self.d))

  def attack(self):
    print("{}이 {}의 데미지를 입힙니다.".format(self.name,self.a))

  def defense(self):
    print("{}이 {}의 데미지를 방어합니다.".format(self.name,self.d))
   
# w1 = Warrior("이순신", 20, 10)
# w2 = Warrior("강감찬", 15, 15)

# w1.status() # 이름 : 이순신, 공격력 : 20, 방어력 : 10 
# w2.status() # 이름 : 강감찬, 공격력 : 15, 방어력 : 15 

# w1.attack() # 이순신이 20의 데미지를 입힙민다.
# w2.attack() # 강감찬이 15의 데미지를 입힙민다. 

# w1.defense() # 이순신이 10 데미지를 방어합니다.
# w2.defense() # 강감찬이 15 데미지를 방어합니다.