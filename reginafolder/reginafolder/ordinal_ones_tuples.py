from . import number_patterns as npa
from . import tuple_rules as tp

ordinal_ones_tuples = []
for rule, string in tp.two_ordinal_zip:
    ordinal_ones_tuples.append((npa.ones_ptrn_no11 + "2\.$", rule, 'ones', string))
    
for rule, letter in tp.ordinal_letters:
    ordinal_ones_tuples.append(("^0\.$", rule, 'ones', 'núllt' + letter))
    for string, number, col in tp.ordinal_ones_zip[:8]:
        ordinal_ones_tuples.append((npa.ones_ptrn_no11 + number + "\.$", rule, col, string + letter))
    for string, number, col in tp.ordinal_ones_zip[8:]:
        ordinal_ones_tuples.append((npa.tns_ptrn + number + "\.$", rule, col, string + letter))

for rule, letter in tp.dozens_ordinal_letters:
	for string, number in tp.dozens_ordinal_zip:
		ordinal_ones_tuples.append((npa.tns_ptrn + number + "0\.$", rule, 'dozens', string + letter))
		ordinal_ones_tuples.append((npa.tns_ptrn + number + "[1-9]\.$", rule, 'dozens', string + letter + ' og'))