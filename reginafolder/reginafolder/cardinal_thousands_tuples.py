from . import tuple_rules as tp
from . import number_patterns as npa

cardinal_thousands_tuples = [(npa.hndrds_ptrn_def + "1([01][1-9]|[1-9]0)" + npa.dec_ptrn, '.*', 'hundreds', ' eitt hundrað og'),
                            (npa.hndrds_ptrn_def + "1[2-9]0\.$", '.*', 'hundreds', ' eitt hundrað og'),
                            ("^1([01][1-9]|[1-9]0)" + npa.dec_ptrn, '.*', 'hundreds', 'hundrað og'),
                            ("^1([2-9]0)\.$", '.*', 'hundreds', 'hundrað og'),
                            (npa.hndrds_ptrn_def + "1([2-9][1-9]|00)" + npa.dec_ptrn_ordinal, '.*', 'hundreds', ' eitt hundrað'),
                            ("^100" + npa.dec_ptrn, '.*', 'hundreds', 'hundrað'),
                            ("^1([2-9][1-9])" + npa.dec_ptrn_ordinal, '.*', 'hundreds', 'hundrað'),
                            (npa.ones_ptrn_no11 + "1" + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'thousands', ' eitt þúsund og'),
                            (npa.ones_ptrn_no11 + "1" + npa.thsnds_and_ptrn_ordinal, '.*', 'thousands', ' eitt þúsund og'),
                            (npa.ones_ptrn_no11 + "1\.?((000$)|(([1-9](?!00)\d{2})|(0[2-9][1-9]))" + npa.dec_ptrn_ordinal + ")", '.*', 'thousands', ' eitt þúsund'),
                            ("^1\.?000$", '.*', 'thousands', ' þúsund')]

for string, number in tp.dozens_zip:
    cardinal_thousands_tuples.append((npa.tns_ptrn + number + "0" + npa.dec_ptrn, '.*', 'dozens', string))
    cardinal_thousands_tuples.append((npa.tns_ptrn + number + "[1-9]" + npa.dec_ptrn, '.*', 'dozens', string + ' og'))
    
for string, number in tp.hundreds_thousands_zip:
    cardinal_thousands_tuples.append((npa.hndrds_ptrn + number + "([01][1-9]|[1-9]0)" + npa.dec_ptrn, '.*', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append((npa.hndrds_ptrn + number + "[2-9]0\.$", '.*', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append((npa.hndrds_ptrn + number + "00" + npa.dec_ptrn, '.*', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append((npa.hndrds_ptrn + number + "[2-9][1-9]" + npa.dec_ptrn_ordinal, '.*', 'hundreds', string + ' hundruð'))

    cardinal_thousands_tuples.append((npa.ones_ptrn_no11 + number + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((npa.ones_ptrn_no11 + number + npa.thsnds_and_ptrn_ordinal, '.*', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((npa.ones_ptrn_no11 + number + "\.?((000$)|(([1-9](?!00)\d{2})|(0[2-9][1-9]))" + npa.dec_ptrn_ordinal + ")", '.*', 'thousands', string + ' þúsund'))
    
for string, number in tp.tens_zip[1:]:
    cardinal_thousands_tuples.append(("^" + number + "([01][1-9]|[1-9]0)" + npa.dec_ptrn, '.*', 'hundreds', string + ' hundruð og'))
    cardinal_thousands_tuples.append(("^" + number + "00" + npa.dec_ptrn, '.*', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append(("^" + number + "([2-9][1-9])" + npa.dec_ptrn_ordinal, '.*', 'hundreds', string + ' hundruð'))
    cardinal_thousands_tuples.append(("^" + number + "([01][1-9]|[1-9]0)" + npa.dec_ptrn, '.*', 'thousands', ""))
    cardinal_thousands_tuples.append(("^" + number + "00" + npa.dec_ptrn, '.*', 'thousands', ""))
    cardinal_thousands_tuples.append(("^" + number + "([2-9][1-9])" + npa.dec_ptrn_ordinal, '.*', 'thousands', ""))
for string, number in tp.tens_zip:
    cardinal_thousands_tuples.append((npa.tns_ptrn + number + npa.thsnds_and_ptrn_cardinal + npa.dec_ptrn, '.*', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((npa.tns_ptrn + number + npa.thsnds_and_ptrn_ordinal, '.*', 'thousands', string + ' þúsund og'))
    cardinal_thousands_tuples.append((npa.tns_ptrn + number + npa.thsnds_ptrn_after + npa.dec_ptrn_ordinal, '.*', 'thousands', string + ' þúsund'))
