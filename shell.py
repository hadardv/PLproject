import Functastic

while True:
    text = input('Functastic > ')
    result, error = Functastic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)