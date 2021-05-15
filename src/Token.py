# tokens

class Token:
     def __init__(self, type_, value=None):
         self.type  = type_
         self.value = value

     def __repr__(self):
         # vai retorna o tipo e o valor
         if self.value: return f'{self.type}:{self.value}'
         # se não tiver valor, retorna o tipo
         return f'{self.type}'