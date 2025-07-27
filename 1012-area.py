PI = 3.14159
a,b,c = input().split() #fatia em 3 partes o input a cada espaço
a = float(a)
b = float(b)
c = float(c)
print(f'TRIANGULO: {(a*c)/2:.3f}') # (base * altura) / 2
print(f'CIRCULO: {PI*c**2:.3f}') # PI * raio**2
print(f'TRAPEZIO: {((a+b)*c)/2:.3f}') # ((base maior + base menor) * altura) / 2
print(f'QUADRADO: {b**2:.3f}') # lado**2
print(f'RETANGULO: {a*b:.3f}') # base * altura