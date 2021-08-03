from . import abbr_patterns as ap

distance_ptrn = r"[\′\″]|\b([pnµmcsdkN]?m|ft)\.?\b"

def make_distance_dict():

    distance_dict = {"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) (\′|ft\.?)(\W|$)": "\g<1> feti\g<11>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) (\′|ft\.?)(\W|$)": "\g<1> fets\g<11>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) (\′|ft\.?)(\W|$)": "\g<1> fetum\g<11>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " (\′|ft\.?)(\W|$)": "\g<1> \g<11> fetum\g<15>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) (\′|ft\.?)(\W|$)": "\g<1> feta\g<11>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " (\′|ft\.?)(\W|$)": "\g<1> \g<11> feta\g<15> ",
                    "(\d|" + ap.amounts + " )(\′|ft\.?)(\W|$)": "\g<1> fet \g<4>",
                     
                    "((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?\″(\W|$)": "\g<1> tommu \g<11>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\″(\W|$)": "\g<1> tommum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ?\″(\W|$)": "\g<1> \g<11> tommum\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\″(\W|$)": "\g<1> tomma\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ?\″(\W|$)": "\g<1> \g<11> tomma\g<10> ",                    
                    "(1 ?)\″\.?(\W|$)": "\g<1> tomma\g<2>",
                    "([02-9]|" + ap.amounts + ") ?\″\.?(\W|$)": "\g<1> tommur \g<3>",
                     
                    "((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1)) )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1> metra\g<14>",
                    "((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9])) )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1> metra\g<12>",
                    "((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + " )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1> \g<13> metra\g<16>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9])) )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1> metrum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + " )m\.?( (?![kmgyabefstvö]\.)(?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1> \g<11> metrum\g<14>",
                    "(1 )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1>metri\g<2>",
                    "([02-9] )m\.?( (?![kmgyabefstvö]\.)[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]*(\W|$))": "\g<1>metrar\g<2>"}    

    prefix_meter = [("p", "píkó"),
                    ("n", "nanó"),
                    ("µ", "míkró"),
                    ("m", "milli"),
                    ("[cs]", "senti"),
                    ("d", "desi"),
                    ("k", "kíló"),
                    ("N", "njúton")]

    for letter, prefix in prefix_meter:
        distance_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "m\.?(\W|$)": "\g<1> " + prefix + "metra\g<14>"})
        distance_dict.update({"((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "m\.?(\W|$)": "\g<1> " + prefix + "metra\g<12>"})
        distance_dict.update({"((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "m\.?(\W|$)": "\g<1> \g<13> " + prefix + "metra\g<16>"})
        distance_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "m\.?(\W|$)": "\g<1> " + prefix + "metrum\g<10>"})
        distance_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "m\.?(\W|$)": "\g<1> \g<11> " + prefix + "metrum\g<14>"})
        distance_dict.update({"(1 )" + letter + "m\.?(\W|$)": "\g<1>" + prefix + "metri \g<2>"})
        distance_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "m\.?(\W|$)": "\g<1> " + prefix + "metrar \g<3>"})

    return distance_dict