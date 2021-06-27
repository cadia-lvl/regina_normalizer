from . import tuple_rules as tp

sport_tuples = [("^[1-9]\d?\/[1-9]?\d$", '.*', 'between_teams', " <sil>")]

for rule, string, number in tp.ones_zip:
    sport_tuples.append(("^[1-9]?" + number + "\/[1-9]\d?$", rule, 'first_one', string))
    sport_tuples.append(("^[1-9]\d?\/[1-9]?" + number + "$", rule, 'second_one', string))

for string, number in tp.tens_zip:
    sport_tuples.append(("^" + number + "\/[1-9]\d?$", '.*', 'first_one', string))
    sport_tuples.append(("^[1-9]\d?\/" + number, '.*', 'second_one', string))

for string, number in tp.dozens_zip:
    sport_tuples.append(("^" + number + "0\/[1-9]\d?$", '.*', 'first_ten', string))
    sport_tuples.append(("^[1-9]\d?\/" + number + "0$", '.*', 'second_ten', string))
    sport_tuples.append(("^" + number + "[1-9]\/[1-9]\d?$", '.*', 'first_ten', string + " og"))
    sport_tuples.append(("^[1-9]\d?\/" + number + "[1-9]$", '.*', 'second_ten', string + " og"))