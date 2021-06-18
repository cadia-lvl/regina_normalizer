# ORDINAL
from number_patterns import hndrds_ptrn_def, ones_ptrn_no11, tns_ptrn, hndrds_ptrn, ones_ptrn_11
from tuple_rules import dozens_ordinal_letters, tens_zip, hundreds_thousands_zip


ordinal_thousands_tuples = []

for rule, letter in dozens_ordinal_letters:
    ordinal_thousands_tuples.append((hndrds_ptrn_def + "1([01][1-9]|10)\.$", rule, 'hundreds', ' eitt hundrað' + letter + ' og'))
    ordinal_thousands_tuples.append(("^1([01][1-9]|10)\.$", rule, 'hundreds', 'hundrað' + letter + ' og'))
    ordinal_thousands_tuples.append((hndrds_ptrn_def + "100\.$", rule, 'hundreds', ' eitt hundrað' + letter))
    ordinal_thousands_tuples.append(("^100\.$", rule, 'hundreds', 'hundrað' + letter))
    ordinal_thousands_tuples.append((ones_ptrn_no11 + "1\.?0([01][1-9]|10)\.$", rule, 'thousands', ' eitt þúsund' + letter + ' og'))
    ordinal_thousands_tuples.append((ones_ptrn_no11 + "1\.?000\.$", rule, 'thousands', ' eitt þúsund' + letter))
    for string, number in tens_zip:
        ordinal_thousands_tuples.append(("^" + number + "([01][1-9]|10)\.$", rule, 'hundreds', string + ' hundruð' + letter + ' og'))
        ordinal_thousands_tuples.append((tns_ptrn + number + "\.?0([01][1-9]|10)\.$", rule, 'thousands', string + ' þúsund' + letter + ' og'))
        ordinal_thousands_tuples.append(("^" + number + "([01][1-9]|10)\.$", rule, 'thousands', ""))        
    for string, number in hundreds_thousands_zip:
        ordinal_thousands_tuples.append((hndrds_ptrn + number + "([01][1-9]|10)\.$", rule, 'hundreds', string + ' hundruð' + letter + ' og'))
        ordinal_thousands_tuples.append((hndrds_ptrn + number + "00\.$", rule, 'hundreds', string + ' hundruð' + letter))
        ordinal_thousands_tuples.append((ones_ptrn_11 + number + "\.?0([01][1-9]|10)\.$", rule, 'thousands', string + ' þúsund' + letter + ' og'))
        ordinal_thousands_tuples.append((ones_ptrn_11 + number + "\.?000\.$", rule, 'thousands', string + ' þúsund' + letter))
