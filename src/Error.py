
# POSITION

class Position:
    def __init__(self, indice, number_line, coluna, file_name, file_txt):
        self.indice      = indice
        self.number_line = number_line
        self.coluna      = coluna
        self.file_name   = file_name
        self.file_txt    = file_txt

    def advance(self, current_char):
        self.indice += 1
        self.coluna += 1

        if current_char == '\n':
           self.number_line += 1
           self.coluna = 0

        return self

#error

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.error_name = error_name
        self.details    = details
        self.pos_start  = pos_start
        self.pos_end    = pos_end
    
    def string_result(self):
        result = f'{self.error_name}:{self.details}\n'
        result += f'File {self.pos_start.file_name}, line {self.pos_start.number_line + 1}'

        return result

class CharError(Error):
    def __init__(self,  pos_start, pos_end, details):
        super().__init__( pos_start, pos_end, 'Não aceitamos esses caracter', details)



    def copy(self):

        return Position(self.indice, self.number_line, self.coluna, self.file_name, self.file_txt)

