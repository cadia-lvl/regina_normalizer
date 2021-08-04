

from . import number_patterns as npa
from . import tuple_rules as tp

cardinal_million_tuples = [#(npa.tns_ptrn + "10" + npa.thsnds_and_ptrn_ordinal, '.*', 'ten thousands', ' tíu þúsund og'),
                            #(npa.tns_ptrn + "10" + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'ten thousands', ' tíu þúsund'),
                            (npa.hndrds_ptrn + "100" + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'hundred thousands', ' eitt hundrað þúsund og'),
                            ("^100" + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'hundred thousands', 'hundrað þúsund og'),
                            (npa.hndrds_ptrn + "100" + npa.thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað þúsund og'),
                            ("^100" + npa.thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað þúsund og'),

                            (npa.hndrds_ptrn_def + "100" + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað þúsund'),
                            ("^100" + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað þúsund'),
                            (npa.hndrds_ptrn + "1" + npa.hndrd_and_thsnd + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað og'),
                            ("^1" + npa.hndrd_and_thsnd + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', ' hundrað og'),
                            (npa.hndrds_ptrn + "1" + npa.hndrd_thsnd_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', ' eitt hundrað'),
                            ("^1" + npa.hndrd_thsnd_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', 'hundrað'),]

for string, number in tp.dozens_zip:
    cardinal_million_tuples.append((npa.tns_ptrn + number + "0" + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'ten thousands', string + ' þúsund og'))
    cardinal_million_tuples.append((npa.tns_ptrn + number + "0" + npa.thsnds_and_ptrn_ordinal, '.*', 'ten thousands', string + ' þúsund og'))
    cardinal_million_tuples.append((npa.tns_ptrn + number + "0" + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'ten thousands', string + ' þúsund'))
    cardinal_million_tuples.append((npa.tns_ptrn + number + "[1-9]\.?\d{3}" + npa.dec_ptrn_ordinal, '.*', 'ten thousands', string + ' og'))

for string, number in tp.hundreds_thousands_zip:
    cardinal_million_tuples.append((npa.hndrds_ptrn + number + "00" + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð þúsund'))
    cardinal_million_tuples.append((npa.hndrds_ptrn + number + "00" + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'hundred thousands', string + ' hundruð þúsund og'))
    cardinal_million_tuples.append((npa.hndrds_ptrn + number + "00" + npa.thsnds_and_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð þúsund og'))
    cardinal_million_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_and_thsnd + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð og'))
    cardinal_million_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_thsnd_after + npa.dec_ptrn_ordinal, '.*', 'hundred thousands', string + ' hundruð'))