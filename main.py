from tkinter import *
from tkinter import _setit as tk_setit
from witch import Witch
from tkinter import messagebox
import params
import spell

FONT = ('Helvetica', 8)
OPTIONS = {"Form": params.FORMS,
           "Effect": params.EFFECTS,
           "Intensity": params.INTENSITY_VAR,
           "Effect2": params.EFFECTS,
           "Intensity2": params.INTENSITY_VAR,
           "Target": params.TARGETS,
           "Target2": params.TARGETS,
           "Attachment": params.ATTACHMENTS,
           "Attachment2": params.ATTACHMENTS,
           "Range": params.RANGES,
           "Range2": params.RANGES,
           "Area": params.AREAS,
           "Area2": params.AREAS,
           "Delivery": params.DELIVERY,
           "Duration": params.DURATIONS,
           "Time": params.DURATION_VAR,
           "Duration2": params.DURATIONS,
           "Time2": params.DURATION_VAR,
           "Complexity": params.COMPLEXITY}

OPTIONS_FORM = {"All": params.FORMS,
                "Law": params.FORMS_LAW,
                "Chaos": params.FORMS_CHAOS}
OPTIONS_EFFECT = {"All": params.EFFECTS,
                  "Law": params.EFFECTS_LAW,
                  "Chaos": params.EFFECTS_CHAOS}
OPTIONS_DURATION = {"All": params.DURATIONS,
                    "Law": params.DURATIONS,
                    "Chaos": params.DURATIONS_CHAOS}
OPTIONS_RUNE_TYPE = {"Form": OPTIONS_FORM,
                     "Effect": OPTIONS_EFFECT,
                     "Effect2": OPTIONS_EFFECT,
                     "Duration": OPTIONS_DURATION,
                     "Duration2": OPTIONS_DURATION}

SAVE_FILE = 'spells.txt'
RUNE_TYPES = {"All": "All",
              "Law": "Law",
              "Chaos": "Chaos"}

BG_COLOR_MENU = 'linen'


def save_spell():
    spell_desc = descbox.get("1.0", "end")
    rune_spell = calculate()
    if rune_spell is None:
        return
    w_string = f"{rune_spell.name}\n----------------\n"
    w_string += spell_desc
    w_string += "----------------\n"
    w_string += rune_spell.dump_spell_without_name()
    w_string += "==============================\n"

    if messagebox.askokcancel(title='Save Spell to File', message=w_string):
        try:
            with open(SAVE_FILE, "a") as f:
                f.write(w_string)
        except FileNotFoundError:
            pass


def reset_values():
    if messagebox.askokcancel(title='Reset All Parameters', message="Reset all parameters to initial states."):
        for ko in OPTIONS.keys():
            optval_dict[ko][0].set(OPTIONS[ko][0])
        descbox.delete('1.0', 'end')
        descbox.insert('1.0', "User Can Type Description Here")


def calculate():
    args = []
    spell_name = name_entry.get()
    for opt, opt_tuple in optval_dict.items():
        args.append(opt_tuple[0].get())
        # print(f"{opt}: {opt_tuple[0].get()}")
    if args[1] != 'None':
        rune_spell = spell.Spell(spell_name, *args)
    else:
        rune_spell = None
    return rune_spell


def alter_label(*args):
    args = []
    menus = []
    for opt, opt_tuple in optval_dict.items():
        args.append(opt_tuple[0].get())
        menus.append(opt_tuple[1])
    form = args[0]
    effect = args[1]
    effect_menu = menus[1]

    if not spell.is_compatible(form, effect):
        effect_menu.config(bg="red")
        spell_text = ""
        witch_text = ""
    else:
        effect_menu.config(bg=BG_COLOR_MENU)
        rune_spell = calculate()
        if rune_spell is not None:
            spell_text = rune_spell.dump_spell()
            witch_text = witch.assess_spell(rune_spell)
        else:
            spell_text = ""
            witch_text = ""

    textbox.delete(1.0, END)
    textbox.insert(1.0, spell_text)
    witchbox.delete(1.0, END)
    witchbox.insert(1.0, witch_text)


def update_rune_types(*args):
    rune = rune_choice.get()
    fields = ["Form", "Effect", "Effect2", "Duration", "Duration2"]

    var_dict = {kf: optval_dict[kf][0].get() for kf in fields}
    build_dict = {kf: optval_dict[kf][1] for kf in var_dict.keys()}
    for ko, o_menu in build_dict.items():
        o_menu['menu'].delete(0, 'end')
        for opt in OPTIONS_RUNE_TYPE[ko][rune]:
            o_menu['menu'].add_command(label=opt, command=tk_setit(optval_dict[ko][0], opt))
        if var_dict[ko] in OPTIONS_RUNE_TYPE[ko][rune]:
            optval_dict[ko][0].set(var_dict[ko])
        else:
            optval_dict[ko][0].set(OPTIONS_RUNE_TYPE[ko][rune][0])


def alter_wmagic(*args):
    global witch
    witch.magic = witch_magic.get()
    alter_label()


def alter_wrune(*args):
    global witch
    witch.rune_skill = witch_rune_skill.get()
    alter_label()


window = Tk()
window.minsize(width=600, height=600)
window.title("Spell Creator")
window.config(padx=20, pady=20, bg="white")

rune_choice = StringVar(window, "All")
idx = 0
for text, val in RUNE_TYPES.items():
    Radiobutton(text=text, variable=rune_choice, value=val).grid(row=idx, column=0, sticky="w")
    idx += 1
rune_choice.trace_add("write", update_rune_types)

# witch
witch_magic = StringVar(window, "Weak (1)")
witch_rune_skill = StringVar(window, "Weak (1)")

witch_magic.trace_add('write', alter_wmagic)
witch_rune_skill.trace_add('write', alter_wrune)

wm_label = Label(text="Witch Magic Score:", bg="white")
wm_label.config(font=FONT)
wm_label.grid(row=1, column=1, sticky="e")
wrs_label = Label(text="Witch Rune Skill:", bg="white")
wrs_label.config(font=FONT)
wrs_label.grid(row=2, column=1, sticky="e")

witch = Witch(witch_magic.get(), witch_rune_skill.get())

wm_menu = OptionMenu(window, witch_magic, *params.LEVELS)
wm_menu.config(width=20, font=FONT)
wm_menu.grid(row=1, column=2, sticky="w")
wrs_menu = OptionMenu(window, witch_rune_skill, *params.LEVELS)
wrs_menu.config(width=20, font=FONT)
wrs_menu.grid(row=2, column=2, sticky="w")

# witch textbox
witchbox = Text(width=40, height=5)
witchbox.config(padx=5, pady=5)
witchbox.grid(row=3, column=2, rowspan=4)
witchbox.insert(1.0, "The chance of successful casting will\nappear here.")

labels = []

name_label = Label(text="Name:", bg="white")
name_label.config(font=FONT)
name_label.grid(row=idx, column=0)
labels.append(name_label)
name_entry = Entry(width=45)
name_entry.config(font=FONT)
name_entry.grid(row=idx, column=1)
idx += 1

optval_dict = {}

for key, option in OPTIONS.items():
    opt_label = Label(text=f"{key}:", bg="white")
    opt_label.config(font=FONT)
    opt_label.grid(row=idx, column=0)
    labels.append(opt_label)

    opt_var = StringVar(window)
    opt_var.set(option[0])
    opt_var.trace_add('write', alter_label)
    option_menu = OptionMenu(window, opt_var, *option)
    option_menu.config(width=40, font=FONT, bg=BG_COLOR_MENU)
    option_menu.grid(row=idx, column=1)
    idx += 1
    optval_dict[key] = (opt_var, option_menu)

# calc_button = Button(text="Calculate", command=calculate)
# calc_button.grid(row=idx, column=0)

reset_button = Button(text="Reset", command=reset_values)
reset_button.config(bg="grey")
reset_button.grid(row=idx, column=1)

save_button = Button(text=f"Save Spell to \'{SAVE_FILE}\'", command=save_spell)
save_button.config(bg="pink")
save_button.grid(row=idx, column=2)

textbox = Text(width=40, height=20)
textbox.config(padx=5, pady=5)
textbox.grid(row=5, column=2, rowspan=17)
textbox.insert(1.0, "Spell Details will appear here.")

descbox = Text(width=40, height=4)
descbox.config(padx=5, pady=5)
descbox.grid(row=19, column=2, rowspan=4)
descbox.insert(1.0, "User Can Type Description Here")

calculate()

window.mainloop()
