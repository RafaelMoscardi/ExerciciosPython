import math
a = float(input('Digite um ângulo qualquer: '))
cos = math.cos(math.radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}' .format(a, cos))
seno = math.sin(math.radians(a))
print('O ângulo de {} tem o seno de {:.2f}' .format(a, seno))
tan = math.tan(math.radians(a))
print('O ângulo de {} tem a tangente de {:.2f}' .format(a, tan))