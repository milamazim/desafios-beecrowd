valor = int(input())

def decompor_notas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    resultado = []

    for nota in cedulas:
        qtd = valor // nota        
        resultado.append((qtd, nota))
        valor %= nota
    
    return resultado

print(valor)

for qtd, nota in decompor_notas(valor):
    print(f'{qtd} nota(s) de R$ {nota},00')