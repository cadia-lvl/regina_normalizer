# These control the case of the succeeding number, whether it's accusative, dative, genitive or a combination.
# Nominative is default
acc_words = '[Uu]m(fram|hverfis)|UM(FRAM|HVERFIS)|[Uu]m|UM|[Gg]egnum|GEGNUM|[Kk]ringum|KRINGUM|[Vv]ið|VIÐ|[Íí]|[Áá]'
dat_words = '[Ff]rá|FRÁ|[Aa][ðf]|A[ÐF]|[Áá]samt|ÁSAMT|[Gg]agnvart|GAGNVART|[Gg]egnt?|GEGNT?|[Hh]anda|HANDA|[Hh]já|HJÁ|[Mm]eð( )?fram|MEÐ( )?FRAM|[Mm]óti?|MÓTI?|[Uu]ndan|UNDAN|[Nn]álægt|NÁLÆGT'
gen_words = '[Tt]il|TIL|[Aa]uk|AUK|[Áá]n|ÁN|[Hh]andan|HANDAN|[Ii]nnan|INNAN|[Mm]eðal|MEÐAL|[Mm]egin|MEGIN|[Mm]ill(i|um)|MILL(I|UM)|[Oo]fan|OFAN|[Ss]akir|SAKIR|[Ss]ökum|SÖKUM|[Uu]tan|UTAN|[Vv]egna|VEGNA'
accdat_words = "[Ee]ftir|EFTIR|[Ff]yrir|FYRIR|[Mm]eð|MEÐ|[Uu]ndir|UNDIR|[Vv]ið|VIÐ|[Yy]fir|YFIR"
accgen_words = acc_words + "|" + gen_words
accdat_words_comb = acc_words + "|" + dat_words + "|" + accdat_words
accdatgen_words_comb = accdat_words_comb + "|" + gen_words

amounts = "([Hh]undr[au]ð|HUNDR[AU]Ð|[Þþ]úsund|ÞÚSUND|[Mm]illjón(ir)?|MILLJÓN(IR)?)"
# Dates can have a date consisting of a day from 01. to 31., a month, and a year of two to four digits
date_ptrn = r"^((([012]?[1-9]|3[01])\. ?)?(jan(úar)?|feb(rúar)?|mars?|apr(íl)?|maí|jú[nl]í?|ág(úst)?|sep(t(ember)?)?|okt(óber)?|nóv(ember)?|des(ember)?) )\d{2,4}$"
# The link patterns handle external patterns like https://mbl.is/innlent, internal patterns like https://localholst:8888, 
# mail patterns like name@address.com, twitter handles like @handle and hashtags, e.g. #thisrules2021
link_ptrn_external = "(https?:\/\/)?(www\.)?([A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.\/]+)?\.[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.\/]+"
link_ptrn_internal = "(file|(https?:\/\/)?localhost):[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d_\?\/\.=\-\&\%\#]+"
link_ptrn_mail = "[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.]*@[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.]+(\.[A-Za-z])?"
link_ptrn_hashtag = "# ?[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_]+"
link_ptrn_all = "^(" + link_ptrn_external + "|" + link_ptrn_internal + "|" + link_ptrn_mail + "|" + link_ptrn_hashtag + ")$"
