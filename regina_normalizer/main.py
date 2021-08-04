#!/usr/bin/env python3

import re
import sys
from tokenizer import split_into_sentences
import time
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf


def handle_input(sent, domain):
	sent = af.replace_abbreviations(sent, domain)
	sent = nf.handle_sentence(sent, domain)
	print(sent)
	
if __name__ == '__main__':
    handle_input(sys.argv[1], sys.argv[2])