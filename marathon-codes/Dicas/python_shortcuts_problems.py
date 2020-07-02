###### ASCCI valu of char

## ord(char):  converter uma letra (string) no numero na tabela ASCCI
## chr(number): converte o numero no char da respectiva posiçãop na tabela ASCII

# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
# >>> chr(ord('a') + 3)
# 'd'

##### REVERSE A STRING IN PYTHON

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

##### Remover epaços em branco de string 
## Remover de forma a deixar um unico espaço entre palavras, 
## Sem espaço em branco no inicio ou no fim, da melhor forma possivel

exemplo = "   This  is      Test String     to test    duplicate spaces  in  a string   "
# se você printar o .split() disso, tira todos os esços vazios
print(x.split()) # OUTPUT: ['This', 'is', 'Test', 'String', 'to', 'test', 'duplicate', 'spaces', 'in', 'a', 'string']
# se você juntar com " ", vai colcoar um " " entre cada elemento. Assim, ficará como queremos
print(" ".join(x.split())) 
# OUTPUT: "This is Test String to test duplicate spaces in a string"
# Da pra trabalhar bem com somente o .split() da string suja

# "zxya" => "axyz"
def sort_inside_string(s):
  return ''.join(sorted(s))

# "aaaabbbbcccc" => "abc"
def remove_duplicate_char_in_string(s):
  d = {}
  for i in s:
    d[i] = True
  ss = ''
  for key in d:
    ss = ss + key
  return ss

# retorna base 32 de um numero n (sendo h dicionario com os simbolos alfabeticos {10: "A", 11: "B", ....})
h = {}
def base_32(n):
  if(n == 0):
    return "0"
  result = []
  while(n != 0):
    resto = n % 32
    result.append(h[resto])
    n = n // 32
  return "".join(result[::-1]) # inverte e junta numa string