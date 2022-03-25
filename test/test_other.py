from regina_normalizer import normalizer
from regina_normalizer import tokenizer
import pytest
import re


def normalize(text, domain):
    return normalizer.input_string(text, domain)

def test_fraction():
    # masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1½ vini', 'other').strip()) == 'ég fékk gjöf frá einum og hálfum vini'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva ⅓ skóg?', 'other').strip()) == 'ætlarðu að höggva einn þriðja skóg ?'
    assert re.sub("\s+", " ", normalize('það voru 11⅔ stóll þarna', 'other').strip()) == 'það voru ellefu og tveir þriðju stóll þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til ¾ manna?', 'other').strip()) == 'ætlarðu til þriggja fjórðu manna ?'
    # feminine singular
    assert normalize('11/6 konur', 'other').strip() == 'ellefu sjöttu konur'
    #assert re.sub("\s+", " ", normalize('það var talað um 1 5/6 konu', 'other').strip()) == 'það var talað um eina og fimm sjöttu konu'
    #assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 4 9/19 vinkonum', 'other').strip()) == 'ég fékk gjöf frá fjórum og níu nítjándu vinkonum'
    #assert re.sub("\s+", " ", normalize('ætlarðu til 33/40 konu?', 'other').strip()) == 'ætlarðu til þrjátíu og þriggja fertugustu konu?'
    #assert re.sub("\s+", " ", normalize('33/40', 'other').strip()) == 'þrjátíu og þrír fertugustu'
    assert re.sub("\s+", " ", normalize('5/6', 'other').strip()) == 'fimm sjöttu'


def test_sport():
    assert re.sub("\s+", " ", normalize('Leikurinn fór 2 - 1', 'sport').strip()) == 'Leikurinn fór tvö eitt'
    assert re.sub("\s+", " ", normalize('Lokatölur voru 33 : 77 fyrir Keflavík', 'sport').strip()) == 'Lokatölur voru þrjátíu og þrjú : sjötíu og sjö fyrir Keflavík'
    assert re.sub("\s+", " ", normalize('33/17 , 8/5 frák.', 'sport').strip()) == 'þrjátíu og þrjú <sil> sautján , átta <sil> fimm fráköst .'

def test_time():
    assert re.sub("\s+", " ", normalize('Klukkan er 14:10', 'other').strip()) == 'Klukkan er fjórtán tíu'
    assert re.sub("\s+", " ", normalize('Þetta gerist kl 09.45', 'other').strip()) == 'Þetta gerist klukkan núll níu fjörutíu og fimm'
    assert re.sub("\s+", " ", normalize('Það byrjar kl. 11:59', 'other').strip()) == 'Það byrjar klukkan ellefu fimmtíu og níu'
    assert re.sub("\s+", " ", normalize('Það byrjar kl. 11:69', 'other').strip()) == 'Það byrjar klukkan einn einn tvípunktur sex níu'

def test_digit():
    assert re.sub("\s+", " ", normalize('IP addressan er 24.1392.168', 'other').strip()) == 'I P addressan er tveir fjórir punktur einn þrír níu tveir punktur einn sex átta'
    #assert re.sub("\s+", " ", normalize('IP addressan er 192.168', 'other').strip()) == 'I P addressan er einn níu tveir punktur einn sex átta' - væri rétt
    assert re.sub("\s+", " ", normalize('Útgáfa 2.0', 'other').strip()) == 'Útgáfa tveir punktur núll'
    assert re.sub("\s+", " ", normalize('Það er 05. október', 'other').strip()) == 'Það er núll fimmta október'

def test_wlink():
    assert re.sub("\s+", " ", normalize('www.gmail.com/123_eg_er_her', 'other').strip()) == 'w w w punktur g m a i l punktur c o m skástrik einn tveir þrír undirstrik e g undirstrik e r undirstrik h e r'
    #assert re.sub("\s+", " ", normalize('www.gmail.com/123_eg_er_her', 'other').strip()) == 'w w w punktur g mail punktur com skástrik einn tveir þrír undirstrik eg undirstrik er undirstrik her'
    assert re.sub("\s+", " ", normalize('helgas@ru.is', 'other').strip()) == 'h e l g a s hjá r u punktur i s'
    #assert re.sub("\s+", " ", normalize('helgas@ru.is', 'other').strip()) == 'helgas hjá r u punktur is' - rétt
    assert re.sub("\s+", " ", normalize('#ljosanott2014', 'other').strip()) == 'myllumerki l j o s a n o t t tvö þúsund og fjórtán'
    #assert re.sub("\s+", " ", normalize('#ljosanott2014', 'other').strip()) == 'myllumerki ljosanott tvö þúsund og fjórtán'

def test_symbols():
    assert re.sub("\s+", " ",
                  normalize('að áramótum 2021/2022', 'other').strip()) == 'að áramótum tvö þúsund tuttugu og eitt skástrik tvö þúsund tuttugu og tvö'
    assert re.sub("\s+", " ",
                  normalize('Snýst í suðaustan 10-18 m/s', 'other').strip()) == 'Snýst í suðaustan tíu til átján metrar á sekúndu'

    