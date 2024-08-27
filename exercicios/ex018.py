import math

ang = int(input('insira o ângulo: '))
rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print(f'angulo de {ang}, seno: {math.ceil(sen)}, cosseno: {math.ceil(cos)}, tangente: {math.ceil(tan)}')