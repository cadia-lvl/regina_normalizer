## Prerequisites

Download POS tagger v2.0.0 from https://github.com/cadia-lvl/POS and have the file `tagger-v2.0.0.pt` in the same folder as all the files.

`pip install tokenizer`

## To run in notebook

Run the import cells in `regina-notebook.ipynb` and then run `run_sentence(input, domain)` for an input sentence, the domain can be 'sport' or 'other'.

## To run in command line (not recommended because the tagger has to be initialized for each sentence)

Clone the directory, it should be named regina_normalizer (change from regina_normalizer-main if needed).

Put the tagger file (named ‘tagger-v2.0.0.pt’ inside the inner regina_normalizer folder, which includes the code)

Run `pip install -e .` inside the folder which contains `setup.py`

Run `pytest test` for tests from the same place.

For normalization, run:

`python3 -W ignore -m regina_normalizer.main {sentence-to-be-normalized} {domain}`

for example

`python3 -W ignore -m regina_normalizer.main "10.010.000 kr aukalega" other`
tíu milljónir og tíu þúsund krónur aukalega 
`python3 -W ignore -m regina_normalizer.main "Leikurinn for 3 - 2" sport`
Leikurinn for  þrjú  tvö 

