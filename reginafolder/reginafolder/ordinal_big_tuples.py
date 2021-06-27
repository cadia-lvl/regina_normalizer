from . import number_patterns as npa
from . import tuple_rules as tp

ordinal_big_tuples = [(npa.ones_ptrn_no11 + "1\.000\.0([01][1-9]|10)\.$", '.*', 'millions', ' einmilljónasta og'),
    ("^1\.000\.0([01][1-9]|10)\.$", '.*', 'millions',' milljónasta og'),
    (npa.ones_ptrn_no11 + "1\.000\.000\.$", '.*', 'millions', ' einmilljónasta'),
    ("^1\.000\.000\.$", '.*', 'millions', ' milljónasta'),
    (npa.tns_ptrn + "10\.000\.0([01][1-9]|10)\.$", '.*', 'ten millions', ' tímilljónasta og'),
    (npa.tns_ptrn + "10\.000\.000\.$", '.*', 'ten millions', ' tímilljónasta'),
    (npa.hndrds_ptrn + "100\.000\.0([01][1-9]|10)\.$", '.*', 'hundred millions', ' eitt hundraðmilljónasta og'),
    ("^100\.000\.0([01][1-9]|10)\.$", '.*', 'hundred millions', 'hundraðmilljónasta og'),
    (npa.hndrds_ptrn + "100(\.000){2}\.$", '.*', 'hundred millions', ' eitt hundraðmilljónasta'),
    ("^100(\.000){2}\.$", '.*', 'hundred millions', 'hundraðmilljónasta'),
    (npa.ones_ptrn_no11 + "1(\.000){2}\.0([01][1-9]|10)\.$", '.*', 'billions', ' einmilljarðasta og'),
    ("^1(\.000){2}\.0([01][1-9]|10)\.$", '.*', 'billions', 'milljarðasta og'),
    (npa.tns_ptrn + "10(\.000){2}\.0([01][1-9]|10)\.$", '.*', 'ten billions', 'tímilljarðasta og'),
    (npa.hndrds_ptrn + "100(\.000){2}\.0([01][1-9]|10)\.$", '.*', 'hundred billions', ' eitt hundrað milljarðasta og'),
    ("^100(\.000){2}\.0([01][1-9]|10)\.$", '.*', 'hundred billions', 'hundraðmilljarðasta og'),
    (npa.ones_ptrn_no11 + "1(\.000){3}\.$", '.*', 'billions', ' einmilljarðasta'),
    ("^1(\.000){3}\.$", '.*', 'billions', 'milljarðasta'),
    (npa.tns_ptrn + "10(\.000){3}\.$", '.*', 'ten billions', 'tímilljarðasta'),
    (npa.hndrds_ptrn + "100(\.000){3}\.$", '.*', 'hundred billions', ' eitt hundraðmilljarðasta'),
    ("^100(\.000){3}\.$", '.*', 'hundred billions', 'hundraðmilljarðasta')]

for rule, letter in tp.dozens_ordinal_letters:
    ordinal_big_tuples.append((npa.ones_ptrn_no11 + "1\.000\.0([01][1-9]|10)\.$", rule, 'millions', ' einmilljón' + letter + ' og'))
    ordinal_big_tuples.append(("^1\.000\.0([01][1-9]|10)\.$", rule, 'millions', ' milljón' + letter + ' og'))
    ordinal_big_tuples.append((npa.ones_ptrn_no11 + "1(\.000){2}\.$", rule, 'millions', ' einmilljón' + letter))
    ordinal_big_tuples.append(("^1(\.000){2}\.$", rule, 'millions', ' milljón' + letter))
    ordinal_big_tuples.append((npa.tns_ptrn + "10\.000\.0([01][1-9]|10)\.$", rule, 'ten millions', ' tímilljón'+ letter + ' og'))
    ordinal_big_tuples.append((npa.tns_ptrn + "10(\.000){2}\.$", rule, 'ten millions', ' tímilljón'+ letter))
    ordinal_big_tuples.append((npa.hndrds_ptrn + "100\.000\.0([01][1-9]|10)\.$", rule, 'hundred millions', ' eitt hundraðmilljón' + letter + ' og'))
    ordinal_big_tuples.append(("^100\.000\.0([01][1-9]|10)\.$", rule, 'hundred millions', 'hundraðmilljón' + letter + ' og'))
    ordinal_big_tuples.append((npa.hndrds_ptrn + "100(\.000){2}\.$", rule, 'hundred millions', ' eitt hundraðmilljón' + letter))
    ordinal_big_tuples.append(("^100(\.000){2}\.$", rule, 'hundred millions', 'hundraðmilljón' + letter))
    ordinal_big_tuples.append((npa.ones_ptrn_no11 + "1(\.000){2}\.0([01][1-9]|10)\.$", rule, 'billions', ' einmilljarð' + letter + ' og'))
    ordinal_big_tuples.append(("^1(\.000){2}\.0([01][1-9]|10)\.$", rule, 'billions', 'milljarð' + letter + ' og'))
    ordinal_big_tuples.append((npa.tns_ptrn + "10(\.000){2}\.0([01][1-9]|10)\.$", rule, 'ten billions', ' tímilljarð' + letter + ' og'))
    ordinal_big_tuples.append((npa.hndrds_ptrn + "100(\.000){2}\.0([01][1-9]|10)\.$", rule, 'hundred billions', ' eitt hundraðmilljarð' + letter + ' og'))
    ordinal_big_tuples.append(("^100(\.000){2}\.0([01][1-9]|10)\.$", rule, 'hundred billions', 'hundraðmilljarð' + letter + ' og'))
    ordinal_big_tuples.append((npa.ones_ptrn_no11 + "1(\.000){3}\.$", rule, 'billions', ' einmilljarð' + letter))
    ordinal_big_tuples.append(("^1(\.000){3}\.$", rule, 'billions', 'milljarð' + letter))
    ordinal_big_tuples.append((npa.tns_ptrn + "10(\.000){3}\.$", rule, 'ten billions', 'tímilljarð' + letter))
    ordinal_big_tuples.append((npa.hndrds_ptrn + "100(\.000){3}\.$", rule, 'hundred billions', ' eitt hundraðmilljarð' + letter))
    ordinal_big_tuples.append(("^100(\.000){3}\.$", rule, 'hundred billions', 'hundrað milljarð' + letter))
    
    for string, number in tp.hundreds_thousands_zip:
        ordinal_big_tuples.append((npa.hndrds_ptrn + number + "00\.000\.0([01][1-9]|10)\.$", rule, 'hundred millions', string + ' hundruðmilljón' + letter + ' og'))
        ordinal_big_tuples.append((npa.hndrds_ptrn + number + "00(\.000){2}\.$", rule, 'hundred millions', string + ' hundruðmilljón' + letter))
        ordinal_big_tuples.append((npa.hndrds_ptrn + number + "00(\.000){2}\.0([01][1-9]|10)\.$", rule, 'hundred billions', string + ' hundruðmilljarð' + letter + ' og'))
        ordinal_big_tuples.append((npa.hndrds_ptrn + number + "00(\.000){3}\.$", rule, 'hundred billions', string + ' hundruðmilljarð' + letter))
    
    for string, number in tp.dozens_zip:
        ordinal_big_tuples.append((npa.tns_ptrn + number + "0\.000\.0([01][1-9]|10)\.$", rule, 'ten millions', string + 'milljón'+ letter + ' og'))
        ordinal_big_tuples.append((npa.tns_ptrn + number + "0(\.000){2}\.$", rule, 'ten millions', string + 'milljón'+ letter))
        ordinal_big_tuples.append((npa.tns_ptrn + number + "0(\.000){2}\.0([01][1-9]|10)\.$", rule, 'ten billions', string + 'milljarð' + letter + ' og'))
        ordinal_big_tuples.append((npa.tns_ptrn + number + "0(\.000){3}\.$", rule, 'ten billions', string + 'milljarð' + letter))

    for string, number in tp.mb_ordinal_zip:
        ordinal_big_tuples.append((npa.ones_ptrn_11 + number + "\.000\.0([01][1-9]|10)\.$", rule, 'millions', string + 'milljón' + letter + ' og'))
        ordinal_big_tuples.append((npa.ones_ptrn_11 + number + "(\.000){2}\.$", rule, 'millions', string + 'milljón' + letter))
        ordinal_big_tuples.append((npa.ones_ptrn_11 + number + "(\.000){2}\.0([01][1-9]|10)\.$", rule, 'billions', string + 'milljarð' + letter + ' og'))
        ordinal_big_tuples.append((npa.ones_ptrn_11 + number + "(\.000){3}\.$", rule, 'billions', string + 'milljarð' + letter))

    for string, number in tp.tens_zip:
        ordinal_big_tuples.append(("^[1-9]?" + number + "\.000\.0([01][1-9]|10)\.$", rule, 'millions', string + ' milljón' + letter + ' og'))
