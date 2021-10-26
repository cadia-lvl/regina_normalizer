from . import abbr_patterns as ap

currency_ptrn = "(\W|^)((ma?\.?)?[Kk]r\.?\-?|C(HF|AD|ZK)|(DK|SE|NO)K|EUR|GBP|I(NR|SK)|JPY|PTE|(AU|US)D|mlj[óa]\.?)(\W|$)|[\$£¥€₹₤]"


def make_currency_dict():

    currency_dict = {"((\W|^)(" + ap.dat_words + ")) kr\.?\-? ?((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> krónum\g<15>",
                    "((\W|^)(" + ap.gen_words + ")) kr\.?\-? ?((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> króna\g<15>",
                    "(\W|^)[Kk]r\.? ?((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<2> krónur\g<11>",

                    "((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?kr\.?\-?(\W|$)": "\g<1> krónu\g<14>",
                    "((\W|^)(" + ap.accdatgen_words_comb + ")) kr\.?\-? ?((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<10> krónu\g<14>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) kr\.?\-?(\W|$)": "\g<1> krónum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") kr\.?\-?(\W|$)": "\g<1> \g<8>krónum\g<14>",
                    "((\W|^)(" + ap.dat_words + ")) kr\.?\-? ?((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> krónum\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) kr\.?\-?(\W|$)": "\g<1> króna\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") kr\.?\-?(\W|$)": "\g<1> \g<8>króna\g<14>",
                    "((\W|^)(" + ap.gen_words + ")) kr\.?\-? ?((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> króna\g<10>",
                    "(1 ?)kr\.?\-?(\W|$)": "\g<1>króna\g<2>",
                    "([02-9]|" + ap.amounts + ") ?kr\.?\-?(\W|$)": "\g<1> krónur \g<3>",
                    "(\W|^)[Kk]r\.? ?(\d)": "\g<1>krónur \g<2>",
        
                    "((\W|^)(" + ap.accgen_words + ")) \$((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<8> dollara\g<17>",
                    "((\W|^)(" + ap.dat_words + ")) \$((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> dollurum\g<15>",
                    "(\W|^)\$((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<2> dollarar\g<11>",                    
                    "((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?\$(\W|$)": "\g<1> dollara\g<14>",
                    "((\W|^)(" + ap.accdatgen_words_comb + ")) \$((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<10> dollara\g<14>",                    
                    "((\W|^)(" + ap.accgen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\$(\W|$)": "\g<1> dollara\g<12>",
                    "((\W|^)(" + ap.accgen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ?\$(\W|$)": "\g<1> \g<13> dollara\g<16>",
                    "((\W|^)(" + ap.accgen_words + ")) \$((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<11> dollara\g<12>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?\$(\W|$)": "\g<1> dollurum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)?) " + ap.amounts + " ?\$(\W|$)": "\g<1> \g<11> dollurum\g<14>",
                    "((\W|^)(" + ap.dat_words + ")) \$((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> dollurum\g<10>",
                    "(1 ?)\$(\W|$)": "\g<1> dollari\g<2>",
                    "([02-9]|" + ap.amounts + ") ?\$(\W|$)": "\g<1> dollarar\g<2>",
                    "(\W|^) ?\$((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1>\g<2> dollari\g<6>",
                    "(\W|^) ?\$((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1>\g<2> dollarar\g<6>",  
                    "(\W|^)\$(\W|$)": "\g<1>dollari\g<2>",
    
                    "((\W|^)(" + ap.dat_words + ")) £((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> pundum\g<15>",
                    "((\W|^)(" + ap.gen_words + ")) £((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> punda\g<15>",
                    "(\W|^)£((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + "?)(\W|$)": "\g<1> \g<2> pund\g<11>",
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?£(\W|$)": "\g<1> pundi\g<10>",
                    "((\W|^)(" + ap.dat_words + ")) £((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<6> pundi\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?£(\W|$)": "\g<1> punds\g<10>",
                    "((\W|^)(" + ap.gen_words + ")) £((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<6> punds\g<10>",                    
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?£(\W|$)": "\g<1> pundum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?£(\W|$)": "\g<1> \g<8>pundum\g<14>",
                    "((\W|^)(" + ap.dat_words + ")) £((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> pundum\g<10>",                   
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?£(\W|$)": "\g<1> punda\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?£(\W|$)": "\g<1> \g<8>punda\g<14>",
                    "((\W|^)(" + ap.gen_words + ")) £((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> punda\g<10>",                                       
                    "(\W|^) ?£(((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)(\W|$)": "\g<1>\g<2> pund\g<7>",                  
                    "(\W|^)£(\W|$)": "\g<1>pund\g<2>",

                    "((\W|^)(" + ap.dat_words + ")) ¥((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> japönskum jenum\g<15>",
                    "((\W|^)(" + ap.gen_words + ")) ¥((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> japanskra jena\g<15>",                 
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?¥(\W|$)": "\g<1> japönsku jeni\g<10>",
                    "((\W|^)(" + ap.dat_words + ")) ¥((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<6> japönsku jeni\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?¥(\W|$)": "\g<1> japansks jens\g<10>",
                    "((\W|^)(" + ap.gen_words + ")) ¥((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<6> japansks jens\g<10>",                  
                    "((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?¥(\W|$)": "\g<1> japönskum jenum\g<10>",
                    "((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?¥(\W|$)": "\g<1> \g<8>japönskum jenum\g<14>",
                    "((\W|^)(" + ap.dat_words + ")) ¥((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9>japönskum jenum\g<10>",
                    "((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?¥(\W|$)": "\g<1> japanskra jena\g<10>",
                    "((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?¥(\W|$)": "\g<1> \g<8>japanskra jena\g<14>",
                    "((\W|^)(" + ap.gen_words + ")) ¥((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> japanskra jena\g<10>",                    
                    "(1 ?)¥(\W|$)": "\g<1>japanskt jen\g<2>",
                    "([02-9]|" + ap.amounts + ") ?¥(\W|$)": "\g<1> japönsk jen\g<2>",                  
                    "(\W|^) ?¥((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1>\g<2> japanskt jen\g<6>",
                    "(\W|^) ?¥((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1>\g<2> japönsk jen\g<6>",       
                    "(\W|^)¥(\W|$)": "\g<1>japönsk jen\g<2>",
                    "((\W|^)("+ ap.dat_words + ") (\d{1,2}\.)?(\d{3}\.?)*\d+(,\d+)?) þ\.?kr\.?\-?(\W|$)": "\g<1> þúsund krónum\g<9>",
                    "((\W|^)("+ ap.gen_words + ") (\d{1,2}\.)?(\d{3}\.?)*\d+(,\d+)?) þ\.?kr\.?\-?(\W|$)": "\g<1> þúsund króna\g<9>",
                    "(\W|^)þ\.?kr\.?\-?(\W|$)": "\g<1>þúsund krónur\g<2>"}


    currency_list = [("evr", "€"), ("rúpí", "₹"), ("lír", "₤")]

    for word, symbol in currency_list:
        currency_dict.update({"((\W|^)(" + ap.dat_words + ")) " + symbol + "((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> " + word + "um\g<15>"})
        currency_dict.update({"((\W|^)(" + ap.gen_words + ")) " + symbol + "((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<6> " + word + "a\g<15>"})
        currency_dict.update({"(\W|^)" + symbol + "((((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ")(\W|$)": "\g<1> \g<2> " + word + "ur\g<11>"})

        currency_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))) ?" + symbol + "(\W|$)": "\g<1> " + word + "u\g<14>"})
        currency_dict.update({"((\W|^)(" + ap.accdatgen_words_comb + ")) " + symbol + "((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1> \g<10> " + word + "u\g<14>"})

        currency_dict.update({"((\W|^)(" + ap.dat_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?" + symbol + "(\W|$)": "\g<1> " + word + "um\g<10>"})
        currency_dict.update({"((\W|^)(" + ap.dat_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?" + symbol + "(\W|$)": "\g<1> \g<8>" + word + "um\g<14>"})
        currency_dict.update({"((\W|^)(" + ap.dat_words + ")) " + symbol + "((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> " + word + "um\g<10>"})
        currency_dict.update({"((\W|^)(" + ap.gen_words + ") ((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))) ?" + symbol + "(\W|$)": "\g<1> " + word + "a\g<10>"})
        currency_dict.update({"((\W|^)(" + ap.gen_words + ") (((\d{1,2}\.)?(\d{3}\.?)*|\d+)(,\d+)?)? " + ap.amounts + ") ?" + symbol + "(\W|$)": "\g<1> \g<8>" + word + "a\g<14>"})
        currency_dict.update({"((\W|^)(" + ap.gen_words + ")) " + symbol + "((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1> \g<9> " + word + "a\g<10>"})

        currency_dict.update({"(1 ?)" + symbol + "(\W|$)": "\g<1> " + word + "a\g<2>"})
        currency_dict.update({"([02-9]|" + ap.amounts + ") ?" + symbol + "(\W|$)": "\g<1> " + word + "ur\g<2>"})

        currency_dict.update({"(\W|^) ?" + symbol + "((\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1))(\W|$)": "\g<1>\g<2> " + word + "a\g<6>"})
        currency_dict.update({"(\W|^) ?" + symbol + "((\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d,\d*[02-9]))(\W|$)": "\g<1>\g<2> " + word + "ur\g<6>"})

        currency_dict.update({"(\W|^)" + symbol + "(\W|$)": "\g<1>" + word + "ur\g<2>"})
        
    currency_letters = [("ISK", "íslenskar krónur"), ("GBP", "sterlingspund"), ("EUR", "evrur"),
                        ("USD", "bandaríkjadalir"), ("DKK", "danskar krónur"), ("AUD", "ástralskir dalir"),
                        ("JPY", "japönsk jen"), ("CHF", "svissneskir frankar"), ("CAD", "kanadískir dalir"),
                        ("CZK", "tékkneskar krónur"), ("INR", "indverskar rúpíur"), ("SEK", "sænskar krónur"),
                        ("NOK", "norskar krónur"), ("PTE", "portúgalskir skútar")]

    for letters, word in currency_letters:
        currency_dict.update({"(\W|^)" + letters + "(\W|$)": "\g<1>" + word + "\g<2>"})

    million_list = [("m\.?kr\.?\-?", " króna"),
                    ("mljó\.?", "")]

    for letters, suffix in million_list:
        currency_dict.update({"((\W|^)(" + ap.gen_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1) )" + letters + "(\W|$)": "\g<1>milljónar" + suffix + "\g<9>"})
        currency_dict.update({"((\W|^)("+ ap.dat_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d+(,\d*[02-9])) )" + letters + "(\W|$)": "\g<1>milljónum" + suffix + "\g<10>"})
        currency_dict.update({"((\W|^)("+ ap.gen_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d+(,\d*[02-9])) )" + letters + "(\W|$)": "\g<1>milljóna" + suffix + "\g<10>"})
        currency_dict.update({"(1 )" + letters + "(\W|$)": "\g<1>milljón" + suffix + "\g<2>"})
        currency_dict.update({"([02-9] )" + letters + "(\W|$)": "\g<1>milljónir" + suffix + "\g<2>"})


    billion_list = [("ma\.?kr\.?\-?", " króna"),
                    ("mlja\.?", "")]

    for letters, suffix in billion_list:
        currency_dict.update({"((\W|^)(" + ap.acc_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1) )" + letters + "(\W|$)": "\g<1>milljarð" + suffix + "\g<9>"})
        currency_dict.update({"((\W|^)(" + ap.dat_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1) )" + letters + "(\W|$)": "\g<1>milljarði" + suffix + "\g<9>"})
        currency_dict.update({"((\W|^)(" + ap.gen_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*1|\d,\d*1) )" + letters + "(\W|$)": "\g<1>milljarðs" + suffix + "\g<9>"})
        currency_dict.update({"((\W|^)("+ ap.accgen_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d+(,\d*[02-9])) )" + letters + "(\W|$)": "\g<1>milljarða" + suffix + "\g<12>"})
        currency_dict.update({"((\W|^)("+ ap.dat_words + ") (\d{1,2}\.)?(\d{3}\.?)*(\d*[02-9]|\d+(,\d*[02-9])) )" + letters + "(\W|$)": "\g<1>milljörðum" + suffix + "\g<10>"})
        currency_dict.update({"(1 )" + letters + "(\W|$)": "\g<1> milljarður" + suffix + "\g<2>"})
        currency_dict.update({"([02-9] )" + letters + "(\W|$)": "\g<1> milljarðar" + suffix + "\g<2>"})

    return currency_dict
