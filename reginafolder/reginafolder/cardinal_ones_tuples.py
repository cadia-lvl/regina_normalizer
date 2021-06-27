from . import tuple_rules as tp
from . import number_patterns as npa

# pattern, tag, column, wo

cardinal_ones_tuples = [("^0(,\d+)?$", 'ones', 'núll ekkert að frétta hér?')]

for rule, string, number in tp.ones_zip:
    cardinal_ones_tuples.append(((npa.ones_ptrn_no11 + number + npa.dec_ptrn), rule, 'ones', string))
    
for string, number in tp.tens_zip:
    cardinal_ones_tuples.append((npa.tns_ptrn + number + npa.dec_ptrn, '.*', 'dozens', string))

