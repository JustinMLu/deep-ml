import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	# again, we have a 2d list maximum
	# [ [1, 2, 3], 
	#   [4, 5, 6], 
	#   [7, 8, 9] ]

	# so like, 'column' is np mean by dim=-1, 'row' is dim=1

	mat = np.array(matrix)
	print(mat.shape)

	if mode == 'column':
		return np.mean(mat, axis=0, keepdims=False)

	else:
		return np.mean(mat, axis=-1, keepdims=False) 

