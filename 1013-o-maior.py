a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior_ab = (a+b+abs(a-b))/2
maior_abc = (maior_ab+c+abs(maior_ab-c))/2

if maior_ab > maior_abc: 
    maior = int(maior_ab)
else: 
    maior = int(maior_abc)

print(f'{maior} eh o maior')