from . import number_patterns as npa
from . import tuple_rules as tp

fraction_tuples = []
for word_num, no_num in tp.ones_numerator:
    for word_doz_num, no_doz_num in tp.dozens_numerator:
        fraction_tuples.append((npa.fraction_ptrn_before + no_num + "\/\d+$", '.*', 'points', ' og' + word_num))
        fraction_tuples.append(("^" + no_num + "\/\d+$", '.*', 'points', word_num))
        fraction_tuples.append((npa.fraction_ptrn_before + no_doz_num + no_num + "\/\d+$", '.*', 'points', ' og' + word_doz_num + ' og' + word_num))
        fraction_tuples.append(("^" + no_doz_num + no_num + "\/\d+$", '.*', 'points', word_doz_num + ' og' + word_num))         
        
for word_num, no_num in tp.tens_zip:
    for word_den, no_den in tp.tens_denominator:
        fraction_tuples.append((npa.fraction_ptrn_before + no_num + "\/\d+$", '.*', 'points', ' og' + word_num))
        fraction_tuples.append(("^" + no_num + "\/\d+$", '.*', 'points', word_num))
        fraction_tuples.append((npa.fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', ' og' + word_den))
        fraction_tuples.append((npa.fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', '.*', ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_den + "$", '.*', 'point2', word_den))

for word_den, no_den in tp.ones_denominator:
    for word_doz_den, no_doz_den in tp.dozens_denominator:
        fraction_tuples.append((npa.fraction_ptrn_before + "\d+\/" + no_den + "$", '.*', 'point2', ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_den + "$", '.*', 'point2', word_den))
        fraction_tuples.append((npa.fraction_ptrn_before + "\d+\/" + no_doz_den + no_den + "$", '.*', 'point2', word_doz_den + ' og' + word_den))
        fraction_tuples.append(("^\d+\/" + no_doz_den + no_den + "$", '.*', 'point2', word_doz_den + ' og' + word_den))         

for rule, string, ptrn in tp.half_zip:
    fraction_tuples.append((ptrn, rule, 'points', ' og' + string))
    fraction_tuples.append(("^" + ptrn + "$", rule, 'points', string))
    fraction_tuples.append((ptrn, rule, 'point2', ''))
    fraction_tuples.append(("^" + ptrn + "$", rule, 'point2', ''))

    
    