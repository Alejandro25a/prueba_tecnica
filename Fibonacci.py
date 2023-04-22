def fibonacci(n):
    # inicializar la secuencia con los primeros dos términos
    secuencia_inicial = [0, 1]

    # calcular la secuencia para n términos
    for i in range(2, n):
        # sumar los dos términos anteriores
        termino_sig = secuencia_inicial[i-1] + secuencia_inicial[i-2]

        # agregar el siguiente término a la secuencia
        secuencia_inicial.append(termino_sig)

    return secuencia_inicial[n-1]

usuario = int(input("Dime un número entero para calcular: "))

fibonacci_final = fibonacci(usuario + 1)

print(f"{usuario}={fibonacci_final}")
