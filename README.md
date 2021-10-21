This version of Regína is presented as a package and can be run on command line.

## Prerequisites

`pip install git+https://github.com/cadia-lvl/POS.git@v3.0.0`

`pip install tokenizer`

## To run in command line

Clone the directory, it should be named regina_normalizer (change from regina_normalizer-main if needed).

Run `pip install -e .` inside the folder which contains `setup.py`

Run `pytest test` for tests from the same place.

For normalization, run:

`python3 -W ignore -m regina_normalizer.main {sentence-to-be-normalized} {domain}`

for example

`python3 -W ignore -m regina_normalizer.main "10.010.000 kr aukalega" other`

tíu milljónir og tíu þúsund krónur aukalega 

`python3 -W ignore -m regina_normalizer.main "Leikurinn for 3 - 2" sport`

Leikurinn for  þrjú  tvö 

