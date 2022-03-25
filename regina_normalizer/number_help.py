int_cols_thousand = ['thousands', 'hundreds','dozens', 'ones']

int_cols_million = ['hundred thousands','ten thousands','thousands', 'hundreds','dozens', 'ones']

int_cols_big = ['hundred billions', 'ten billions','billions', 'hundred millions','ten millions','millions',
                   'hundred thousands','ten thousands','thousands', 'hundreds','dozens', 'ones']

decimal_cols_thousand = ['thousands', 'hundreds','dozens', 'ones','points','point2','point3','point4',
                           'point5','point6','point7','point8','point9','point10']

decimal_cols_big= ['hundred billions', 'ten billions','billions', 'hundred millions','ten millions','millions',
                    'hundred thousands','ten thousands','thousands', 'hundreds','dozens', 'ones','points',
                    'point2','point3','point4','point5','point6','point7','point8','point9','point10']


# time, timedigit, sport
time_sport_cols = ['first_ten', 'first_one','between_teams','second_ten', 'second_one']

ordinal_thousand_ptrn = "^([1-9]\.?\d{3}|[1-9]\d{0,2}|0)\.$"
ordinal_million_ptrn = "^[1-9]\d{0,2}\.?\d{3}\.$"
ordinal_big_ptrn = "^[1-9]\d{0,2}(\.\d{3}){2,3}\.$"

cardinal_thousand_ptrn = "^([1-9]\.?\d{3}|[1-9]\d{0,2})$"
cardinal_million_ptrn = "^[1-9]\d{0,2}\.?\d{3}$"
cardinal_big_ptrn = "^[1-9]\d{0,2}(\.\d{3}){2,3}$"

decimal_thousand_ptrn = "^([1-9]\.?\d{3}|[1-9]\d{0,2}|0),\d+$"
decimal_big_ptrn = "^[1-9]\d{0,2}\.?(\d{3}){1,3},\d+$"

# TODO: provide examples of what patterns should be matched
fraction_ptrn = "^([1-9]\d{0,2} ?)?([1-9]\d*\/([2-9]|[1-9]\d+)|(½|⅓|⅔|¼|¾))$"
time_ptrn = "^(([01]?\d|2[0-4])[:\.][0-5]|0)\d$"
sport_ptrn = "^(?!1\/2)([1-9]\d?\/[1-9]\d?)$"

letters_ptrn = r"^(?!^(RÚV|SPRON|\-|\.)$)[\-\.A-ZÁÐÉÍÓÚÝÞÆÖ]{1,4}$"
roman_letters_ptrn = r"[IVXLCDM]{4,20}"

symbol_ptrn = "^[^A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d]$"

digit_numbers = [('0', ' núll'),
                 ('1', ' einn'),
                 ('2', ' tveir'),
                 ('3', ' þrír'),
                 ('4', ' fjórir'),
                 ('5', ' fimm'),
                 ('6', ' sex'),
                 ('7', ' sjö'),
                 ('8', ' átta'),
                 ('9', ' níu'),
                 ('\-', ' <sil>'),
                 ('\+', ' plús'),
                 ('\.', ' punktur'),
                 (':', ' tvípunktur'),
                 (',', ' komma'),
                 ('\/', ' skástrik')]

digits_ord = [('0', 'núllta'),
                 ('1', 'fyrsta'),
                 ('2', 'annan'),
                 ('3', 'þriðja'),
                 ('4', 'fjórða'),
                 ('5', 'fimmta'),
                 ('6', 'sjötta'),
                 ('7', 'sjöunda'),
                 ('8', 'áttunda'),
                 ('9', 'níunda')]

wlink_numbers = [('0', 'núll'),
                 ('1', 'einn'),
                 ('2', 'tveir'),
                 ('3', 'þrír'),
                 ('4', 'fjórir'),
                 ('5', 'fimm'),
                 ('6', 'sex'),
                 ('7', 'sjö'),
                 ('8', 'átta'),
                 ('9', 'níu'),
                 ('\.', 'punktur'),
                 ('\-', 'bandstrik'),
                 ('\/', 'skástrik'),
                 ('_', 'undirstrik'),
                 ('@', 'hjá'),
                 (':', 'tvípunktur'),
                 ('=', 'jafnt og'),
                 ('\?', 'spurningarmerki'),
                 ('!', 'upphrópunarmerki'),
                 ('&', 'og'),
                 ('%', 'prósent'),
                 ('#', 'myllumerki')]


