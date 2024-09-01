#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverterString(string):
  string_invertida = ''

  for char in string:
    string_invertida = char + string_invertida
  
  return string_invertida
  
string = str(input('Digite uma String para ser invertida: '))
print(inverterString(string))






