from string import punctuation as p
extended_punctuation = p + "–„”“—«»"


def format_token_out(token, start_punct, end_punct):
    tok_and_punct = ''
    if start_punct:
        tok_and_punct += start_punct
    tok_and_punct += token
    if end_punct:
        tok_and_punct += end_punct
    if tok_and_punct.endswith('—'):
        return tok_and_punct
    return tok_and_punct + ' '


def clean_token(token):
    token_out = token.strip(extended_punctuation.replace('-', ''))
    if token.endswith('-') and not token_out.endswith('-'):
        token_out += '-'
    if token.startswith('--'):
        token_out = token_out[1:]
    return token_out
    

def split_keep_delimiter(line, delimiter):
    line = line.split(delimiter)
    return [token + delimiter for token in line[:-1]] + [line[-1]]





if __name__ == '__main__':
    spl = ' '.join(split_keep_delimiter('sjeu stjzttarflokkur,—talsmenn', '—'))
    print(spl.split())
