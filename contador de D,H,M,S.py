segundos = int(input("Digite a quantidade de segundos: "))

dias = segundos // 86400
segundos = segundos % 86400

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

mensagem = '{} dias, {} horas, {} minutos e {} segundos.'.format(dias,horas,minutos,segundos)

print(mensagem)
