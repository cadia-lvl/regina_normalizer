import re
import json
import os

import abbr_dict as abd 
import area_dict as ad
import currency_dict as cd
import denominator_dict as dend
import direction_dict as dird
import distance_dict as dd
import electronic_dict as ed
import period_dict as pd
import rest_dict as rd
import time_dict as td
import volume_dict as vd
import weight_dict as wd
import pre_help_dicts as phd
import symbols_dict as sd

direction_ptrn = "[SN]?V|N|[SN]?A|S"

pre_help_dict = phd.pre_help_dicts
abbr_dict = abd.abbr_dict
area_dict = ad.make_area_dict()
currency_dict = cd.make_currency_dict()
denominator_dict = dend.denominator_dict
direction_dict = dird.direction_dict
distance_dict = dd.make_distance_dict()
electronic_dict = ed.make_electronic_dict()
period_dict = pd.make_period_dict()
rest_dict = rd.make_rest_measure_dict()
time_dict = td.make_time_dict()
volume_dict = vd.make_volume_dict()
weight_dict = wd.make_weight_dict()
symb_dict = sd.symb_dict

# replace words according to the appropriate dictionary 
def replace_all(text, dic, ptrn=""):
    if re.findall(ptrn, text):
        for i, j in dic.items():
            text = re.sub(i, j, text)
    return text

# replace words according to the appropriate domain 
def replace_domain(splitsent, domain, ptrn="\-|\–|\—"):
    finalstring = ""
    for i in range(len(splitsent)):
        try:
            if re.match("\d", splitsent[i-1]) and re.match(ptrn, splitsent[i]) and re.match("\d", splitsent[i+1]):
                if domain == 'sport':
                    splitsent[i] = ""
                else:
                    splitsent[i] = "til"
        except:
            pass
        finalstring += splitsent[i] + " "
    return finalstring

def replace_abbreviations(sent, domain):
    sent = replace_all(sent, direction_dict, direction_ptrn)
    sent = replace_all(sent, pre_help_dict)
    sent = replace_all(sent, denominator_dict, "\/")
    sent = replace_all(sent, weight_dict, wd.weight_ptrn)
    sent = replace_all(sent, distance_dict, dd.distance_ptrn)
    sent = replace_all(sent, area_dict, ad.area_ptrn)
    sent = replace_all(sent, volume_dict, vd.volume_ptrn)
    sent = replace_all(sent, time_dict, td.time_ptrn)
    sent = replace_all(sent, currency_dict, cd.currency_ptrn)
    sent = replace_all(sent, electronic_dict, ed.electronic_ptrn)
    sent = replace_all(sent, rest_dict, rd.rest_ptrn) 
    sent = replace_all(sent, period_dict, pd.period_ptrn)
    sent = replace_all(sent, abbr_dict)
    sent = replace_domain(sent.split(), domain)
    return sent

