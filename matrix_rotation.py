# program to rotate NxN matrix rotate 90 deg clockwise

def rot_clock(mat):
    n = len(mat)

    for i in range(int(n/2)):
        for j in range(i, n-1-i):
            temp = mat[i][j]
        
            # move left to top (n-1-j)
            mat[i][j] = mat[n-1-j][i]

            # move bottom to left
            mat[n-1-j][i] = mat[n-1-i][n-1-j]

            # move right to bottom
            mat[n-1-i][n-1-j] = mat[j][n-1-i]

            # move temp to left
            mat[j][n-1-i] = temp

    return mat

orig_matrix = [[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6]]


for i in range(len(orig_matrix)):
    print(orig_matrix[i])

rot_clock(orig_matrix)
print()

for i in range(len(orig_matrix)):
    print(orig_matrix[i])