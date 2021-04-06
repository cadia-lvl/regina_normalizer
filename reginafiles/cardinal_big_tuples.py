from number_patterns import *
from tuple_rules import *

cardinal_big_tuples = [(ones_ptrn_no11 + "1" + million_and_cardinal + dec_ptrn, '^.*$', 'millions', ' ein milljón og'),
                    (ones_ptrn_no11 + "1" + million_and_ordinal + dec_ptrn, '^.*$', 'millions', ' ein milljón og'),
                    (ones_ptrn_no11 + "1" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'millions', ' ein milljón'),

                    (tns_ptrn + "10" + million_and_cardinal + dec_ptrn, '^.*$', 'ten millions', 'tíu milljónir og'),
                    (tns_ptrn + "10" + million_and_ordinal, '^.*$', 'ten millions', 'tíu milljónir og'),
                    (tns_ptrn + "10" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'ten millions', 'tíu milljónir'),

                    (hndrds_ptrn_11 + "100" + million_and_cardinal + dec_ptrn, '^.*$', 'hundred millions', ' eitt hundrað milljónir og'),
                    (hndrds_ptrn_11 + "100" + million_and_ordinal, '^.*$', 'hundred millions', ' eitt hundrað milljónir og'),
                    ("^100" + million_and_cardinal + dec_ptrn, '^.*$', 'hundred millions', 'hundrað milljónir og'),
                    ("^100" + million_and_ordinal, '^.*$', 'hundred millions', 'hundrað milljónir og'),
                    (hndrds_ptrn_11 + "100" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'hundred millions', ' eitt hundrað milljónir'),
                    ("^100" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'hundred millions', 'hundrað milljónir'),
                    (hndrds_ptrn_11 + "1" + hndrd_and_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', ' eitt hundrað og'),
                    ("^1" + hndrd_and_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', 'hundrað og'),
                    (hndrds_ptrn_11 + "1" + hndrd_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', ' eitt hundrað'),
                    ("^1" + hndrd_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', 'hundrað'),

                    (ones_ptrn_no11 + "1" + billion_and_cardinal + dec_ptrn, '^.*$', 'billions', ' einn milljarður og'),
                    (ones_ptrn_no11 + "1" + billion_and_ordinal, '^.*$', 'billions', ' einn milljarður og'),
                    (ones_ptrn_no11 + "1" + billion_after + dec_ptrn_ordinal, '^.*$', 'billions', ' einn milljarður'),

                    (tns_ptrn + "10" + billion_and_cardinal + dec_ptrn, '^.*$', 'ten billions', 'tíu milljarðar og'),
                    (tns_ptrn + "10" + billion_and_ordinal, '^.*$', 'ten billions', 'tíu milljarðar og'),
                    (tns_ptrn + "10" + billion_after + dec_ptrn_ordinal, '^.*$', 'ten billions', 'tíu milljarðar'),

                    (hndrds_ptrn_11 + "100" + billion_and_cardinal + dec_ptrn, '^.*$', 'hundred billions', ' eitt hundrað milljarðar og'),
                    (hndrds_ptrn_11 + "100" + billion_and_ordinal, '^.*$', 'hundred billions', ' eitt hundrað milljarðar og'),
                    ("^100" + billion_and_cardinal + dec_ptrn, '^.*$', 'hundred billions', 'hundrað milljarðar og'),
                    ("^100" + billion_and_ordinal, '^.*$', 'hundred billions', 'hundrað milljarðar og'),
                    (hndrds_ptrn_11 + "100" + billion_after + dec_ptrn_ordinal, '^.*$', 'hundred billions', ' eitt hundrað milljarðar'),
                    ("^100" + billion_after + dec_ptrn_ordinal, '^.*$', 'hundred billions', 'hundrað milljarðar'),

                    (hndrds_ptrn_11 + "1" + hndrd_and_billion + dec_ptrn_ordinal, '^.*$', 'hundred millions', ' eitt hundrað og'),
                    ("^1" + hndrd_and_billion + dec_ptrn_ordinal, '^.*$', 'hundred billions', 'hundrað og'),
                    (hndrds_ptrn_11 + "1" + hndrd_billion + dec_ptrn_ordinal, '^.*$', 'hundred billions', ' eitt hundrað'),
                    ("^1" + hndrd_billion + dec_ptrn_ordinal, '^.*$', 'hundred billions', 'hundrað')]


# CARDINAL
for string, number in hundreds_thousands_zip:
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + million_and_cardinal + dec_ptrn, '^.*$', 'hundred millions', string + ' hundruð milljónir og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + million_and_ordinal, '^.*$', 'hundred millions', string + ' hundruð milljónir og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'hundred millions', string +  ' hundruð milljónir'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + hndrd_and_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', string + ' hundruð og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + hndrd_million + dec_ptrn_ordinal, '^.*$', 'hundred millions', string + ' hundruð'))

    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + billion_and_cardinal + dec_ptrn, '^.*$', 'hundred billions', string + ' hundruð milljarðar og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + billion_and_ordinal, '^.*$', 'hundred billions', string + ' hundruð milljarðar og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + "00" + billion_after + dec_ptrn_ordinal, '^.*$', 'hundred billions', string + ' hundruð milljarðar'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + hndrd_and_billion + dec_ptrn_ordinal, '^.*$', 'hundred billions', string + ' hundruð og'))
    cardinal_big_tuples.append((hndrds_ptrn_11 + number + hndrd_billion + dec_ptrn_ordinal, '^.*$', 'hundred billions', string + ' hundruð'))

for string, number in dozens_zip:
    cardinal_big_tuples.append((tns_ptrn + number + "0" + million_and_cardinal + dec_ptrn, '^.*$', 'ten millions', string + ' milljónir og'))
    cardinal_big_tuples.append((tns_ptrn + number + "0" + million_and_ordinal, '^.*$', 'ten millions', string + ' milljónir og'))
    cardinal_big_tuples.append((tns_ptrn + number + "0" + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'ten millions', string + ' milljónir'))
    cardinal_big_tuples.append((tns_ptrn + number + "[1-9](\.\d{3}){2}" + dec_ptrn_ordinal, '^.*$', 'ten millions', string + ' og'))

    cardinal_big_tuples.append((tns_ptrn + number + "0" + billion_and_cardinal + dec_ptrn, '^.*$', 'ten billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((tns_ptrn + number + "0" + billion_and_ordinal, '^.*$', 'ten billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((tns_ptrn + number + "0" + billion_after + dec_ptrn_ordinal, '^.*$', 'ten billions', string + ' milljarðar'))
    cardinal_big_tuples.append((tns_ptrn + number + "[1-9](\.\d{3}){3}" + dec_ptrn_ordinal, '^.*$', 'ten billions', string + ' og'))

for string, number in millions_zip:
    cardinal_big_tuples.append((ones_ptrn_no11 + number + million_and_cardinal + dec_ptrn, '^.*$', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append((ones_ptrn_no11 + number + million_and_ordinal, '^.*$', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append((ones_ptrn_no11 + number + milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'millions', string + ' milljónir'))

for string, number in billions_zip:
    cardinal_big_tuples.append((ones_ptrn_no11 + number + billion_and_cardinal + dec_ptrn, '^.*$', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((ones_ptrn_no11 + number + billion_and_ordinal, '^.*$', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append((ones_ptrn_no11 + number + billion_after + dec_ptrn_ordinal, '^.*$', 'billions', string + ' milljarðar'))
    
for string, number in tens_zip:
    cardinal_big_tuples.append(("^[1-9]?" + number +  million_and_cardinal + dec_ptrn, '^.*$', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append(("^[1-9]?" + number +  million_and_ordinal, '^.*$', 'millions', string + ' milljónir og'))
    cardinal_big_tuples.append(("^[1-9]?" + number +  milln_ptrn_after + dec_ptrn_ordinal, '^.*$', 'millions', string + ' milljónir'))
    cardinal_big_tuples.append(("^[1-9]?" + number +  billion_and_cardinal + dec_ptrn, '^.*$', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append(("^[1-9]?" + number +  billion_and_ordinal, '^.*$', 'billions', string + ' milljarðar og'))
    cardinal_big_tuples.append(("^[1-9]?" + number +  billion_after + dec_ptrn_ordinal, '^.*$', 'billions', string + ' milljarðar'))
    