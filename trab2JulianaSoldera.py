import numpy as np
import matplotlib.pyplot as pp
import math

# inputs = velocidade em m/s (V0)
#         angulo do lancamento em graus
# outputs = distancia percorrida (alcance)
#             altura maxima
#             duracao do lancamento

while True:
	try:
		iV0 = int(input("Digite a velocidade (em m/s):"))
		
		if iV0 <= 0:
			raise ValueError
			
		iAngulo = int(input("Digite o ângulo de lançamento (em graus):"))
		
		if iAngulo < 0 or iAngulo > 90:
			raise ValueError

		break
	except ValueError:
		print("Valor inválido! Favor informar somente valores positivos para a velocidade e ângulos entre 0 e 90 graus")

angRAd = np.deg2rad(iAngulo)
g = 9.8

alcanceMax = round(((iV0**2) * np.sin(2*angRAd)) / g, 1)
alturaMax = round((iV0**2) * (np.sin(angRAd))**2 / (2*g), 1)
tempoTotal = round((((2*iV0) * np.sin(angRAd)) / g), 1)

t = np.arange(0, tempoTotal, 0.1)

x = abs(iV0) * np.cos(angRAd) * t
y = (abs(iV0) * np.sin(angRAd) * t) - ((g*(t**2))/2)

print("\n\n\n*******************************")
print("Distância percorrida:", alcanceMax, "metros")
print("Altura máxima:", alturaMax, "metros")
print("Duração do lançamento:", tempoTotal, "segundos")
print("*******************************")

pp.title("Trajetória do Projétil")
pp.xlabel("Distância (m)")
pp.ylabel("Altura (m)")

pp.plot(x, y, 'r3')
pp.show()