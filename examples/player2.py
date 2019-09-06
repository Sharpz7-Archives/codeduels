from codeduel import Ability, DuelBot


class OppsBot(DuelBot):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def strategy(self, duel, opp):
        duel.attack(attack)


attack = Ability(
    name="Knife",
    damage=10,
)

cpu = OppsBot("Opponent")
