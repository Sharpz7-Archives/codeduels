def strategy(self, duel, opp):
    """
    The strategy for the Dueler Bot.
    This has a lot of potential, we will give a example
    below
    """
    duel.attack(self.ability)
    # Here is a light example of whats possible
    # The combinations are virtually endless
    #
    # if self.health > 50 or self.energy < 40:
    #     duel.attack(self.low_energy_ability)
    # elif self.health < 10:
    #     duel.attack(self.high_mobility_ability)
    # elif opp.health < 20:
    #     duel.attack(self.high_damage_ability)
