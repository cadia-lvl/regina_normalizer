from number_patterns import *
# NUMBERS
ones_zip = [(einn, ' einn', "1"), (einum, ' einum', "1"), (eins, ' eins', "1"),
            (ein, ' ein', "1"), (eina, ' eina', "1"), (einni, ' einni', "1"), (einnar, ' einnar', "1"),
            (eitt, ' eitt', "1"), (einu, ' einu', "1"), (nonoun, ' eitt',  '1'),
            (tveir, ' tveir', "2"), (tvo, ' tvo', "2"), (tveimur, ' tveimur', "2"), (tveggja, ' tveggja', "2"),
            (tvær, ' tvær', "2"), (tvö, ' tvö', "2"), (nonoun, ' tvö', '2'),
            (þrír, ' þrír', "3"), (þrjá, ' þrjá', "3"), (þremur, ' þremur', "3"), (þriggja, ' þriggja', "3"),
            (þrjár, ' þrjár', "3"), (þrjú, ' þrjú', "3"), (nonoun, ' þrjú', '3'),
            (fjórir, ' fjórir', "4"), (fjóra, ' fjóra', "4"), (fjórum, ' fjórum', "4"), (fjögurra, ' fjögurra', "4"),
            (fjórar, ' fjórar', "4"), (fjögur, ' fjögur', "4"), (nonoun, ' fjögur', "4"),
            ('^.*$', ' fimm', '5'), ('^.*$', ' sex', '6'), ('^.*$', ' sjö', '7'), ('^.*$', ' átta', '8'), ('^.*$', ' níu', '9')]

dec_ones_male = [(nonoun, ' einn', '1'), (nonoun, ' tveir', '2'), (nonoun, ' þrír', '3'), (nonoun, ' fjórir', '4')]

tens_zip = [(' tíu', '10'), (' ellefu', '11'), (' tólf', '12'), (' þrettán', '13'), (' fjórtán', '14'),
            (' fimmtán', '15'), (' sextán', '16'), (' sautján', '17'), (' átján', '18'), (' nítján', '19')]

ones_numerator = [(' einn', '1'), (' tveir', '2'), (' þrír', '3'), (' fjórir', '4'), (' fimm', '5'), 
                  (' sex', '6'), (' sjö', '7'), (' átta', '8'), (' níu', '9')]
 
dozens_numerator = [(' tuttugu', '2'), (' þrjátíu', '3'), (' fjörutíu', '4'), (' fimmtíu', '5'), (' sextíu', '6'),
                    (' sjötíu', '7'), (' áttatíu', '8'), (' níutíu', '9')]

ones_denominator = [(' aðrir', '2'), (' þriðju', '3'), (' fjórðu', '4'), (' fimmtu', '5'), 
                    (' sjöttu', '6'), (' sjöundu', '7'), (' áttundu', '8'), (' níundu', '9')]

tens_denominator = [(' tíundu', '10'), (' elleftu', '11'), (' tólftu', '12'), (' þrettándu', '13'), 
                    (' fjórtándu', '14'), (' fimmtándu', '15'), (' sextándu', '16'), (' sautjándu', '17'),
                    (' átjándu', '18'), (' nítjándu', '19')]

dozens_denominator = [(' tuttugustu', '2'), (' þrítugustu', '3'), (' fertugustu', '4'), (' fimmtugustu', '5'), 
                    (' sextugustu', '6'), (' sjötugustu', '7'), (' áttugustu', '8'), (' nítugustu', '9')]

half_zip = [(hálfur, ' hálfur'), (hálfan, ' hálfan'), (hálfum, ' hálfum'), (hálfs, ' hálfs'),
            (hálf, ' hálf'), (hálfa, ' hálfa'), (hálfri, ' hálfri'), (hálfrar, ' hálfrar'),
            (hálft, ' hálft'), (hálfu, ' hálfu'), (hálfir, ' hálfir'), (hálfra, ' hálfra'), (nonoun, ' hálfur')]

two_ordinal_zip = [(annar, ' annar'),(annan, ' annan'), (öðrum, ' öðrum'),( annars, ' annars'),
                    (aðrir, ' aðrir'), (aðra, ' aðra'), (annarra, ' annarra'),
                    (önnur, ' önnur'), (annarri, ' annarri'), (annarrar, ' annarrar'),
                    (aðrar, ' aðrar'), (annað, ' annað'), (öðru, ' öðru'), (annars, ' annars'), (nonoun, ' annan')]

ordinal_ones_zip = [(' fyrst', '1', 'ones'), (' þriðj', '3', 'ones'), (' fjórð', '4', 'ones'), 
                    (' fimmt', '5', 'ones'), (' sjött', '6', 'ones'), (' sjöund', '7', 'ones'),
                    (' áttund', '8', 'ones'), (' níund', '9', 'ones'), (' tíund', '10', 'dozens'), 
                    (' elleft', '11', 'dozens'), (' tólft', '12', 'dozens'), (' þrettánd', '13', 'dozens'), 
                    (' fjórtánd', '14', 'dozens'), (' fimmtánd', '15', 'dozens'), (' sextánd', '16', 'dozens'),
                    (' sautjánd', '17', 'dozens'), (' átjánd', '18', 'dozens'), (' nítjánd', '19', 'dozens')]

ordinal_letters = [(fyrsti, 'i'), (fyrsta, 'a'), (fyrstu, 'u'), (nonoun, 'a')]

dozens_ordinal_zip = [(' tuttug', '2'), (' þrítug', '3'), (' fertug', '4'), (' fimmtug', '5'),
                      (' sextug', '6'), (' sjötug', '7'), (' áttug', '8'), (' nítug', '9')]

dozens_ordinal_letters = [(fyrsti, 'asti'), (fyrsta, 'asta'), (fyrstu, 'ustu'), (nonoun, 'asta')]

hundreds_thousands_zip = [(' tvö', '2'), (' þrjú', '3'), (' fjögur', '4'), (' fimm', '5'),
                          (' sex', '6'), (' sjö', '7'), (' átta', '8'), (' níu', '9')]

millions_zip = [(' tvær', '2'), (' þrjár', '3'), (' fjórar', '4'), (' fimm', '5'),
                (' sex', '6'), (' sjö', '7'), (' átta', '8'), (' níu', '9')]

billions_zip = [(' tveir', '2'), (' þrír', '3'), (' fjórir', '4'), (' fimm', '5'),
                (' sex', '6'), (' sjö', '7'), (' átta', '8'), (' níu', '9')]

mb_ordinal_zip = [(' tví', '2'), (' þrí', '3'), (' fer', '4'), (' fimm', '5'),
                  (' sex', '6'), (' sjö', '7'), (' átt', '8'), (' ní', '9')]

ones_zip_time = [(' eitt', '1'), (' tvö', '2'), (' þrjú', '3'), (' fjögur', '4'), (' fimm', '5'),
                 (' sex', '6'), (' sjö', '7'), (' átta', '8'), (' níu', '9')]

dozens_zip = [(' tuttugu', '2'),
               (' þrjátíu', '3'),
               (' fjörutíu', '4'), 
               (' fimmtíu', '5'),
               (' sextíu', '6'), 
               (' sjötíu', '7'),
               (' áttatíu', '8'),
               (' níutíu', '9')]
