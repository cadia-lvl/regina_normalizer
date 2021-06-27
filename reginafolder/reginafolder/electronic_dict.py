from . import abbr_patterns as ap

electronic_ptrn = r"\b([kMGT]?(V|Hz|B|W|W\.?(st|h)))\.?\b"

def make_electronic_dict():

    electronic_dict = {}

    watt_prefix = [("", ""), ("k", "kíló"), ("M", "Mega"), ("G", "Gíga"), ("T", "Tera")]
    measurement = [('V', 'volt'), ('Hz', 'herz')]

    for letter, prefix in watt_prefix:
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> " + prefix + "vattstundar\g<11>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> " + prefix + "vattstundum\g<11>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> \g<11> " + prefix + "vattstundum\g<15>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> " + prefix + "vattstunda\g<11>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> \g<11> " + prefix + "vattstunda\g<15>"})
        electronic_dict.update({"(1 )" + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> " + prefix + "vattstund\g<3>"})
        electronic_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "[Ww]\.?(st|h)\.?(\W|$)": "\g<1> " + prefix + "vattstundir \g<3>"})
        
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "W(\W|$)": "\g<1> " + prefix + "vatti\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "W(\W|$)": "\g<1> " + prefix + "vatts\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "W(\W|$)": "\g<1> " + prefix + "vöttum\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "W(\W|$)": "\g<1> \g<11> " + prefix + "vöttum\g<14>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "W(\W|$)": "\g<1> " + prefix + "vatta\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "W(\W|$)": "\g<1> \g<11> " + prefix + "vatta\g<14> "})
        electronic_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "W(\W|$)": "\g<1> " + prefix + "vött \g<3>"})
        electronic_dict.update({"(1 )" + letter + "W(\W|$)": "\g<1> " + prefix + "vatt\g<2>"})  

        for symbol, word in measurement:
   
            electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + symbol + "(\W|$)": "\g<1> " + prefix + word + "i\g<10>"})
            electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + symbol + "(\W|$)": "\g<1> " + prefix + word + "s\g<10>"})
            electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + symbol + "(\W|$)": "\g<1> " + prefix + word + "um\g<10>"})
            electronic_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + symbol + "(\W|$)": "\g<1> \g<11> " + prefix + word + "um\g<14>"})
            electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + symbol + "(\W|$)": "\g<1> " + prefix + word + "a\g<10>"})
            electronic_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + symbol + "(\W|$)": "\g<1> \g<11> " + prefix + word + "a\g<14> "})
            electronic_dict.update({"(\d|" + ap.amounts + ") " + letter + symbol + "(\W|$)": "\g<1> " + prefix + word + " \g<3>"})

    for letter, prefix in watt_prefix[1:]:
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "B(\W|$)": "\g<1> " + prefix + "bæti\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "B(\W|$)": "\g<1> " + prefix + "bæts\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "B(\W|$)": "\g<1> " + prefix + "bætum\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "B(\W|$)": "\g<1> \g<11> " + prefix + "bætum\g<14>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "B(\W|$)": "\g<1> " + prefix + "bæta\g<10>"})
        electronic_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "B(\W|$)": "\g<1> \g<11> " + prefix + "bæta\g<14> "})
        electronic_dict.update({"(\d|" + ap.amounts + ") " + letter + "B(\W|$)": "\g<1> " + prefix + "bæt \g<3>"})

    return electronic_dict