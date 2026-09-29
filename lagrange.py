def lagrange_interpolation(x_values,y_values,x_target):

    polynome = 0
    n = len(x_values)

    for i in range(n):
        Li = 1

        for j in range(n):
            if i!=j:
                Li *= (x_target-x_values[j])/(x_values[i]-x_values[j])

        polynome += y_values[i] * Li 

    return polynome
