from creature import Creature

print("Welcome to Agachi simulator")
difficulty = int(input("Please choose a difficulty (1-5) : "))
Creature.set_difficulty(difficulty)

is_running = True
round = 1
creature = Creature(input("Name your creature : "))
creature.show_status()
while is_running:
    
    print(f"Round {round}")
    print("Choose an action : ")
    print("1. Eat")
    print("2. Play")
    print("3. Bath")

    action = int(input("Enter your choice : "))
    if action == 1 :
        creature.eat()
    if action == 2 :
        creature.play()
    if action == 3 :
        creature.bath()

    round += 1
    creature.update_values()
    if creature.is_dead():
        print(f"{creature.name} is dead. You survived for {round - 1} Rounds!!")
        is_running = False
    input("Press Enter to continue......")
        