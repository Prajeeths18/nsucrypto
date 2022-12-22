"""
	Cipher Text: CYPH XWQE !WNK HZOZ
	Plain  Text:  ??   ??  FORW  ??
"""

mapping = {}
for i in range(26):
	mapping[i] = chr(i+65)
mapping[26] = '0'
mapping[27] = '1'
mapping[28] = ','
mapping[29] = '!'

# create the integer ring field
R30 = IntegerModRing(30)

# create the lhs and rhs matrices for the known ciphertext
lhs = Matrix(R30, [[5, 17], [14, 22]])
rhs = Matrix(R30, [[29, 13], [22, 10]])

sols = [lhs.solve_left(rhs) for _ in range(4)]

"""
there are 3 more solutions, because, if [[a,b],[c,d]] is a solution,
then, [[a,b-15],[c,d]],[[a,b],[c,d-15]],[[a,b-15],[c,d-15]] all are solutions

[[a, b]  * [[5, 17]     =   [[5a + 14b, 17a + 22b]
 [c, d]]    [14, 22]]		 [5c + 14d, 17c + 22d]]

Subtracting 15 from b gives 14(b-15) mod 30 and 22(b-15) mod 30, which are equivalent to 14b and 22b
Subtracting 15 from d gives 14(d-15) mod 30 and 22(d-15) mod 30, which are equivalent to 14d and 22d
"""

sols[1][0,1] -= 15
sols[2][1,1] -= 15
sols[3][0,1] -= 15
sols[3][1,1] -= 15

# Using these solutions, generate the value for the first part
cipher = [Matrix(R30, [[2, 15], [24, 7]]), 
		  Matrix(R30, [[23, 16], [22, 4]]), 
		  Matrix(R30, [[29, 13], [22, 10]]), 
		  Matrix(R30, [[7, 26], [25, 25]])]

def get_string(matrix):
	return ''.join([mapping[matrix[0,0]], mapping[matrix[1,0]], mapping[matrix[0,1]], mapping[matrix[1,1]]])

def solve(sol):
	try:
		plain = [sol.solve_right(x) for x in cipher]
		print(''.join([get_string(x) for x in plain]))
	except ValueError:
		print("No solution")


for i in range(4):
	solve(sols[i])


