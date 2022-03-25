import os
import re

package_path = os.path.dirname(os.path.abspath(__file__))
ABBR_FILE = os.path.join(package_path, 'abbreviations_general.txt')
ABBR_NONENDING_FILE = os.path.join(package_path, 'abbreviations_nonending.txt')

ALPHABETIC = '[A-Za-záéíóúýðþæöÁÉÍÓÚÝÐÞÆÖ]+'
UPPER_CASE = '[A-ZÁÉÍÓÚÝÐÞÆÖ]'
# we can't use \\w because it only takes ascii chars into account
WORD_CHAR = '[A-Za-záéíóúýðþæöÁÉÍÓÚÝÐÞÆÖ\\d.µ]'
EOS_SYMBOL = '[.:?!;)(]'


class Tokenizer:

    def __init__(self):
        self.abbreviations = self.read_list(ABBR_FILE)
        self.abbreviations_non_ending = self.read_list(ABBR_NONENDING_FILE)

    @staticmethod
    def read_list(filename: str) -> list:
        with open(filename) as f:
            return f.read().splitlines()

    def detect_sentences(self, text: str) -> list:
        """
            Takes a cleaned text as input and returns a list of sentences
            as strings. A white space split on these strings gives a token list, where punctuation has been
            separated from word tokens, except from digits and abbreviations. However, a full stop at the
            end of a sentence is always separated from the last token, even if the last token is an
            abbreviation.
        """
        sentences = []
        tokens = text.split()
        tmp_str = ''
        last_token = ''
        # loop through all tokens in text and determine sentence boundaries, store tokens ending with '.' in the
        # last_token variable
        for token in tokens:
            if not token:
                continue
            tokenized = token
            if not re.fullmatch(ALPHABETIC, token):
                tokenized = self.process_special_characters(token.strip())
            tmp_str = self.check_last_token(sentences, tmp_str, last_token, tokenized)
            # keep tokens ending with '.' for the next iteration
            last_token = self.update_last_token(tokenized)
            if last_token:
                continue
            tmp_str = self.update_tmp_string(sentences, tmp_str, tokenized)

        self.finish_sentence(sentences, tmp_str, last_token)
        return sentences

    def finish_sentence(self, sentences: list, tmp_string: str, last_token: str) -> None:
        """ Check the content of 'tmp_str' and 'last_token' and finish the sentence contained in 'tmp_str'.
        'sentences' is the list of sentences already detected from the input text. After processing
        'tmp_str' and 'last_token' we create a new sentence string to add to 'sentences'
        """
        # we might still have a dangling last token
        if last_token:
            sent = self.ensure_full_stop(tmp_string, last_token)
            sentences.append(sent)
            tmp_string = ''

        # last token of text might not have ended with an EOS symbol, we still want to collect the last token
        # and return
        if tmp_string:
            last_sentence = tmp_string
            if not re.match('.*' + ALPHABETIC + '.*|.*\\d+.*', last_sentence):
                # we dont' want to add a sentence only constisting of symbols, do we?
                # rather add to last sentence, was probably a mistake to finish that one
                if sentences:
                    sent = sentences[-1]
                    sent += ' ' + last_sentence
                    sentences[-1] = sent
            # add a full stop ef the current sentence does not end with an EOS symbol
           # elif not re.match(EOS_SYMBOL, last_sentence.strip()[-1]):
           #     sentences.append(tmp_string.strip() + ' .')
            else:
                sentences.append(tmp_string.strip())

    def update_tmp_string(self, sentences: list, tmp_string: str, tokenized: str) -> str:
        """ Append 'tokenized' to 'tmp_string', check if 'tokenized' represents an end of a sentence,
        if yes, create a new sentence from tmp_string and add to sentences. Return tmp_string, that
        might have been reset to an empty string if we had a full sentence."""
        tmp_string += tokenized + ' '
        if self.is_EOS(tokenized):
            sentences.append(tmp_string)
            tmp_string = ''
        return tmp_string

    def update_last_token(self, tokenized: str) -> str:
        if self.ends_with_dot(tokenized):
            return tokenized
        return ''

    def check_last_token(self, sentences: list, tmp_string: str, last_token: str, tokenized: str) -> str:
        if last_token:
            if not self.is_full_stop_EOS(tokenized, last_token):
                tmp_string = self.append_token(tmp_string, last_token)
            else:
                sentence = self.ensure_full_stop(tmp_string, last_token)
                sentences.append(sentence)
                tmp_string = ''
        return tmp_string

    @staticmethod
    def append_token(tmp_string: str, token: str) -> str:
        """ 'token' might end with ' .', delete the space, because we are dealing with an abbreviation
        or a digits pattern that should not contain a space before the '.'"""
        token = token.replace(' ', '')
        return tmp_string + token + ' '

    @staticmethod
    def ensure_full_stop(tmp_string: str, token: str) -> str:
        """ Finish a sentence, take a look if the tmp_string content has a correct
        sentence ending, if not, add a ' .' to the sentence and return."""
        tmp_string += token.strip()
       # if not tmp_string.endswith(' .') and not tmp_string.endswith(' . \"'):
       #     tmp_string = tmp_string[:-1] + ' .'
        return tmp_string

    @staticmethod
    def ends_with_dot(token: str) -> bool:
        """ A token might end with a dot or a dot plus a quotation mark.
        TODO: we might have to add more patterns here. """
        return token.endswith('.') or token.endswith('. \"')

    def is_full_stop_EOS(self, current: str, last: str) -> bool:
        """ If last token ended with a dot we look at if the current token starts with an uppercase character and if
        last token is non sentence ending abbreviation. Generally, if next token starts with an uppercase letter
        we have an EOS unless the last token (the dot - token) is a one letter uppercase abbreviation or a defined
        non sentence ending abbreviation (like 'Hr.' which should always be followed by a name)
        """
        if not current:
            return False
        if current[0].isupper() or current[0] == '"':
            return not self.is_uppercase_abbr(last) and last.lower() not in self.abbreviations_non_ending
        return False

    @staticmethod
    def is_EOS(token: str) -> bool:
        """ Most EOS symbols are not as ambiguous like the dot, check for them here. The ':' is a matter of
        definition, we define it as EOS for now at least."""

        return token.endswith(' ?') or token.endswith('? "') or token.endswith(' !') or token.endswith('! "') \
               or token.endswith(' :') or token.endswith(' :)')

    def process_special_characters(self, token: str) -> str:
        """
        If a token contains some other character(s) than alphabetic characters, we take a closer look.
        """
        # First, check if we need to process the token, several categories do not need further processing even if
        # the token contains a non-alphabetic character, just return the token as is
        if not self.should_process(token):
            return token

        # For all kinds of punctuation we need to insert spaces at the correct positions
        # Patterns:
        processed_token = token
        # insert space after these symbols: '(', '[', '{'
        insert_space_after_anywhere = '([\\(\\[\\{])'
        # insert space before these symbols: ')', '[', '}' TODO: shouldn't '[' be ']' ?
        insert_space_before_anywhere = '([\\)\\]\\}])'
        # insert space after these symbols at the beginning of a token: '"',
        insert_space_after_if_beginning = '^(\")(.+)'
        # insert space before these symbols at the end of a token: '"', ':', ',', '.', '!', '?'
        insert_space_before_if_end = '(.+)([\":,.!?])$'
        # insert space before these symbols if two of them occur at the end of a token
        insert_space_before_if_end_and_punct = '(.+)([\":,.!?])(\\s[\":,.!?])$'

        # Replacements
        processed_token = re.sub(insert_space_after_anywhere, '\\g<1> ', processed_token)
        processed_token = re.sub(insert_space_before_anywhere, ' \\g<1>', processed_token)
        processed_token = re.sub(insert_space_after_if_beginning, '\\g<1> \\g<2>', processed_token)
        processed_token = re.sub(insert_space_before_if_end, '\\g<1> \\g<2>', processed_token)
        processed_token = re.sub(insert_space_before_if_end_and_punct, '\\g<1> \\g<2>\\g<3>', processed_token)

        return processed_token

    def should_process(self, token: str) -> bool:
        """ We assume 'token' contains some non-alphabetic characters and we test if it needs further processing.
        Tokens of size 0 or 1 do not need processing, and digits (with or without punctuation) and defined
        abbreviations are also not to be processed further. For all other tokens the method returns True
        """
        if len(token) <= 1:
            return False
        # a simple cardinal or ordinal number
        if re.fullmatch('\\d+\\.?', token):
            return False
        # a more complex combination of digits and punctuations, e.g. dates and large numbers
        if re.fullmatch('(\\d+[.,:]\\d+)+[,.]?', token):
            return False
        # telephone number or 'kennitala', don't split on hyphen
        if re.fullmatch('\\d{3}-\\d{4}', token):
            return False
        if re.fullmatch('\\d{6}-\\d{4}', token):
            return False
        # don't split on hyphen if we have a digits pattern with more than one hyphen
        if re.fullmatch('(\\d+-){2,}\\d+', token):
            return False
        # don't split on hyphen for non-digits
        if re.fullmatch('[^\\d]+-[^\\d]+', token):
            return False
        # don't split on slash for small number of chars on each side (digits or letters)
        if re.fullmatch(WORD_CHAR + '{1,3}/' + WORD_CHAR + '{1,3}', token):
            return False
        # special cases - resolve! We need to have simple rules for when to split and when not, the tokenizer
        # should not have to know too much about the normalizer!
        if re.match('(millj./)|(.+/klst)|(.+/kwst)|(.+/gwst)|(.+/gw\\.st)|(.+/mwst)|(.+/twst)|(.+/m²)|(.+/m³)'
                    '|(.+/mm²)|(.+/mm³)|(.+/cm²)|(.+/cm³)|(.+/ferm)|(.+/%)', token.lower()):
            return False
        # don't split smileys TODO: add more patterns here
        if re.fullmatch('(:\))|(:\()', token):
            return False
        # don't do anything with tokens that look like links and e-mail addresses
        if re.match('(www)|(http)|@', token):
            return False
        # don't process abbreviations
        if self.is_abbreviation(token):
            return False
        if self.is_uppercase_abbr(token):
            return False
        return True

    def is_uppercase_abbr(self, token: str) -> bool:
        return re.match('(' + UPPER_CASE + '\\.)+', token) and not self.is_abbreviation(token)

    def is_abbreviation(self, token: str) -> bool:
        if token.lower() in self.abbreviations:
            return True
        return token.lower() in self.abbreviations_non_ending


def main():
    input_text = 'hvort viltu fjórða, fimmta eða sjötta valkostinn?'
    tokenizer = Tokenizer()
    sentences = tokenizer.detect_sentences(input_text)
    for sent in sentences:
        print(sent)


if __name__ == '__main__':
    main()