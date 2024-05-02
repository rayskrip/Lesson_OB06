import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        self.attack_power = random.randint(10, 20)
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name}, нанося урон {self.attack_power}. Здоровье {other.name} теперь {other.health}.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        initial_player_attack = random.randint(10, 20)
        initial_computer_attack = random.randint(10, 20)
        self.player = Hero(player_name, health=100, attack_power=initial_player_attack)
        self.computer = Hero(computer_name, health=100, attack_power=initial_computer_attack)

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


player_name = input("Введите имя игрока: ")
computer_name = "Компьютер"
game = Game(player_name, computer_name)
game.start()
