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
        self._cooldown_length = 0

        # Buff args
        self._health = 0
        self._move = 0

        # Debuff args
        self._damage = 0
        self._accuracy = 0
        self._range = 0

        # Set the actual args
        for key, value in kwargs.items():
            setattr(self, f"_{key}", int(value))

        # Deal with Negatives
        self._cooldown_length = abs(self._cooldown_length)
        self._range = abs(self._range)
        self._accuracy = abs(self._accuracy)

        # Setup vars
        self._cooldown = self._cooldown_length
        self._energy = self.calc_energy()

    def do_ability(self, main, opp):
        """
        Run the ability method

        Checks to see if the cooldown is off or on,
        and takes away the energy.
        """

        cooldown_ready = self._cooldown >= self._cooldown_length
        if cooldown_ready:
            self.apply_ability(main, opp)
            main._energy -= self._energy
            self.cooldown = 0
            return True

        self._cooldown += 1

    def distance(self, main, opp):
        """
        Calculate the Distance between the two
        players.
        """

        return abs(main._position - opp._position)

    def calc_energy(self):
        """
        Use a equation to calculate the energy of the ability
        """

        energy = 0

        if self._cooldown_length:
            energy -= self._cooldown_length * 2

        if self._health:
            energy += self._health * 3

        if self._move:
            energy += int(self._move * 1.5)

        if self._damage:
            energy += self._damage * 2

        if self._accuracy:
            energy += self._accuracy * 5

        if self._range:
            energy += int(self._range * 1.5)

        if energy < 0:
            energy = 0

        return energy

    def apply_ability(self, main, opp):
        """
        Applies the changes stats to both users.
        """

        # If the move hit...
        if r.random() < main._accuracy/100:
            if self._move:
                main._position += self._move

            if self._health:
                main._health += self._health

            if self._damage:
                if self._range >= self.distance(main, opp):
                    opp._health -= self._damage

            if self._accuracy:
                opp._accuracy -= self._accuracy
