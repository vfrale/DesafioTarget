#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
#retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonnaci(number):
  fibonnaci = [0, 1]
  while len(fibonnaci) < number:
    next_number = fibonnaci[-1] + fibonnaci[-2]
    fibonnaci.append(next_number)
  return fibonnaci

def conferirFibo(number):
  fibo = fibonnaci(number)
  if number in fibo:
    return print('O número ESTÁ contido na sequência de fibbonaci')
  else:
    return print('O número NÃO está contido na sequência de fibbonaci')


entrada = int(input('Digite o número que deseja conferir se está contido na sequência de fibbonaci: '))
conferirFibo(entrada)
