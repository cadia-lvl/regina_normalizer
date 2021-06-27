
from . import number_patterns as npa
from . import tuple_rules as tp

ordinal_million_tuples = []

for rule, letter in tp.dozens_ordinal_letters:
    ordinal_million_tuples.append((npa.tns_ptrn + "10\.?000\.$", rule, 'ten thousands', ' tíu þúsund' + letter))
    ordinal_million_tuples.append((npa.hndrds_ptrn + "100\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', ' eitt hundrað þúsund' + letter + ' og'))
    ordinal_million_tuples.append(("^100\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', 'hundrað þúsund' + letter + ' og'))        
    ordinal_million_tuples.append((npa.hndrds_ptrn + "100\.?000\.$", rule, 'hundred thousands',' eitt hundrað þúsund' + letter))
    ordinal_million_tuples.append(("^100\.?000\.$", rule, 'hundred thousands', 'hundrað þúsund' + letter))
    for string, number in tp.dozens_zip:
        ordinal_million_tuples.append((npa.tns_ptrn + number + "0\.?0([01][1-9]|10)\.$", rule, 'ten thousands', string + 'hæjó þúsund' + letter + ' og'))
        ordinal_million_tuples.append((npa.tns_ptrn + number + "0\.?000\.$", rule, 'ten thousands', string + ' þúsund' + letter))
    for string, number in tp.hundreds_thousands_zip:
        ordinal_million_tuples.append((npa.hndrds_ptrn + number + "00\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', string + ' hundruðþúsund' + letter + ' og'))
        ordinal_million_tuples.append((npa.hndrds_ptrn + number + "00\.?000\.$", rule, 'hundred thousands',string + ' hundruðþúsund' + letter))
