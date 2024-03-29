import os
import random as r
import time

from tabulate import tabulate


class Duel:
    """
    The logic for duels.

    Currently setup to work with the CPU class,
    but this is written in the same way as the user
    class.
    """
    def __init__(self, player1, player2):
        # Setup Vars

        self.headers = ["Name", "Health", "Energy", "Accuracy", "Position"]
        # Player args
        self.p1 = player1
        self.p2 = player2

        # Make the starting player random.
        self._order = r.sample([self.p1, self.p2], 2)

    def start(self):
        """
        Starts the duel.
        """

        # While both players are alive
        while self.p1._health > 0 and self.p2._health > 0:

            # Ensures both users have a move
            for x, y in [(0, 1), (1, 0)]:
                time.sleep(1)

                # Sets the player and opponent
                self.main = self._order[x]
                self.opp = self._order[y]

                # Runs the bots strategy
                self.main.strategy(self, self.opp)

                # Display the game
                self.display()
                self.main._energy += 5

                if self.main._health <= 0 or self.opp._health <= 0:
                    break

        # If player 1 died, show player 2 won
        if self.p1._health <= 0:
            print(f"{self.p2.name} has won!!!")
            exit()

        # If player 2 died, show player 1 won.
        elif self.p2._health <= 0:
            print(f"{self.p1.name} has won!!!")
            exit()

        # Its a draw...
        else:
            print("You both died... lol get good")
            exit()

    def display(self):
        os.system("clear||cls")
        print(tabulate([self.p1, self.p2], headers=self.headers))

    def ability(self, ability):
        """
        Ability Method

        Errors if there is not enough energy

        This method is really not needed
        """
        if ability._energy <= self.main._energy:
            ability.do_ability(self.main, self.opp)


class DuelBot:
    """
    Main DuelBot class
    """
    def __init__(self):
        # Setup vars
        self._position = 0
        self._health = 100
        self._accuracy = 100
        self._energy = 100

    def __iter__(self):
        for stat in [
            self.name,
            self._health,
            self._energy,
            self._accuracy,
            self._position
        ]:
            yield stat

    def position(self):
        return self._position

    def health(self):
        return self._health

    def accuracy(self):
        return self._accuracy

    def energy(self):
        return self._energy
