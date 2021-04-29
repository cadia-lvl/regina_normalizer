## Prerequisites

Download POS tagger v2.0.0 from https://github.com/cadia-lvl/POS and have the file `tagger-v2.0.0.pt` in the same folder as all the files.

`pip install tokenizer`

## To run in notebook

Run the import cells in `regina-notebook.ipynb` and then run `run_sentence(input, domain)` for an input sentence, the domain can be 'sport' or 'other'.

## To run in command line (not recommended because the tagger has to be initialized for each sentence)

`python regina.py {sentence-to-be-normalized} {domain}`
