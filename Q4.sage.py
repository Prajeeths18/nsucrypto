"""
	Cipher Text: CYPH XWQE !WNK HZOZ
	Plain  Text:  ??   ??  FORW  ??
"""


# This file was *autogenerated* from the file Q4.sage
from sage.all_cmdline import *   # import sage library

_sage_const_26 = Integer(26); _sage_const_65 = Integer(65); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_5 = Integer(5); _sage_const_17 = Integer(17); _sage_const_14 = Integer(14); _sage_const_22 = Integer(22); _sage_const_13 = Integer(13); _sage_const_10 = Integer(10); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_15 = Integer(15); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_24 = Integer(24); _sage_const_7 = Integer(7); _sage_const_23 = Integer(23); _sage_const_16 = Integer(16); _sage_const_25 = Integer(25)
mapping = {}
for i in range(_sage_const_26 ):
	mapping[i] = chr(i+_sage_const_65 )
mapping[_sage_const_26 ] = '0'
mapping[_sage_const_27 ] = '1'
mapping[_sage_const_28 ] = ','
mapping[_sage_const_29 ] = '!'

# create the integer ring field
R30 = IntegerModRing(_sage_const_30 )

# create the lhs and rhs matrices for the known ciphertext
lhs = Matrix(R30, [[_sage_const_5 , _sage_const_17 ], [_sage_const_14 , _sage_const_22 ]])
rhs = Matrix(R30, [[_sage_const_29 , _sage_const_13 ], [_sage_const_22 , _sage_const_10 ]])

sols = [lhs.solve_left(rhs) for _ in range(_sage_const_4 )]

"""
there are 3 more solutions, because, if [[a,b],[c,d]] is a solution,
then, [[a,b-15],[c,d]],[[a,b],[c,d-15]],[[a,b-15],[c,d-15]] all are solutions

[[a, b]  * [[5, 17]     =   [[5a + 14b, 17a + 22b]
 [c, d]]    [14, 22]]		 [5c + 14d, 17c + 22d]]

Subtracting 15 from b gives 14(b-15) mod 30 and 22(b-15) mod 30, which are equivalent to 14b and 22b
Subtracting 15 from d gives 14(d-15) mod 30 and 22(d-15) mod 30, which are equivalent to 14d and 22d
"""

sols[_sage_const_1 ][_sage_const_0 ,_sage_const_1 ] -= _sage_const_15 
sols[_sage_const_2 ][_sage_const_1 ,_sage_const_1 ] -= _sage_const_15 
sols[_sage_const_3 ][_sage_const_0 ,_sage_const_1 ] -= _sage_const_15 
sols[_sage_const_3 ][_sage_const_1 ,_sage_const_1 ] -= _sage_const_15 

# Using these solutions, generate the value for the first part
cipher = [Matrix(R30, [[_sage_const_2 , _sage_const_15 ], [_sage_const_24 , _sage_const_7 ]]), 
		  Matrix(R30, [[_sage_const_23 , _sage_const_16 ], [_sage_const_22 , _sage_const_4 ]]), 
		  Matrix(R30, [[_sage_const_29 , _sage_const_13 ], [_sage_const_22 , _sage_const_10 ]]), 
		  Matrix(R30, [[_sage_const_7 , _sage_const_26 ], [_sage_const_25 , _sage_const_25 ]])]

def get_string(matrix):
	return ''.join([mapping[matrix[_sage_const_0 ,_sage_const_0 ]], mapping[matrix[_sage_const_1 ,_sage_const_0 ]], mapping[matrix[_sage_const_0 ,_sage_const_1 ]], mapping[matrix[_sage_const_1 ,_sage_const_1 ]]])

def solve(sol):
	try:
		plain = [sol.solve_right(x) for x in cipher]
		print(''.join([get_string(x) for x in plain]))
	except ValueError:
		print("No solution")


for i in range(_sage_const_4 ):
	solve(sols[i])



