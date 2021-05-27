import re

link_ptrn_external = "^(https?:\/\/)?(www\.)?([A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.\/]+)?"
link_ptrn_internal = "(file|(https?:\/\/)?localhost):[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d_\?\/\.=\-\&\%\#]+"
link_ptrn_mail = "[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.]*@[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_\.]+(\.[A-Za-z])?"
link_ptrn_hashtag = "# ?[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö\d\-_]+"
link_ptrn_all = "^(" + link_ptrn_external + "|" + link_ptrn_internal + "|" + link_ptrn_mail + "|" + link_ptrn_hashtag + ")$"
ordinal_ptrn = "^(\d{1,2}(\.\d{3})*|\d+)\.$"

# kemur bara ef það er núll á undan

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


def wlink_fun(text, ptrn=link_ptrn_all):
    if re.findall(ptrn, text):
        substr = " ".join(text)
        for symbol, word in wlink_numbers:
            substr = re.sub(symbol, word, substr)
        return substr
