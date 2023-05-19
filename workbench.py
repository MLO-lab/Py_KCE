for i in range(n):
    for j in range(i+1, n):
        matrix[i, j] = calculate_SKCE_Matrix_Element(predictions[i], outcomes[i], predictions[j], outcomes[j], kernel)

def helper_(tuple):
    i, j = tuple
    return calculate_SKCE_Matrix_Element(predictions[i], outcomes[i], predictions[j], outcomes[j], kernel)
matrix = np.array(list(map(helper_, [[(i, j) for i in range(j+1, n)] for j in range(n)]))).reshape((n,n))
