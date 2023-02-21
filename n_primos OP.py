def n_primos(n):
    # Função para verificar se um número é primo
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    # Contador de números primos
    count = 0

    # Percorre todos os números entre 2 e n
    for i in range(2, n + 1):
        # Se o número é primo, incrementa o contador
        if eh_primo(i):
            count += 1

    # Retorna a quantidade de números primos
    return count
