from .ability import Ability
from .errors import NotEnoughEnergy
import random as r
import time


class Duel:
    """
    The logic for duels.

    Currently setup to work with the CPU class,
    but this is written in the same way as the user
    class.
    """
    def __init__(self, player1, player2=None):
        # Player args
        self.p1 = player1
        self.p2 = player2

        # If player2 is not set, make it the CPU
        if not self.p2:
            self.p2 = CPU("CPU", attack)

        # Make the starting player random.
        self.order = r.sample([self.p1, self.p2], 2)

    def start(self):
        """
        Starts the duel.
        """

        # While both players are alive
        while self.p1.health > 0 and self.p2.health > 0:

            # Ensures both users have a move
            for x, y in [(0, 1), (1, 0)]:
                time.sleep(1)

                # Sets the player and opponent
                self.main = self.order[x]
                self.opp = self.order[y]

                # Runs the bots strategy
                self.main.strategy(self, self.opp)

                # Debugging
                print(self.main, "\n")

        # If player 1 died, show player 2 won
        if self.p1.health < 0:
            print(f"{self.p2.name} has won!!!")
            exit()

        # If player 2 died, show player 1 won.
        elif self.p2.health < 0:
            print(f"{self.p1.name} has won!!!")
            exit()

        # Its a draw...
        else:
            print("You both died... lol get good")
            exit()

    def attack(self, ability):
        """
        Attack Method

        Errors if there is not enough energy

        This method is really not needed
        """
        if ability.energy < self.main.energy:
            ability.do_ability(self.main, self.opp)
        elif not isinstance(self.main, CPU):
            raise NotEnoughEnergy(f"{ability.name} took too much energy")


class DuelBot:
    """
    Main DuelBot class
    """
    def __init__(self, ability):
        # Setup vars
        self.position = 0
        self.health = 100
        self.accuracy = 1
        self.energy = 100

    def begin(self):
        """
        Start a duel

        Again, I feel this can be reworked.
        """
        duel = Duel(self)
        duel.start()
    
    def strategise(self):
        with open("strategy.py", "r") as sF:
            strategyCode = sF.read()[31::]
        
        strategyCode = [i.lstrip() for i in strategyCode.split("\n")]
        strategyCode = [i + "\n" for i in strategyCode]
        strategyCode = "".join(strategyCode)
        print(strategyCode)
        #
        eval(strategyCode)

    def __repr__(self):
        return (
            f"{self.name} Stats\n"
            f"Health {self.health}\n"
            f"Position {self.position}\n"
            f"Accuracy {self.accuracy}\n"
            f"Energy {self.energy}"
        )


class CPU(DuelBot):
    """
    CPU Bot for singleplayer
    """
    def __init__(self, name, ability):
        super().__init__(ability)
        self.name = name
        self.ability = ability

    def strategy(self, duel, opp):
        duel.attack(self.ability)


attack = Ability(
    name="Knife",
    damage=10,
)
