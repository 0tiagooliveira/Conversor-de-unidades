medida = float(input('Digite uma distância em metros: '))
# m metros
cm = medida / 100
# cm = centimetro
mm = medida / 1000
# mm = milimetros
km = medida / 100
# km = kilometro
hm = medida * 10
# hectometro
dam = medida * 100
#dm = decimetro
dm = medida / 10
#dm = decameto
print('a medida de {} m coresponde a {:.2f} cm, {:.2f} mm,{:.0f} km, {:.2f} hm, , {:.2f} dam, , {:.2f} dm'.format(medida, cm, mm, km, hm, dam, dm))
