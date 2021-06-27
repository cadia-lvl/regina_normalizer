from . import tuple_rules as tp

time_tuples = [("^0\d[:\.][0-5]\d$", '.*', 'first_ten', ' núll'),
                ("^00[:\.][0-5]\d$", '.*', 'first_one', ' núll'),
                ("^([01]?[0-9]|2[0-4])[:\.]0\d$", '.*', 'second_ten', ' núll'),
                ("^([01]?[0-9]|2[0-4])[:\.]00$", '.*', 'second_one', ' núll')]

for string, number in tp.ones_zip_time:
    time_tuples.append(("^[02]?" + number + "[:\.][0-5]\d$", '.*', 'first_one', string))
    time_tuples.append(("^([01]?[0-9]|2[0-4])[:\.][02-5]" + number + "$", '.*', 'second_one', string))
    time_tuples.append(("^0" + number + "$", '.*', 'second_one', "núll " + string))
    
tens_zip_time = tp.tens_zip + [(' tuttugu', '20')]

for string, number in tens_zip_time:
    time_tuples.append(("^" + number + "[:\.][0-5]\d$", '.*', 'first_ten', string))
    time_tuples.append(("^([01]?[0-9]|2[0-4])[:\.]" + number + "$", '.*', 'second_ten', string))
    time_tuples.append(("^2[1-4][:\.][0-5]\d$", '.*', 'first_ten', "tuttugu og"))

for string, number in tp.dozens_zip[:4]:
    time_tuples.append(("^([01]?\d|2[0-4])[:\.]" + number + "0$", '.*', 'second_ten', string))
    time_tuples.append(("^([01]?\d|2[0-4])[:\.]" + number + "[1-9]$", '.*', 'second_ten', string + " og"))
