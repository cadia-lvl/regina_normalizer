from . import number_patterns as npa
from . import tuple_rules as tp

cardinal_big_tuples = [(npa.ones_ptrn_no11 + "1" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'millions', ' ein milljón og'),
                    (npa.ones_ptrn_no11 + "1" + npa.million_and_ordinal + npa.dec_ptrn, '.*', 'millions', ' ein milljón og'),
                    (npa.ones_ptrn_no11 + "1" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'millions', ' ein milljón'),

                    #(npa.tns_ptrn + "10" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'ten millions', 'tíu milljónir og'),
                    #(npa.tns_ptrn + "10" + npa.million_and_ordinal, '.*', 'ten millions', 'tíu milljónir og'),
                    #(npa.tns_ptrn + "10" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'ten millions', 'tíu milljónir'),

                    (npa.hndrds_ptrn + "100" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'hundred millions', ' eitt hundrað milljónir og'),
                    (npa.hndrds_ptrn + "100" + npa.million_and_ordinal, '.*', 'hundred millions', ' eitt hundrað milljónir og'),
                    ("^100" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'hundred millions', 'hundrað milljónir og'),
                    ("^100" + npa.million_and_ordinal, '.*', 'hundred millions', 'hundrað milljónir og'),
                    (npa.hndrds_ptrn + "100" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred millions', ' eitt hundrað milljónir'),
                    ("^100" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred millions', 'hundrað milljónir'),
                    (npa.hndrds_ptrn + "1" + npa.hndrd_and_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', ' eitt hundrað og'),
                    ("^1" + npa.hndrd_and_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', 'hundrað og'),
                    (npa.hndrds_ptrn + "1" + npa.hndrd_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', ' eitt hundrað'),
                    ("^1" + npa.hndrd_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', 'hundrað'),

                    (npa.ones_ptrn_no11 + "1" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'billions', ' einn milljarður og'),
                    (npa.ones_ptrn_no11 + "1" + npa.billion_and_ordinal, '.*', 'billions', ' einn milljarður og'),
                    (npa.ones_ptrn_no11 + "1" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'billions', ' einn milljarður'),

                    (npa.tns_ptrn + "10" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'ten billions', 'tíu milljarðar og'),
                    (npa.tns_ptrn + "10" + npa.billion_and_ordinal, '.*', 'ten billions', 'tíu milljarðar og'),
                    (npa.tns_ptrn + "10" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'ten billions', 'tíu milljarðar'),

                    (npa.hndrds_ptrn + "100" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'hundred billions', ' eitt hundrað milljarðar og'),
                    (npa.hndrds_ptrn + "100" + npa.billion_and_ordinal, '.*', 'hundred billions', ' eitt hundrað milljarðar og'),
                    ("^100" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'hundred billions', 'hundrað milljarðar og'),
                    ("^100" + npa.billion_and_ordinal, '.*', 'hundred billions', 'hundrað milljarðar og'),
                    (npa.hndrds_ptrn + "100" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'hundred billions', ' eitt hundrað milljarðar'),
                    ("^100" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'hundred billions', 'hundrað milljarðar'),

                    (npa.hndrds_ptrn + "1" + npa.hndrd_and_billion + npa.dec_ptrn_ordinal, '.*', 'hundred millions', ' eitt hundrað og'),
                    ("^1" + npa.hndrd_and_billion + npa.dec_ptrn_ordinal, '.*', 'hundred billions', 'hundrað og'),
                    (npa.hndrds_ptrn + "1" + npa.hndrd_billion + npa.dec_ptrn_ordinal, '.*', 'hundred billions', ' eitt hundrað'),
                    ("^1" + npa.hndrd_billion + npa.dec_ptrn_ordinal, '.*', 'hundred billions', 'hundrað')]


# CARDINAL
for string, number in tp.hundreds_thousands_zip:
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'hundred millions', string + ' hundruð milljónir og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.million_and_ordinal, '.*', 'hundred millions', string + ' hundruð milljónir og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'hundred millions', string +  ' hundruð milljónir'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_and_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', string + ' hundruð og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_million + npa.dec_ptrn_ordinal, '.*', 'hundred millions', string + ' hundruð'))

    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'hundred billions', string + ' hundruð milljarðar og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.billion_and_ordinal, '.*', 'hundred billions', string + ' hundruð milljarðar og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + "00" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'hundred billions', string + ' hundruð milljarðar'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_and_billion + npa.dec_ptrn_ordinal, '.*', 'hundred billions', string + ' hundruð og'))
    cardinal_big_tuples.append((npa.hndrds_ptrn + number + npa.hndrd_billion + npa.dec_ptrn_ordinal, '.*', 'hundred billions', string + ' hundruð'))

for string, number in tp.dozens_zip:
    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'ten millions', string + ' milljónir og'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.million_and_ordinal, '.*', 'ten millions', string + ' milljónir og'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'ten millions', string + ' milljónir'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "[1-9](\.\d{3}){2}" + npa.dec_ptrn_ordinal, '.*', 'ten millions', string + ' og'))

    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'ten billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.billion_and_ordinal, '.*', 'ten billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "0" + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'ten billions', string + ' milljarðar'))
    cardinal_big_tuples.append((npa.tns_ptrn + number + "[1-9](\.\d{3}){3}" + npa.dec_ptrn_ordinal, '.*', 'ten billions', string + ' og'))

for string, number in tp.millions_zip:
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.million_and_ordinal, '.*', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'millions', string + ' milljónir'))

for string, number in tp.billions_zip:
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.billion_and_ordinal, '.*', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((npa.ones_ptrn_no11 + number + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'billions', string + ' milljarðar'))
    
for string, number in tp.tens_zip:
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.million_and_cardinal + npa.dec_ptrn, '.*', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.million_and_ordinal, '.*', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.milln_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'millions', string + ' milljónir'))
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.billion_and_cardinal + npa.dec_ptrn, '.*', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.billion_and_ordinal, '.*', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append(("^[1-9]?" + number + npa.billion_after + npa.dec_ptrn_ordinal, '.*', 'billions', string + ' milljarðar'))