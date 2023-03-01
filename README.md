# Conversor-de-unidades
Vamos agora explicar linha a linha o que o código faz:

medida = float(input('Digite uma distância em metros: '))
Esta linha solicita que o usuário digite um valor de distância em metros, e armazena este valor na variável "medida". O valor digitado é convertido para um número real (float).

cm = medida / 100
Esta linha calcula o valor correspondente em centímetros, dividindo o valor em metros por 100. O resultado é armazenado na variável "cm".

mm = medida / 1000
Esta linha calcula o valor correspondente em milímetros, dividindo o valor em metros por 1000. O resultado é armazenado na variável "mm".

km = medida / 1000
Esta linha calcula o valor correspondente em quilômetros, dividindo o valor em metros por 1000. O resultado é armazenado na variável "km".

hm = medida * 10
Esta linha calcula o valor correspondente em hectômetros, multiplicando o valor em metros por 10. O resultado é armazenado na variável "hm".

dam = medida * 100
Esta linha calcula o valor correspondente em decâmetros, multiplicando o valor em metros por 100. O resultado é armazenado na variável "dam".

dm = medida / 10
Esta linha calcula o valor correspondente em decímetros, dividindo o valor em metros por 10. O resultado é armazenado na variável "dm".

print('a medida de {} m corresponde a {:.2f} cm, {:.2f} mm,{:.0f} km, {:.2f} hm, , {:.2f} dam, , {:.2f} dm'.format(medida, cm, mm, km, hm, dam, dm))
Esta linha exibe os valores calculados em metros, centímetros, milímetros, quilômetros, hectômetros e decâmetros, usando a função "print". A função "format" é usada para formatar a saída, exibindo o valor da variável "medida" em metros e os outros valores calculados com duas casas decimais para os valores em centímetros, milímetros, hectômetros e decímetros, e sem casas decimais para o valor em quilômetros.
