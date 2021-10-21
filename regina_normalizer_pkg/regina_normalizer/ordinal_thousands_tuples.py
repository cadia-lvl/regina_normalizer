# ORDINAL
from . import number_patterns as npa
from . import tuple_rules as tp


ordinal_thousands_tuples = []

for rule, letter in tp.dozens_ordinal_letters:
    ordinal_thousands_tuples.append((npa.hndrds_ptrn_def + "1([01][1-9]|10)\.$", rule, 'hundreds', ' eitt hundrað' + letter + ' og'))
    ordinal_thousands_tuples.append(("^1([01][1-9]|10)\.$", rule, 'hundreds', 'hundrað' + letter + ' og'))
    ordinal_thousands_tuples.append((npa.hndrds_ptrn_def + "100\.$", rule, 'hundreds', ' eitt hundrað' + letter))
    ordinal_thousands_tuples.append(("^100\.$", rule, 'hundreds', 'hundrað' + letter))
    ordinal_thousands_tuples.append((npa.ones_ptrn_no11 + "1\.?0([01][1-9]|10)\.$", rule, 'thousands', ' eitt þúsund' + letter + ' og'))
    ordinal_thousands_tuples.append((npa.ones_ptrn_no11 + "1\.?000\.$", rule, 'thousands', ' eitt þúsund' + letter))
    for string, number in tp.hundreds_thousands_zip:
        ordinal_thousands_tuples.append((npa.hndrds_ptrn + number + "([01][1-9]|10)\.$", rule, 'hundreds', string + ' hundruð' + letter + ' og'))
        ordinal_thousands_tuples.append((npa.hndrds_ptrn + number + "00\.$", rule, 'hundreds', string + ' hundruð' + letter))
        ordinal_thousands_tuples.append((npa.ones_ptrn_11 + number + "\.?0([01][1-9]|10)\.$", rule, 'thousands', string + ' þúsund' + letter + ' og'))
        ordinal_thousands_tuples.append((npa.ones_ptrn_11 + number + "\.?000\.$", rule, 'thousands', string + ' þúsund' + letter))
    for string, number in tp.tens_zip:
        ordinal_thousands_tuples.append(("^" + number + "([01][1-9]|10)\.$", rule, 'hundreds', string + ' hundruð' + letter + ' og'))
        ordinal_thousands_tuples.append((npa.tns_ptrn + number + "\.?0([01][1-9]|10)\.$", rule, 'thousands', string + ' þúsund' + letter + ' og'))
        ordinal_thousands_tuples.append(("^" + number + "00\.$", rule, 'hundreds', string + ' hundruð' + letter))
        ordinal_thousands_tuples.append(("^" + number + "([01][1-9]|[01]0)\.$", rule, 'thousands', ""))        

