

from number_patterns import *
from tuple_rules import dozens_zip, hundreds_thousands_zip

cardinal_million_tuples = [(tns_ptrn + "10" + thsnds_and_ptrn_cardinal + dec_ptrn_ordinal, '.*', 'ten thousands', ' tíu þúsund og'),
                            (tns_ptrn + "10" + thsnds_and_ptrn_ordinal, '.*', 'ten thousands', ' tíu þúsund og'),
                            (tns_ptrn + "10" + thsnds_ptrn_after + dec_ptrn_ordinal, '.*', 'ten thousands', ' tíu þúsund'),
                            (hndrds_ptrn + "100" + thsnds_and_ptrn_cardinal + dec_ptrn, '.*', 'hundred thousands', ' eitt hundrað þúsund og'),
                            ("^100" + thsnds_and_ptrn_cardinal + dec_ptrn, '.*', 'hundred thousands', 'hundrað þúsund og'),
                            (hndrds_ptrn + "100" + thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað þúsund og'),
                            ("^100" + thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað þúsund og'),

                            (hndrds_ptrn_def + "100" + thsnds_ptrn_after + dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað þúsund'),
                            ("^100" + thsnds_ptrn_after + dec_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað þúsund'),
                            (hndrds_ptrn + "1" + hndrd_and_thsnd + dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað og'),
                            ("^1" + hndrd_and_thsnd + dec_ptrn_ordinal, '.*', 'hundred thousands', ' hundrað og'),
                            (hndrds_ptrn + "1" + hndrd_thsnd_after + dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað'),
                            ("^1" + hndrd_thsnd_after + dec_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað'),]

for string, number in dozens_zip:
    cardinal_million_tuples.append((tns_ptrn + number + "0" + thsnds_and_ptrn_cardinal + dec_ptrn, '.*', 'ten thousands', string + ' þúsund og'))
    cardinal_million_tuples.append((tns_ptrn + number + "0" + thsnds_and_ptrn_ordinal, '.*', 'ten thousands', string + ' þúsund og'))
    cardinal_million_tuples.append((tns_ptrn + number + "0" + thsnds_ptrn_after + dec_ptrn_ordinal, '.*', 'ten thousands', string + ' þúsund'))
    cardinal_million_tuples.append((tns_ptrn + number + "[1-9]\.?\d{3}" + dec_ptrn_ordinal, '.*', 'ten thousands', string + ' og'))

for string, number in hundreds_thousands_zip:
    cardinal_million_tuples.append((hndrds_ptrn + number + "00" + thsnds_ptrn_after + dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð þúsund'))
    cardinal_million_tuples.append((hndrds_ptrn + number + "00" + thsnds_and_ptrn_cardinal + dec_ptrn, '.*', 'hundred thousands', string + ' hundruð þúsund og'))
    cardinal_million_tuples.append((hndrds_ptrn + number + "00" + thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð þúsund og'))
    cardinal_million_tuples.append((hndrds_ptrn + number + hndrd_and_thsnd + dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð og'))
    cardinal_million_tuples.append((hndrds_ptrn + number + hndrd_thsnd_after + dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð'))