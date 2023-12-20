def check_simplex_w(mat, height, width):
    for i in range(width - 2):
        if mat[height - 1][i] < 0:
            return 1
    return 0

def ratio_simplex_w(mat, height, width, c, v):
    max_val = mat[c][0]
    pos = 0
    for i in range(1, v + c):
        if max_val > mat[c][i]:
            max_val = mat[c][i]
            pos = i
    return pos