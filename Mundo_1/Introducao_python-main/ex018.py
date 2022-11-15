from math import (sin, cos, tan, radians)

angulo = float(input('Digite o ângulo que você deseja: '))

radiano = radians(angulo) # função radians() converte de graus para radianos (math só calcula em rad)

print(f'\n O ângulo de {angulo:.1f} tem o SENO de {sin(radiano):.2f} \n O ângulo de {angulo:.1f} tem o COSSENO de {cos(radiano):.2f} \n O ângulo de {angulo:.1f} tem a TANGENTE de {tan(radiano):.2f}')