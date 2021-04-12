from tuple_rules import dozens_zip, hundreds_thousands_zip, tens_zip
from number_patterns import *

cardinal_thousands_tuples = [(hndrds_ptrn_no11_def + "1([01][1-9]|[1-9]0)" + dec_ptrn, '^.*$', 'hundreds', ' eitt hundrað og'),
                            (hndrds_ptrn_no11_def + "1[2-9]0\.$", '^.*$', 'hundreds', ' eitt hundrað og'),
                            ("^1([01][1-9]|[1-9]0)" + dec_ptrn, '^.*$', 'hundreds', 'hundrað og'),
                            ("^1([2-9]0)\.$", '^.*$', 'hundreds', 'hundrað og'),
                            (hndrds_ptrn_no11_def + "1([2-9][1-9]|00)" + dec_ptrn_ordinal, '^.*$', 'hundreds', ' eitt hundrað'),
                            ("^100" + dec_ptrn, '^.*$', 'hundreds', 'hundrað'),
                            ("^1([2-9][1-9])" + dec_ptrn_ordinal, '^.*$', 'hundreds', 'hundrað'),
                            (ones_ptrn_no11 + "1" + thsnds_and_ptrn_cardinal + dec_ptrn, '^.*$', 'thousands', ' eitt þúsund og'),
                            (ones_ptrn_no11 + "1" + thsnds_and_ptrn_ordinal, '^.*$', 'thousands', ' eitt þúsund og'),
                            (ones_ptrn_no11 + "1\.?((000$)|(([1-9](?!00)\d{2})|(0[2-9][1-9]))" + dec_ptrn_ordinal + ")", '^.*$', 'thousands', ' eitt þúsund'),
                            ("^1\.?000$", '^.*$', 'thousands', ' þúsund')]

for string, number in dozens_zip:
    cardinal_thousands_tuples.append((tns_ptrn + number + "0" + dec_ptrn, '^.*$', 'dozens', string))
    cardinal_thousands_tuples.append((tns_ptrn + number + "[1-9]" + dec_ptrn, '^.*$', 'dozens', string + ' og'))
    
for string, number in hundreds_thousands_zip:
    cardinal_thousands_tuples.append((hndrds_ptrn_11 + number + "([01][1-9]|[1-9]0)" + dec_ptrn, '^.*$', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append((hndrds_ptrn_11 + number + "[2-9]0\.$", '^.*$', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append((hndrds_ptrn_11 + number + "00" + dec_ptrn, '^.*$', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append((hndrds_ptrn_11 + number + "[2-9][1-9]" + dec_ptrn_ordinal, '^.*$', 'hundreds', string + ' hundruð'))

    cardinal_thousands_tuples.append((ones_ptrn_no11 + number + thsnds_and_ptrn_cardinal + dec_ptrn, '^.*$', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((ones_ptrn_no11 + number + thsnds_and_ptrn_ordinal, '^.*$', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((ones_ptrn_no11 + number + "\.?((000$)|(([1-9](?!00)\d{2})|(0[2-9][1-9]))" + dec_ptrn_ordinal + ")", '^.*$', 'thousands', string + ' þúsund'))
    
for string, number in tens_zip[1:]:
    cardinal_thousands_tuples.append(("^" + number + "([01][1-9]|[1-9]0)" + dec_ptrn, '^.*$', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append(("^" + number + "00" + dec_ptrn, '^.*$', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append(("^" + number + "([2-9][1-9])" + dec_ptrn_ordinal, '^.*$', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append(("^" + number + "([01][1-9]|[1-9]0)" + dec_ptrn, '^.*$', 'thousands', ""))
    cardinal_thousands_tuples.append(("^" + number + "00" + dec_ptrn, '^.*$', 'thousands', ""))
    cardinal_thousands_tuples.append(("^" + number + "([2-9][1-9])" + dec_ptrn_ordinal, '^.*$', 'thousands', ""))
for string, number in tens_zip:
    cardinal_thousands_tuples.append((tns_ptrn + number + thsnds_and_ptrn_cardinal + dec_ptrn, '^.*$', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((tns_ptrn + number + thsnds_and_ptrn_ordinal, '^.*$', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((tns_ptrn + number + thsnds_ptrn_after + dec_ptrn_ordinal, '^.*$', 'thousands', string + ' þúsund'))
