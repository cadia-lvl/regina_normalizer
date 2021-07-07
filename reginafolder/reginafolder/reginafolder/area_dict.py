from . import abbr_patterns as ap

area_ptrn = r"\b(ha|(f(er)?|rúm)[pnµmcsdk]?m\b\.?)|[pnµmcsdk]?m[²2³3]"

def make_area_dict():
    area_dict = {"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ha\.?(\W|$)": "\g<1> hektara\g<14>",
                "((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ha\.?(\W|$)": "\g<1> hektara\g<12>",
                "((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ha\.?(\W|$)": "\g<1> \g<13> hektara\g<16>",
                "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ha\.?(\W|$)": "\g<1> hekturum\g<10>",
                "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ha\.?(\W|$)": "\g<1> \g<11> hekturum\g<14>",
                "(1) ha\.?(\W|$)": "\g<1> hektari\g<2>",
                "([02-9]|" + ap.amounts + ") ha\.?(\W|$)": "\g<1> hektarar \g<3>"}

    dimension_after = [("²", "fer"),
                       ("2", "fer"),
                       ("³", "rúm"),
                       ("3", "rúm")]

    dimension_before = [("f", "fer"),
                        ("fer", "fer"),
                        ("rúm", "rúm")]

    prefix_meter_dimension = [("", ""),
                            ("p", "píkó"),
                            ("n", "nanó"),
                            ("µ", "míkró"),
                            ("m", "milli"),
                            ("[cs]", "senti"),
                            ("d", "desi"),
                            ("k", "kíló")]

    for letter, prefix in prefix_meter_dimension:
        for superscript, dimension in dimension_after:
            area_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "m" + superscript + "(\W|$)": "\g<1> " + dimension + prefix + "metra\g<14>"})
            area_dict.update({"((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "m" + superscript + "(\W|$)": "\g<1> " + dimension + prefix + "metra\g<12>"})
            area_dict.update({"((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "m" + superscript + "(\W|$)": "\g<1> \g<13> " + dimension + prefix + "metra\g<16>"})
            area_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "m" + superscript + "(\W|$)": "\g<1> " + dimension + prefix + "metrum\g<10>"})
            area_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "m" + superscript + "(\W|$)": "\g<1> \g<11> " + dimension + prefix + "metrum\g<14>"})      
            area_dict.update({"(1 )" + letter + "m" + superscript + "(\W|$)": "\g<1>" + dimension + prefix + "metri\g<2>"})
            area_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "m" + superscript + "(\W|$)": "\g<1> " + dimension + prefix + "metrar \g<3>"})

    for letter, prefix in prefix_meter_dimension:
        for preprefix, dimension in dimension_before:
            area_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + preprefix + letter + "m\.?(\W|$)": "\g<1> " + dimension + prefix + "metra\g<14>"})
            area_dict.update({"((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + preprefix + letter + "m\.?(\W|$)": "\g<1> " + dimension + prefix + "metra\g<12>"})
            area_dict.update({"((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + preprefix + letter + "m\.?(\W|$)": "\g<1> \g<13> " + dimension + prefix + "metra\g<16>"})
            area_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + preprefix + letter + "m\.?(\W|$)": "\g<1> " + dimension + prefix + "metrum\g<10>"})
            area_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + preprefix + letter + "m\.?(\W|$)": "\g<1> \g<11> " + dimension + prefix + "metrum\g<14>"})
            area_dict.update({"(1 )" + preprefix + letter + "m\.?(\W|$)": "\g<1>" + dimension + prefix + "metri\g<2>"})
            area_dict.update({"([02-9]|" + ap.amounts + ") " + preprefix + letter + "m\.?(\W|$)": "\g<1> " + dimension + prefix + "metrar \g<3>"})

    return area_dict