tomadas_list = []
soma = 0

for i in range(4): # qtd de réguas
    tomadas_list.append(int(input())) # qtd de tomadas por regua

for i in tomadas_list:
    soma += i

total = soma - 3 # A última régua não perde uma tomada para cascateamento
print(total) # Tomadas disponiveis para uso