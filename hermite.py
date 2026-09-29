def hermite_interpolation(x, y, dy, value):
    n = len(x)
    size = 2 * n

    # Duplicate x values
    z = [0.0] * size

    # Divided differences table
    Q = [[0.0] * size for _ in range(size)]

    for i in range(n):
        z[2 * i] = x[i]
        z[2 * i + 1] = x[i]

        Q[2 * i][0] = y[i]
        Q[2 * i + 1][0] = y[i]

        # Derivative
        Q[2 * i + 1][1] = dy[i]

        if i != 0:
            Q[2 * i][1] = (
                Q[2 * i][0] - Q[2 * i - 1][0]
            ) / (z[2 * i] - z[2 * i - 1])

    # Higher divided differences
    for j in range(2, size):
        for i in range(size - j):
            Q[i][j] = (
                Q[i + 1][j - 1] - Q[i][j - 1]
            ) / (z[i + j] - z[i])

    # Evaluate polynomial
    result = Q[0][0]
    product = 1.0

    for j in range(1, size):
        product *= value - z[j - 1]
        result += Q[0][j] * product

    return result