import re
import sys
from tokenizer import split_into_sentences
import time
import abbr_functions as af
import number_functions as nf


sent = sys.argv[1]
domain = sys.argv[2]
sent = af.replace_abbreviations(sent, domain)
sent = nf.handle_sentence(sent)
print(sent)

