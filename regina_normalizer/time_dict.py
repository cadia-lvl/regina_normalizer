from . import abbr_patterns as ap

time_ptrn = r"\b(klst|mín|m?s(ek)?)\b"

def make_time_dict():

    time_dict = {"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) klst\.?(\W|$)": "\g<1> klukkustundar\g<10>",
        "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) klst\.?(\W|$)": "\g<1> klukkustundum\g<10>",
        "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " klst\.?(\W|$)": "\g<1> \g<11> klukkustundum\g<14>",
        "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) klst\.?(\W|$)": "\g<1> klukkustunda\g<10>",
        "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " klst\.?(\W|$)": "\g<1> \g<11> klukkustunda\g<14>",

        "(1 )klst\.?(\W|$)": "\g<1> klukkustund\g<2>",
        "(\W|^)klst\.?(\W|$)": "\g<1>klukkustundir\g<2>"}

    prefix_time = [("mín()?", "mínút"),
                   ("s(ek)?", "sekúnd"),
                   ("ms(ek)?", "millisekúnd")]

    for letters, prefix in prefix_time:
        time_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letters + "\.?(\W|$)": "\g<1> " + prefix + "u\g<15>"})
        time_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letters + "\.?(\W|$)": "\g<1> " + prefix + "u\g<11>"})
        time_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letters + "\.?(\W|$)": "\g<1> " + prefix + "um\g<11>"})
        time_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letters + "\.?(\W|$)": "\g<1> \g<11> " + prefix + "um\g<15>"})
        time_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letters + "\.?(\W|$)": "\g<1> " + prefix + "na\g<11>"})
        time_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letters + "\.?(\W|$)": "\g<1> \g<11> " + prefix + "na\g<15>"})
        time_dict.update({"(1 )" + letters + "\.?(\W|$)": "\g<1>" + prefix + "a\g<3>"})
        time_dict.update({"([02-9]|" + ap.amounts + ") " + letters + "\.?(\W|$)": "\g<1> " + prefix + "ur \g<3>"})

    return time_dict