from number_patterns import ones_ptrn_no11, tns_ptrn
from tuple_rules import two_ordinal_zip, ordinal_letters, ordinal_ones_zip, dozens_ordinal_letters, dozens_ordinal_zip

ordinal_ones_tuples = []
for rule, string in two_ordinal_zip:
    ordinal_ones_tuples.append((ones_ptrn_no11 + "2\.$", rule, 'ones', string))
    
for rule, letter in ordinal_letters:
    ordinal_ones_tuples.append(("^0\.$", rule, 'ones', 'núllt' + letter))
    for string, number, col in ordinal_ones_zip:
        ordinal_ones_tuples.append((ones_ptrn_no11 + number + "\.$", rule, col, string + letter))

for rule, letter in dozens_ordinal_letters:
	for string, number in dozens_ordinal_zip:
		ordinal_ones_tuples.append((tns_ptrn + number + "0\.$", rule, 'dozens', string + letter))
		ordinal_ones_tuples.append((tns_ptrn + number + "[1-9]\.$", rule, 'dozens', string + letter + ' og'))