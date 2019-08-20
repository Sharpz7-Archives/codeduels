import random as r


class Ability:
    """
    Allows for custom abilities to be created.

    By using energy, there are clear limits of how powerful these
    abilites can be.

    Some will increase energy (Extra damage, extra health etc)
    but some will decrease energy, like longer cooldowns, and lower accuracy.
    """
    def __init__(self, name, **kwargs):
        # Name arg
        self.name = name

        # General Args
        self.cooldown_length = 0
        self.buff = False

        # Buff args
        self.health = None
        self.move = None

        # Debuff args
        self.damage = None
        self.accuracy = None
        self.range = None

        # Set the actual args
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Setup vars
        self.cooldown = self.cooldown_length
        self.energy = self.calc_energy()

    def do_ability(self, main, opp):
        """
        Run the ability method

        Checks to see if the cooldown is off or on,
        and takes away the energy.
        """

        cooldown_ready = self.cooldown >= self.cooldown_length
        if cooldown_ready:
            self.apply_ability(main, opp)
            main.energy -= self.energy
            self.cooldown = 0
            return True

        self.cooldown += 1

    def check_stats(self):
        """
        Check if all stats make sense and match
        """
        pass

    def calc_energy(self):
        """
        Use a equation to calculate the energy of the ability
        """
        # TODO write the equation
        return 10

    def apply_ability(self, main, opp):
        """
        Applies the changes stats to both users.
        """

        # If the move hit...
        if r.random() < main.accuracy:
            if self.move:
                self.dueler += self.move

            if self.range:
                # if opp in range
                opp -= self.damage

            if self.health:
                main.health += self.health

            if self.damage:
                opp.health -= self.damage
