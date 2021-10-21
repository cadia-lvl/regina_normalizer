This version of Regína is not a package, and can be run from command line or in a jupyter notebook.

## To run in command line

1. For normalization with a string on command line, run:

`python3 -W ignore main.py {string-to-be-normalized} {domain}`

for example

`python3 -W ignore main.py "10.010.000 kr aukalega. Þetta gerði 500 kall í viðbót." other`

tíu milljónir og tíu þúsund krónur aukalega .
þetta gerði fimm hundruð kall í viðbót .

`python3 -W ignore main.py "Leikurinn for 4-2. Gunni skoraði 3 mörk." sport`
Leikurinn fór fjögur tvö .
Gunni skoraði þrjú mörk .

Leikurinn for  þrjú  tvö

2. For normalization with an input file, run:

`python3 -W ignore main.py {input-file} {output-file} {domain}`

for example

`python3 -W ignore main.py "path/to/input.txt" "path/to/output.txt" other`

## To run in Jupyter notebook (faster for repetitive runs and experiments since the tagger is only once initialized)

Open `regina-notebook.ipynb` 

Run the import cells in `regina-notebook.ipynb` and then run `normalize(input, domain)` for an input sentence, the domain can be 'sport' or 'other'.
