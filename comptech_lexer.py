import re

TOKEN_TYPES = [
    ("KEYWORD", r"\b(INT|FLOAT|CHAR|IF|WHILE|RETURN|ELSE)\b"),
    ("ID", r"[a-zA-Z_][a-zA-Z_0-9]*"),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("CHAR_LITERAL", r"\'[a-zA-Z0-9]\'"),
    ("ASSIGN_OP", r"="),
    ("ARITH_OP", r"[\+\-\*/]"),
    ("LEFT_BRACE", r"\{"),
    ("RIGHT_BRACE", r"\}"),
    ("LEFT_PAREN", r"\("),
    ("RIGHT_PAREN", r"\)"),
    ("SEMICOLON", r";"),
    ("COMMA", r","),
    ("WHITESPACE", r"[ \t\n]+"),  
]

input_code = """
INT x;
FLOAT y = 3.14;
 (x + y) RETURN x * y;
"""
# input_code = """
# INT a;
# FLOAT pi = 3.14159;
# CHAR c = 'A';
# """

def lex_analyze(input_code):
    tokens = []
    position = 0
    line_number = 1

    while position < len(input_code):
        match = None
        for token_type, token_regex in TOKEN_TYPES:
            pattern = re.compile(token_regex)
            match = pattern.match(input_code, position)
            if match:
                lexeme = match.group(0)
                if token_type != "WHITESPACE": 
                    tokens.append((token_type, lexeme))
                position = match.end(0)

                line_number += lexeme.count("\n")
                break
        
        if not match:
            raise SyntaxError(f"Unexpected character '{input_code[position]}' at line {line_number}, position {position}")
    
    return tokens

tokens = lex_analyze(input_code)

for token in tokens:
    print(token)