from Function_case1 import *
from Function_case2 import *
from Function_case3 import *  
base = []

def copy_matrix(source_matrix,c):
    matidentite = [[0 for _ in range(c)] for _ in range(c)]
    for i in range(c):
        for j in range(c):
            if i == j:
                matidentite[i][j] = 1
    
    destination_matrix = [[0 for _ in range(len(source_matrix[0])+c)] for _ in range(len(source_matrix))]
    for i in range(len(source_matrix)):
        for j in range(len(source_matrix[0])-1):
            destination_matrix[i][j] = source_matrix[i][j]
    for row in destination_matrix:
        print(row)

    for i in range(len(source_matrix)-1):
        destination_matrix[i][len(source_matrix[0])+i-1] = 1
    for i in range(len(source_matrix)):
        destination_matrix[i][len(destination_matrix[0])-1] = source_matrix[i][len(source_matrix[0])-1]
    for row in destination_matrix:
        print(row)
    return destination_matrix


def convert_to_int(matrix):
    return [[int(val) for val in row] for row in matrix]

def maximisationfirst(mat,v,c):
        print(c)
        print(v)
        mat = convert_to_int(mat)
        mat =copy_matrix(mat,c)
        height = len(mat)
        width = len(mat[0])
        affichage_case2(mat, height, width)
        for i in range(c):
            base.append(v + i + 1)
        x = len(mat[0])
        while check_simplex_case2(mat, height, width) == 1 :
            if x < len(mat[0]) :
                for row in mat:
                    row.pop()
                height = len(mat)
                width = len(mat[0])           
            
            pos = ratio_simplex_case2(mat, height, width, c, v)
            for i in range(c):
                if mat[i][pos] != 0 and (float(mat[i][v + c]) / mat[i][pos]) > 0 :
                    mat[i].append(float(mat[i][v + c]) / mat[i][pos])
                else :
                    mat[i].append(999)
            mat[len(mat)-1].append(0)
            posmin = find_lowest_ratio_case2(mat)
            base[posmin] = pos+1
            tempmat = [[0 for _ in range(width)] for _ in range(height)]
            height = len(mat)
            width = len(mat[0])
            pivot_first_case2(mat, tempmat, height, width, c, v, pos, posmin)
            temptomain_case2(mat, tempmat, c, v)
            affichage_case2(mat, height, width)
            print("Base array:", base)
        tab = []
        tab = find_last_number_in_row_with_value_case2(mat,base)
        tab.append(f"This is the value of Z = {mat[height-1][width-2]} ")
        tab.append(f"Z = {mat[height-1][width-2]}")
        return tab
    