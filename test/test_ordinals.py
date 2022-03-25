from regina_normalizer import normalizer
from regina_normalizer import tokenizer
import pytest
import re


def normalize(text, domain):
    return normalizer.input_string(text, domain)


def test_ones_ord():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1. vininum', 'other').strip()) == 'ég fékk gjöf frá fyrsta vininum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 3. skóginn?', 'other').strip()) == 'ætlarðu að höggva þriðja skóginn ?'
    assert re.sub("\s+", " ", normalize('það var 4. stóllinn þarna', 'other').strip()) == 'það var fjórði stóllinn þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 5. mannsins?', 'other').strip()) == 'ætlarðu til fimmta mannsins ?'
    # feminine singular
    assert normalize('6. konan', 'other').strip() == 'sjötta konan'
    assert re.sub("\s+", " ", normalize('það var talað um 7. konuna', 'other').strip()) == 'það var talað um sjöundu konuna'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 8. vinkonunni', 'other').strip()) == 'ég fékk gjöf frá áttundu vinkonunni'
    assert re.sub("\s+", " ", normalize('ætlarðu til 9. konunnar?', 'other').strip()) == 'ætlarðu til níundu konunnar ?'
    # neutral singular
    assert normalize('10. borðið', 'other').strip() == 'tíunda borðið'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 11. tréð?', 'other').strip()) == 'ætlarðu að höggva ellefta tréð ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12. barninu', 'other').strip()) == 'ég fékk gjöf frá tólfta barninu'
    assert re.sub("\s+", " ", normalize('ætlarðu til 13. landsins?', 'other').strip()) == 'ætlarðu til þrettánda landsins ?'
    # masculine plural
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 14. vinunum', 'other').strip()) == 'ég fékk gjöf frá fjórtándu vinunum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 15. skógana?', 'other').strip()) == 'ætlarðu að höggva fimmtándu skógana ?'
    assert re.sub("\s+", " ", normalize('það voru 16. stólarnir þarna', 'other').strip()) == 'það voru sextándu stólarnir þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 17. mannanna?', 'other').strip()) == 'ætlarðu til sautjándu mannanna ?'
    # feminine plural
    assert normalize('18. konurnar', 'other').strip() == 'átjándu konurnar'
    assert re.sub("\s+", " ", normalize('það var talað um 19. konurnar', 'other').strip()) == 'það var talað um nítjándu konurnar'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1. vinkonunum', 'other').strip()) == 'ég fékk gjöf frá fyrstu vinkonunum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 3. kvennanna?', 'other').strip()) == 'ætlarðu til þriðju kvennanna ?'
    # neutral plural
    assert normalize('4. borðin', 'other').strip() == 'fjórðu borðin'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 7. trén?', 'other').strip()) == 'ætlarðu að höggva sjöundu trén ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 13. börnunum', 'other').strip()) == 'ég fékk gjöf frá þrettándu börnunum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 17. landanna?', 'other').strip()) == 'ætlarðu til sautjándu landanna ?'

def test_two_ord():
    # masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. vininum', 'other').strip()) == 'ég fékk gjöf frá öðrum vininum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2. skóginn?', 'other').strip()) == 'ætlarðu að höggva annan skóginn ?'
    assert re.sub("\s+", " ", normalize('það var 2. stóllinn þarna', 'other').strip()) == 'það var annar stóllinn þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. mannsins?', 'other').strip()) == 'ætlarðu til annars mannsins ?'
    # feminine singular
    assert normalize('2. konan', 'other').strip() == 'önnur konan'
    assert re.sub("\s+", " ", normalize('það var talað um 2. konuna', 'other').strip()) == 'það var talað um aðra konuna'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. vinkonunni', 'other').strip()) == 'ég fékk gjöf frá annarri vinkonunni'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. konunnar?', 'other').strip()) == 'ætlarðu til annarrar konunnar ?'
    # neutral singular
    assert normalize('2. borðið', 'other').strip() == 'annað borðið'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2. tréð?', 'other').strip()) == 'ætlarðu að höggva annað tréð ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. barninu', 'other').strip()) == 'ég fékk gjöf frá öðru barninu'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. landsins?', 'other').strip()) == 'ætlarðu til annars landsins ?'

    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. vinunum', 'other').strip()) == 'ég fékk gjöf frá öðrum vinunum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2. skógana?', 'other').strip()) == 'ætlarðu að höggva aðra skógana ?'
    assert re.sub("\s+", " ", normalize('það voru 2. stólarnir þarna', 'other').strip()) == 'það voru aðrir stólarnir þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. mannanna?', 'other').strip()) == 'ætlarðu til annarra mannanna ?'
    # feminine singular
    assert normalize('2. konurnar', 'other').strip() == 'aðrar konurnar'
    assert re.sub("\s+", " ", normalize('það var talað um 2. konurnar', 'other').strip()) == 'það var talað um aðrar konurnar'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. vinkonunum', 'other').strip()) == 'ég fékk gjöf frá öðrum vinkonunum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. kvennanna?', 'other').strip()) == 'ætlarðu til annarra kvennanna ?'
    # neutral singular
    assert normalize('2. borðin', 'other').strip() == 'önnur borðin'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2. trén?', 'other').strip()) == 'ætlarðu að höggva önnur trén ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2. börnunum', 'other').strip()) == 'ég fékk gjöf frá öðrum börnunum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2. landanna?', 'other').strip()) == 'ætlarðu til annarra landanna ?'


def test_no_context_ord():
    assert re.sub("\s+", " ", normalize('hún var 1. þarna', 'other').strip()) == 'hún var fyrsta þarna'
    assert re.sub("\s+", " ", normalize('þetta gerðist 2. þess mánaðar', 'other').strip()) == 'þetta gerðist annan þess mánaðar'
    assert re.sub("\s+", " ", normalize('hún var 3. í röðinni', 'other').strip()) == 'hún var þriðja í röðinni'
    assert re.sub("\s+", " ", normalize('hún var 4. í röðinni', 'other').strip()) == 'hún var fjórða í röðinni'
    assert re.sub("\s+", " ", normalize('hún var 1.', 'other').strip()) == 'hún var fyrsta'
    assert re.sub("\s+", " ", normalize('þetta gerðist 2.', 'other').strip()) == 'þetta gerðist annan'
    #assert re.sub("\s+", " ", normalize('hann var 1. þarna', 'other').strip()) == 'hann var fyrsti þarna'
    #assert re.sub("\s+", " ", normalize('hann var 3. þarna', 'other').strip()) == 'hann var þriðji þarna'
    #assert re.sub("\s+", " ", normalize('hann var 4. þarna', 'other').strip()) == 'hann var fjórði þarna'
    assert re.sub("\s+", " ", normalize('hann var 1. barnabarnið', 'other').strip()) == 'hann var fyrsta barnabarnið'
    #assert re.sub("\s+", " ", normalize('hann var 2.', 'other').strip()) == 'hann var annar'
    assert re.sub("\s+", " ", normalize('hún var 1.', 'other').strip()) == 'hún var fyrsta'
    #assert re.sub("\s+", " ", normalize('hún var 2.', 'other').strip()) == 'hún var önnur'
    assert re.sub("\s+", " ", normalize('það var 1.', 'other').strip()) == 'það var fyrsta'
    #assert re.sub("\s+", " ", normalize('það var 2.', 'other').strip()) == 'það var annað'
    #assert re.sub("\s+", " ", normalize('þeir voru 1.', 'other').strip()) == 'þeir voru fyrstu'
    #assert re.sub("\s+", " ", normalize('þeir voru 2.', 'other').strip()) == 'þeir voru aðrir'
    #assert re.sub("\s+", " ", normalize('þær voru 1.', 'other').strip()) == 'þær voru fyrstu'
    #assert re.sub("\s+", " ", normalize('þær voru 2.', 'other').strip()) == 'þær voru aðrar'
    #assert re.sub("\s+", " ", normalize('þau voru 1.', 'other').strip()) == 'þau voru fyrstu'
    #assert re.sub("\s+", " ", normalize('þau voru 2.', 'other').strip()) == 'þau voru önnur'


def test_onehundred_ord():
    assert re.sub("\s+", " ", normalize('ég á 0. vininn', 'other').strip()) == 'ég á núllta vininn'
    # ATHUGA assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2100. vininum', 'other').strip()) == 'ég fékk gjöf frá tvö þúsund og eitt hundraðasta vininum' - eitt hundrað vininum
    assert re.sub("\s+", " ", normalize('þetta var 104. konan', 'other').strip()) == 'þetta var hundraðasta og fjórða konan'
    assert re.sub("\s+", " ", normalize('þetta var 3001. konan', 'other').strip()) == 'þetta var þrjú þúsundasta og fyrsta konan'
    # ATHUGA assert re.sub("\s+", " ", normalize('næst er 119. hálfleikur', 'other').strip()) == 'næst er hundraðasti og nítjándi hálfleikur' - hundraðasti og hálfleikur
    assert re.sub("\s+", " ", normalize('21019. mennirnir', 'other').strip()) == 'tuttugu og eitt þúsundustu og nítjándu mennirnir'

def test_dozens_ord():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 21. vininum', 'other').strip()) == 'ég fékk gjöf frá tuttugasta og fyrsta vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 32. vinunum', 'other').strip()) == 'ég fékk gjöf frá þrítugustu og öðrum vinunum'
    assert re.sub("\s+", " ", normalize('þetta voru 43. konurnar', 'other').strip()) == 'þetta voru fertugustu og þriðju konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 54. konurnar', 'other').strip()) == 'þetta voru fimmtugustu og fjórðu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 64. börnin', 'other').strip()) == 'þetta voru sextugustu og fjórðu börnin'
    assert re.sub("\s+", " ", normalize('næst eru 70. grömmin', 'other').strip()) == 'næst eru sjötugustu grömmin'
    #assert re.sub("\s+", " ", normalize('næst eru 85. kg', 'other').strip()) == 'næst eru áttugustu og fimmtu kílóin'
    assert re.sub("\s+", " ", normalize('95. mennirnir', 'other').strip()) == 'nítugustu og fimmtu mennirnir'

def test_hundreds_thousands_ord():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 211. vinunum', 'other').strip()) == 'ég fékk gjöf frá tvö hundruðustu og elleftu vinunum'
    assert re.sub("\s+", " ", normalize('þetta var 302. vinurinn', 'other').strip()) == 'þetta var þrjú hundruðasti og annar vinurinn'
    assert re.sub("\s+", " ", normalize('þetta voru 400. konurnar', 'other').strip()) == 'þetta voru fjögur hundruðustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 2014. konurnar', 'other').strip()) == 'þetta voru tvö þúsundustu og fjórtándu konurnar'
    assert re.sub("\s+", " ", normalize('þetta var 3001. konan', 'other').strip()) == 'þetta var þrjú þúsundasta og fyrsta konan'
    assert re.sub("\s+", " ", normalize('4005. börnin týndust', 'other').strip()) == 'fjögur þúsundustu og fimmtu börnin týndust'
    assert re.sub("\s+", " ", normalize('5005. barnið týndist', 'other').strip()) == 'fimm þúsundasta og fimmta barnið týndist'
    assert re.sub("\s+", " ", normalize('6012. börnin fundust', 'other').strip()) == 'sex þúsundustu og tólftu börnin fundust'

def test_tens_ord():
    assert re.sub("\s+", " ", normalize('1106. vinirnir', 'other').strip()) == 'ellefu hundruðustu og sjöttu vinirnir'# - eitt þúsund ellefu hundruðustu og sjöttu vinirnir
    assert re.sub("\s+", " ", normalize('1200. börnin', 'other').strip()) == 'tólf hundruðustu börnin'
    assert re.sub("\s+", " ", normalize('1206. börnin', 'other').strip()) == 'tólf hundruðustu og sjöttu börnin'
    assert re.sub("\s+", " ", normalize('1511. konurnar', 'other').strip()) == 'fimmtán hundruðustu og elleftu konurnar'
    assert re.sub("\s+", " ", normalize('16014. ungmennin', 'other').strip()) == 'sextán þúsundustu og fjórtándu ungmennin'# + sex þúsundustu og fjórtándu ungmennin
    # assert re.sub("\s+", " ", normalize('1800. kr.', 'other').strip()) == 'átján hundruðustu krónurnar'
    assert re.sub("\s+", " ", normalize('árið var 1923.', 'other').strip()) == 'árið var nítján hundruð tuttugasta og þriðja'
    # assert re.sub("\s+", " ", normalize('karlinn var 1902. í mark', 'other').strip()) == 'karlinn var nítján hundruðasti og annar í mark'
    # assert re.sub("\s+", " ", normalize('konan var 1902. í mark', 'other').strip()) == 'konan var nítján hundruðasta og önnur í mark'
    # assert re.sub("\s+", " ", normalize('hann var 4.', 'other').strip()) == 'hann var fjórði'
    assert re.sub("\s+", " ", normalize('hún var 5.', 'other').strip()) == 'hún var fimmta'


def test_million_ord():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10009. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsundasta og níunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10014. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsundasta og fjórtánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10019. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsundasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10109. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsund eitt hundraðasta og níunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10114. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsund eitt hundraðasta og fjórtánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10119. vininum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsund eitt hundraðasta og nítjánda vininum' 
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11009. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsundasta og níunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11014. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsundasta og fjórtánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11019. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsundasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11109. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund eitt hundraðasta og níunda vininum'

    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11414. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund fjögur hundruðasta og fjórtánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11419. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund fjögur hundruðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11409. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund fjögur hundruðasta og níunda vininum' 
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11114. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund eitt hundraðasta og fjórtánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11119. vininum', 'other').strip()) == 'ég fékk gjöf frá ellefu þúsund eitt hundraðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12009. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsundasta og níunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12119. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsund eitt hundraðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12019. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsundasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12219. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsund tvö hundruðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12519. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsund fimm hundruðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('þetta voru 2.000.003. konurnar', 'other').strip()) == 'þetta voru tvímilljónustu og þriðju konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 2.000.013. konurnar', 'other').strip()) == 'þetta voru tvímilljónustu og þrettándu konurnar'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 219. vininum', 'other').strip()) == 'ég fékk gjöf frá tvö hundruðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 109. vininum', 'other').strip()) == 'ég fékk gjöf frá hundraðasta og níunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 110. vininum', 'other').strip()) == 'ég fékk gjöf frá hundraðasta og tíunda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 119. vininum', 'other').strip()) == 'ég fékk gjöf frá hundraðasta og nítjánda vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 119 vinum', 'other').strip()) == 'ég fékk gjöf frá hundrað og nítján vinum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 103. vininum', 'other').strip()) == 'ég fékk gjöf frá hundraðasta og þriðja vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 120. vininum', 'other').strip()) == 'ég fékk gjöf frá hundrað og tuttugasta vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 204. vininum', 'other').strip()) == 'ég fékk gjöf frá tvö hundruðasta og fjórða vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12020. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsund og tuttugasta vininum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 19. vininum', 'other').strip()) == 'ég fékk gjöf frá nítjánda vininum'
    assert re.sub("\s+", " ", normalize('þetta voru 2.000.018. konurnar', 'other').strip()) == 'þetta voru tvímilljónustu og átjándu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 100.010. konurnar', 'other').strip()) == 'þetta voru hundrað þúsundustu og tíundu konurnar'


def test_dozen_million_ord():
    assert re.sub("\s+", " ", normalize('þetta voru 14002. konurnar', 'other').strip()) == 'þetta voru fjórtán þúsundustu og aðrar konurnar'# + þetta voru fjögur þúsundustu og aðrar konurnar
    #assert re.sub("\s+", " ", normalize('þetta var 20010. konan', 'other').strip()) == 'þetta var tuttugu þúsundasta og tíunda konan'
    #assert re.sub("\s+", " ", normalize('þetta voru 40.004. konurnar', 'other').strip()) == 'þetta voru fjörutíu þúsundustu og fjórðu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 45.425. konurnar', 'other').strip()) == 'þetta voru fjörutíu og fimm þúsund fjögur hundruð tuttugustu og fimmtu konurnar'

def test_hundreds_million_ord():
    assert re.sub("\s+", " ", normalize('þetta voru 200.000. konurnar', 'other').strip()) == 'þetta voru tvö hundruðþúsundustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 200.004. konurnar', 'other').strip()) == 'þetta voru tvö hundruðþúsundustu og fjórðu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 300.002. konurnar', 'other').strip()) == 'þetta voru þrjú hundruðþúsundustu og aðrar konurnar'

def test_ordinal_big():
    assert normalize('100.001.000.000. borðin', 'other').strip() == 'hundrað milljarðar og einmilljónustu borðin'
    assert normalize('200.004.000.000. borðin', 'other').strip() == 'tvö hundruð milljarðar og fermilljónustu borðin'
    assert normalize('321.324.123. borðið', 'other').strip() == 'þrjú hundruð tuttugu og ein milljón þrjú hundruð tuttugu og fjögur þúsund eitt hundrað tuttugasta og þriðja borðið'

