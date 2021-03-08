# regina-normalizer

SCRIPT MODEL_DATA_STRUCTURE.IPYNB
SCRIPT FUNCTIONS-FIRSTANDLAST.IPYNB

pd.read_csv: Les inn dataframe sem er með þessa dálka (sýna mynd)
make_dataframe_for_abbr(df, ‘first’, ‘before’)
set_type(df)
first_functions(df)
second_functions(df)
tokenize_nsw(df, ‘after’)
df_expanded = flatten_nsw(df[[‘sentence_id’, ‘token_id’, ‘before’, ‘after’, ‘type]])
make_dataframe_for_abbr(df_expanded, ‘second’, ‘after’)
df_expanded[‘after_measure] = df_expanded[‘after’]

MEASURES

main_measurement(df_expanded)

TAGGER

tokenize_nsw(df_expanded, ‘after_measure’)
set_type_second(df_expanded)
df_expanded2 = flatten_nsw(df_expanded[['sentence_id', 'token_id', 'before', 'after_measure', 'type']])
tag_into_df(df_expanded2)
df_expanded_save = df_expanded2[[‘sentence_id’, ‘token_id’, ‘after_measure’, ‘next_tag’, ‘type’]]
df_expanded_save.to_csv(“df_expanded2.csv”)

SCRIPT NUMBERS-SECOND.IPYNB
df = pd.read_csv(‘df_expanded2.csv’)
make_type(df, ‘other’)
df[‘tag’] = df[‘next_tag’]
df[‘word’] = df[‘after_measure’]
df_run = df[[‘sentence_id, ‘token_id’, ‘word’, ‘tag’, ‘type’]]
NUMBERS
run_numbers(df_run, ‘other’)
df_clean = clean_df(df_run)

TIME
df_clean['sentbefore'] = [""] + list(df_clean['word'][:-1])
df_clean['sent2before'] = ["", ""] + list(df_clean['word'][:-2])
run_time(df_clean)
df_time = clean_df_time(df_clean)
SPORT (if sport)
DIGIT
same
LETTERS
same
PLAIN
same
REORGANIZE TAGS
save
