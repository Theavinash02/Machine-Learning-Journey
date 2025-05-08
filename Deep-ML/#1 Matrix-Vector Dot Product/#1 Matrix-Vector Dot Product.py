import numpy as np
def matrix_dot_vector(
    a: list[list[int|float]], 
    b: list[int|float]
    ) -> list[int|float]:
    m = 0
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
    if len(a[0]) == len(b):  # comparing columns vs. vector length 
        mat = np.array(a) @ np.array(b)
        return mat.tolist()
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    else :
        return -1
    pass
