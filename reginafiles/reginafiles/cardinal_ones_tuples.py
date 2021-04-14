from tuple_rules import ones_zip, tens_zip
from number_patterns import ones_ptrn_no11, dec_ptrn, tns_ptrn

# pattern, tag, column, wo

cardinal_ones_tuples = [("^0(,\d+)?$", 'ones', 'núll')]

for rule, string, number in ones_zip:
    cardinal_ones_tuples.append(((ones_ptrn_no11 + number + dec_ptrn), rule, 'ones', string))
    
for string, number in tens_zip:
    cardinal_ones_tuples.append((tns_ptrn + number + dec_ptrn, '.*$', 'dozens', string))

