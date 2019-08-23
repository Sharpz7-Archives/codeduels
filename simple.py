"""
TODO
Rework how multiplayer will function.
Rework how CPU will work.
"""

from codeduel import Ability, DuelBot

# Abilities can be created by the user
# There are limits of how OP these can be, so its
# very useful.
attack = Ability(
    name="Knife",
    damage=10,
)

dueler = DuelBot("James", attack)
dueler.strategise()
dueler.begin()
