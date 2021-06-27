from reginafolder import regina as r
import pytest
import re


def normalize(sent, domain):
    return r.handle_input(sent, domain)

def test_prehelp():
    # masculine singular
    assert re.sub("\s+", " ", normalize('hún verður 2ja ára næsta sumar :)', 'other').strip()) == 'hún verður tveggja ára næsta sumar :)'
    assert re.sub("\s+", " ", normalize('hann er 3ja ára', 'other').strip()) == 'hann er þriggja ára'
    assert re.sub("\s+", " ", normalize('hvort viltu 4ða, 5ta eða 6ta valkostinn?', 'other').strip()) == 'hvort viltu fjórða, fimmta eða sjötta valkostinn?'
    assert re.sub("\s+", " ", normalize('þetta var ekki 7di valkosturinn, kannski 8di eða 9di', 'other').strip()) == 'þetta var ekki sjöundi valkosturinn, kannski áttundi eða níundi'
    assert re.sub("\s+", " ", normalize('tökum orðið 14EP30 í sundur', 'other').strip()) == 'tökum orðið fjórtán E P þrjátíu í sundur'
    assert re.sub("\s+", " ", normalize('það er 9,1°C', 'other').strip()) == 'það er níu komma ein gráða á selsíus'
    assert re.sub("\s+", " ", normalize('85,4% eru bólusett', 'other').strip()) == 'áttatíu og fimm komma fjögur prósent eru bólusett'
    assert re.sub("\s+", " ", normalize('hún er fædd 28.12.1995', 'other').strip()) == 'hún er fædd tuttugasta og áttunda tólfta nítján hundruð níutíu og fimm'
    assert re.sub("\s+", " ", normalize('símanúmerið er 697-3245', 'other').strip()) == 'símanúmerið er sex níu sjö <sil> þrír tveir fjórir fimm'

def test_abbreviations():
    assert re.sub("\s+", " ", normalize('5. gr. , 4. mgr. , 6. nmgr.', 'other').strip()) == 'fimmta grein , fjórða málsgrein , sjötta neðanmálsgrein'
    assert re.sub("\s+", " ", normalize('Innsk. blm. árið 45 f.o.t. eða f.Kr. eða ca 21 e.Kr.', 'other').strip()) == 'innskot blaðamanns árið fjörutíu og fimm fyrir okkar tímatal eða fyrir Krist eða sirka tuttugu og eitt eftir Krist'
    assert re.sub("\s+", " ", normalize('5. sek. , 6. mín.', 'other').strip()) == 'fimmta sekúnda , sjötta mínúta'
    assert re.sub("\s+", " ", normalize('hann var með 24/14 frák. , 4 stoðs.', 'sport').strip()) == 'hann var með tuttugu og fjögur <sil> fjórtán fráköst , fjórar stoðsendingar'
    assert re.sub("\s+", " ", normalize('5. apr. nk. er sýning frá Bland ehf. og það er atr. þar', 'other').strip()) == 'fimmta apríl næstkomandi er sýning frá Bland E H F og það er atriði þar'
    assert re.sub("\s+", " ", normalize('ATH að það má ekki klappa í f.hl. en s.hl. er í lagi', 'other').strip()) == 'athugið að það má ekki klappa í fyrri hluti en síðari hluti er í lagi'
    #assert re.sub("\s+", " ", normalize('ATH að það má ekki klappa í f.hl. en s.hl. er í lagi', 'other').strip()) == 'athugið að það má ekki klappa í fyrri hluta en síðari hluti er í lagi'
    assert re.sub("\s+", " ", normalize('þú getur talið þetta frá bls hundrað', 'other').strip()) == 'þú getur talið þetta frá blaðsíða hundrað'
    #assert re.sub("\s+", " ", normalize('þú getur talið þetta frá bls hundrað', 'other').strip()) == 'þú getur talið þetta frá blaðsíðu hundrað'
    assert re.sub("\s+", " ", normalize('þetta er a.n.l. frh af síðustu bók', 'other').strip()) == 'þetta er að nokkru leyti framhald af síðustu bók'
    assert re.sub("\s+", " ", normalize('hún er með b.sc. í mannfræði og m.sc. í ritstjórn ( e. editorial studies )', 'other').strip()) == 'hún er með B S C í mannfræði og M S C í ritstjórn (enska editorial studies )'
    assert re.sub("\s+", " ", normalize('það er e.k. rof , etv e-ð skrítið í gangi', 'other').strip()) == 'það er einhvers konar rof , ef til vill eitthvað skrítið í gangi'
    assert re.sub("\s+", " ", normalize('það er e-s konar rof , grf að það hafi komið e-ju skrítnu í gang', 'other').strip()) == 'það er einhvers konar rof , gerum ráð fyrir að það hafi komið einhverju skrítnu í gang'
    assert re.sub("\s+", " ", normalize('það er e-r maður þarna með e-n hund og í e-um jakka', 'other').strip()) == 'það er einhver maður þarna með einhvern hund og í einhverjum jakka'
    assert re.sub("\s+", " ", normalize('hann var með 24/14 frák. , 4 stoðs.', 'sport').strip()) == 'hann var með tuttugu og fjögur <sil> fjórtán fráköst , fjórar stoðsendingar'
    assert re.sub("\s+", " ", normalize('hvað er að gerast í frt ? fél. var stofnað', 'other').strip()) == 'hvað er að gerast í framtíð ? félag var stofnað'
    assert re.sub("\s+", " ", normalize('GMG þetta er ekki í lagi , er þessi maður hdl ? varla hrl.', 'other').strip()) == 'guð minn góður þetta er ekki í lagi , er þessi maður héraðsdómslögmaður ? varla hæstaréttarlögmaður'
    assert re.sub("\s+", " ", normalize('höf. þessarar bókar er hr. júlli jóns', 'other').strip()) == 'höfundur þessarar bókar er herra júlli jóns'
    assert re.sub("\s+", " ", normalize('hv. þingmaður er h.u.b. verstur í þetta starf', 'other').strip()) == 'háttvirtur þingmaður er hér um bil verstur í þetta starf'
    assert re.sub("\s+", " ", normalize('Kt: 180679-3529 , rn. 532-26-2342', 'other').strip()) == 'kennitala: einn átta núll sex sjö níu <sil> þrír fimm tveir níu , reikningsnúmer fimm þrír tveir <sil> tveir sex <sil> tveir þrír fjórir tveir'
    assert re.sub("\s+", " ", normalize('er blær í kk , kvk eða hk ?', 'other').strip()) == 'er blær í karlkyn , kvenkyn eða hvorugkyn ?'
    #assert re.sub("\s+", " ", normalize('er blær í kk , kvk eða hk ?', 'other').strip()) == 'er blær í karlkyni , kvenkyni eða hvorugkyni ?'
    assert re.sub("\s+", " ", normalize('ég er frá Sltjn en bjó í STHLM en svo KBH , hjólandi er lh.nt. , hjóluð er lh.þt.', 'other').strip()) == 'ég er frá Seltjarnarnes en bjó í Stokkhólmur en svo Kaupmannahöfn , hjólandi er lýsingarháttur nútíðar , hjóluð er lýsingarháttur þátíðar'
    #assert re.sub("\s+", " ", normalize('ég er frá sltjn. en bjó í STHLM en svo KBH , hjólandi er lh.nt. , hjóluð er lh.þt.', 'other').strip()) == 'ég er frá Seltjarnarnesi en bjó í stokkhólmi en svo kaupmannahöfn , hjólandi er lýsingarháttur nútíðar , hjóluð er lýsingarháttur þátíðar'
    assert re.sub("\s+", " ", normalize('rvk geothermal ltd er m.a. 500 m.y.s.', 'other').strip()) == 'Reykjavík geothermal limited er meðal annars fimm hundruð metra yfir sjávarmáli'
    assert re.sub("\s+", " ", normalize('það er m.a.s. sól m.t.t. roksins', 'other').strip()) == 'það er meira að segja sól með tilliti til roksins'
    assert re.sub("\s+", " ", normalize('þetta er m.ö.o. ekki í lagi m.v. að þetta voru 100 fm', 'other').strip()) == 'þetta er með öðrum orðum ekki í lagi miðað við að þetta voru hundrað fermetrar'
    assert re.sub("\s+", " ", normalize('Mfl KR er m.a.o. í svörtum búningum o.fl.', 'other').strip()) == 'meistaraflokkur K R er meðal annarra orða í svörtum búningum og fleira'
    assert re.sub("\s+", " ", normalize('þetta voru 3,3 m^3 , n.t.t. 6 m^2', 'sport').strip()) == 'þetta voru þrír komma þrír rúmmetrar , nánar tiltekið sex fermetrar'
    assert re.sub("\s+", " ", normalize('núv. ráðherra er nkl 44 ára , símanr er 843-1234 osfrv', 'other').strip()) == 'núverandi ráðherra er nákvæmlega fjörutíu og fjögurra ára , símanúmer er átta fjórir þrír <sil> einn tveir þrír fjórir og svo framvegis'
    assert re.sub("\s+", " ", normalize('Ritstj. þessa blaðs er líka rslm. o.m.fl. !', 'other').strip()) == 'ritstjóri þessa blaðs er líka rannsóknarlögreglumaður og margt fleira !'
    assert re.sub("\s+", " ", normalize('pk. bíður eftir þér , s: 432-2352', 'other').strip()) == 'pakki bíður eftir þér , sími: fjórir þrír tveir <sil> tveir þrír fimm tveir'
    assert re.sub("\s+", " ", normalize('það þarf appelsínur o.þ.h. , epli o.þ.u.l. , sbr. atburðum sl. þri', 'other').strip()) == 'það þarf appelsínur og þess háttar , epli og því um líkt , samanber atburðum síðastliðinn þriðjudag'
    #assert re.sub("\s+", " ", normalize('það þarf appelsínur o.þ.h. , epli o.þ.u.l. , sbr. atburðum sl. þri', 'other').strip()) == 'það þarf appelsínur og þess háttar , epli og því um líkt , samanber atburðum síðastliðins þriðjudags'
    assert re.sub("\s+", " ", normalize('skv. nýjustu tölum þarf að mynda sk. hjarðónæmi', 'other').strip()) == 'samkvæmt nýjustu tölum þarf að mynda svokallað hjarðónæmi'
    assert re.sub("\s+", " ", normalize('sgt pepper\'s lonely hearts club band er s.s. frábær plata', 'other').strip()) == 'sergeant pepper\'s lonely hearts club band er svo sem frábær plata'
    assert re.sub("\s+", " ", normalize('st. germain er lið í París , ég leik t.h. , t.a.m. fyrir Man Utd', 'other').strip()) == 'saint germain er lið í París , ég leik til hægri , til að mynda fyrir Man united'
    assert re.sub("\s+", " ", normalize('Samþ. liggur ekki fyrir í 4. tbl. , t.d. með 24,5% vsk', 'other').strip()) == 'samþykki liggur ekki fyrir í fjórða tölublað , til dæmis með tuttugu og fjögur komma fimm prósent virðisaukaskatt'
    #assert re.sub("\s+", " ", normalize('Samþ. liggur ekki fyrir í 4. tbl. , t.d. með 24,5% vsk', 'other').strip()) == 'samþykki liggur ekki fyrir í fjórða tölublaði , til dæmis með tuttugu og fjögurra komma fimm prósenta virðisaukaskatti'
    assert re.sub("\s+", " ", normalize('5. tl. t.v. , t.d. skjal þeas pappír', 'other').strip()) == 'fimmti tengiliður til vinstri , til dæmis skjal það er að segja pappír'
    assert re.sub("\s+", " ", normalize('það voru uþb allar uppl. aðgengilegar', 'sport').strip()) == 'það voru um það bil allar upplýsingar aðgengilegar'
    assert re.sub("\s+", " ", normalize('KR vs FH f.h. Hafnfirðinga', 'other').strip()) == 'K R versus F H fyrir hönd Hafnfirðinga'
    assert re.sub("\s+", " ", normalize('Dr Mikki jr. er mikka í þf. og þgf', 'other').strip()) == 'doktor Mikki junior er mikka í þolfall og þágufall'
    #assert re.sub("\s+", " ", normalize('Dr Mikki jr. er mikka í þf. , þgf. og ef.', 'other').strip()) == 'Doktor Mikki junior er mikka í þolfalli , þágufalli og eignarfalli'
    assert re.sub("\s+", " ", normalize('þetta verður að gerast þ.þ.a.a. þú biðjist afsökunar fyrir atburði þ.á.', 'other').strip()) == 'þetta verður að gerast þá og því aðeins að þú biðjist afsökunar fyrir atburði þessa árs'
    #assert re.sub("\s+", " ", normalize('koma er komið í þlt. , þ.a.l. kemur maðurinn', 'other').strip()) == 'koma er komið í þáliðin tíð , þar af leiðandi kemur maðurinn'
    #assert re.sub("\s+", " ", normalize('koma er komið í þ.lt.', 'other').strip()) == 'koma er komið í þáliðinni tíð'
    #assert re.sub("\s+", " ", normalize('það þarf appelsínur o.þ.h. , epli o.þ.u.l. , sbr. atburðum sl. þri', 'other').strip()) == 'það þarf appelsínur og þess háttar , epli og því um líkt , samanber atburðum síðastliðins þriðjudags'
    assert re.sub("\s+", " ", normalize('5. árg. , 3. útg. á ísl. og þ.h. , þ.e. ekki á prenti', 'other').strip()) == 'fimmti árgangur , þriðja útgáfa á íslenska og þess háttar , það er ekki á prenti'
    assert re.sub("\s+", " ", normalize('100 þús. manns búa þarna , mörg þús í RVK , þ.m.t. í úthverfum', 'other').strip()) == 'hundrað þúsund manns búa þarna , mörg þúsund í Reykjavík , þar með talið í úthverfum'
    assert re.sub("\s+", " ", normalize('ég gerði mistök þ.a. ég biðst afsökunar með það og þ.u.l. , þ.á m. fyrir ummæli mín um óákv.gr.', 'other').strip()) == 'ég gerði mistök þannig að ég biðst afsökunar með það og því um líkt , þar á meðal fyrir ummæli mín um óákveðinn greinir'
    #assert re.sub("\s+", " ", normalize('ég gerði mistök þ.a. ég biðst afsökunar með það og þ.u.l. , þ.á m. fyrir ummæli mín um óákv. gr.', 'other').strip()) == 'ég gerði mistök þannig að ég biðst afsökunar með það og því um líkt , þar á meðal fyrir ummæli mín um óákveðinn greini'

"""
def test_direction():
    #assert re.sub("\s+", " ", normalize('SV-átt 3 - 8 m/s . Léttskýjað A-til . Hiti 10 til 20 stig , hlýjast N- og A-lands .', 'other').strip()) == 'suðvestanátt þrír til átta metrar á sekúndu . Léttskýjað austan til . Hiti tíu til tuttugu stig , hlýjast norðan og austanlands .'
    assert re.sub("\s+", " ", normalize('SA-átt , NV-verðu , A-vert landið .', 'other').strip()) == 'suðaustanátt , norðvestanverðu , austanvert landið .'
    assert re.sub("\s+", " ", normalize('A-land , N-land , S-land , V-land .', 'other').strip()) == 'austurland , norðurland , suðurland , vesturland'
    assert re.sub("\s+", " ", normalize('SV-til , NV-átt , NA–verðu , SA-vert landið .', 'sport').strip()) == 'suðvestan til , norðvestanátt , norðaustanverðu , suðaustanvert landið .'
"""    
   