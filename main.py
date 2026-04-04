
def tribonacci(n):
    """
    Calcula el n-ésimo número de la sucesión de Tribonacci módulo 10^5.
    Definición:
        T_0 = 0
        T_1 = 1
        T_2 = 1
        T_n = T_{n-1} + T_{n-2} + T_{n-3}  para n >= 3

    Parámetros:
        n (int): índice del término a calcular

    Retorna:
        int: T_n módulo 100000
    """

    # Definimos el módulo
    MOD = 10**5

    # Casos base
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Inicialización
    t0, t1, t2 = 0, 1, 1

    # Programación dinámica (enfoque bottom-up)
    for i in range(3, n + 1):
        t3 = (t0 + t1 + t2) % MOD
        t0, t1, t2 = t1, t2, t3

    return t2


# --- Ejecución ---
if __name__ == "__main__":
    n = int(input("Ingresa n: "))
    print(f"T_{n} mod 10^5 =", tribonacci(n))