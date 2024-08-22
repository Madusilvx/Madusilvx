C, N = map(int, input("Número de mt que leonardo pretende correr e o comprimento da pista (separados por espaço):").split())

if 1 <= C <= 1e8 and 1 <= N <= 100:
    ponto_termino = C % N
    print(f"ponto de término: {ponto_termino} metros")
else:
    print("entrada invalida")