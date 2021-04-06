from number_patterns import zeropnt_ptrn, ones_ptrn_no11, dec_ptrn_def
from tuple_rules import ones_zip, dec_ones_male

decimal_thousands_tuples = [
((zeropnt_ptrn + "\d{9}0\d*$"), '^.*$', 'point10', ' núll'),
((zeropnt_ptrn + "\d{8}0\d*$"), '^.*$', 'point9', ' núll'),
((zeropnt_ptrn + "\d{7}0\d*$"), '^.*$', 'point8', ' núll'),
((zeropnt_ptrn + "\d{6}0\d*$"), '^.*$', 'point7', ' núll'),
((zeropnt_ptrn + "\d{5}0\d*$"), '^.*$', 'point6', ' núll'),
((zeropnt_ptrn + "\d{4}0\d*$"), '^.*$', 'point5', ' núll'),
((zeropnt_ptrn + "\d{3}0\d*$"), '^.*$', 'point4', ' núll'),
((zeropnt_ptrn + "\d{2}0\d*$"), '^.*$', 'point3', ' núll'),
((zeropnt_ptrn + "\d{2}0\d*$"), '^.*$', 'point2', ' núll'),
((zeropnt_ptrn + "0\d*$"), '^.*$', 'points', ' komma núll')]

for rules in ones_zip + dec_ones_male:
    for rule, string, number in ones_zip:
        decimal_thousands_tuples.append(((zeropnt_ptrn + number + "\d*$"), rule, 'points', ' komma' + string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d" + number + "\d*$"), rule, 'point2', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{2}" + number + "\d*$"), rule, 'point3', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{3}" + number + "\d*$"), rule, 'point4', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{4}" + number + "\d*$"), rule, 'point5', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{5}" + number + "\d*$"), rule, 'point6', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{6}" + number + "\d*$"), rule, 'point7', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{7}" + number + "\d*$"), rule, 'point8', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{8}" + number + "\d*$"), rule, 'point9', string))
        decimal_thousands_tuples.append(((zeropnt_ptrn + "\d{9}" + number + "\d*$"), rule, 'point10', string))

for rule, string, number in dec_ones_male:
    decimal_thousands_tuples.append(((ones_ptrn_no11 + number + dec_ptrn_def), rule, 'ones', string))