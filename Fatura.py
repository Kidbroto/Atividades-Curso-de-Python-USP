nome = input("Digite o nome do cliente: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

mensagem = 'Olá {}, A sua fatura com vencimento em {} de {} no valor de R$ {} foi recebida.'.format(nome,dia_vencimento,mes_vencimento,valor)

print(mensagem)
