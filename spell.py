import math

import params
import pandas

COST_CSV = 'costs.csv'
DUR_LOG_BASE = 1.2


def get_level(cost):
    idx = 0
    for boundary in params.LEVEL_BOUNDARIES:
        idx += 1
        if cost < boundary:
            break
    return idx


def get_intensity_desc(effect, intensity):
    if intensity >= len(params.INTENSITY_DESC[effect]):
        idx = -1
    else:
        idx = intensity

    return params.INTENSITY_DESC[effect][idx]


def is_compatible(form, effect):
    if effect == 'None':
        return True
    df_temp = pandas.read_csv(COST_CSV)
    df_cost = df_temp[df_temp["Rune"] == form]

    return df_cost[effect].values[0] != 0


def get_duration_string(index, dur, dvar):
    if dur == 'None':
        return ""
    durstring = f"Duration{index}: "
    if dur in params.DURATION_DICT.keys():
        durstring += f"{dvar} {params.DURATION_DICT[dur]}\n"
    else:
        durstring += f"{dur}\n"
    return durstring


class Spell:
    def __init__(self, name, *args):
        self.name = name
        # print(args)
        self.form = args[0]
        self.effect = args[1]
        if args[2] == 'None':
            self.intensity = 0
        else:
            self.intensity = int(args[2])
        self.effect2 = args[3]
        if args[4] == 'None':
            self.intensity2 = 0
        else:
            self.intensity2 = int(args[4])
        self.target = args[5]
        self.target2 = args[6]
        self.attachment = args[7]
        self.attachment2 = args[8]
        self.spell_range = args[9]
        self.spell_range2 = args[10]
        self.area = args[11]
        self.area2 = args[12]
        self.delivery = args[13]
        self.duration = args[14]
        if args[15] == 'None':
            self.duration_var = 0
        else:
            self.duration_var = int(args[15])
        self.duration2 = args[16]
        if args[17] == 'None':
            self.duration_var2 = 0
        else:
            self.duration_var2 = int(args[17])
        self.complexity = args[18]
        df_temp = pandas.read_csv(COST_CSV)
        self.df_cost = df_temp[df_temp["Rune"] == self.form]
        self.power_cost = self.calculate_power_cost()
        self.difficulty_cost = self.calculate_difficulty_cost()
        self.power_idx, self.difficulty_idx = \
            self.modify_levels(get_level(self.power_cost), get_level(self.difficulty_cost))

    def calc_duration_power_cost(self):
        cost = self.get_dur_pow_subcost(self.duration, self.duration_var)
        if self.duration2 != 'None':
            cost += self.get_dur_pow_subcost(self.duration2, self.duration_var2)
        return cost

    def get_dur_pow_subcost(self, dur, dur_var):
        duration_base = self.df_cost["Duration"].values[0]
        d_to_log = params.DURATION_COSTS["multiplier"][dur] * dur_var
        if d_to_log == 0:
            duration_cost = params.DURATION_COSTS["no_log"][dur]
        else:
            duration_cost = math.log(d_to_log, DUR_LOG_BASE) + 1
        duration_cost *= duration_base
        return duration_cost

    def calc_duration_difficulty_cost(self):
        return self.calc_duration_power_cost() / 2

    def calculate_power_cost(self):
        # get effect_intensity cost
        intsq = self.intensity ** 2
        ei_base = self.df_cost[self.effect].values[0]
        ei_cost = intsq * ei_base
        if self.effect2 != 'None':
            intsq2 = self.intensity2 ** 2
            ei_base2 = self.df_cost[self.effect2].values[0]
            ei_cost2 = intsq2 * ei_base2
            ei_cost = max(ei_cost, ei_cost2)
        # get target cost
        target_cost = params.TARGET_COSTS["power"][self.target]
        if self.target2 != 'None':
            target_cost += params.TARGET_COSTS["power"][self.target2]
        # get attachment cost
        att_cost = params.ATTACHMENT_COSTS["power"][self.attachment]
        if self.attachment2 != 'None':
            att_cost += params.ATTACHMENT_COSTS["power"][self.attachment2]
        # get range cost
        range_base = self.df_cost["Range"].values[0]
        range_idx = params.RANGES.index(self.spell_range)
        range_cost = range_base * range_idx
        if self.spell_range2 != 'None':
            print("********************")
            print(self.spell_range2)
            print("********************")
            range_cost += range_base * params.RANGES.index(self.spell_range2)
        # get area cost
        area_base = self.df_cost["Area"].values[0]
        area_idx = params.AREAS.index(self.area)
        area_cost = area_base * area_idx ** 4
        if self.area2 != 'None':
            area_cost += area_base * params.AREAS.index(self.area2) ** 4
        # get delivery cost
        delivery_cost = params.DELIVERY_COSTS["power"][self.delivery]
        # get duration cost
        duration_cost = self.calc_duration_power_cost()
        print("POWER COSTS")
        print(f"ei_cost: {ei_cost}")
        print(f"target cost: {target_cost}")
        print(f"attachment cost: {att_cost}")
        print(f"range cost: {range_cost}")
        print(f"area cost: {area_cost}")
        print(f"delivery cost: {delivery_cost}")
        print(f"duration cost: {duration_cost}")
        print("=============================")

        total = ei_cost + target_cost + att_cost + range_cost + area_cost + delivery_cost + duration_cost
        return total

    def calculate_difficulty_cost(self):
        # get effect_intensity cost
        ei_base = self.df_cost[self.effect].values[0]
        ei_cost = self.intensity * ei_base * 2
        if self.effect2 != 'None':
            ei_base2 = self.df_cost[self.effect2].values[0]
            ei_cost2 = self.intensity2 * ei_base2 * 2
            ei_cost = ei_cost + ei_cost2
        # get target cost
        target_cost = params.TARGET_COSTS["difficulty"][self.target]
        if self.target2 != 'None':
            target_cost += params.TARGET_COSTS["difficulty"][self.target2]
        # get attachment cost
        att_cost = params.ATTACHMENT_COSTS["difficulty"][self.attachment]
        if self.attachment2 != 'None':
            att_cost += params.ATTACHMENT_COSTS["difficulty"][self.attachment2]
        # get range cost
        range_base = self.df_cost["Range"].values[0]
        range_idx = params.RANGES.index(self.spell_range)
        range_cost = range_base * int(math.sqrt(range_idx))
        if self.spell_range2 != 'None':
            range_cost += self.df_cost["Range"].values[0] * int(math.sqrt(params.RANGES.index(self.spell_range2)))
        # get area cost
        area_base = self.df_cost["Area"].values[0]
        area_idx = params.AREAS.index(self.area)
        area_cost = area_base * area_idx ** 4
        if self.area2 != 'None':
            area_cost += self.df_cost["Area"].values[0] * params.AREAS.index(self.area2) ** 2
        # get delivery cost
        delivery_cost = params.DELIVERY_COSTS["difficulty"][self.delivery]
        # get duration cost
        duration_cost = self.calc_duration_difficulty_cost()
        print("DIFFICULTY COSTS")
        print(f"ei_cost: {ei_cost}")
        print(f"target cost: {target_cost}")
        print(f"attachment cost: {att_cost}")
        print(f"range cost: {range_cost}")
        print(f"area cost: {area_cost}")
        print(f"delivery cost: {delivery_cost}")
        print(f"duration cost: {duration_cost}")
        print("==============================")

        total = ei_cost + target_cost + att_cost + range_cost + area_cost + delivery_cost + duration_cost
        return total

    def modify_levels(self, power_level, difficulty_level):
        power_level += params.COMPLEXITY_MOD[self.complexity][0]
        difficulty_level += params.COMPLEXITY_MOD[self.complexity][1]
        return int(power_level), int(difficulty_level)

    def dump_spell(self):
        return self.name + "\n---------------\n" + self.dump_spell_without_name()

    def dump_spell_without_name(self):
        # spell_text = self.name + "\n---------------\n"
        spell_text = f"Form: {self.form}\n"
        spell_text += f"Effect: {self.effect}\n"
        spell_text += f"Intensity: {self.intensity} --> {get_intensity_desc(self.effect, self.intensity)}\n"
        if self.effect2 != 'None':
            spell_text += f"Effect2: {self.effect2}\n"
            spell_text += f"Intensity2: {self.intensity2} - {get_intensity_desc(self.effect2, self.intensity2)}\n"
        spell_text += f"Target: {self.target}\n"
        if self.target2 != 'None':
            spell_text += f"Target2: {self.target2}\n"
        spell_text += f"Attachment: {self.attachment}\n"
        if self.attachment2 != 'Normal':
            spell_text += f"Attachment2: {self.attachment2}\n"
        spell_text += f"Spell range: {self.spell_range}\n"
        if self.spell_range2 != 'None':
            spell_text += f"Spell range2: {self.spell_range2}\n"
        spell_text += f"Area: {self.area}\n"
        if self.area2 != 'None':
            spell_text += f"Area2: {self.area2}\n"
        spell_text += f"Delivery: {self.delivery}\n"
        spell_text += get_duration_string("", self.duration, self.duration_var)
        spell_text += get_duration_string("2", self.duration2, self.duration_var2)
        spell_text += f"Complexity: {self.complexity}\n"
        spell_text += f"Power cost: {self.power_cost:.2f}\n"
        spell_text += f"Difficulty cost: {self.difficulty_cost:.2f}\n"
        spell_text += "================================\n"
        spell_text += f"Power level: {params.LEVELS[self.power_idx]}\n"
        spell_text += f"Difficulty level: {params.LEVELS[self.difficulty_idx]}\n"

        return spell_text
