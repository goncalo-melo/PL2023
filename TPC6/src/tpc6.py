import ply.lex as lex

# Comment state
states = (
    ('comment', 'exclusive'),
)

# List of token names
tokens = (
    'OPEN_COMMENT_MULTILINE', # /*
    'CLOSE_COMMENT_MULTILINE', # */
    'COMMENT_MULTILINE',
    'OPEN_COMMENT', # //
    'CLOSE_COMMENT',
    'COMMENT',
    'OPEN_CURLY_BRACKET', # {
    'CLOSE_CURLY_BRACKET', # }
    'OPEN_SQUARE_BRACKET', # [
    'CLOSE_SQUARE_BRACKET', # ]
    'OPEN_ROUND_BRACKET', # (
    'CLOSE_ROUND_BRACKET', # )
    'COMMA', # ,
    'SEMICOLON', # ;
    'VAR_TYPE', # int, double, float...
    'VAR_NAME',
    'FUNCTION',
    'FUNCTION_NAME',
    'PROGRAM',
    'PROGRAM_NAME',
    'NUMBER',
    'COMPARATOR',
    'OP',
    'ASSIGN',
    'IF',
    'FOR',
    'WHILE',
    'RANGE', # ..
    'IN'
)

# Regular expression rules for simple tokens
t_OPEN_CURLY_BRACKET = r"{"
t_CLOSE_CURLY_BRACKET = r"}"
t_OPEN_SQUARE_BRACKET = r"\["
t_CLOSE_SQUARE_BRACKET = r"\]"
t_OPEN_ROUND_BRACKET = r"\("
t_CLOSE_ROUND_BRACKET = r"\)"
t_COMMA = r","
t_SEMICOLON = r";"
t_VAR_TYPE = r"\b(int|bool|float|double|string|char)\b"
t_VAR_NAME = r"\w+"
t_FUNCTION_NAME = r"\w+(?=\()"
t_PROGRAM_NAME = r"(?<=program\ )\w+"
t_NUMBER = r"\b\d+\b"
t_OP = r"(?<=\d|\s)[\+\-\*\/](?=\d+|\s*)"
t_ASSIGN = r"="
t_RANGE = r"\.\."


def t_OPEN_COMMENT_MULTILINE(t):
    r"\/\*"
    t.lexer.begin("comment")
    return t

def t_comment_CLOSE_COMMENT_MULTILINE(t):
    r"\*\/"
    t.lexer.begin("INITIAL")
    return t

def t_comment_COMMENT_MULTILINE(t):
    r"(.|\n)*?(?=\*\/)"
    return t

def t_OPEN_COMMENT(t):
    r"\/\/"
    t.lexer.begin("comment")
    return t

def t_comment_CLOSE_COMMENT(t):
    r"\n"
    t.lexer.begin("INITIAL")
    return t

def t_comment_COMMENT(t):
    r".*(?=\n)"
    return t

def t_FUNCTION(t):
    r"\bfunction\b"
    return t

def t_PROGRAM(t):
    r"\bprogram\b"
    return t

def t_COMPARATOR(t):
    r">=|<=|>|<"
    return t

def t_IF(t):
    r"\bif\b"
    return t

def t_FOR(t):
    r"\bfor\b"
    return t

def t_WHILE(t):
    r"\bwhile\b"
    return t

def t_IN(t):
    r"\bin\b"
    return t

# Strings containing ignored characters
t_INITIAL_ignore = " \t\n"
t_comment_ignore = ""

# Error handling rule
def t_ANY_error(t):
    print(f"Caracter inválido: '{t.value[0]}'")
    t.lexer.skip(1)



example1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res >= 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

example2= """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

# Build the lexer
lexer = lex.lex()

# Give input
#lexer.input(example1)
lexer.input(example2)

for tok in lexer:
    print(tok)