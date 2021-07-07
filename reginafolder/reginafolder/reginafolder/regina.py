import re
import sys
from tokenizer import split_into_sentences
import time
from . import abbr_functions as af
from . import number_functions as nf


def handle_input(sent, domain):
	sent = af.replace_abbreviations(sent, domain)
	sent = nf.handle_sentence(sent, domain)
	#print(sent)
	return sent
	
#handle_input(sys.argv[1], sys.argv[2])

