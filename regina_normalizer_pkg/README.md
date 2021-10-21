## To run in command line

Run `pip install -e .` inside the folder which contains `setup.py`

Run `pytest test` for tests from the same place.

1. For normalization with a string on command line, run:

`python3 -W ignore -m regina_normalizer.main {sentence-to-be-normalized} {domain}`

for example

`python3 -W ignore -m regina_normalizer.main "10.010.000 kr aukalega" other`

tíu milljónir og tíu þúsund krónur aukalega 

`python3 -W ignore -m regina_normalizer.main "Leikurinn for 3 - 2" sport`

Leikurinn for  þrjú  tvö

2. For normalization with an input file, run:

`python3 -W ignore -m regina_normalizer.main {input-file} {output-file} {domain}`

for example

`python3 -W ignore -m regina_normalizer.main "path/to/input.txt" "path/to/output.txt" other`
