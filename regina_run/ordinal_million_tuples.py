
from number_patterns import tns_ptrn, hndrds_ptrn_11
from tuple_rules import dozens_ordinal_letters, dozens_zip, hundreds_thousands_zip

ordinal_million_tuples = []

for rule, letter in dozens_ordinal_letters:
    ordinal_million_tuples.append((tns_ptrn + "10\.?0([01][1-9]|10)\.$", rule, 'ten thousands', ' tíu þúsund' + letter + ' og'))
    ordinal_million_tuples.append((tns_ptrn + "10\.?000\.$", rule, 'ten thousands', ' tíu þúsund' + letter))
    ordinal_million_tuples.append((hndrds_ptrn_11 + "100\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', ' eitt hundrað þúsund' + letter + ' og'))
    ordinal_million_tuples.append(("^100\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', 'hundrað þúsund' + letter + ' og'))        
    ordinal_million_tuples.append((hndrds_ptrn_11 + "100\.?000\.$", rule, 'hundred thousands',' eitt hundrað þúsund' + letter))
    ordinal_million_tuples.append(("^100\.?000\.$", rule, 'hundred thousands', 'hundrað þúsund' + letter))
    for string, number in dozens_zip:
        ordinal_million_tuples.append((tns_ptrn + number + "0\.?0([01][1-9]|10)\.$", rule, 'ten thousands', string + ' þúsund' + letter + ' og'))
        ordinal_million_tuples.append((tns_ptrn + number + "0\.?000\.$", rule, 'ten thousands', string + ' þúsund' + letter))
    for string, number in hundreds_thousands_zip:
        ordinal_million_tuples.append((hndrds_ptrn_11 + number + "00\.?0([01][1-9]|10)\.$", rule, 'hundred thousands', string + ' hundruðþúsund' + letter + ' og'))
        ordinal_million_tuples.append((hndrds_ptrn_11 + number + "00\.?000\.$", rule, 'hundred thousands',string + ' hundruðþúsund' + letter))
