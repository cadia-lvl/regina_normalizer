from number_patterns import fraction_ptrn_before
from tuple_rules import ones_numerator, ones_denominator, dozens_numerator, dozens_denominator, tens_denominator, half_zip, tens_zip

fraction_tuples = []
for word_num, no_num in ones_numerator:
    for word_doz_num, no_doz_num in dozens_numerator:
        fraction_tuples.append((fraction_ptrn_before + no_num + "\/\d+$", '.*', 'points', ' og' + word_num))
        fraction_tuples.append(("^" + no_num + "\/\d+$", '.*', 'points', word_num))
        fraction_tuples.append((fraction_ptrn_before + no_doz_num + no_num + "\/\d+$", '.*', 'points', ' og' + word_doz_num + ' og' + word_num))
        fraction_tuples.append(("^" + no_doz_num + no_num + "\/\d+$", '.*', 'points', word_doz_num + ' og' + word_num))         
        
for word_num, no_num in tens_zip:
    for word_den, no_den in tens_denominator:
        fraction_tuples.append((fraction_ptrn_before + no_num + "\/\d+$", '.*', 'points', ' og' + word_num))
        fraction_tuples.append(("^" + no_num + "\/\d+$", '.*', 'points', word_num))
        fraction_tuples.append((fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', ' og' + word_den))
        fraction_tuples.append((fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', '.*', ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_den + "$", '.*', 'point2', word_den))

for word_den, no_den in ones_denominator:
    for word_doz_den, no_doz_den in dozens_denominator:
        fraction_tuples.append((fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_den + "$", '.*', 'point2', word_den))
        fraction_tuples.append((fraction_ptrn_before + "\d+\/" + no_doz_den + no_den + "$", '.*', 'point2', word_doz_den + ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_doz_den + no_den + "$", '.*', 'point2', word_doz_den + ' og' + word_den))         

for rule, string, ptrn in half_zip:
    fraction_tuples.append((ptrn, rule, 'points', ' og' + string))
    fraction_tuples.append(("^" + ptrn + "$", rule, 'points', string))
    fraction_tuples.append((ptrn, rule, 'point2', ''))
    fraction_tuples.append(("^" + ptrn + "$", rule, 'point2', ''))

    
    