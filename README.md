# python-projeto-2
Movimento de Projétil - Cálculo e Gráfico.

Criar um programa em Python que representa graficamente a trajetória de um projétil em movimento oblíquo 
(conhecido também como movimento balístico). 
Nesse tipo de movimento, o projétil se desloca para a frente até uma altura máxima, e depois 
começa a descer devido à ação da força da gravidade, formando uma trajetória parabólica. <br />
 <br />
O projétil é lançado a um ângulo 𝜃 com uma velocidade inicial 𝑣0, estando sob a ação da força da gravidade 𝑔. 
As componentes horizontal e vertical da trajetória podem ser calculadas em função do tempo por meio das seguintes equações, 
respectivamente: 
 
𝑥(𝑡) = |𝑣0|.cos(𝜃).𝑡 <br />
𝑦(𝑡) = |𝑣0|.sen(𝜃).𝑡 − 𝑔𝑡² 2
 
Especificações: <br />
• O ângulo de lançamento (𝜃) deve ser lido do usuário (garanta que seja um valor válido). <br />
• A velocidade inicial de lançamento (𝑣0) deve ser lida do usuário (garanta que seja um valor válido). <br />
• Deve-se variar o tempo (𝑡) em incrementos de 0,1 s. <br />
• Deve-se assumir 𝑔 = 9,8 𝑚/𝑠² (aceleração da gravidade no planeta Terra). <br />
• Além de apresentar na tela o gráfico da trajetória do projétil, deve-se apresentar também: 
a distância total percorrida pelo mesmo (em metros), a altura máxima atingida (em metros) e a duração total do lançamento (em segundos).
