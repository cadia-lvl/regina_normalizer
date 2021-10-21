#!/usr/bin/env python3

import re
import sys
from tokenizer import split_into_sentences
import time
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf

def handle_input_command(text_string, domain):
    sent_grein = list(split_into_sentences(text_string))  
    for sent in sent_grein:
        abbr_sent = af.replace_abbreviations(sent, domain)
        no_sent = nf.handle_sentence(abbr_sent, domain)
        print(no_sent)

def handle_input_file(input_file, output_file, domain):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    sent_grein = list(split_into_sentences(lines))  
    sent_expand = []
    for sent in sent_grein:
        abbr_sent = af.replace_abbreviations(sent, domain)
        no_sent = nf.handle_sentence(abbr_sent, domain)
        sent_expand.append(no_sent)
    with open(output_file, 'w') as f:
        for item in sent_expand:
            f.write("%s\n" % item)   
	
if __name__ == '__main__':
	if len(sys.argv) == 3:
		handle_input_command(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 4:
		handle_input_file(sys.argv[1], sys.argv[2], sys.argv[3])
		print("Done writing output file!")
	else:
		print("\nERROR MESSAGE\n\nFor command line, you need to write: python3 -W ignore main.py {string-to-be-normalized} {domain}\n"+
			  "For a text file, you need to write: python3 -W ignore main.py {file-to-be-normalized} {output-file-normalized} {domain}\n"+
			  "{domain} can be 'sport' or 'other'\n")