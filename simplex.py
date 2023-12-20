def remplissage_matrice(mat, height, width, c, v):
    matidentite = [[0 for _ in range(c)] for _ in range(c)]
    for i in range(c):
        for j in range(c):
            if i == j:
                matidentite[i][j] = 1

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

def affichage(mat, height, width):
    print("\nMatrice après copiage :\n")
    for i in range(height):
        for j in range(width):
            print(f"{mat[i][j]} ", end="")
        print()

def check_simplex(mat, height, width):
    for i in range(width - 2):
        if mat[height - 1][i] > 0:
            return 1
    return 0

def check_simplex_w(mat, height, width):
    for i in range(width - 2):
        if mat[height - 1][i] < 0:
            return 1
    return 0

def ratio_simplex(mat, height, width, c, v):
    max_val = mat[c][0]
    pos = 0
    for i in range(1, v + c):
        if max_val < mat[c][i]:
            max_val = mat[c][i]
            pos = i
    return pos

def ratio_simple_min(mat, height, width, c, v):
    min_val = mat[0][v + c ]
    posmin = 0
    for i in range(1, c + 1):
        if 0 < mat[i][v + c ] < min_val:
            min_val = mat[i][v + c ]
            posmin = i
    return posmin

def pivot_first(mat, tempmat, height, width, c, v, pos, posmin):
    for i in range(c + v + 1):
        tempmat[posmin][i] = float(mat[posmin][i]) / mat[posmin][pos]

    for j in range(1, c + 1):
        if j != posmin:
            for i in range(c + v + 1):
                tempmat[j][i] = mat[j][i] - (float(mat[j][pos]) * tempmat[posmin][i])

def temptomain(mat, tempmat, c, v):
    for i in range(c + 1):
        for j in range(v + c + 1):
            mat[i][j] = tempmat[i][j]

def main():
    c = int(input("Nombre de contraintes : "))
    v = int(input("Nombre de variables : "))
    choice = int(input("Choisissez une option (1 pour minimisation, 2 pour maximisation) : "))
    height = c + 1
    width = v + c + 1
    mat = [[0 for _ in range(width)] for _ in range(height)]
    base = []

    if choice == 1:
        print("Vous avez choisi la Minimisation.")
    elif choice == 2:
        remplissage_matrice(mat, height, width, c, v)
        affichage(mat, height, width)

        for i in range(c):
            base.append(v + i + 1)
        print("Vous avez choisi la Maximisation.")

        while check_simplex(mat, height, width) == 1:
            print("Nous devons utiliser l'algorithme du Simplex.")
            pos = ratio_simplex(mat, height, width, c, v)

            for i in range(c):
                mat[i][v + c ] = float(mat[i][v + c]) / mat[i][pos]

            posmin = ratio_simple_min(mat, height, width, c, v)
            print(f"{pos}, {posmin}")
            tempmat = [[0 for _ in range(width)] for _ in range(height)]
            pivot_first(mat, tempmat, height, width, c, v, pos, posmin)
            affichage(tempmat, height, width)

            for i in range(c):
                if mat[posmin][base[i] - 1] == 1:
                    base[i] = pos + 1
            temptomain(mat, tempmat, c, v)
            affichage(mat, height, width)
            for i in range(c):
                print(f"{base[i]}, ", end="")
            print()

        for i in range(c):
            if c == i:
                print(f"La solution optimale est Z = {mat[i][c + v + 1]}")
            else:
                print(f"X{i + 1} = {mat[i][c + v ]}")

    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()
