#!/usr/bin/env python3

import re
import sys
from tokenizer import split_into_sentences
import time
from reginafolder import abbr_functions as af
from reginafolder import number_functions as nf


def main(sent, domain):
	sent = af.replace_abbreviations(sent, domain)
	sent = nf.handle_sentence(sent, domain)
	print(sent)
	
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])