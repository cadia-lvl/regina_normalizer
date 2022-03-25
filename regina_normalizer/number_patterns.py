# [n(noun)l(acjective)][k(masculine)v(feminine)h(neutral)][e(singular)f(plural)][n(nominative)o(accusative)þ(dative)e(genitive)]
# see Markamengi

# GRAMMAR
# ½ skammtur: hálfur skammtur
# ½ followed by a masculine, singular, nominative word
hálfur = r"[nl]ke[n]-?((g?s?)|([svo]?[fme]?))"
# ½ skammt: hálfan skammt
# the following word is masculine, singular, accusative
hálfan = r"[nl]ke[o]-?((g?s?)|([svo]?[fme]?))"
# ½ skammti: hálfum skammti
# whichever gender, singular, dative
hálfum = r"[nl][kvh][ef]þ-?((g?s?)|([svo]?[fme]?))"
# ½ skammts: hálfs skammts
# masculine or neutral, singular, genitive
hálfs = r"[nl][kh]ee-?((g?s?)|([svo]?[fme]?))"
# ½ teskeið: hálf teskeið/hálf epli
# feminine, singular, nominative or neutral, plural, nominative/accusative
hálf = r"(([nl]ven)|([nl]hf[no]))-?((g?s?)|([svo]?[fme]?))"
# ½ teskeið: hálfa teskeið, ½ skammta: hálfa skammta
hálfa = r"[nl][kv][fe]o-?((g?s?)|([svo]?[fme]?))"
# ½ teskeið: hálfri teskeið
hálfri = r"[nl]veþ-?((g?s?)|([svo]?[fme]?))"
# ½ teskeiðar: hálfrar teskeiðar
hálfrar = r"[nl]vee-?((g?s?)|([svo]?[fme]?))"
# ½ epli: hálft epli
hálft = r"[nl]he[no]-?((g?s?)|([svo]?[fme]?))"
# ½ epli: hálfu epli
hálfu = r"[nl]heþ-?((g?s?)|([svo]?[fme]?))"
# ½ skammtar: hálfir skammtar
hálfir = r"[nl]kfn-?((g?s?)|([svo]?[fme]?))"
# ½ skammta: hálfra skammta, ½ teskeiða: hálfra teskeiða, ½ epla: hálfra epla
hálfra = r"[nl][kvh]fe-?((g?s?)|([svo]?[fme]?))"
# ½ teskeiðar: hálfar teskeiðar
hálfar = r"[nl]vf[no]-?((g?s?)|([svo]?[fme]?))"

# 2/3 hlutar: tveir þriðju hlutar
fractionnom = r"[nl][kvh][ef]n-?((g?s?)|([svo]?[fme]?))"
# 2/3 hluta: tvo þriðju hluta
fractiondat = r"[nl][kvh][ef]o-?((g?s?)|([svo]?[fme]?))"
# 2/3 hlutum: tveimur þriðju hlutum
fractionacc = r"[nl][kvh][ef]þ-?((g?s?)|([svo]?[fme]?))"
# 2/3 hluta: tveggja þriðju hluta
fractiongen = r"[nl][kvh][ef]e-?((g?s?)|([svo]?[fme]?))"

# similar to before 
# 1 followed by noun or adjective, masc., nom. or acc.
einn = r"[nl]k[ef][no]-?((g?s?)|([svo]?[fme]?))"
einum = r"[nl]k[ef]þ-?((g?s?)|([svo]?[fme]?))"
eins = r"[nl][kh][ef]e-?((g?s?)|([svo]?[fme]?))"
ein = r"(([nl]v[ef]n)|([n|l]hf[n|o]))-?((g?s?)|([svo]?[fme]?))"
eina = r"[nl]v[ef]o-?((g?s?)|([svo]?[fme]?))"
einni = r"[nl]v[ef]þ-?((g?s?)|([svo]?[fme]?))"
einnar = r"[nl]v[ef]e-?((g?s?)|([svo]?[fme]?))"
eitt = r"[nl]h[ef][no]-?((g?s?)|([svo]?[fme]?))"
einu = r"[nl]h[ef]þ-?((g?s?)|([svo]?[fme]?))"

# 2
tveir = r"[nl]k[ef]n-?((g?s?)|([svo]?[fme]?))"
tvo = r"[nl]k[ef]o-?((g?s?)|([svo]?[fme]?))"
tveimur = r"[nl][kvh][ef]þ-?((g?s?)|([svo]?[fme]?))"
tveggja = r"[nl][kvh][ef]e-?((g?s?)|([svo]?[fme]?))"
tvær = r"[nl]v[ef][no]-?((g?s?)|([svo]?[fme]?))"
tvö = r"[nl]h[ef][no]-?((g?s?)|([svo]?[fme]?))"

# 3
þrír = r"[nl]k[ef]n-?((g?s?)|([svo]?[fme]?))"
þrjá = r"[nl]k[ef]o-?((g?s?)|([svo]?[fme]?))"
þremur = r"[nl][kvh][ef]þ-?((g?s?)|([svo]?[fme]?))"
þriggja = r"[nl][kvh][ef]e-?((g?s?)|([svo]?[fme]?))"
þrjár = r"[nl]v[ef][no]-?((g?s?)|([svo]?[fme]?))"
þrjú = r"[nl]h[ef][no]-?((g?s?)|([svo]?[fme]?))"

# 4
fjórir = r"[nl]k[ef]n-?((g?s?)|([svo]?[fme]?))"
fjóra = r"[nl]k[ef]o-?((g?s?)|([svo]?[fme]?))"
fjórum = r"[nl][kvh][ef]þ-?((g?s?)|([svo]?[fme]?))"
fjögurra = r"[nl][kvh][ef]e-?((g?s?)|([svo]?[fme]?))"
fjórar = r"[nl]v[ef][no]-?((g?s?)|([svo]?[fme]?))"
fjögur = r"[nl]h[ef][no]-?((g?s?)|([svo]?[fme]?))"

# patterns for the ordinal number 2.
# 2. followed by noun or adjective, masculine, singular, nominative
annar = r"[nl]ken-?(g?s?|[svo]?[fme]?)"
annan = r"[nl]keo-?(g?s?|[svo]?[fme]?)"
öðrum = r"[nl]((ke)|([kvh]f))þ-?(g?s?|[svo]?[fme]?)"
annars = r"[nl]kee-?(g?s?|[svo]?[fme]?)"
aðrir = r"[nl]kfn-?(g?s?|[svo]?[fme]?)"
aðra = r"[nl](kf|ve)o-?((g?s?)|([svo]?[fme]?))"
annarra = r"[nl][kvh]fe-?(g?s?|[svo]?[fme]?)"
önnur = r"[nl](ven|hf[no])-?(g?s?|[svo]?[fme]?)"
annarri = r"[nl]veþ-?(g?s?|[svo]?[fme]?)"
annarrar = r"[nl]vee-?(g?s?|[svo]?[fme]?)"
aðrar = r"[nl]vf[no]-?(g?s?|[svo]?[fme]?)"
annað = r"[nl]he[no]-?(g?s?|[svo]?[fme]?)"
öðru = r"[nl]heþ-?(g?s?|[svo]?[fme]?)"
annars = r"[nl][kh]ee-?(g?s?|[svo]?[fme]?)"

# patterns for all ordinal numbers except 2. (see above)
fyrsti = r"[nl]ken-?(g?s?|[svo]?[fme]?)"
fyrsta = r"[nl](ke[oþe]|ven|he[noþe])-?(g?s?|[svo]?[fme]?)"
fyrstu = r"[nl](([kvh]f[noþe])|(ve[oþe]))-?(g?s?|[svo]?[fme]?)"

# when a number is not followed by a noun or an adjective
nonoun = r"^(?![nl][kvh][ef][noþe]-?((g?s?)|([svo]?[fme]?)))[a-záðéíóúýþæö\d\-]*$"

# NUMBER RULES

# digits in decimal numbers preceding the decimal place, can be any positive number and 0
# for example {0,}35 or {13.234,}2342
zeropnt_ptrn = r"^(([1-9]((\d{0,2}(\.\d{3})*\.)\d{3}))|\d+|0),"
# 

# a possibility of digits in decimal numbers succeeding the decimal place, can be any positive number or fraction
# for example 1{,24} or 4{½}
dec_ptrn = r"((,\d*)|(\s1\/2|\s?(½|⅓|¼|⅔|¾)))?$"
# definitely digits in decimal numbers succeeding the decimal place
# 210{,432}
dec_ptrn_def = r"(,\d*)|(\s1\/2|\s?(½|⅓|¼|⅔|¾))$"
# a possibility of digits in decimal numbers succeeding the decimal place, can also be an ordinal number
# 210{.}, 243{,543}, 243
dec_ptrn_ordinal = r"(\.|(,\d*)|(\s1\/2|\s?(½|⅓|¼|⅔|¾)))?$"
# before fraction {123 }3/4
fraction_ptrn_before = r"^(([1-9]((\d{0,2}(\.\d{3})*))|\d+))\s"

# pattern before a number that is not 11-19, so the number becomes "and number"
# legal - 1: einn
# illegal - 11: ellefu
# legal - 21: tuttugu og einn 
ones_ptrn_no11 = r"^((([1-9]((\d{0,2}(\.\d{3})*\.\d)|\d*))[02-9])|[2-9]?)?"
# 11 is legal
ones_ptrn_11 = r"^([1-9]((\d{0,2}(\.\d{3})*\.\d{2}|\d*))|[1-9]?)?"

# pattern before a dozens place: {135.235.2}13
tns_ptrn = r"^((([1-9]((\d{0,2}(\.\d{3})*\.)|\d*))\d)|[1-9])?"

# pattern before a hundreds place: {135.235.}213
hndrds_ptrn = r"^((([1-9]((\d{0,2}(\.\d{3})*\.)|\d*)))|[1-9]?)"
# must occur
hndrds_ptrn_def = r"^((([1-9]((\d{0,2}(\.\d{3})*\.)|\d*)))|[1-9])"


# where you say "tvö þúsund ... "
# {2.000}, {2.021}, {2421}
thsnds_ptrn_after = r"(\.?(000|(0[2-9][1-9])|([1-9](?!00)\d{2})))"
# where you say "tvö þúsund og"
# {2008}, {2019}, {2090}
thsnds_and_ptrn_cardinal = r"\.?(0([01][1-9]|[1-9]0)|[1-9]00)"
# ordinal, where you say "tvö þúsund og"
# {2008.}: tvö þúsundasti og áttundi
thsnds_and_ptrn_ordinal = r"\.?(0[2-9]0|[1-9]00)\.$"

#hndrds_ptrn_after = r"(0([01][1-9]|[2-9]0)|00)"
# "hundruð"
#{2}21.342
hndrd_thsnd_after = r"([2-9][1-9])(\.?\d{3})"
# "hundruð og"
#{2}14.342
hndrd_and_thsnd = r"(([01][1-9]\.?\d{3})|([2-9]0\.?\d{3}))"

# milljón(ir) og
# {2.000.002}: tvær milljónir og tveir
million_and_cardinal = r"\.(([1-9]00\.000)|(0[1-9]0\.000)|(00[1-9]\.000)|(000\.[1-9]00)|(000\.0([01][1-9]|[2-9]0)))"
# milljónasti og
# {2.000.002.}: tvímilljónasti og annar
million_and_ordinal = r"\.(([1-9]00\.000)|(0[1-9]0\.000)|(00[1-9]\.000)|(000\.[1-9]00)|(000\.0[2-9]0))\.$"
# milljónir ..
# {2.034.435} tvær milljónir þrjátíu og fjögur þúsund fjögur hundruð þrjátíu og fimm
milln_ptrn_after = r"\.((000\.000)|([1-9](?!00\.000)\d{2}\.\d{3})|(0[1-9](?!0\.000)\d\.\d{3})|(00[1-9]\.(?!0{3})\d{3})|(0{3}\.0[2-9][1-9]))"
hndrd_and_million = r"([01][1-9]|[2-9]0)(\.\d{3}){2}"
hndrd_million = r"([2-9][1-9])(\.\d{3}){2}"

# milljarðar og
# {2.000.000.003}: tveir milljarðar og þrír
billion_and_cardinal = r"\.((([1-9]00)|(0[1-9]0)|(00[1-9]))(\.0{3}){2}|(0{3}\.([1-9]00|0[1-9]0|00[1-9])\.0{3})|((0{3}\.){2}([1-9]00|0[1-9]0|0[01][1-9])))"
# milljarðasti og
# {2.000.000.003.}: tvímilljarðasti og þrír
billion_and_ordinal = r"\.((([1-9]00)|(0[1-9]0)|(00[1-9]))(\.0{3}){2}|(0{3}\.([1-9]00|0[1-9]0|00[1-9])\.0{3})|((0{3}\.){2}([1-9]00|0[1-9]0)|10))\.$"

# Patterns to make up "milljarðar .."
# {2.001.023.425}: tveir milljarðar ein milljón tuttugu og þrjú þúsund fjögur hundruð tuttugu og fimm
billion1 = r"([1-9](?!00(\.000){2})\d{2}(\.\d{3}){2})"
billion2 = r"(0[1-9](?!0(\.000){2})\d(\.\d{3}){2})"
billion3 = r"(00[1-9](?!(\.000){2})(\.\d{3}){2})"
billion4 = r"(0{3}\.[1-9](?!00\.000)\d{2}\.\d{3})"
billion5 = r"(0{3}\.0[1-9](?!0\.000)\d\.\d{3})"
billion6 = r"(0{3}\.00[1-9]\.(?!000)\d{3})"
billion7 = r"((0{3}\.){2}[1-9](?!00)\d{2})"
billion8 = r"((0{3}\.){2}0[2-9][1-9])"

billion_after = r"\.((000(\.0{3}){2})|" + billion1 + "|" + billion2 + "|" + billion3 + "|" + billion4 + "|" + billion5 + "|" + billion6 + "|" + billion7 + "|" + billion8 + ")"

# 203.000.321.023
hndrd_and_billion = r"([01][1-9]|[2-9]0)(\.\d{3}){3}"
# 234.234.123.234
hndrd_billion = r"([2-9][1-9])(\.\d{3}){3}"