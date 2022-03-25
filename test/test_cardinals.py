from regina_normalizer import normalizer
from regina_normalizer import tokenizer
import pytest
import re


def normalize(text, domain):
    return normalizer.input_string(text, domain)


def test_one_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1 vini', 'other').strip()) == 'ég fékk gjöf frá einum vini'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 1 skóg?', 'other').strip()) == 'ætlarðu að höggva einn skóg ?'
    assert re.sub("\s+", " ", normalize('það var 1 stóll þarna', 'other').strip()) == 'það var einn stóll þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 1 manns?', 'other').strip()) == 'ætlarðu til eins manns ?'
    # feminine singular
    assert normalize('1 kona', 'other').strip() == 'ein kona'
    assert re.sub("\s+", " ", normalize('það var talað um 1 konu', 'other').strip()) == 'það var talað um eina konu'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1 vinkonu', 'other').strip()) == 'ég fékk gjöf frá einni vinkonu'
    assert re.sub("\s+", " ", normalize('ætlarðu til 1 konu?', 'other').strip()) == 'ætlarðu til einnar konu ?'
    # neutral singular
    assert normalize('1 borð', 'other').strip() == 'eitt borð'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 1 tré?', 'other').strip()) == 'ætlarðu að höggva eitt tré ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 1 barni', 'other').strip()) == 'ég fékk gjöf frá einu barni'
    assert re.sub("\s+", " ", normalize('ætlarðu til 1 lands?', 'other').strip()) == 'ætlarðu til eins lands ?'

def test_two_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2 vinum', 'other').strip()) == 'ég fékk gjöf frá tveimur vinum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2 skóga?', 'other').strip()) == 'ætlarðu að höggva tvo skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 2 stólar þarna', 'other').strip()) == 'það voru tveir stólar þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2 manna?', 'other').strip()) == 'ætlarðu til tveggja manna ?'
    # feminine singular
    assert normalize('2 konur', 'other').strip() == 'tvær konur'
    assert re.sub("\s+", " ", normalize('það var talað um 2 konur', 'other').strip()) == 'það var talað um tvær konur'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2 vinkonum', 'other').strip()) == 'ég fékk gjöf frá tveimur vinkonum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2 kvenna?', 'other').strip()) == 'ætlarðu til tveggja kvenna ?'
    # neutral singular
    assert normalize('2 borð', 'other').strip() == 'tvö borð'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 2 tré?', 'other').strip()) == 'ætlarðu að höggva tvö tré ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2 börnum', 'other').strip()) == 'ég fékk gjöf frá tveimur börnum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 2 landa?', 'other').strip()) == 'ætlarðu til tveggja landa ?'

def test_three_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 3 vinum', 'other').strip()) == 'ég fékk gjöf frá þremur vinum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 3 skóga?', 'other').strip()) == 'ætlarðu að höggva þrjá skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 3 stólar þarna', 'other').strip()) == 'það voru þrír stólar þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 3 manna?', 'other').strip()) == 'ætlarðu til þriggja manna ?'
    # feminine singular
    assert normalize('3 konur', 'other').strip() == 'þrjár konur'
    assert re.sub("\s+", " ", normalize('það var talað um 3 konur', 'other').strip()) == 'það var talað um þrjár konur'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 3 vinkonum', 'other').strip()) == 'ég fékk gjöf frá þremur vinkonum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 3 kvenna?', 'other').strip()) == 'ætlarðu til þriggja kvenna ?'
    # neutral singular
    assert normalize('3 borð', 'other').strip() == 'þrjú borð'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 3 tré?', 'other').strip()) == 'ætlarðu að höggva þrjú tré ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 3 börnum', 'other').strip()) == 'ég fékk gjöf frá þremur börnum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 3 landa?', 'other').strip()) == 'ætlarðu til þriggja landa ?'

def test_four_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 4 vinum', 'other').strip()) == 'ég fékk gjöf frá fjórum vinum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 4 skóga?', 'other').strip()) == 'ætlarðu að höggva fjóra skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 4 stólar þarna', 'other').strip()) == 'það voru fjórir stólar þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 4 manna?', 'other').strip()) == 'ætlarðu til fjögurra manna ?'
    # feminine singular
    assert normalize('4 konur', 'other').strip() == 'fjórar konur'
    assert re.sub("\s+", " ", normalize('það var talað um 4 konur', 'other').strip()) == 'það var talað um fjórar konur'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 4 vinkonum', 'other').strip()) == 'ég fékk gjöf frá fjórum vinkonum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 4 kvenna?', 'other').strip()) == 'ætlarðu til fjögurra kvenna ?'
    # neutral singular
    assert normalize('4 borð', 'other').strip() == 'fjögur borð'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 4 tré?', 'other').strip()) == 'ætlarðu að höggva fjögur tré ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 4 börnum', 'other').strip()) == 'ég fékk gjöf frá fjórum börnum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 4 landa?', 'other').strip()) == 'ætlarðu til fjögurra landa ?'

def test_no_context_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('hún var 1 þarna', 'other').strip()) == 'hún var eitt þarna'
    assert re.sub("\s+", " ", normalize('þau voru 2 þarna', 'other').strip()) == 'þau voru tvö þarna'
    assert re.sub("\s+", " ", normalize('þau voru 3 þarna', 'other').strip()) == 'þau voru þrjú þarna'
    assert re.sub("\s+", " ", normalize('þau voru 4 þarna', 'other').strip()) == 'þau voru fjögur þarna'

def test_other_ones_card():
	# masculine singular
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 5 vinum', 'other').strip()) == 'ég fékk gjöf frá fimm vinum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 6 skóga?', 'other').strip()) == 'ætlarðu að höggva sex skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 7 stólar þarna', 'other').strip()) == 'það voru sjö stólar þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 8 manna?', 'other').strip()) == 'ætlarðu til átta manna ?'
    # feminine singular
    assert normalize('9 konur', 'other').strip() == 'níu konur'
    assert re.sub("\s+", " ", normalize('það var talað um 10 konur', 'other').strip()) == 'það var talað um tíu konur'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 11 vinkonum', 'other').strip()) == 'ég fékk gjöf frá ellefu vinkonum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 12 kvenna?', 'other').strip()) == 'ætlarðu til tólf kvenna ?'
    # neutral singular
    assert normalize('13 borð', 'other').strip() == 'þrettán borð'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 14 tré?', 'other').strip()) == 'ætlarðu að höggva fjórtán tré ?'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 15 börnum', 'other').strip()) == 'ég fékk gjöf frá fimmtán börnum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 16 landa?', 'other').strip()) == 'ætlarðu til sextán landa ?'

    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 17 vinum', 'other').strip()) == 'ég fékk gjöf frá sautján vinum'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 18 skóga?', 'other').strip()) == 'ætlarðu að höggva átján skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 19 stólar þarna', 'other').strip()) == 'það voru nítján stólar þarna'

def test_onehundred_card():
    assert re.sub("\s+", " ", normalize('ég á 0 vini', 'other').strip()) == 'ég á núll vini'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2101 vini', 'other').strip()) == 'ég fékk gjöf frá tvö þúsund eitt hundrað og einum vini'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 2120. vininum', 'other').strip()) == 'ég fékk gjöf frá tvö þúsund eitt hundrað og tuttugasta vininum'
    assert re.sub("\s+", " ", normalize('þetta voru 104 konur', 'other').strip()) == 'þetta voru hundrað og fjórar konur'
    assert re.sub("\s+", " ", normalize('þetta var 120. konan', 'other').strip()) == 'þetta var hundrað og tuttugasta konan'
    assert re.sub("\s+", " ", normalize('þetta var 3121. konan', 'other').strip()) == 'þetta var þrjú þúsund eitt hundrað tuttugasta og fyrsta konan'
    assert re.sub("\s+", " ", normalize('næst eru 100,6 grömm', 'other').strip()) == 'næst eru hundrað komma sex grömm'
    assert re.sub("\s+", " ", normalize('næst er 121. hálfleikur', 'other').strip()) == 'næst er hundrað tuttugasti og fyrsti hálfleikur'
    # if we write "21004" then it will say "tveir einn núll núll fjórir", it has to have a thousands separator for it to expand correctly
    assert re.sub("\s+", " ", normalize('21.004 menn', 'other').strip()) == 'tuttugu og eitt þúsund og fjórir menn'
    assert re.sub("\s+", " ", normalize('21.020. mennirnir', 'other').strip()) == 'tuttugu og eitt þúsund og tuttugustu mennirnir'
    assert re.sub("\s+", " ", normalize('21.304 menn', 'other').strip()) == 'tuttugu og eitt þúsund þrjú hundruð og fjórir menn'
    assert re.sub("\s+", " ", normalize('1000 kr.', 'other').strip()) == 'þúsund krónur .'

def test_dozens_card():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 21 vini', 'other').strip()) == 'ég fékk gjöf frá tuttugu og einum vini'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 32 vinum', 'other').strip()) == 'ég fékk gjöf frá þrjátíu og tveimur vinum'
    assert re.sub("\s+", " ", normalize('þetta voru 43 konur', 'other').strip()) == 'þetta voru fjörutíu og þrjár konur'
    assert re.sub("\s+", " ", normalize('þetta voru 54 konur', 'other').strip()) == 'þetta voru fimmtíu og fjórar konur'
    assert re.sub("\s+", " ", normalize('þetta voru 64 börn', 'other').strip()) == 'þetta voru sextíu og fjögur börn'
    assert re.sub("\s+", " ", normalize('næst eru 70,4 grömm', 'other').strip()) == 'næst eru sjötíu komma fjögur grömm'
    assert re.sub("\s+", " ", normalize('næst eru 85,2 kg', 'other').strip()) == 'næst eru áttatíu og fimm komma tvö kíló'
    assert re.sub("\s+", " ", normalize('95 menn', 'other').strip()) == 'níutíu og fimm menn'

def test_hundreds_thousands_card():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 211 vinum', 'other').strip()) == 'ég fékk gjöf frá tvö hundruð og ellefu vinum'
    assert re.sub("\s+", " ", normalize('þetta var 330. vinurinn', 'other').strip()) == 'þetta var þrjú hundruð og þrítugasti vinurinn'
    assert re.sub("\s+", " ", normalize('þetta voru 400,3 konur', 'other').strip()) == 'þetta voru fjögur hundruð komma þrjár konur'
    assert re.sub("\s+", " ", normalize('þetta voru 2554 konur', 'other').strip()) == 'þetta voru tvö þúsund fimm hundruð fimmtíu og fjórar konur'
    assert re.sub("\s+", " ", normalize('þetta var 3121. konan', 'other').strip()) == 'þetta var þrjú þúsund eitt hundrað tuttugasta og fyrsta konan'
    assert re.sub("\s+", " ", normalize('4005 börn týndust', 'other').strip()) == 'fjögur þúsund og fimm börn týndust'
    assert re.sub("\s+", " ", normalize('5005. barnið týndist', 'other').strip()) == 'fimm þúsundasta og fimmta barnið týndist'
    assert re.sub("\s+", " ", normalize('6022 börn fundust', 'other').strip()) == 'sex þúsund tuttugu og tvö börn fundust'

def test_tens_card():
    assert re.sub("\s+", " ", normalize('1106 vinir', 'other').strip()) == 'ellefu hundruð og sex vinir'
    assert re.sub("\s+", " ", normalize('1200,5 börn', 'other').strip()) == 'tólf hundruð komma fimm börn'
    assert re.sub("\s+", " ", normalize('1532 konur', 'other').strip()) == 'fimmtán hundruð þrjátíu og tvær konur'
    assert re.sub("\s+", " ", normalize('16.124 ungmenni', 'other').strip()) == 'sextán þúsund eitt hundrað tuttugu og fjögur ungmenni'
    assert re.sub("\s+", " ", normalize('1800 kr.', 'other').strip()) == 'átján hundruð krónur .'
    assert re.sub("\s+", " ", normalize('árið var 1923', 'other').strip()) == 'árið var nítján hundruð tuttugu og þrjú'
    assert re.sub("\s+", " ", normalize('árið var 1922', 'other').strip()) == 'árið var nítján hundruð tuttugu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 1903', 'other').strip()) == 'árið var nítján hundruð og þrjú'
    assert re.sub("\s+", " ", normalize('árið var 1874', 'other').strip()) == 'árið var átján hundruð sjötíu og fjögur'
    assert re.sub("\s+", " ", normalize('árið var 1873', 'other').strip()) == 'árið var átján hundruð sjötíu og þrjú'
    assert re.sub("\s+", " ", normalize('11.005 menn', 'other').strip()) == 'ellefu þúsund og fimm menn'
    assert re.sub("\s+", " ", normalize('14.020. maðurinn', 'other').strip()) == 'fjórtán þúsund og tuttugasti maðurinn'
    assert re.sub("\s+", " ", normalize('17.405 menn', 'other').strip()) == 'sautján þúsund fjögur hundruð og fimm menn'

def test_million_card():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10500 vinum', 'other').strip()) == 'ég fékk gjöf frá tíu þúsund og fimm hundruð vinum'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 12020. vininum', 'other').strip()) == 'ég fékk gjöf frá tólf þúsund og tuttugasta vininum'
    assert re.sub("\s+", " ", normalize('þetta voru 30104 konur', 'other').strip()) == 'þetta voru þrjátíu þúsund eitt hundrað og fjórar konur'
    assert re.sub("\s+", " ", normalize('þetta voru 2.100.020 konur', 'other').strip()) == 'þetta voru tvær milljónir eitt hundrað þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 100.020 konur', 'other').strip()) == 'þetta voru hundrað þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 2.100.020. konurnar', 'other').strip()) == 'þetta voru tvær milljónir eitt hundrað þúsund og tuttugustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 100.020. konurnar', 'other').strip()) == 'þetta voru hundrað þúsund og tuttugustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 2.100.020. konurnar', 'other').strip()) == 'þetta voru tvær milljónir eitt hundrað þúsund og tuttugustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 100.020. konurnar', 'other').strip()) == 'þetta voru hundrað þúsund og tuttugustu konurnar'
    assert re.sub("\s+", " ", normalize('þetta voru 2.130.020 konur', 'other').strip()) == 'þetta voru tvær milljónir eitt hundrað og þrjátíu þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 130.020 konur', 'other').strip()) == 'þetta voru hundrað og þrjátíu þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 2.135.020 konur', 'other').strip()) == 'þetta voru tvær milljónir eitt hundrað þrjátíu og fimm þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 135.020 konur', 'other').strip()) == 'þetta voru hundrað þrjátíu og fimm þúsund og tuttugu konur'


def test_dozen_million_card():
    assert re.sub("\s+", " ", normalize('þetta voru 14002 konur', 'other').strip()) == 'þetta voru fjórtán þúsund og tvær konur'
    assert re.sub("\s+", " ", normalize('þetta var 20020. konan', 'other').strip()) == 'þetta var tuttugu þúsund og tuttugasta konan'
    assert re.sub("\s+", " ", normalize('þetta voru 40.520 konur', 'other').strip()) == 'þetta voru fjörutíu þúsund fimm hundruð og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 45.425 konur', 'other').strip()) == 'þetta voru fjörutíu og fimm þúsund fjögur hundruð tuttugu og fimm konur'

def test_hundreds_million_card():
    assert re.sub("\s+", " ", normalize('þetta voru 200.520 konur', 'other').strip()) == 'þetta voru tvö hundruð þúsund fimm hundruð og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 200.020 konur', 'other').strip()) == 'þetta voru tvö hundruð þúsund og tuttugu konur'
    assert re.sub("\s+", " ", normalize('þetta voru 220000 konur', 'other').strip()) == 'þetta voru tvö hundruð og tuttugu þúsund konur'
    assert re.sub("\s+", " ", normalize('þetta voru 225.532 konur', 'other').strip()) == 'þetta voru tvö hundruð tuttugu og fimm þúsund fimm hundruð þrjátíu og tvær konur'


def test_cardinal_big():
    assert normalize('100.321.324.123 borð', 'other').strip() == 'hundrað milljarðar þrjú hundruð tuttugu og ein milljón þrjú hundruð tuttugu og fjögur þúsund eitt hundrað tuttugu og þrjú borð'
    assert normalize('321.324.123 borð', 'other').strip() == 'þrjú hundruð tuttugu og ein milljón þrjú hundruð tuttugu og fjögur þúsund eitt hundrað tuttugu og þrjú borð'

def test_neutral_card():
    assert re.sub("\s+", " ", normalize('það voru 22 konur þarna', 'other').strip()) == 'það voru tuttugu og tvær konur þarna'
    assert re.sub("\s+", " ", normalize('það voru 1922 menn þarna', 'other').strip()) == 'það voru nítján hundruð tuttugu og tveir menn þarna'
    assert re.sub("\s+", " ", normalize('það voru 1873 börn þarna', 'other').strip()) == 'það voru átján hundruð sjötíu og þrjú börn þarna'
    assert re.sub("\s+", " ", normalize('árið var 1903', 'other').strip()) == 'árið var nítján hundruð og þrjú'
    assert re.sub("\s+", " ", normalize('árið var 1912', 'other').strip()) == 'árið var nítján hundruð og tólf'
    assert re.sub("\s+", " ", normalize('árið var 1922', 'other').strip()) == 'árið var nítján hundruð tuttugu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 1920', 'other').strip()) == 'árið var nítján hundruð og tuttugu'
    assert re.sub("\s+", " ", normalize('árið var 1927', 'other').strip()) == 'árið var nítján hundruð tuttugu og sjö'
    assert re.sub("\s+", " ", normalize('árið var 1722', 'other').strip()) == 'árið var sautján hundruð tuttugu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 1933', 'other').strip()) == 'árið var nítján hundruð þrjátíu og þrjú'
    assert re.sub("\s+", " ", normalize('árið var 1942', 'other').strip()) == 'árið var nítján hundruð fjörutíu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 1951', 'other').strip()) == 'árið var nítján hundruð fimmtíu og eitt'
    assert re.sub("\s+", " ", normalize('árið var 1874', 'other').strip()) == 'árið var átján hundruð sjötíu og fjögur'
    assert re.sub("\s+", " ", normalize('árið var 1989', 'other').strip()) == 'árið var nítján hundruð áttatíu og níu'
    assert re.sub("\s+", " ", normalize('barnið var 3 ára', 'other').strip()) == 'barnið var þriggja ára'
    assert re.sub("\s+", " ", normalize('árið var 3 þegar ég var 4 ára', 'other').strip()) == 'árið var þrjú þegar ég var fjögurra ára'
    assert re.sub("\s+", " ", normalize('árið var 22', 'other').strip()) == 'árið var tuttugu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 11.722', 'other').strip()) == 'árið var ellefu þúsund sjö hundruð tuttugu og tvö'
    assert re.sub("\s+", " ", normalize('árið var 933', 'other').strip()) == 'árið var níu hundruð þrjátíu og þrjú'
    assert re.sub("\s+", " ", normalize('árið var 42 en ég var ekki fædd', 'other').strip()) == 'árið var fjörutíu og tvö en ég var ekki fædd'
    assert re.sub("\s+", " ", normalize('árið var 251', 'other').strip()) == 'árið var tvö hundruð fimmtíu og eitt'
    assert re.sub("\s+", " ", normalize('árið var 174', 'other').strip()) == 'árið var hundrað sjötíu og fjögur'

