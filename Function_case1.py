#maximisation avec AX >= b
def remplissage_matrice_case1(mat, c, v):
    matidentite = [[0 for _ in range(c)] for _ in range(c)]
    for i in range(c):
        for j in range(c):
            if i == j:
                matidentite[i][j] = -1

    for i in range(c):
        print(f"Contrainte {i + 1} :")
        for j in range(v):
            mat[i][j] = float(input(f"Coefficient {j + 1} de la contrainte {i + 1}: "))
        mat[i][v + c] = float(input(f"Résultat de la contrainte {i + 1}: "))

                   
    for i in range(c):
        for j in range(c):
            mat[i][v + j] = matidentite[i][j]

    print("Coefficients de la fonction objectif :")
    for j in range(v):
        mat[c][j] = float(input(f"Coefficient {j + 1}: "))

    for j in range(c):
        mat[c][v + j] = 0

    mat[c][v + c] = float(input("Valeur de la fonction objectif : "))

