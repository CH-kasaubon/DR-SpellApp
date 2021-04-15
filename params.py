FORMS = ['Fire', 'Ice', 'Lightning', 'Law', 'Chaos', 'Stasis',
         'Movement', 'Air', 'Earth', 'Water', 'Strength', 'Luck',
         'Seeming', 'Life']
FORMS_LAW = ['Ice', 'Law', 'Stasis', 'Earth', 'Water', 'Strength', 'Seeming']
FORMS_CHAOS = ['Fire', 'Lightning', 'Chaos', 'Movement', 'Air', 'Luck']
EFFECTS = ['None', 'Damage', 'DurationDamage', 'DamageStickyMax', 'Restrict', 'Enhance', 'Dislocate',
           'Levitate', 'Animate', 'Barrier', 'Create', 'Destroy', 'Warp', 'Transform', 'Light',
           'Obscure', 'Find', 'Dispel', 'Heal']
EFFECTS_LAW = ['None', 'Damage', 'DurationDamage', 'DamageStickyMax', 'Restrict',
               'Enhance', 'Barrier', 'Create', 'Warp', 'Transform', 'Obscure', 'Find', 'Dispel']
EFFECTS_CHAOS = ['None', 'Damage', 'DurationDamage', 'DamageStickyMax', 'Restrict', 'Enhance', 'Dislocate',
                 'Levitate', 'Animate', 'Barrier', 'Destroy', 'Warp', 'Transform', 'Light',
                 'Obscure', 'Find', 'Dispel']
TARGETS = ['None', 'Mark', 'Living', 'Connection', 'Magic', 'Undifferentiated', 'Feature']
RANGES = ['None', 'Self', 'Touch', '10cm', '1m', '2m', '5m',
          '10m', '20m', '30m', '50m', '100m', '200m', '300m', '500m']
AREAS = ['None', 'Weapon', 'Person', '2 People in Contact, big creature',
         'Room/3m diam/6 people', 'Hall/8m diam/12 people',
         'Clearing/15m diam/20 people', 'Street/30m diam/50 people',
         'Village/50m diam/100 people', 'Small Town/100m diam/few hundred people',
         'Large Town/200m diam/500 people', 'City/500m diam/thousand people']
DELIVERY = ['Contact', 'Self', 'Ray', 'Direct', 'Selective', 'Trigger']
DURATIONS = ['None', 'Instant', 'Transient', 'Temporary (Rounds)',
             'Medium Term (Minutes)', 'Long Term (Hours)', 'Permanent']
DURATION_DICT = {
    'Temporary (Rounds)': 'rounds', 'Medium Term (Minutes)': 'minutes', 'Long Term (Hours)': 'hours'
}
DURATIONS_CHAOS = ['None', 'Transient', 'Temporary (Rounds)', 'Medium Term (Minutes)']
DURATION_NEED_VAR = ['Temporary (Rounds)', 'Medium Term (Minutes)', 'Long Term (Hours)']
DURATION_VAR = ["None", "1", "2", "3", "6", "12", "24", "30"]
INTENSITY_VAR = ['None'] + [str(x) for x in range(1, 17)]

ATTACHMENTS = ['Normal', 'Suspended', 'Sticky - Unwilling', 'Sticky']
COMPLEXITY = ['Normal', 'More Efficient', 'Much More Efficient',
              'More Brute Force', 'Much More Brute Force']
# intensity meaning for some effects
# the first entry in each list is for 'None'
INTENSITY_DESC = {
    "None": [" "],
    "Damage": ['0 Damage', '1 Damage', '2 Damage', '3 Damage', '3 Damage', '4 Damage', '4 Damage',
               '5 Damage', '5 Damage', '5 Damage', '6 Damage', '6 Damage', '6 Damage', '6 Damage',
               '7 Damage', '7 Damage', '7 Damage'],
    "DurationDamage": ['0 duration damage', '0 duration damage', '1 duration damage', '1 duration damage',
                       '2 duration damage', '2 duration damage', '3 duration damage', '3 duration damage',
                       '3 duration damage', '4 duration damage', '4 duration damage', '4 duration damage',
                       '4 duration damage', '4 duration damage', '5 duration damage', '5 duration damage',
                       '5 duration damage'],
    "DamageStickyMax": ['0 max damage', '2 max damage', '4 max damage', '5 max damage', '6 max damage', '7 max damage',
                        '8 max damage', '9 max damage', '10 max damage', '11 max damage', '12 max damage',
                        '13 max damage', '14 max damage', '14 max damage', '15 max damage'],
    "Restrict": ['0 Restriction', '1 Restriction', '2 Restriction', '3 Restriction', '3 Restriction',
                 '4 Restriction', '4 Restriction', '5 Restriction', '5 Restriction', '5 Restriction',
                 '6 Restriction', '6 Restriction', '6 Restriction', '6 Restriction',
                 '7 Restriction', '7 Restriction', '7 Restriction'],
    "Enhance": ['+0 Enhancement', '+1 Enhancement', '+1 Enhancement',
                '+2 Enhancement', '+2 Enhancement', '+3 Enhancement', '+3 Enhancement', '+3 Enhancement',
                '+4 Enhancement', '+4 Enhancement', '+4 Enhancement', '+5 Enhancement', '+5 Enhancement',
                '+5 Enhancement', '+6 Enhancement', '+6 Enhancement', '+6 Enhancement'],
    "Barrier": ['0 Barrier', '1 Barrier', '1 Barrier', '2 Barrier', '2 Barrier', '3 Barrier', '3 Barrier',
                '4 Barrier', '4 Barrier', '5 Barrier', '5 Barrier', '6 Barrier', '6 Barrier',
                '7 Barrier', '7 Barrier', '8 Barrier'],
    "Dislocate": ["", "Sense", "Object", "Living"],
    "Levitate": ["", "Waft", "Walk", "Run", "Horse"],
    "Animate": ["", "Just Moving", "Slow (-2)", "Normal", "Fast (+1)"],
    "Create": ["", "Seeming (Plain)", "Gas (real)/Seeming(simply pattern)",
               "Liquid (real)/ Seeming complex pattern, simple movement)",
               "Soft solid (ice/earth)/ Seeming (animation)",
               "Hard Solid (stone)"],
    "Destroy": ["", "Gas", "Liquid", "Soft solid (wood)", "Hard Solid", "Q"],
    "Warp": ["", "Gas", "Liquid", "Soft solid (wood)", "Hard Solid"],
    "Transform": ["", "Seeming(variant)", "Same Size/ Seeming (different person)/Fire to smoke etc",
                  "Smaller/Seeming - very different/To similar element", "Larger/Combine eg earth to mud"],
    "Light": ["", "Candle", "Torch", "Indoor", "Daylight"],
    "Obscure": ["", "Mist", "Fog", "Pitch Black"],
    "Dispel": ["", "Dispel"],
    "Find": ["", "Det:Y/N", "Direction", "Dir and dist", "Location"],
}

TARGET_COSTS = {
    "difficulty": {
        'None': 0,
        'Mark': 30,
        'Living': 10,
        'Connection': 50,
        'Magic': 10,
        'Undifferentiated': 0,
        'Feature': 60,
    },
    "power": {
        'None': 0,
        'Mark': 10,
        'Living': 5,
        'Connection': 10,
        'Magic': 5,
        'Undifferentiated': 0,
        'Feature': 30,
    }
}
ATTACHMENT_COSTS = {
    "difficulty": {
        'None': 0,
        'Normal': 0,
        'Suspended': 10,
        'Sticky - Unwilling': 20,
        'Sticky': 15,
    },
    "power": {
        'None': 0,
        'Normal': 0,
        'Suspended': 30,
        'Sticky - Unwilling': 20,
        'Sticky': 10,
    }
}
DELIVERY_COSTS = {
    "difficulty": {
        'None': 0,
        'Contact': 5,
        'Self': 0,
        'Ray': 10,
        'Direct': 30,
        'Selective': 50,
        'Trigger': 60,
    },
    "power": {
        'None': 0,
        'Contact': 2,
        'Self': 0,
        'Ray': 5,
        'Direct': 10,
        'Selective': 10,
        'Trigger': 20,
    }
}
DURATION_COSTS = {
    "no_log": {
        'None': 0,
        'Transient': 1,
        'Temporary (Rounds)': 1,
        'Medium Term (Minutes)': 1,
        'Long Term (Hours)': 1,
        'Permanent': 60,
        'Instant': 60,
    },
    "multiplier": {
        'None': 0,
        'Transient': 0,
        'Temporary (Rounds)': 1,
        'Medium Term (Minutes)': 12,
        'Long Term (Hours)': 720,
        'Permanent': 0,
        'Instant': 0,
    }
}
COMPLEXITY_MOD = {
    'Normal': (0, 0),
    'More Efficient': (-1, 1),
    'Much More Efficient': (-2, 3),
    'More Brute Force': (1, -1),
    'Much More Brute Force': (2, -3),
}
LEVEL_BOUNDARIES = [60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

LEVELS = ['None', 'Weak (1)', 'Basic (2)',
          'Mediocre (3)', 'Fair (4)', 'Good (5)',
          'Great (6)', 'Superb (7)',
          'Legendary (8)', 'Legendary 2 (9)',
          'Legendary 3 (10)', 'Legendary 4 (11)',
          'Legendary 5 (12)', 'Legendary 6 (13)',
          'Legendary 7 (14)', 'Legendary 8 (15)', ]

LEVELS_DICT = {LEVELS[k]: k for k in range(16)}
