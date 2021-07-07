from . import abbr_patterns as ap

rest_ptrn = r"\%|\b(stk|[Kk][Cc]al)\.?\b"

def make_rest_measure_dict():
    rest_measure_dict = {"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?\%(\W|$)": "\g<1> prósenti\g<10>",
                        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?\%(\W|$)": "\g<1> prósents\g<10>",
                        "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\%(\W|$)": "\g<1> prósentum\g<10>",
                        "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " \%(\W|$)": "\g<1> \g<11> prósentum\g<14>",
                        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\%(\W|$)": "\g<1> prósenta\g<10>",
                        "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " \%(\W|$)": "\g<1> \g<11> prósenta\g<14> ",
                        "\%": " prósent",

                        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) stk\.?(\W|$)": "\g<1> stykkis\g<10>",
                        "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) stk\.?(\W|$)": "\g<1> stykkjum\g<10>",
                        "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " stk\.?(\W|$)": "\g<1> \g<11> stykkjum\g<14>",
                        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) stk\.?(\W|$)": "\g<1> stykkja\g<10>",
                        "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " stk\.?(\W|$)": "\g<1> \g<11> stykkja\g<14> ",
                        "(\W|^)[Ss]tk\.?(\W|$)": "\g<1>stykki\g<2>",

                        "((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) [Kk][Cc]al(\W|$)": "\g<1> kílókaloríu\g<14>",
                        "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) [Kk][Cc]al(\W|$)": "\g<1> kílókaloríu\g<10>",
                        "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) [Kk][Cc]al(\W|$)": "\g<1> kílókaloríum\g<10>",
                        "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " [Kk][Cc]al(\W|$)": "\g<1> \g<11> kílókaloríum\g<14>",
                        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) [Kk][Cc]al(\W|$)": "\g<1> kílókaloría\g<10>",
                        "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " [Kk][Cc]al(\W|$)": "\g<1> \g<11> kílókaloría\g<14> ",
                        "(1 )[Kk][Cc]al(\W|$)": "\g<1>kílókaloría\g<2>",
                        "(\W|^)[Kk][Cc]al\.?(\W|$)": "\g<1>kílókaloríur\g<2>"}
     
    return rest_measure_dict
