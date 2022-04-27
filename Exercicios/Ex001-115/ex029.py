v = float(input('qual a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. ' )
    m = (v-80) * 7
    print('Você deve pagar uma multa de R$ {:.2f} !'.format(m))
print('Tenha um bom dia! dirija com segurança. ')