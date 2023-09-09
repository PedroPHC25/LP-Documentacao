### Assertivas (assert)

import documentacao_modulo as dm

def soma_float(a, b):
    assert (a == 42), "Erro, tipo diferente recebido."
    assert isinstance(b, float), "Erro, tipo diferente recebido."
    pass

numero = 42

assert isinstance(numero, int), "Erro, tipo diferente recebido."
# assert isinstance(numero, float), "Erro, tipo diferente recebido."

print(dm.juros_compostos(10000, 15.18, 12))
# print(dm.juros_compostos(10000, 15, 12))

print(f"__debug__ = {__debug__}")

if __debug__:
    print("Execução em modo normal")
else:
    print("Execução em modo otimizado")
    
print("#"*100)
    
    
### Exceções (try/except)
    
# var -> 0 / 0   => Erro sintático
# var = 0/0   => Erro de exceção (divisão por 0)

# with open("emap.fgv") as file:
#     read_data = file.read()   => Erro de exceção (arquivo inexistente)

try:
    with open("emap.fgv") as file:
        read_data = file.read()
except:
    print("1 Arquivo não existe!")
    
    
x = 10
y = 0

try:
    resultado = x/y
except:
    print("2 Divisão não pode ser realizada")
    
    
try:
    resultado = x/z
except NameError:
    print("3 Variável não existe")
except ZeroDivisionError:
    print("3 Não é possível realizar a divisão")
    
try:
    resultado = x/y
except NameError:
    print("4 Variável não existe")
except ZeroDivisionError:
    print("4 Não é possível realizar a divisão")
    
try:
    resultado = x/z
except NameError:
    print("5 Variável não existe")
#   raise ZeroDivisionError
except ZeroDivisionError:
    print("5 Não é possível realizar a divisão")
except:
    print("")
    
try:
    raise ZeroDivisionError
except NameError:
    print("6 Variável não existe")
except ZeroDivisionError:
    print("6 Não é possível realizar a divisão")
except:
    print("")
    
try:
    raise ZeroDivisionError
except NameError:
    print("7 Variável não existe")
except ArithmeticError:
    print("7 Não é possível realizar a divisão")
except:
    print("")
    
try:
    raise FloatingPointError
except NameError:
    print("8 Variável não existe")
except ArithmeticError:
    print("8 Não é possível realizar a divisão")
except:
    print("")
    
try:
    raise OverflowError
except NameError:
    print("9 Variável não existe")
except ArithmeticError:
    print("9 Não é possível realizar a divisão")
except:
    print("")
    
try:
    raise OverflowError
except NameError:
    print("10 Variável não existe")
except ArithmeticError:
    print("10 Não é possível realizar a divisão")
except Exception:
    print("")

try:
    resultado = x / z
except NameError as erro:
    print("11 Variável não existe", erro)
except ArithmeticError:
    print("11 Não é possível realizar a divisão")
except Exception:
    print("")
    
try:
    resultado = x / z
except NameError as erro:
    print("12 Variável não existe", erro.__class__)
except ArithmeticError:
    print("12 Não é possível realizar a divisão")
except Exception:
    print("")
    
try:
    resultado = x / z
except NameError as erro:
    print("13 Variável não existe", erro.__class__.mro())
except ArithmeticError:
    print("13 Não é possível realizar a divisão")
except Exception:
    print("")
    
try:
    resultado = 10 / 0
except NameError as erro:
    print("14 Variável não existe", erro.__class__.mro())
except ZeroDivisionError as erro:
    print("14 Não é possível realizar a divisão", erro.__class__.mro())
except Exception:
    print("")
    
try:
    resultado = 10 / z
except (ZeroDivisionError, NameError) as erro:   # Erro 1 ou erro 2
    print("15 Não é possível realizar a divisão", erro)
except Exception:
    print("")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    