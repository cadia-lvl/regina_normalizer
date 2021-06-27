from . import number_patterns as npa
# NUMBERS
ones_zip = [(npa.einn, ' einn', "1"), (npa.einum, ' einum', "1"), (npa.eins, ' eins', "1"),
            (npa.ein, ' ein', "1"), (npa.eina, ' eina', "1"), (npa.einni, ' einni', "1"), (npa.einnar, ' einnar', "1"),
            (npa.eitt, ' eitt', "1"), (npa.einu, ' einu', "1"), (npa.nonoun, ' eitt',  '1'),
            (npa.tveir, ' tveir', "2"), (npa.tvo, ' tvo', "2"), (npa.tveimur, ' tveimur', "2"), (npa.tveggja, ' tveggja', "2"),
            (npa.tvær, ' tvær', "2"), (npa.tvö, ' tvö', "2"), (npa.nonoun, ' tvö', '2'),
            (npa.þrír, ' þrír', "3"), (npa.þrjá, ' þrjá', "3"), (npa.þremur, ' þremur', "3"), (npa.þriggja, ' þriggja', "3"),
            (npa.þrjár, ' þrjár', "3"), (npa.þrjú, ' þrjú', "3"), (npa.nonoun, ' þrjú', '3'),
            (npa.fjórir, ' fjórir', "4"), (npa.fjóra, ' fjóra', "4"), (npa.fjórum, ' fjórum', "4"), (npa.fjögurra, ' fjögurra', "4"),
            (npa.fjórar, ' fjórar', "4"), (npa.fjögur, ' fjögur', "4"), (npa.nonoun, ' fjögur', "4"),
            ('^.*$', ' fimm', '5'), ('^.*$', ' sex', '6'), ('^.*$', ' sjö', '7'), ('^.*$', ' átta', '8'), ('^.*$', ' níu', '9')]

dec_ones_male = [(npa.nonoun, ' einn', '1'), (npa.nonoun, ' tveir', '2'), (npa.nonoun, ' þrír', '3'), (npa.nonoun, ' fjórir', '4')]

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

half_zip = [(npa.hálfur, ' hálfur', "(1\/2|½)"), (npa.hálfan, ' hálfan', "(1\/2|½)"), (npa.hálfum, ' hálfum', "(1\/2|½)"), (npa.hálfs, ' hálfs', "(1\/2|½)"),
            (npa.hálf, ' hálf', "(1\/2|½)"), (npa.hálfa, ' hálfa', "(1\/2|½)"), (npa.hálfri, ' hálfri', "(1\/2|½)"), (npa.hálfrar, ' hálfrar', "(1\/2|½)"),
            (npa.hálft, ' hálft', "(1\/2|½)"), (npa.hálfu, ' hálfu', "(1\/2|½)"), (npa.hálfir, ' hálfir', "(1\/2|½)"), (npa.hálfra, ' hálfra', "(1\/2|½)"), (npa.nonoun, ' hálfur', "(1\/2|½)"),
            
            (npa.fractionnom, ' einn þriðji', "(1\/3|⅓)"), (npa.fractiondat, ' einn þriðja', "(1\/3|⅓)"), (npa.fractionacc, ' einum þriðja', "(1\/3|⅓)"),
            (npa.fractiongen, ' eins þriðja', "(1\/3|⅓)"), (npa.nonoun, ' einn þriðji', "(1\/3|⅓)"),

            (npa.fractionnom, ' einn fjórði', "(1\/4|¼)"), (npa.fractiondat, ' einn fjórða', "(1\/4|¼)"), (npa.fractionacc, ' einum fjórða', "(1\/4|¼)"), 
            (npa.fractiongen, ' eins fjórða', "(1\/4|¼)"), (npa.nonoun, ' einn fjórði', "(1\/4|¼)"),
            
            (npa.fractionnom, ' tveir þriðju', "(2\/3|⅔)"), (npa.fractiondat, ' tvo þriðju', "(2\/3|⅔)"), (npa.fractionacc, ' tveimur þriðju', "(2\/3|⅔)"), 
            (npa.fractiongen, ' tveggja þriðju', "(2\/3|⅔)"), (npa.nonoun, ' tveir þriðju', "(2\/3|⅔)"),

            (npa.fractionnom, ' þrír fjórðu', "(3\/4|¾)"), (npa.fractiondat, ' þrjá fjórðu', "(3\/4|¾)"), (npa.fractionacc, ' þremur fjórðu', "(3\/4|¾)"),
            (npa.fractiongen, ' þriggja fjórðu', "(3\/4|¾)"), (npa.nonoun, ' þrír fjórðu', "(3\/4|¾)")]


two_ordinal_zip = [(npa.annar, ' annar'),(npa.annan, ' annan'), (npa.öðrum, ' öðrum'),(npa.annars, ' annars'),
                    (npa.aðrir, ' aðrir'), (npa.aðra, ' aðra'), (npa.annarra, ' annarra'),
                    (npa.önnur, ' önnur'), (npa.annarri, ' annarri'), (npa.annarrar, ' annarrar'),
                    (npa.aðrar, ' aðrar'), (npa.annað, ' annað'), (npa.öðru, ' öðru'), (npa.annars, ' annars'), (npa.nonoun, ' annan')]

ordinal_ones_zip = [(' fyrst', '1', 'ones'), (' þriðj', '3', 'ones'), (' fjórð', '4', 'ones'), 
                    (' fimmt', '5', 'ones'), (' sjött', '6', 'ones'), (' sjöund', '7', 'ones'),
                    (' áttund', '8', 'ones'), (' níund', '9', 'ones'), (' tíund', '10', 'dozens'), 
                    (' elleft', '11', 'dozens'), (' tólft', '12', 'dozens'), (' þrettánd', '13', 'dozens'), 
                    (' fjórtánd', '14', 'dozens'), (' fimmtánd', '15', 'dozens'), (' sextánd', '16', 'dozens'),
                    (' sautjánd', '17', 'dozens'), (' átjánd', '18', 'dozens'), (' nítjánd', '19', 'dozens')]

ordinal_letters = [(npa.fyrsti, 'i'), (npa.fyrsta, 'a'), (npa.fyrstu, 'u'), (npa.nonoun, 'a')]

dozens_ordinal_zip = [(' tuttug', '2'), (' þrítug', '3'), (' fertug', '4'), (' fimmtug', '5'),
                      (' sextug', '6'), (' sjötug', '7'), (' áttug', '8'), (' nítug', '9')]

dozens_ordinal_letters = [(npa.fyrsti, 'asti'), (npa.fyrsta, 'asta'), (npa.fyrstu, 'ustu'), (npa.nonoun, 'asta')]

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
