def newton_interpolation(x, y, value):
    n = len(x)

    # Divided differences table
    table = [[0.0 for _ in range(n)] for _ in range(n)]

    # First column = y values
    for i in range(n):
        table[i][0] = y[i]

    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (
                table[i + 1][j - 1] - table[i][j - 1]
            ) / (x[i + j] - x[i])

    # Evaluate Newton polynomial
    result = table[0][0]
    product = 1

    for j in range(1, n):
        product *= (value - x[j - 1])
        result += table[0][j] * product

    return result, table