from regina_normalizer import normalizer
from regina_normalizer import tokenizer
import pytest
import re


def normalize(text, domain):
    return normalizer.input_string(text, domain)


def test_decimal_thousands():
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 10,1 vini', 'other').strip()) == 'ég fékk gjöf frá tíu komma einum vini'
    assert re.sub("\s+", " ", normalize('ætlarðu að höggva 0,02 skóga?', 'other').strip()) == 'ætlarðu að höggva núll komma núll tvo skóga ?'
    assert re.sub("\s+", " ", normalize('það voru 5,003 stólar þarna', 'other').strip()) == 'það voru fimm komma núll núll þrír stólar þarna'
    assert re.sub("\s+", " ", normalize('ætlarðu til 9,0004 manna?', 'other').strip()) == 'ætlarðu til níu komma núll núll núll fjögurra manna ?'
    assert normalize('0,00005 konur', 'other').strip() == 'núll komma núll núll núll núll fimm konur'
    assert re.sub("\s+", " ", normalize('það var talað um 0,000206 konur', 'other').strip()) == 'það var talað um núll komma núll núll núll tvær núll sex konur'
    assert re.sub("\s+", " ", normalize('ég fékk gjöf frá 0,0400037 vinkonum', 'other').strip()) == 'ég fékk gjöf frá núll komma núll fjórum núll núll núll þremur sjö vinkonum'
    assert re.sub("\s+", " ", normalize('ætlarðu til 0,0012350008 kvenna?', 'other').strip()) == 'ætlarðu til núll komma núll núll einnar tveggja þriggja fimm núll núll núll átta kvenna ?'
    assert normalize('1,942905161 borð', 'other').strip() == 'eitt komma níu fjögur tvö níu núll fimm eitt sex eitt borð'
    # decimals only work up to hundreds of thousands
    assert normalize('324.123,942905161 borð', 'other').strip() == 'þrjú hundruð tuttugu og fjögur þúsund eitt hundrað tuttugu og þrjú komma níu fjögur tvö níu núll fimm eitt sex eitt borð'

