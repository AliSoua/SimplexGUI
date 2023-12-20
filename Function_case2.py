#maximisation avec AX <= b
def affichage_case2(mat, height, width):
    print("\nMatrice après copiage :\n")
    for i in range(height):
        for j in range(width):
            print(f"{mat[i][j]} ", end="")
        print()

def check_simplex_case2(mat, height, width):
    for i in range(width - 2):
        if mat[height - 1][i] > 0:
            return 1
    return 0

def ratio_simplex_case2(mat, height, width, c, v):
    max_val = mat[c][0]
    pos = 0
    for i in range(1, v + c):
        if max_val < mat[c][i]:
            max_val = mat[c][i]
            pos = i
    return pos

def find_lowest_ratio_case2(mat):
    lowest = mat[0][-1]  
    lowest_pos = 0 
    for i, row in enumerate(mat[:-1]): 
        if row[-1] < lowest:
            lowest = row[-1]
            lowest_pos = i
    return lowest_pos

def pivot_first_case2(mat, tempmat, height, width, c, v, pos, posmin):
    for i in range(c + v + 1):
        tempmat[posmin][i] = float(mat[posmin][i]) / mat[posmin][pos]

    for j in range(0, c + 1):
        if j != posmin:
            for i in range(c + v + 1):
                tempmat[j][i] = mat[j][i] - (float(mat[j][pos]) * tempmat[posmin][i])

def temptomain_case2(mat, tempmat, c, v):
    for i in range(c + 1):
        for j in range(v + c + 1):
            mat[i][j] = tempmat[i][j]

def remplissage_matrice_case2(mat, c, v):
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

def find_last_number_in_row_with_value_case2(mat, base):
    result =[]
    for col_num in base:
        column = [row[col_num - 1] for row in mat[:-1]] 
        if 1 in column:
            row_index = column.index(1) 
            print(f"This is X{col_num}, {mat[row_index][-2]}")
            result.append(f"This is X{col_num}, {mat[row_index][-2]}")
    return result