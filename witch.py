from spell import Spell
from fractions import Fraction
import params

FUDGE_PROBS = {
    4: Fraction(1, 81),  # rolling +4
    3: Fraction(5, 81),  # rolling +3 or better
    2: Fraction(15, 81),  # rolling +2 or better
    1: Fraction(31, 81),  # rolling +1 or better
    0: Fraction(50, 81),  # etc.. etc...
    -1: Fraction(66, 81),
    -2: Fraction(76, 81),
    -3: Fraction(80, 81),
}


class Witch:
    def __init__(self, magic, rune_skill):
        self.magic = magic
        self.rune_skill = rune_skill

    def assess_spell(self, rune_spell: Spell):
        magic_num = params.LEVELS_DICT[self.magic]
        assess_string = ""
        cast_chance = float(self.cast_chance(rune_spell)) * 100
        chance_str = "{:.0f}".format(cast_chance)
        if rune_spell.power_idx > magic_num:
            assess_string = f"Spell Power ({params.LEVELS[rune_spell.power_idx]} is higher than Magic ({self.magic}.\n"
        elif cast_chance == 0:
            assess_string = "Spell is too difficult to cast.\n"
        else:
            assess_string = f"Witch can cast spell -> {chance_str}% of success."
        return assess_string

    def cast_chance(self, rune_spell: Spell):
        roll_required = rune_spell.difficulty_idx - params.LEVELS_DICT[self.rune_skill]
        if roll_required > 4:
            return 0
        elif roll_required < -3:
            return 1
        else:
            return FUDGE_PROBS[roll_required]
