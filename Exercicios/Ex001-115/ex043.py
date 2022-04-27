kg = float(input('Qual é seu peso? (KG) '))
alt = float(input('Qual é sua altura? (m)'))
imc = kg / (alt **2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO! ')
elif 18.5 <= imc < 25:
    print('PESO IDEAL! ')
elif 25 <= imc < 30:
    print('SOBREPESO! ')
elif 30 <= imc < 40:
    print('OBESIDADE! ')
else:
    print('OBESIDADE MÓRBIDA')