acc_words = '[Uu]m(fram|hverfis)|UM(FRAM|HVERFIS)|[Uu]m|UM|[Gg]egnum|GEGNUM|[Kk]ringum|KRINGUM|[Vv]ið|VIÐ|[Íí]|[Áá]'
dat_words = '[Ff]rá|FRÁ|[Aa][ðf]|A[ÐF]|[Áá]samt|ÁSAMT|[Gg]agnvart|GAGNVART|[Gg]egnt?|GEGNT?|[Hh]anda|HANDA|[Hh]já|HJÁ|[Mm]eð( )?fram|MEÐ( )?FRAM|[Mm]óti?|MÓTI?|[Uu]ndan|UNDAN|[Nn]álægt|NÁLÆGT'
gen_words = '[Tt]il|TIL|[Aa]uk|AUK|[Áá]n|ÁN|[Hh]andan|HANDAN|[Ii]nnan|INNAN|[Mm]eðal|MEÐAL|[Mm]egin|MEGIN|[Mm]ill(i|um)|MILL(I|UM)|[Oo]fan|OFAN|[Ss]akir|SAKIR|[Ss]ökum|SÖKUM|[Uu]tan|UTAN|[Vv]egna|VEGNA'
accdat_words = "[Ee]ftir|EFTIR|[Ff]yrir|FYRIR|[Mm]eð|MEÐ|[Uu]ndir|UNDIR|[Vv]ið|VIÐ|[Yy]fir|YFIR"
accgen_words = acc_words + "|" + gen_words
accdat_words_comb = acc_words + "|" + dat_words + "|" + accdat_words
accdatgen_words_comb = accdat_words_comb + "|" + gen_words

amounts = "([Hh]undr[au]ð|HUNDR[AU]Ð|[Þþ]úsund|ÞÚSUND|[Mm]illjón(ir)?|MILLJÓN(IR)?)"
date_ptrn = r"^((([012]?[1-9]|3[01])\. ?)?(jan(úar)?|feb(rúar)?|mars?|apr(íl)?|maí|jú[nl]í?|ág(úst)?|sep(t(ember)?)?|okt(óber)?|nóv(ember)?|des(ember)?) )\d{2,4}$"

weight_ptrn = r"\b(t|[knmµpazy]?gr?|lbs)\.?\b"