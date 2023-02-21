def soma_digitos(n):
    return sum(int(d) for d in str(n))

num = int(input("Informe um número: "))
print( soma_digitos(num))
