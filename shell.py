from src.python  import *

while True:
    text = input("> ")
    result, error = run('arquivo meu ovo', text)

    if error: print(error.string_result())
    else: print(result)