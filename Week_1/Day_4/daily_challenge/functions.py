# Daily challenge: Solve the Matrix

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

rows = MATRIX_STR.strip().split("\n")

matrix = [list(row) for row in rows]

for row in matrix:
    print(row)