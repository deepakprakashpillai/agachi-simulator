import random

class Creature:
    __difficulty = 0

    def __init__(self,name) -> None:
        self.name = name
        self.hunger = Creature.__difficulty
        self.boredom = Creature.__difficulty
        self.dirtiness = Creature.__difficulty
        self.is_alive = True

    @classmethod
    def set_difficulty(cls,diff):
        cls.__difficulty = diff

    def is_dead(self):
        if self.hunger == 10 or self.boredom == 10 or self.dirtiness == 10:
            self.is_alive = False
        return not self.is_alive

    def eat(self):
        self.hunger = max(self.hunger -random.randint(1,4),0)
        print("------------------------------------------------------------------------------------------------")
        print("After Eating")
        self.show_status()

    def play(self):
        num = random.randint(0,2)
        print(f"{self.name} is thinking of a number 0,1,2")
        guess = int(input("What is your guess : "))
        if num == guess:
            self.boredom = max(0,self.boredom-3)
        else:
            self.boredom = max(0,self.boredom-1)
        print("------------------------------------------------------------------------------------------------")
        print("After Playing")
        self.show_status()


    def bath(self):
        self.dirtiness = 0
        print("------------------------------------------------------------------------------------------------")
        print("After Bathing")
        self.show_status()

    def show_status(self):
        print(f"{self.name} Status")
        print("------------------------------------------------------------------------------------------------")
        print(f"Hunger : {self.hunger}")
        print(f"Boredom : {self.boredom}")
        print(f"Dirtiness : { self.dirtiness}")
        print("------------------------------------------------------------------------------------------------")

    def update_values(self):
        self.hunger  = min(10,self.hunger + Creature.__difficulty)        
        self.boredom = min(10,self.boredom + Creature.__difficulty)
        self.dirtiness = min(10,self.dirtiness + Creature.__difficulty)
        self.show_status()
