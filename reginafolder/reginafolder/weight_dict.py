from . import abbr_patterns as ap

# Weight is a ton (t), kg, ng, mg, µg, pg, ag, zg, yg, gr or lbs
weight_ptrn = r"\b(t|[knmµpazy]?gr?|lbs)\.?\b"

def make_weight_dict():
    weight_dict = {"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) t\.?(\W|$)": "\g<1> tonni\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) t\.?(\W|$)": "\g<1> tonns\g<10>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) t\.?(\W|$)": "\g<1> tonnum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " t\.?(\W|$)": "\g<1> \g<11> tonnum\g<13>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) t\.?(\W|$)": "\g<1> tonna\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " t\.?(\W|$)": "\g<1> \g<11> tonna\g<13> ",
                    "(\d|" + ap.amounts + ") t\.?(\W|$)": "\g<1> tonn \g<3>",
                   
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) gr?\.?(\W|$)": "\g<1> grammi\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) gr?\.?(\W|$)": "\g<1> gramms\g<10>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) gr?\.?(\W|$)": "\g<1> grömmum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " gr?\.?(\W|$)": "\g<1> \g<11> grömmum\g<14>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) gr?\.?(\W|$)": "\g<1> gramma\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " gr?\.?(\W|$)": "\g<1> \g<11> gramma\g<14>",
                    "(1 )gr?\.?(\W|$)": "\g<1>gramm\g<2>",
                    "([02-9]|" + ap.amounts + ") gr?\.?(\W|$)": "\g<1> grömm \g<3>"}

    prefix_weight = [("nanó", "n"),
                     ("milli", "m"),
                     ("míkró", "µ"),
                     ("píkó", "p"),
                     ("ató", "a"),
                     ("septó", "z"),
                     ("jogtó", "y")]

    base_weight = [("kíló", "kg"),
                   ("pund", "lbs")]

    for prefix, letter in prefix_weight:
        weight_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "g\.?(\W|$)": "\g<1> " + prefix + "grammi\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letter + "g\.?(\W|$)": "\g<1> " + prefix + "gramms\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "g\.?(\W|$)": "\g<1> " + prefix + "grömmum\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "g\.?(\W|$)": "\g<1> \g<11> " + prefix + "grömmum\g<14>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letter + "g\.?(\W|$)": "\g<1> " + prefix + "gramma\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letter + "g\.?(\W|$)": "\g<1> \g<11> " + prefix + "gramma\g<14>"})

        weight_dict.update({"(1 )" + letter + "g\.?(\W|$)": "\g<1>" + prefix + "gramm\g<2>"})
        weight_dict.update({"([02-9]|" + ap.amounts + ") " + letter + "g\.?(\W|$)": "\g<1> " + prefix + "grömm \g<3>"})

    for prefix, letter in prefix_weight[:3]:
        weight_dict.update({"(\W|^)" + letter + "g\.?(\W|$)": "\g<1>" + prefix + "grömm\g<2>"})

    for word, letters in base_weight:
        weight_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letters + "\.?(\W|$)": "\g<1> " + word + "i\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) " + letters + "\.?(\W|$)": "\g<1> " + word + "s\g<10>"})

        weight_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letters + "\.?(\W|$)": "\g<1> " + word + "um\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letters + "\.?(\W|$)": "\g<1> \g<11> " + word + "um\g<13>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) " + letters + "\.?(\W|$)": "\g<1> " + word + "a\g<10>"})
        weight_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " " + letters + "\.?(\W|$)": "\g<1> \g<11> " + word + "a\g<13> "})

        weight_dict.update({"(\W|^)" + letters + "(\W|$)": "\g<1>" + word + "\g<2>"})
    return weight_dict