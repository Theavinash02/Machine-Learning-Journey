import numpy as np
def matrix_dot_vector(
    a: list[list[int|float]], 
    b: list[int|float]
    ) -> list[int|float]:
    m = 0
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
    for i in a:
        m+=1
    if m == len(b):
        mat = np.array(a) @ np.array(b)
        return mat.tolist()
    else :
        return -1
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass
