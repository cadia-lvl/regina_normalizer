
import re
import sys
import os
import pos
import torch

from . import number_help as nh 

from . import abbr_patterns as ap
from . import abbr_functions as af

from . import cardinal_ones_tuples as cot
from . import  cardinal_thousands_tuples as ctt
from . import  cardinal_million_tuples as cmt
from . import  cardinal_big_tuples as cbt
from . import  ordinal_ones_tuples as oot
from . import  ordinal_thousands_tuples as ott
from . import  ordinal_million_tuples as omt
from . import  ordinal_big_tuples as obt
from . import  decimal_thousands_tuples as dtt
from . import  fraction_tuples as ft
from . import  sport_tuples as st
from . import  time_tuples as tt

from . import  symbols_dict as sd

# Initialize the tagger
device = torch.device("cpu")  # CPU
tagger: pos.Tagger = torch.hub.load(
    repo_or_dir="cadia-lvl/POS",
    model="tag", # This specifies which model to use. Set to 'tag_large' for large model.
    device=device,
    force_reload=False,
    force_download=False,
)

cardinal_thousand_tuples = cot.cardinal_ones_tuples + ctt.cardinal_thousands_tuples
cardinal_million_tuples = cardinal_thousand_tuples + cmt.cardinal_million_tuples
cardinal_big_tuples = cardinal_million_tuples + cbt.cardinal_big_tuples
ordinal_thousand_tuples = oot.ordinal_ones_tuples + ctt.cardinal_thousands_tuples + ott.ordinal_thousands_tuples
ordinal_million_tuples = ordinal_thousand_tuples + cmt.cardinal_million_tuples + omt.ordinal_million_tuples
ordinal_big_tuples = ordinal_million_tuples + cbt.cardinal_big_tuples + obt.ordinal_big_tuples
decimal_thousand_tuples = cardinal_thousand_tuples + dtt.decimal_thousands_tuples
decimal_big_tuples = cardinal_big_tuples + dtt.decimal_thousands_tuples
fraction_tuples = cardinal_thousand_tuples + ft.fraction_tuples
sport_tuples = st.sport_tuples
time_tuples = tt.time_tuples

symb_dict = sd.symb_dict
symb_ptrn = "[^A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö]"

# Initializes a dict with the required columns (word parts) for each word
def make_dict(word, type_cols):
    value_dict = {}
    value_dict[word] = {type_cols[0]: ""}
    for col in type_cols[1:]:
        value_dict[word].update({col: ""})
    return value_dict

# Fill the dictionaries with values from appropriate number tuples
# Example: word = 4, tuple = ("\d*4", "nvfn", "ones", "fjórar")
# The number 4 followed by a feminine, plural, nominative noun becomes fjórar
def fill_dict(word, tag, tuples, type_dict, cols):
    tmpword = ""
    for i in range(len(tuples)):
        if re.findall(tuples[i][0], word) and re.findall(tuples[i][1], tag):
            try:
                type_dict[word][tuples[i][2]] = tuples[i][3]
            except:
                pass
    for col in cols:
        tmpword += type_dict[word][col]
    return tmpword           

# Expand the digits, the expansion of digit_numbers is in number_help
def digit_fun(substr):
    substr = re.sub(" ", "<sil> ", substr)
    for digit, word in nh.digit_numbers:
        substr = re.sub(digit, word, substr)
    return substr

# Expand the ordinal digits, the expansion of digits_ord is in number_help
def digit_ord_fun(substr):
    for digit, word in nh.digits_ord:
        substr = re.sub("^0" + digit + "\.$", "núll " + word, substr)
    return substr

def wlink_fun(text, ptrn=ap.link_ptrn_all):
    if re.findall(ptrn, text):
        substr = " ".join(text)
        for symbol, word in nh.wlink_numbers:
            substr = re.sub(symbol, word, substr)
        return substr

# replace words according to the appropriate domain 
def replace_domain(splitsent, domain, ptrn="\-|\–|\—"):
    dashsent = []
    for i in range(len(splitsent)):
        try:
            if re.match("\d", splitsent[i-1]) and re.match(ptrn, splitsent[i]) and re.match("\d", splitsent[i+1]):
                if domain == 'sport':
                    splitsent[i] = ""
                else:
                    splitsent[i] = "til"
        except:
            pass
        if splitsent[i] != "":
            dashsent.append(splitsent[i])
        else:
            pass
    return dashsent

# Fill in the number appropriately based on pattern
def number_findall(word, tag, domain):
    normalized_str = ""
    if re.findall(nh.ordinal_thousand_ptrn, word):
        ordinal_thousand_dict = make_dict(word, nh.int_cols_thousand)
        tmpword = fill_dict(word, tag, ordinal_thousand_tuples, ordinal_thousand_dict, nh.int_cols_thousand)

    elif re.findall(nh.ordinal_million_ptrn, word):
        ordinal_million_dict = make_dict(word, nh.int_cols_million)
        tmpword = fill_dict(word, tag, ordinal_million_tuples, ordinal_million_dict, nh.int_cols_million)

    elif re.findall(nh.ordinal_big_ptrn, word):
        ordinal_big_dict = make_dict(word, nh.int_cols_big)
        tmpword = fill_dict(word, tag, ordinal_big_tuples, ordinal_big_dict, nh.int_cols_big)

    elif re.findall(nh.cardinal_thousand_ptrn, word):
        cardinal_thousand_dict = make_dict(word, nh.int_cols_thousand)
        tmpword = fill_dict(word, tag, cardinal_thousand_tuples, cardinal_thousand_dict, nh.int_cols_thousand)

    elif re.findall(nh.cardinal_million_ptrn, word):
        cardinal_million_dict = make_dict(word, nh.int_cols_million)
        tmpword = fill_dict(word, tag, cardinal_million_tuples, cardinal_million_dict, nh.int_cols_million)

    elif re.findall(nh.cardinal_big_ptrn, word):
        cardinal_big_dict = make_dict(word, nh.int_cols_big)
        tmpword = fill_dict(word, tag, cardinal_big_tuples, cardinal_big_dict, nh.int_cols_big)

    elif re.findall(nh.decimal_thousand_ptrn, word):
        decimal_thousand_dict = make_dict(word, nh.decimal_cols_thousand)
        tmpword = fill_dict(word, tag, decimal_thousand_tuples, decimal_thousand_dict, nh.decimal_cols_thousand)

    elif re.findall(nh.decimal_big_ptrn, word):
        decimal_big_dict = make_dict(word, nh.decimal_cols_big)
        tmpword = fill_dict(word, tag, decimal_big_tuples, decimal_big_dict, nh.decimal_cols_big)

    elif re.findall(nh.time_ptrn, word):
        time_dict = make_dict(word, nh.time_sport_cols)
        tmpword = fill_dict(word, tag, time_tuples, time_dict, nh.time_sport_cols)

    elif re.findall(nh.fraction_ptrn, word):
        if domain == 'other' or re.findall("½|⅓|⅔|¼|¾", word):
            # TODO: this does not solve patterns like '2021/2022' correctly (result: 'og hálfur')
            fraction_dict = make_dict(word, nh.decimal_cols_thousand)
            tmpword = fill_dict(word, tag, fraction_tuples, fraction_dict, nh.decimal_cols_thousand)
        elif domain == 'sport':
            # TODO: this does not handle all patterns matched, only \d{1,2}/\d{1,2}!
            sport_dict = make_dict(word, nh.time_sport_cols)
            tmpword = fill_dict(word, tag, sport_tuples, sport_dict, nh.time_sport_cols)
     
    elif re.findall("^0\d\.$", word):
        tmpword = digit_ord_fun(word)
    else:
        tmpword = digit_fun(word)
    word = tmpword
    return word

# Fill in the number, letter, link or symbol based on the tag of the next word
def handle_sentence(sent, domain):
    returnsent = ""
    sentsplit = sent.split()
    dashsent = replace_domain(sentsplit, domain)
    tagsent = tagger.tag_sent(dashsent)
    split_zip = list(zip(dashsent, list(tagsent[1:]) + [""]))
    for word, nexttag in split_zip:
        if re.match("[\d½⅓¼⅔¾\-\–]", word):
            word = number_findall(word, nexttag, domain)
        if re.match(nh.roman_letters_ptrn, word):
            word = " ".join(word)
        elif re.match(nh.letters_ptrn, word):
            word = " ".join(word)
        elif re.match(ap.link_ptrn_all, word):
            word = wlink_fun(word)
        elif re.match(symb_ptrn, word):
            word = af.replace_all(word, symb_dict, symb_ptrn)
        returnsent += word + " "
    return returnsent



