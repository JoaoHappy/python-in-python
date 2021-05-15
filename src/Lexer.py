from . import Error, Token

#  TT = TIPO DE TOKEN

TT_INT    = 'TT_INT'
TT_FLOAT  = 'FLOAT'
TT_PLUS   = 'PLUS'
TT_MINUS  = 'MINUS'
TT_MUL    = 'MUL'
TT_DIV    = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

DIGITS = '0123456789'

# Iniciando classes


Position = Error.Position

CharError = Error.CharError

class Lexer:
    def __init__(self, file_name, text):
        self.file_name    = file_name
        self.text         = text
        self.pos          = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance()

    # avançar de posição
    def advance(self):
        self.pos.advance(self.current_char)
        # definir o caracter atual na posição do texto tipo: char = t = texto, pos +1 = t na posição 1
        self.current_char = self.text[self.pos.indice] if self.pos.indice < len(self.text) else None

    # criar os tokens
    def make_tokens(self):
        tokens = []

        # verificamos se o caracter está vazio
        while self.current_char != None:
            # caso não esteja vamos verificar quando colocamos o char tem tabulação ou espaço
            if self.current_char in ' \t':
                # se não tiver vamos avançar uma posição e colocamos um char
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_numbers())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                # error
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], CharError(pos_start, self.pos,  "'" + char + "'")

        return tokens, None

    def make_numbers(self):
        num_str   = ''
        # contagem de pontos/ tradução 
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str = '.' 
            else:
                num_str += self.current_char
            self.advance()

        # vamos verificar se o numero é int ou float
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))