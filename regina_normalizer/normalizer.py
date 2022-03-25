# abn pkg
#!/usr/bin/env python3

import re
import sys
import time
from regina_normalizer import tokenizer
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf

def input_string(text_string, domain):
    tok = tokenizer.Tokenizer()
    sentences = tok.detect_sentences(text_string)
    normalized = []
    for sent in sentences:
        abbr_sent = af.replace_abbreviations(sent, domain)
        normalized.append(nf.handle_sentence(abbr_sent, domain))
    final_string = ' '.join(normalized)
    #print(final_string)
    return final_string

def input_file(input_file, output_file, domain):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    tok = tokenizer.Tokenizer()
    sentences = tok.detect_sentences(' '.join(lines))
    normalized = []
    for sent in sentences:
        abbr_sent = af.replace_abbreviations(sent, domain)
        normalized.append(nf.handle_sentence(abbr_sent, domain))
    with open(output_file, 'w') as f:
        for item in normalized:
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