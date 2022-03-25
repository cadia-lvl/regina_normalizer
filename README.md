Run `pip install regina-normalizer`

In a python shell, run:

`import regina_normalizer.normalizer`

**Input string**

`normalizer.input_string({text_string}, {domain})`

Example:

`normalizer.input_string("Leikurinn fór 2-2 fyrir KR.", "sport")`
>>> Leikurinn fór tvö tvö fyrir K R .

**Input file**

`normalizer.input_file({input_file}, {output_file}, "other")`

Example:

`normalizer.input_file("input.txt", "output.txt", "other")`

input.txt:

```Þetta þarf að norma a.m.k. 2x. Ég verð 3ja ára í sumar.
Símanr er 888-3492, en hjá þér?
Þetta ætti að taka 2-3 klst.```

output.txt

```Þetta þarf að norma að minnsta kosti tvö x . Ég verð þriggja ára í sumar . Símanúmer er átta átta átta <sil> þrír fjórir níu tveir , en hjá þér ? Þetta ætti að taka tvö til þrjár klukkustundir .```




