"""
TODO
Rework how multiplayer will function.
Rework how CPU will work.
"""

from codeduel import Ability, DuelBot


class AdamsBot(DuelBot):
    """
    Subclass of the Client class
    This means that we can hide other methods without the
    coders having to worry about it
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def strategy(self, duel, opp):
        """
        The strategy for the Dueler Bot.
        This has a lot of potential, we will give a example
        below
        """

        duel.attack(attack)
        # Here is a light example of whats possible
        # The combinations are virtually endless
        #
        # if self.health > 50 or self.energy < 40:
        #     duel.attack(self.low_energy_ability)
        # elif self.health < 10:
        #     duel.attack(self.high_mobility_ability)
        # elif opp.health < 20:
        #     duel.attack(self.high_damage_ability)


# Abilities can be created by the user
# There are limits of how OP these can be, so its
# very useful.
attack = Ability(
    name="Knife",
    damage=10,
    health=5,
    range=100,
    accuracy=10,
)

dueler = AdamsBot("James")
dueler.begin()
