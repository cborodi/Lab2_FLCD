import re

operators = ['=', '+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '++', '--', '~', '&', '|', '^', '<<',
             '>>', 'not', 'and', 'or', 'sqrt']
separators = ['(', ')', '[', ']', '{', '}', ';', ' ', ':', ',', '\n']
reservedWords = ['begin', 'end', 'def_char', 'def_short', 'def_int', 'def_long', 'def_float', 'def_double', 'def_void',
                 'break', 'continue', 'do', 'if', 'else', 'loop', 'aslongas', 'in', 'out', 'switch']

def generateTokens(self, line):
    splitter = ''
    for separator in separators:
        splitter += separator
    print(re.split(r'[({; :}),\n]', line))
    # print(re.split(r'([{; :}])', line))
