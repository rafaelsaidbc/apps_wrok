

saldo_horas = input("Digite o saldo de horas do mês: ")
horas = saldo_horas[:2]
minutos = saldo_horas[-2:]

minutos_totais = (float(horas) * 60) + float(minutos)


#horas_dias = (float(horas)/8)
#print(horas_dias)
#minutos_dias = (float(minutos)/480)

#total_dias = horas_dias + minutos_dias
total_dias = minutos_totais / 480

print(f'Com o saldo de horas de {saldo_horas}, você tem direito a {total_dias:,.2f} dias de folga...')
