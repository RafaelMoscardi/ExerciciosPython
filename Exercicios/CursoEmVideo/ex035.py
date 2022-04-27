print('=========================')
print('== ANALISADOR DE TRIÂNGULOS ==')
print('=========================')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('PODEM FORMAR TRIÂNGULO')
else:
    print('NÃO PODEM FORMAR TRIÂNGULO')