from . import abbr_patterns as ap

volume_ptrn = r"\b[dcmµ]?[Ll]\.?\b"

def make_volume_dict():

    volume_dict = {}

    prefix_liter = [("", ""),
                 ("d", "desi"),
                 ("c", "senti"),
                 ("m", "milli"),
                 ("µ", "míkró")]

    for letter, prefix in prefix_liter:
        volume_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "[Ll]\.?(\W|$)": "\g<1> " + prefix + "lítra\g<14>"})
        volume_dict.update({"((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "[Ll]\.?(\W|$)": "\g<1> " + prefix + "lítra\g<12>"})
        volume_dict.update({"((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "[Ll]\.?(\W|$)": "\g<1> \g<13> " + prefix + "lítra\g<16>"})
        volume_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "[Ll]\.?(\W|$)": "\g<1> " + prefix + "lítrum\g<10>"})
        volume_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "[Ll]\.?(\W|$)": "\g<1> \g<11> " + prefix + "lítrum\g<14>"})
        volume_dict.update({"(1 )" + letter + "[Ll]\.?(\W|$)": "\g<1>" + prefix + "lítri\g<2>"})
        volume_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "[Ll]\.?(\W|$)": "\g<1> " + prefix + "lítrar \g<3>"})

    for letter, prefix in prefix_liter[1:]:
        volume_dict.update({"(\W|^)" + letter + "l\.?(\W|$)": "\g<1>" + prefix + "lítrar \g<2>"})

    return volume_dict
