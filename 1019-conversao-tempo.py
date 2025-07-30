valor = int(input())

segundos = valor % 60
horas = valor // 3600
minutos = (valor // 60) % 60

print(f'{horas}:{minutos}:{segundos}')