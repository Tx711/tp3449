# To find the transpose of any given matrix

x = [[1,2,3],
     [2,3,4],
     [3,4,5]]
transpose = [list(i) for i in zip(*x)]
print(transpose)
