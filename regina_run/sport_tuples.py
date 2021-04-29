from tuple_rules import ones_zip, ones_zip_time, tens_zip, dozens_zip
from number_patterns import nonoun

sport_tuples = [("^[1-9]\d?\/[1-9]?\d$", '.*', 'between_teams', " <sil>")]

for rule, string, number in ones_zip:
    sport_tuples.append(("^[1-9]?" + number + "\/[1-9]\d?$", rule, 'first_one', string))
    sport_tuples.append(("^[1-9]\d?\/[1-9]?" + number + "$", rule, 'second_one', string))

for string, number in tens_zip:
    sport_tuples.append(("^" + number + "\/[1-9]\d?$", '.*', 'first_one', string))
    sport_tuples.append(("^[1-9]\d?\/" + number, '.*', 'second_one', string))

for string, number in dozens_zip:
    sport_tuples.append(("^" + number + "0\/[1-9]\d?$", '.*', 'first_ten', string))
    sport_tuples.append(("^[1-9]\d?\/" + number + "0$", '.*', 'second_ten', string))
    sport_tuples.append(("^" + number + "[1-9]\/[1-9]\d?$", '.*', 'first_ten', string + " og"))
    sport_tuples.append(("^[1-9]\d?\/" + number + "[1-9]$", '.*', 'second_ten', string + " og"))